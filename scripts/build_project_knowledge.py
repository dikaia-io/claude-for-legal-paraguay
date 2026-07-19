#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_project_knowledge.py — Prepara los archivos para el Knowledge de un Claude Project.

El Knowledge de un Claude Project sube archivos sueltos a una "bolsa" plana. Como todas las
skills se llaman `SKILL.md`, colisionarían. Este script copia el authority map, el glosario y
todas las skills a una carpeta única, renombrando cada `SKILL.md` a `SKILL-<nombre>.md` para
que no choquen. El abogado luego arrastra el contenido de esa carpeta al Knowledge.

Esto es SOLO para la vía Claude Project. Como **plugin de Claude Code no hace falta**: ahí las
skills se identifican por su carpeta, no por el nombre del archivo (ver QUICKSTART.md).

Uso:
    python scripts/build_project_knowledge.py
    python scripts/build_project_knowledge.py --out ./mi-carpeta   # destino personalizado

Sin dependencias externas.
"""
import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "build" / "project-knowledge"


def main():
    ap = argparse.ArgumentParser(description="Empaqueta los archivos del Knowledge para un Claude Project.")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="Carpeta destino (por defecto: build/project-knowledge/).")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    copiados = []

    # 1. Authority map (todos los YAML)
    for yaml_file in sorted((REPO / "shared" / "authorities").glob("*.yaml")):
        shutil.copy(yaml_file, out / yaml_file.name)
        copiados.append(yaml_file.name)

    # 2. Glosario
    glosario = REPO / "shared" / "glossaries" / "terminologia-paraguay.md"
    if glosario.exists():
        shutil.copy(glosario, out / glosario.name)
        copiados.append(glosario.name)

    # 3. Skills (renombradas para no colisionar): SKILL.md -> SKILL-<carpeta>.md
    skills = sorted((REPO / "plugins").glob("*/skills/*/SKILL.md"))
    nombres_vistos = {}
    for skill in skills:
        nombre_skill = skill.parent.name           # carpeta de la skill (p. ej. liquidaciones)
        plugin = skill.parents[2].name             # plugin (p. ej. paraguay-laboral)
        destino = f"SKILL-{nombre_skill}.md"
        # Si dos plugins tienen una skill con el mismo nombre, prefijar con el plugin.
        if destino in nombres_vistos and nombres_vistos[destino] != plugin:
            destino = f"SKILL-{plugin}-{nombre_skill}.md"
        nombres_vistos[destino] = plugin
        shutil.copy(skill, out / destino)
        copiados.append(destino)

    print(f"Carpeta lista: {out}")
    print(f"{len(copiados)} archivos preparados:\n")
    for c in copiados:
        print(f"  - {c}")
    print("\nSiguiente paso: arrastrá el CONTENIDO de esa carpeta al Knowledge de tu Claude Project.")
    print("(Las instrucciones del proyecto — CLAUDE.base.md + legal.local.md — van aparte; ver QUICKSTART.md.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
