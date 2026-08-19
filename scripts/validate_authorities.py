#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida el mapa de autoridad y sus referencias desde los plugins.

Controles bloqueantes:
1. `leyes.yaml` y `jurisprudencia.yaml` cumplen sus JSON Schema.
2. Toda entrada normativa `verified` tiene verificación completa y fila en el log.
3. Todo criterio/fallo `verified` tiene procedencia, certeza, uso permitido y fila en el log.
4. Las claves `[[auth:clave#localizador]]` y las claves internas entre backticks existen.
5. Las leyes/decretos/resoluciones citadas por número existen en el mapa o llevan un
   marcador de incertidumbre junto a la mención.
6. Una autoridad `draft`/`deprecated` no se presenta como confirmada.

Se escanean `SKILL.md` y todos sus recursos Markdown, no solo la portada de la skill.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
AUTHORITIES = REPO / "shared" / "authorities"
LEYES = AUTHORITIES / "leyes.yaml"
JURISPRUDENCIA = AUTHORITIES / "jurisprudencia.yaml"
VERIFICATION_LOG = AUTHORITIES / "verification-log.md"
LAW_SCHEMA = REPO / "schemas" / "authority.schema.json"
JURIS_SCHEMA = REPO / "schemas" / "jurisprudencia.schema.json"
PROJECT_STATUS = REPO / "project-status.json"
PLUGINS = REPO / "plugins"

MARCADORES = {"[VERIFICAR VIGENCIA]", "[FUENTE OFICIAL PENDIENTE]"}
STRUCTURED_AUTH = re.compile(r"\[\[auth:([a-z0-9_]+)(?:#[^\]]+)?\]\]")
BACKTICK_KEY = re.compile(r"`([a-z][a-z0-9_]+)`")
AUTHORITY_CITE = re.compile(
    r"\b(?P<kind>Decreto\s*-?\s*Ley|Decreto|Ley|"
    r"Resoluci[oó]n(?:\s+MTESS)?|Res\.?\s+MTESS)"
    r"\s+(?:N\s*[.°ºo]*\s*)?(?P<number>\d{1,5})"
    r"(?:\s*/\s*(?P<year>\d{2,4}))?",
    re.IGNORECASE,
)


for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


class ValidationContext:
    def __init__(self, strict: bool):
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def cargar_yaml(path: Path):
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PyYAML es obligatorio: pip install pyyaml") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validar_schema(ctx: ValidationContext, data, schema_path: Path, label: str) -> None:
    try:
        import jsonschema
    except ImportError as exc:
        raise RuntimeError("jsonschema es obligatorio: pip install jsonschema") from exc
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    errores = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    for error in errores:
        path = ".".join(str(p) for p in error.absolute_path) or "<raíz>"
        ctx.error(f"[schema {label}] {path}: {error.message}")


def claves_del_log() -> set[str]:
    texto = VERIFICATION_LOG.read_text(encoding="utf-8")
    claves = set()
    for match in re.finditer(
        r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|\s*([^|]+?)\s*\|",
        texto,
        re.MULTILINE,
    ):
        celda = match.group(1).strip().strip("`")
        # Una fila puede documentar varios criterios separados por " / ".
        # No se divide sobre cualquier barra porque las citas legales usan "N/AAAA".
        for fragmento in re.split(r"\s+/\s+", celda):
            clave = re.split(r"\s|\(", fragmento.strip().strip("`"), maxsplit=1)[0]
            if clave:
                claves.add(clave)
    return claves


def validar_verificaciones(
    ctx: ValidationContext,
    laws: dict,
    jurisprudence: dict,
) -> None:
    log_keys = claves_del_log()
    for key, entry in laws.items():
        verification = entry.get("verification", {})
        status = verification.get("status")
        if status == "verified":
            for field in ("verified_at", "verified_by", "verified_against"):
                if not verification.get(field):
                    ctx.error(f"[leyes] {key}: verified sin {field}")
            if not verification.get("official_source_checked"):
                ctx.error(f"[leyes] {key}: verified con official_source_checked=false")
        if status in {"verified", "deprecated"} and key not in log_keys:
            ctx.error(f"[log] {key}: status={status} sin fila en verification-log.md")

    for section in ("criteria", "rulings"):
        for key, entry in jurisprudence.get(section, {}).items():
            verification = entry.get("verification", {})
            if verification.get("status") == "verified" and key not in log_keys:
                ctx.error(f"[log] jurisprudencia {key}: verified sin fila en verification-log.md")
            if section == "rulings" and not verification.get("official_source_checked"):
                ctx.error(f"[jurisprudencia] ruling {key}: debe cotejarse contra PJ/CSJ")


def normalizar_kind(value: str) -> str:
    value = value.lower().replace("ó", "o")
    value = re.sub(r"\s+", " ", value).strip()
    if value.startswith("res"):
        return "resolucion"
    if "ley" in value and "decreto" in value:
        return "decreto-ley"
    return value


def normalizar_year(value: str | None) -> str | None:
    if not value:
        return None
    if len(value) == 2:
        number = int(value)
        return str(1900 + number if number >= 50 else 2000 + number)
    return value


def identidad(match: re.Match) -> tuple[str, str, str | None]:
    return (
        normalizar_kind(match.group("kind")),
        match.group("number"),
        normalizar_year(match.group("year")),
    )


def indice_autoridades(laws: dict) -> dict[tuple[str, str, str | None], set[str]]:
    """Indexa solo el título/cita principal, no modificatorias agregadas en notas."""
    index: dict[tuple[str, str, str | None], set[str]] = defaultdict(set)
    for key, entry in laws.items():
        for field in ("official_title", "short_cite"):
            text = entry.get(field) or ""
            match = AUTHORITY_CITE.search(text)
            if not match:
                continue
            kind, number, year = identidad(match)
            index[(kind, number, year)].add(key)
            index[(kind, number, None)].add(key)
    return index


