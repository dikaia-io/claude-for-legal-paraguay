#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_versiones.py — coherencia tag vs marketplace.json vs los 4 plugin.json.

El drift ya ocurrió dos veces (commits 2aa340f y 40432b2): este chequeo corre en el
workflow de release ANTES de construir nada, y el release no existe si falla.
Uso: python scripts/check_versiones.py vX.Y.Z
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGINS = ["paraguay-legal-core", "paraguay-laboral",
           "paraguay-litigacion", "paraguay-contratos"]


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith("v"):
        print("uso: check_versiones.py vX.Y.Z")
        return 2
    esperada = sys.argv[1][1:]
    errores = []
    mk = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = mk.get("metadata", {}).get("version")
    if version != esperada:
        errores.append(f"marketplace.json metadata.version = {version!r} != {esperada!r}")
    for plugin in PLUGINS:
        ruta = REPO / "plugins" / plugin / ".claude-plugin" / "plugin.json"
        pj = json.loads(ruta.read_text(encoding="utf-8"))
        if pj.get("version") != esperada:
            errores.append(f"{plugin}: version = {pj.get('version')!r} != {esperada!r}")
    if errores:
        print("DRIFT DE VERSIONES — el release no puede continuar:")
        for e in errores:
            print(f"  - {e}")
        return 1
    print(f"Versiones coherentes: {esperada} (marketplace + {len(PLUGINS)} plugins)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
