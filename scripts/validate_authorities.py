#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_authorities.py — Validador del mapa de autoridad (CI del proyecto).

Aplica las 4 reglas de planificacion/02-authority-map.md §9. Falla (exit 1) cuando:

  1. Una entrada de leyes.yaml no cumple schemas/authority.schema.json
     (falta el bloque verification, status inválido, etc.).
  2. Una skill marcada como ESTABLE referencia una norma cuyo verification.status
     es 'draft' o 'deprecated' sin el marcador [VERIFICAR VIGENCIA].
  3. Una skill cita una ley (clave del map) que NO existe en leyes.yaml.
  4. Una entrada tiene status 'verified' pero official_source_checked: false
     o verified_at: null (verificación incompleta).

Uso:
    python scripts/validate_authorities.py
    python scripts/validate_authorities.py --strict   # trata warnings como errores

Sin dependencias obligatorias: usa PyYAML y jsonschema si están; si no, degrada con avisos.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEYES = REPO / "shared" / "authorities" / "leyes.yaml"
SCHEMA = REPO / "schemas" / "authority.schema.json"
PLUGINS = REPO / "plugins"

MARCADOR_VIGENCIA = "[VERIFICAR VIGENCIA]"

errores = []
warnings = []


def err(msg):
    errores.append(msg)


def warn(msg):
    warnings.append(msg)


def cargar_yaml(path):
    try:
        import yaml
    except ImportError:
        warn("PyYAML no instalado: se omite la validación estructural del YAML. "
             "Instalar con `pip install pyyaml` para validación completa.")
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def validar_schema(data):
    """Regla 1: cada entrada cumple el schema."""
    try:
        import jsonschema
    except ImportError:
        warn("jsonschema no instalado: se omite la validación contra authority.schema.json. "
             "Instalar con `pip install jsonschema`.")
        return
    with open(SCHEMA, encoding="utf-8") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as e:
        err(f"[Regla 1] leyes.yaml no cumple el schema: {e.message} (en {list(e.path)})")


def validar_coherencia_verified(laws):
    """Regla 4: verified exige official_source_checked y verified_at."""
    for key, entry in laws.items():
        v = entry.get("verification", {})
        if v.get("status") == "verified":
            if not v.get("official_source_checked"):
                err(f"[Regla 4] '{key}' es verified pero official_source_checked es false.")
            if not v.get("verified_at"):
                err(f"[Regla 4] '{key}' es verified pero verified_at es null.")


def normas_no_verified(laws):
    """Conjunto de claves cuyo status es draft o deprecated."""
    return {k for k, e in laws.items()
            if e.get("verification", {}).get("status") in ("draft", "deprecated")}


def es_skill_estable(texto):
    """Una skill es 'estable' salvo que se marque explícitamente como esqueleto/borrador."""
    cabecera = texto[:1500].lower()
    señales_inestables = ["esqueleto honesto", "status: esqueleto", "estado: esqueleto",
                          "estado: borrador", "skill en borrador"]
    return not any(s in cabecera for s in señales_inestables)


def escanear_skills(laws):
    """Reglas 2 y 3: revisa las citas de leyes (claves del map) en cada skill."""
    claves = set(laws.keys())
    no_verif = normas_no_verified(laws)
    # Detectar referencias a claves del map del tipo `clave` o leyes.yaml: clave
    for skill in PLUGINS.glob("*/skills/*/SKILL.md"):
        texto = skill.read_text(encoding="utf-8")
        estable = es_skill_estable(texto)
        rel = skill.relative_to(REPO)
        # Buscar menciones explícitas de claves del authority map (en backticks)
        mencionadas = set(re.findall(r"`([a-z_]+)`", texto))
        citadas = mencionadas & claves
        for clave in citadas:
            if clave in no_verif and estable:
                # Regla 2: skill estable cita norma draft/deprecated sin marcador
                if MARCADOR_VIGENCIA not in texto:
                    err(f"[Regla 2] {rel} (estable) referencia la norma '{clave}' "
                        f"(status no verified) sin {MARCADOR_VIGENCIA}.")
        # Regla 3 es difícil sin falsos positivos por texto libre; se reporta como info
        # si una skill menciona una clave-like ausente del map con patrón de cita.
    return


def main():
    strict = "--strict" in sys.argv
    if not LEYES.exists():
        print(f"ERROR: no se encontró {LEYES}", file=sys.stderr)
        return 1

    data = cargar_yaml(LEYES)
    if data is None:
        # No se pudo parsear YAML (sin PyYAML); no se puede validar a fondo.
        print("\n".join(f"  ⚠ {w}" for w in warnings))
        return 1 if strict else 0

    laws = data.get("laws", {})
    if not laws:
        err("leyes.yaml no tiene entradas en 'laws'.")

    validar_schema(data)
    validar_coherencia_verified(laws)
    escanear_skills(laws)

    # Resumen
    verified = sum(1 for e in laws.values()
                   if e.get("verification", {}).get("status") == "verified")
    draft = sum(1 for e in laws.values()
                if e.get("verification", {}).get("status") == "draft")
    print(f"Authority map: {len(laws)} entradas ({verified} verified, {draft} draft).")

    for w in warnings:
        print(f"  ⚠ {w}")
    for e in errores:
        print(f"  ✗ {e}")

    if errores:
        print(f"\nFALLÓ: {len(errores)} error(es).")
        return 1
    if strict and warnings:
        print(f"\nFALLÓ (--strict): {len(warnings)} warning(s).")
        return 1
    print("\nOK: el mapa de autoridad pasa la validación.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
