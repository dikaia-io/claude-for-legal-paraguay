#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida la coherencia de versión, madurez y evals del proyecto.

`project-status.json` es la fuente única del estado operativo. Este script
impide que README, marketplace, manifiestos y conteos de evals diverjan.

Uso:
    python scripts/check_project_status.py
    python scripts/check_project_status.py --write-readme
    python scripts/check_project_status.py --for-release
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
STATUS_PATH = REPO / "project-status.json"
MARKETPLACE_PATH = REPO / ".claude-plugin" / "marketplace.json"
README_PATH = REPO / "README.md"
CHANGELOG_PATH = REPO / "CHANGELOG.md"
README_START = "<!-- project-status:start -->"
README_END = "<!-- project-status:end -->"
DIRECT_DOWNLOAD = "releases/latest/download/paquete-claude-ai.zip"
PUBLIC_DOCS = [
    REPO / "README.md",
    REPO / "QUICKSTART.md",
    REPO / "docs" / "instalacion-claude-ai.md",
    REPO / "docs" / "instalador-conversacional.md",
]


for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


def cargar_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contar_evals(directorios: list[str]) -> int:
    total = 0
    for directorio in directorios:
        ruta = REPO / directorio
        if not ruta.is_dir():
            raise ValueError(f"directorio de evals inexistente: {directorio}")
        total += sum(1 for _ in ruta.rglob("caso.md"))
    return total


def renderizar_estado(status: dict) -> str:
    plugins = status["plugins"]
    total = sum(p["evals_total"] for p in plugins.values())
    aprobados = sum(p["evals_approved"] for p in plugins.values())
    pendientes = sum(p["evals_pending"] for p in plugins.values())
    release = status["release"]
    publicacion = (
        "publicada" if release["published"] else
        f"publicación pendiente; última release: v{release['latest_published_version']}"
    )
    return "\n".join([
        README_START,
        f"> ✅ **Estado del código: v{status['version']}** ({publicacion}).",
        "> Núcleo, laboral y litigación están **estables**; contratos permanece en **beta** hasta cerrar sus evals.",
        f"> **Evals versionados:** {total} casos — {aprobados} aprobados y {pendientes} pendientes de cierre formal.",
        "> **Gate de publicación:** saneamiento del historial git pendiente; no crear una nueva release todavía."
        if status.get("security", {}).get("release_blocked") else
        "> **Gate de publicación:** habilitado. El árbol y el historial alcanzable pasan las guardas de datos sensibles.",
        "> Las normas `draft` y toda primera mención no verificada en sesión llevan `[VERIFICAR VIGENCIA]`.",
        README_END,
    ])


def reemplazar_bloque(texto: str, bloque: str) -> str:
    patron = re.compile(
        re.escape(README_START) + r".*?" + re.escape(README_END),
        re.DOTALL,
    )
    if not patron.search(texto):
        raise ValueError("README.md no contiene los marcadores project-status")
    return patron.sub(bloque, texto, count=1)


def validar(status: dict, for_release: bool = False) -> list[str]:
    errores: list[str] = []
    version = status.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errores.append(f"project-status.json: versión semver inválida: {version!r}")

    marketplace = cargar_json(MARKETPLACE_PATH)
    if marketplace.get("metadata", {}).get("version") != version:
        errores.append("marketplace.json: metadata.version diverge de project-status.json")

    entradas = {p["name"]: p for p in marketplace.get("plugins", [])}
    configurados = status.get("plugins", {})
    if set(entradas) != set(configurados):
        errores.append("marketplace.json y project-status.json no enumeran los mismos plugins")

    for nombre, info in configurados.items():
        estado = info.get("status")
        if estado not in {"stable", "beta"}:
            errores.append(f"{nombre}: status inválido: {estado!r}")
            continue
        try:
            reales = contar_evals(info.get("eval_directories", []))
        except ValueError as exc:
            errores.append(f"{nombre}: {exc}")
            reales = -1
        declarados = info.get("evals_total")
        if reales != declarados:
            errores.append(f"{nombre}: {reales} evals reales != {declarados} declarados")
        if info.get("evals_approved", 0) + info.get("evals_pending", 0) != declarados:
            errores.append(f"{nombre}: aprobados + pendientes no coincide con evals_total")

        manifest_path = REPO / "plugins" / nombre / ".claude-plugin" / "plugin.json"
        manifest = cargar_json(manifest_path)
        if manifest.get("version") != version:
            errores.append(f"{nombre}: plugin.json version diverge de project-status.json")
        market_desc = entradas.get(nombre, {}).get("description", "")
        manifest_desc = manifest.get("description", "")
        market_beta = market_desc.startswith("[BETA")
        manifest_beta = manifest_desc.startswith("[BETA")
        debe_ser_beta = estado == "beta"
        if market_beta != debe_ser_beta:
            errores.append(f"{nombre}: marca beta incorrecta en marketplace.json")
        if manifest_beta != debe_ser_beta:
            errores.append(f"{nombre}: marca beta incorrecta en plugin.json")

    esperado = renderizar_estado(status)
    readme = README_PATH.read_text(encoding="utf-8")
    if esperado not in readme:
        errores.append("README.md: bloque de estado desactualizado (usar --write-readme)")
    if f"## [{version}]" not in CHANGELOG_PATH.read_text(encoding="utf-8"):
        errores.append(f"CHANGELOG.md: falta sección para {version}")

    paquete_disponible = status.get("release", {}).get("package_available", False)
    for doc in PUBLIC_DOCS:
        if not doc.exists():
            errores.append(f"documento público faltante: {doc.relative_to(REPO)}")
            continue
        contiene_descarga = DIRECT_DOWNLOAD in doc.read_text(encoding="utf-8")
        if contiene_descarga and not paquete_disponible:
            errores.append(
                f"{doc.relative_to(REPO)} anuncia descarga directa, pero package_available=false"
            )

    security = status.get("security", {})
    if security.get("release_blocked") == security.get("history_sanitized"):
        errores.append(
            "project-status.json: release_blocked debe ser el inverso de history_sanitized"
        )
    if for_release and (
        not security.get("history_sanitized") or security.get("release_blocked")
    ):
        errores.append(
            "release bloqueada: sanear y verificar el historial git antes de publicar"
        )

    return errores


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-readme", action="store_true")
    parser.add_argument("--for-release", action="store_true")
    args = parser.parse_args()
    status = cargar_json(STATUS_PATH)

    if args.write_readme:
        texto = README_PATH.read_text(encoding="utf-8")
        actualizado = reemplazar_bloque(texto, renderizar_estado(status))
        README_PATH.write_text(actualizado, encoding="utf-8", newline="\n")
        print("README.md: bloque de estado actualizado.")

    errores = validar(status, for_release=args.for_release)
    if errores:
        print(f"FALLÓ: {len(errores)} inconsistencia(s):")
        for error in errores:
            print(f"  - {error}")
        return 1
    total = sum(p["evals_total"] for p in status["plugins"].values())
    print(
        f"Estado coherente: v{status['version']}, {len(status['plugins'])} plugins, "
        f"{total} evals versionados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
