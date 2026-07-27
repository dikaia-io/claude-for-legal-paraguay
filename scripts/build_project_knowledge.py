#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_project_knowledge.py — Construye el paquete para claude.ai (Claude Project).

Produce build/paquete/ con:
    LEEME-PRIMERO.md               (copia de docs/instalacion-claude-ai.md)
    instrucciones-del-proyecto.md  (CLAUDE.base.md + bootstrap + sello de versión)
    manifiesto.json                (versión, commit, estado por plugin, archivos + SHA-256)
    LICENSE / NOTICE
    knowledge/                     (skills, references, assets, authority map, glosario,
                                    plantilla de perfil, doc de seguridad — nombres aplanados,
                                    enlaces internos reescritos)

Con --zip, además empaqueta todo en build/paquete-claude-ai.zip (nombre fijo del asset).
Solo stdlib. Spec: planificacion/superpowers/specs/2026-07-26-instalacion-accesible-design.md
(fuera del repo).

Uso:
    python scripts/build_project_knowledge.py            # solo carpeta build/paquete/
    python scripts/build_project_knowledge.py --zip      # carpeta + ZIP
    python scripts/build_project_knowledge.py --yaml-como-txt   # plan B si el Knowledge
                                                                # rechaza .yaml (spec §4.6)
"""
import argparse
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent
SALIDA = REPO / "build" / "paquete"
ZIP = REPO / "build" / "paquete-claude-ai.zip"

# Estado por plugin (spec §4.5). Los beta se incluyen CON banner, nunca en silencio.
# Quitar un plugin de "beta" exige evals aprobados (regla del proyecto).
ESTADO_PLUGINS = {
    "paraguay-legal-core": "estable",
    "paraguay-laboral": "estable",
    "paraguay-litigacion": "estable",
    "paraguay-contratos": "beta",
}

BANNER_BETA = (
    "> ⚠️ **BETA — evals pendientes.** Materia aún sin casos de prueba corridos: "
    "verificá la salida con especial rigor antes de uso profesional.\n\n"
)


class BuildError(Exception):
    """Error de empaquetado: el build debe fallar, nunca degradar en silencio."""


def recolectar():
    """Releva todos los archivos del paquete y les asigna nombre aplanado de destino."""
    items = []

    for yaml_file in sorted((REPO / "shared" / "authorities").glob("*.yaml")):
        items.append({"origen": yaml_file, "destino": yaml_file.name,
                      "plugin": None, "skill": None, "tipo": "yaml"})

    glosario = REPO / "shared" / "glossaries" / "terminologia-paraguay.md"
    if not glosario.exists():
        raise BuildError(f"Falta el glosario: {glosario}")
    items.append({"origen": glosario, "destino": glosario.name,
                  "plugin": None, "skill": None, "tipo": "glosario"})

    nombres_skill = {}
    for skill_md in sorted((REPO / "plugins").glob("*/skills/*/SKILL.md")):
        skill = skill_md.parent.name
        plugin = skill_md.parents[2].name
        destino = f"SKILL-{skill}.md"
        if destino in nombres_skill and nombres_skill[destino] != plugin:
            destino = f"SKILL-{plugin}-{skill}.md"
        nombres_skill[destino] = plugin
        items.append({"origen": skill_md, "destino": destino,
                      "plugin": plugin, "skill": skill, "tipo": "skill"})

    vistos_ref = {}
    for ref in sorted((REPO / "plugins").glob("*/skills/*/references/*")):
        skill = ref.parents[1].name
        plugin = ref.parents[3].name
        if ref.name in vistos_ref:
            raise BuildError(
                f"Reference ambigua: {ref.name} existe en {vistos_ref[ref.name]} y en {skill}. "
                "Renombrar una de las dos (la reescritura de enlaces resuelve por basename).")
        vistos_ref[ref.name] = skill
        items.append({"origen": ref, "destino": f"REF-{skill}--{ref.name}",
                      "plugin": plugin, "skill": skill, "tipo": "ref"})

    for asset in sorted((REPO / "plugins").glob("*/skills/*/assets/*")):
        skill = asset.parents[1].name
        plugin = asset.parents[3].name
        items.append({"origen": asset, "destino": f"ASSET-{skill}--{asset.name}",
                      "plugin": plugin, "skill": skill, "tipo": "asset"})

    plantilla = REPO / "shared" / "templates" / "legal.local.md.template"
    if not plantilla.exists():
        raise BuildError(f"Falta la plantilla de perfil: {plantilla}")
    items.append({"origen": plantilla, "destino": "plantilla-perfil.md",
                  "plugin": None, "skill": None, "tipo": "plantilla"})

    seguridad = REPO / "docs" / "seguridad-y-privacidad.md"
    if not seguridad.exists():
        raise BuildError(f"Falta el doc de seguridad: {seguridad}")
    items.append({"origen": seguridad, "destino": "seguridad-y-privacidad.md",
                  "plugin": None, "skill": None, "tipo": "seguridad"})

    destinos = [it["destino"] for it in items]
    repetidos = {d for d in destinos if destinos.count(d) > 1}
    if repetidos:
        raise BuildError(f"Destinos duplicados: {sorted(repetidos)}")
    return items


RE_RESIDUOS = re.compile(
    r"(?:references|assets)/[A-Za-z0-9_.\-]+"
    r"|shared/[A-Za-z0-9_./\-]+"
    r"|docs/[A-Za-z0-9_.\-]+\.md")


def mapa_reescritura(items):
    """Mapa original→aplanado. Las references se resuelven por basename (único global)."""
    mapa = {}
    for it in items:
        if it["tipo"] == "ref":
            mapa[f"references/{it['origen'].name}"] = it["destino"]
        elif it["tipo"] == "asset":
            mapa[f"assets/{it['origen'].name}"] = it["destino"]
        elif it["tipo"] == "yaml":
            mapa[f"shared/authorities/{it['origen'].name}"] = it["destino"]
        elif it["tipo"] == "glosario":
            mapa[f"shared/glossaries/{it['origen'].name}"] = it["destino"]
    mapa["shared/templates/legal.local.md.template"] = "plantilla-perfil.md"
    mapa["docs/seguridad-y-privacidad.md"] = "seguridad-y-privacidad.md"
    # Encabezado §5 de CLAUDE.base.md: menciona la carpeta a secas, sin archivo.
    mapa["(`shared/authorities/`)"] = "(los archivos `.yaml` del Knowledge)"
    return mapa


def reescribir(texto, mapa):
    for clave in sorted(mapa, key=len, reverse=True):
        texto = texto.replace(clave, mapa[clave])
    return texto


def validar_sin_residuos(nombre, texto):
    residuos = sorted(set(RE_RESIDUOS.findall(texto)))
    if residuos:
        raise BuildError(
            f"{nombre}: referencias sin reescribir o fuera del paquete: {residuos}. "
            "O falta empaquetar el archivo citado, o hay un enlace roto en la fuente.")


BOOTSTRAP = """
---