def marcador_cercano(lines: list[str], index: int, radius: int = 2) -> bool:
    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    context = "\n".join(lines[start:end])
    return any(marker in context for marker in MARCADORES)


def estado_plugin(path: Path, project_status: dict) -> str:
    relative = path.relative_to(PLUGINS)
    plugin = relative.parts[0]
    return project_status["plugins"].get(plugin, {}).get("status", "unknown")


def resolver_cita(
    cite_id: tuple[str, str, str | None],
    authority_index: dict[tuple[str, str, str | None], set[str]],
) -> set[str]:
    kind, number, year = cite_id
    exact = authority_index.get((kind, number, year), set())
    if exact:
        return exact
    return authority_index.get((kind, number, None), set()) if year is None else set()


def registrar_segun_madurez(
    ctx: ValidationContext,
    plugin_status: str,
    message: str,
) -> None:
    if plugin_status == "stable":
        ctx.error(message)
    else:
        ctx.warning(message)


def escanear_plugins(
    ctx: ValidationContext,
    laws: dict,
    jurisprudence: dict,
    project_status: dict,
) -> None:
    law_keys = set(laws)
    jurisprudence_keys = set(jurisprudence.get("criteria", {})) | set(
        jurisprudence.get("rulings", {})
    )
    all_keys = law_keys | jurisprudence_keys
    authority_index = indice_autoridades(laws)

    for path in sorted(PLUGINS.glob("*/skills/**/*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        relative = path.relative_to(REPO)
        plugin_status = estado_plugin(path, project_status)

        for match in STRUCTURED_AUTH.finditer(text):
            key = match.group(1)
            if key not in all_keys:
                registrar_segun_madurez(
                    ctx,
                    plugin_status,
                    f"[clave] {relative}: [[auth:{key}]] no existe en el mapa",
                )

        mentioned = set(BACKTICK_KEY.findall(text))
        key_like = {
            key for key in mentioned
            if key in all_keys or key.startswith(("codigo_", "ley_", "res_", "decreto_"))
        }
        for key in sorted(key_like):
            if key not in all_keys:
                registrar_segun_madurez(
                    ctx,
                    plugin_status,
                    f"[clave] {relative}: `{key}` no existe en el mapa",
                )

        for line_index, line in enumerate(lines):
            for match in AUTHORITY_CITE.finditer(line):
                # En modelos de actos privados, "Resolución N.° 1" es la numeración
                # interna de la empresa, no una autoridad estatal. Las resoluciones
                # genéricas solo se controlan si traen año; las MTESS, siempre.
                matched_text = match.group(0)
                if (
                    normalizar_kind(match.group("kind")) == "resolucion"
                    and "mtess" not in matched_text.lower()
                    and not match.group("year")
                ):
                    continue
                cite_id = identidad(match)
                keys = resolver_cita(cite_id, authority_index)
                citation = matched_text
                marked = marcador_cercano(lines, line_index)
                if not keys:
                    if not marked:
                        registrar_segun_madurez(
                            ctx,
                            plugin_status,
                            f"[autoridad ausente] {relative}:{line_index + 1}: "
                            f"{citation!r} no está en leyes.yaml ni lleva marcador cercano",
                        )
                    continue
                statuses = {
                    laws[key].get("verification", {}).get("status") for key in keys
                }
                if statuses & {"draft", "deprecated"} and not marked:
                    registrar_segun_madurez(
                        ctx,
                        plugin_status,
                        f"[vigencia] {relative}:{line_index + 1}: {citation!r} resuelve a "
                        f"{sorted(keys)} con status {sorted(statuses)} sin marcador cercano",
                    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="tratar warnings como errores")
    args = parser.parse_args()
    ctx = ValidationContext(strict=args.strict)

    try:
        laws_data = cargar_yaml(LEYES)
        jurisprudence_data = cargar_yaml(JURISPRUDENCIA)
        project_status = json.loads(PROJECT_STATUS.read_text(encoding="utf-8"))
        validar_schema(ctx, laws_data, LAW_SCHEMA, "leyes")
        validar_schema(ctx, jurisprudence_data, JURIS_SCHEMA, "jurisprudencia")
        laws = laws_data.get("laws", {})
        validar_verificaciones(ctx, laws, jurisprudence_data)
        escanear_plugins(ctx, laws, jurisprudence_data, project_status)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        ctx.error(f"[infraestructura] {exc}")
        laws = {}
        jurisprudence_data = {"criteria": {}, "rulings": {}}

    verified = sum(
        1 for entry in laws.values()
        if entry.get("verification", {}).get("status") == "verified"
    )
    draft = sum(
        1 for entry in laws.values()
        if entry.get("verification", {}).get("status") == "draft"
    )
    deprecated = sum(
        1 for entry in laws.values()
        if entry.get("verification", {}).get("status") == "deprecated"
    )
    criteria = len(jurisprudence_data.get("criteria", {}))
    rulings = len(jurisprudence_data.get("rulings", {}))
    print(
        f"Authority map: {len(laws)} normas ({verified} verified, {draft} draft, "
        f"{deprecated} deprecated); jurisprudencia: {criteria} criterios, {rulings} fallos."
    )
    for warning in ctx.warnings:
        print(f"  ⚠ {warning}")
    for error in ctx.errors:
        print(f"  ✗ {error}")

    if ctx.errors or (ctx.strict and ctx.warnings):
        total = len(ctx.errors) + (len(ctx.warnings) if ctx.strict else 0)
        print(f"\nFALLÓ: {total} hallazgo(s) bloqueante(s).")
        return 1
    print("\nOK: mapa, procedencia y referencias pasan la validación.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
