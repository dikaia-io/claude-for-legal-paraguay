#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_paquete.py — prueba de humo del ZIP construido (spec §4.4 paso 4).

Verifica estructura, UTF-8 estricto de todos los .md/.yaml(.txt), ausencia de
referencias sin reescribir, hashes del manifiesto, banners beta y sello de versión.
Uso: python scripts/test_paquete.py build/paquete-claude-ai.zip [--tag vX.Y.Z]
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_project_knowledge import RE_RESIDUOS, ESTADO_PLUGINS

RAIZ_OBLIGATORIA = ["LEEME-PRIMERO.md", "instrucciones-del-proyecto.md",
                    "manifiesto.json", "LICENSE", "NOTICE"]
RE_SELLO = re.compile(r"Paquete v(\d+\.\d+\.\d+) — commit (\S+) — generado el "
                      r"(\d{4}-\d{2}-\d{2})\. Contrato de instalación v(\d+)\.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("--tag", default=None, help="Tag esperado (vX.Y.Z)")
    args = ap.parse_args()
    errores = []

    with zipfile.ZipFile(args.zip_path) as z:
        nombres = set(z.namelist())
        for req in RAIZ_OBLIGATORIA:
            if req not in nombres:
                errores.append(f"falta {req} en la raíz del ZIP")
        if errores:
            return reportar(errores)

        manifiesto = json.loads(z.read("manifiesto.json").decode("utf-8"))

        # 1. UTF-8 estricto y sin mojibake, en TODOS los archivos de texto.
        for nombre in sorted(nombres):
            if not re.search(r"\.(md|yaml|yaml\.txt|txt|json)$", nombre):
                continue
            crudo = z.read(nombre)
            try:
                texto = crudo.decode("utf-8", errors="strict")
            except UnicodeDecodeError as e:
                errores.append(f"{nombre}: no es UTF-8 válido ({e})")
                continue
            # La «Ã» suelta puede ser legítima (verification-log.md documenta un barrido
            # de mojibake); solo el par Ã+vocal latin-1 delata doble codificación.
            if "�" in texto or re.search(r"Ã[¡©­³º±¼]", texto):
                errores.append(f"{nombre}: mojibake detectado (¿doble codificación?)")

        # 2. Cero residuos de rutas del repo en knowledge + instrucciones.
        for nombre in sorted(n for n in nombres
                             if n.startswith("knowledge/") and n.endswith(".md")):
            residuos = sorted(set(RE_RESIDUOS.findall(z.read(nombre).decode("utf-8"))))
            if residuos:
                errores.append(f"{nombre}: referencias sin reescribir {residuos}")
        instrucciones = z.read("instrucciones-del-proyecto.md").decode("utf-8")
        residuos = sorted(set(RE_RESIDUOS.findall(instrucciones)))
        if residuos:
            errores.append(f"instrucciones-del-proyecto.md: residuos {residuos}")

        # 3. Manifiesto: cada archivo existe y su hash coincide; total coherente.
        if manifiesto["total_archivos"] != len(manifiesto["archivos"]):
            errores.append("manifiesto: total_archivos no coincide con la lista")
        for entrada in manifiesto["archivos"]:
            if entrada["destino"] not in nombres:
                errores.append(f"manifiesto: {entrada['destino']} no está en el ZIP")
                continue
            digesto = hashlib.sha256(z.read(entrada["destino"])).hexdigest()
            if digesto != entrada["sha256"]:
                errores.append(f"{entrada['destino']}: hash no coincide con el manifiesto")

        # 4. Banner beta: presente en skills de plugins beta, ausente en estables.
        for entrada in manifiesto["archivos"]:
            destino, plugin = entrada["destino"], entrada["plugin"]
            if plugin is None or not destino.endswith(".md"):
                continue
            if not destino.startswith("knowledge/SKILL-") and \
               not destino.startswith("knowledge/REF-"):
                continue
            empieza_beta = z.read(destino).decode("utf-8").startswith("> ⚠️ **BETA")
            if ESTADO_PLUGINS[plugin] == "beta" and not empieza_beta:
                errores.append(f"{destino}: plugin beta sin banner")
            if ESTADO_PLUGINS[plugin] == "estable" and empieza_beta:
                errores.append(f"{destino}: plugin estable con banner beta")

        # 5. Sello: coincide con el manifiesto (y con el tag, si se pasó).
        sello = RE_SELLO.search(instrucciones)
        if not sello:
            errores.append("instrucciones-del-proyecto.md: falta el sello de versión")
        else:
            if sello.group(1) != manifiesto["version"]:
                errores.append(f"sello v{sello.group(1)} != manifiesto v{manifiesto['version']}")
            if args.tag and f"v{sello.group(1)}" != args.tag:
                errores.append(f"sello v{sello.group(1)} != tag {args.tag}")

    return reportar(errores)


def reportar(errores):
    if errores:
        print(f"PAQUETE INVÁLIDO — {len(errores)} problema(s):")
        for e in errores:
            print(f"  - {e}")
        return 1
    print("Paquete OK: estructura, UTF-8, enlaces, hashes, banners y sello verificados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