## Arranque del asistente (paquete Claude Project)

- El perfil del abogado vive en el archivo `perfil-del-abogado.md` del **Knowledge** de este
  Project. Consultalo siempre antes de asumir identidad, rol o preferencias.
- Si ese archivo no existe: en el **primer mensaje** de la conversación, ofrecé la
  **configuración exprés** — 4 preguntas: abogado responsable, matrícula CSJ, circunscripción
  habitual y rol predominante (detalle en `SKILL-setup.md`). Entregá el resultado como un bloque
  listo para guardar como `perfil-del-abogado.md` y subir al Knowledge (indicá cómo: guardarlo
  con el Bloc de notas y arrastrarlo al Knowledge del Project). Ofrecé la entrevista completa de
  `SKILL-setup.md` como paso opcional posterior.
- Las skills cuyo archivo empiece con el banner «⚠️ BETA» son de materias con evals pendientes:
  advertilo cada vez que las uses.
- Si preguntan qué versión del paquete está instalada, respondé con el sello de abajo.
"""


def leer_version():
    mk = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = mk.get("metadata", {}).get("version")
    if not version:
        raise BuildError("marketplace.json sin metadata.version")
    return version


def leer_contrato():
    doc = REPO / "docs" / "instalacion-claude-ai.md"
    m = re.search(r"Contrato de instalación v(\d+)", doc.read_text(encoding="utf-8"))
    if not m:
        raise BuildError(f"{doc.name}: falta el pie «Contrato de instalación vN»")
    return m.group(1)


def commit_actual():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                              capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "sin-git"


def generar_instrucciones(mapa):
    base = (REPO / "shared" / "templates" / "CLAUDE.base.md").read_text(encoding="utf-8")
    texto = reescribir(base, mapa) + BOOTSTRAP + (
        f"\n---\nPaquete v{leer_version()} — commit {commit_actual()} — generado el "
        f"{datetime.date.today().isoformat()}. Contrato de instalación v{leer_contrato()}.\n")
    validar_sin_residuos("instrucciones-del-proyecto.md", texto)
    return texto


def contenido_destino(item, mapa):
    """Contenido final (bytes) de un item de knowledge: reescrito + banner beta si toca."""
    if item["origen"].suffix not in (".md", ".yaml", ".template"):
        return item["origen"].read_bytes()
    texto = reescribir(item["origen"].read_text(encoding="utf-8"), mapa)
    validar_sin_residuos(item["destino"], texto)
    es_beta = item["plugin"] is not None and ESTADO_PLUGINS[item["plugin"]] == "beta"
    if es_beta and item["destino"].endswith(".md"):
        texto = BANNER_BETA + texto
    return texto.encode("utf-8")


def main():
    ap = argparse.ArgumentParser(description="Construye el paquete claude.ai.")
    ap.add_argument("--out", default=str(SALIDA))
    ap.add_argument("--zip", nargs="?", const=str(ZIP), default=None)
    ap.add_argument("--yaml-como-txt", action="store_true",
                    help="Publica los .yaml como .yaml.txt (plan B, spec §4.6).")
    args = ap.parse_args()
    items = recolectar()
    print(f"{len(items)} archivos relevados.")  # las fases siguientes se agregan en Tasks 4-6
    return 0


if __name__ == "__main__":
    sys.exit(main())
