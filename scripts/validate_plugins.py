#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida la estructura del marketplace, los plugins y sus skills.

Controles:
- cada entrada del marketplace apunta a un plugin real;
- dentro de `.claude-plugin/` solo existe `plugin.json`;
- nombre y versión del manifiesto coinciden con el estado del proyecto;
- cada skill tiene `SKILL.md` y frontmatter YAML mínimo (`name`, `description`);
- el nombre declarado por la skill coincide con su directorio.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
STATUS = REPO / "project-status.json"


for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


def cargar_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cargar_frontmatter(path: Path) -> dict:
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PyYAML es obligatorio: pip install pyyaml") from exc

    texto = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", texto, re.DOTALL)
    if not match:
        raise ValueError("frontmatter YAML ausente o mal delimitado")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter no es un objeto YAML")
    return data


def validar() -> list[str]:
    errores: list[str] = []
    marketplace = cargar_json(MARKETPLACE)
    status = cargar_json(STATUS)
    version = status["version"]
    plugins_status = status["plugins"]
    entradas = marketplace.get("plugins", [])

    nombres = [entrada.get("name") for entrada in entradas]
    if len(nombres) != len(set(nombres)):
        errores.append("marketplace.json contiene nombres de plugin duplicados")
    if set(nombres) != set(plugins_status):
        errores.append("marketplace.json y project-status.json difieren en plugins")

    for entrada in entradas:
        nombre = entrada.get("name")
        source = entrada.get("source")
        esperado = f"./plugins/{nombre}"
        if source != esperado:
            errores.append(f"{nombre}: source debe ser {esperado!r}, no {source!r}")
            continue

        raiz = REPO / "plugins" / nombre
        if not raiz.is_dir():
            errores.append(f"{nombre}: directorio del plugin inexistente")
            continue

        metadata = raiz / ".claude-plugin"
        contenidos = sorted(p.name for p in metadata.iterdir()) if metadata.is_dir() else []
        if contenidos != ["plugin.json"]:
            errores.append(
                f"{nombre}: .claude-plugin debe contener solo plugin.json; contiene {contenidos}"
            )
            continue

        manifest = cargar_json(metadata / "plugin.json")
        if manifest.get("name") != nombre:
            errores.append(f"{nombre}: plugin.json declara name={manifest.get('name')!r}")
        if manifest.get("version") != version:
            errores.append(
                f"{nombre}: plugin.json version={manifest.get('version')!r}, esperada {version!r}"
            )
        if not str(manifest.get("description", "")).strip():
            errores.append(f"{nombre}: plugin.json no tiene description")

        skills_dir = raiz / "skills"
        if not skills_dir.is_dir():
            errores.append(f"{nombre}: falta el directorio skills/")
            continue
        skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
        if not skill_dirs:
            errores.append(f"{nombre}: no contiene skills")
        for skill_dir in skill_dirs:
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                errores.append(f"{nombre}/{skill_dir.name}: falta SKILL.md")
                continue
            try:
                frontmatter = cargar_frontmatter(skill_file)
            except (OSError, RuntimeError, ValueError) as exc:
                errores.append(f"{nombre}/{skill_dir.name}: {exc}")
                continue
            if frontmatter.get("name") != skill_dir.name:
                errores.append(
                    f"{nombre}/{skill_dir.name}: frontmatter name={frontmatter.get('name')!r}"
                )
            descripcion = frontmatter.get("description")
            if not isinstance(descripcion, str) or not descripcion.strip():
                errores.append(f"{nombre}/{skill_dir.name}: description vacía")

    return errores


def main() -> int:
    try:
        errores = validar()
    except (OSError, KeyError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        errores = [f"infraestructura: {exc}"]
    if errores:
        print(f"FALLÓ: {len(errores)} problema(s) de estructura:")
        for error in errores:
            print(f"  - {error}")
        return 1
    total_skills = sum(1 for _ in (REPO / "plugins").glob("*/skills/*/SKILL.md"))
    total_plugins = len(cargar_json(MARKETPLACE).get("plugins", []))
    print(f"Plugins válidos: {total_plugins} manifiestos y {total_skills} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
