#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guarda de datos sensibles — Claude for Legal Paraguay.

Este repositorio es PÚBLICO: cada commit pusheado es inmutable y visible.
Este script barre el contenido que está por entrar al historial y bloquea el
commit si detecta patrones de datos sensibles (RUC, CI, correos, teléfonos,
rutas de usuario, números de expediente) o patrones privados definidos
localmente en `.sensitive-patterns.local` (nombres de clientes, etc. — ese
archivo está gitignoreado y NUNCA se versiona).

Uso:
    python scripts/check_sensitive.py --staged     # diff staged (hook pre-commit)
    python scripts/check_sensitive.py --all        # todos los archivos versionados
    python scripts/check_sensitive.py --files A B  # archivos puntuales
    python scripts/check_sensitive.py --install    # configura el hook (core.hooksPath)

Método completo: docs/seguridad-y-privacidad.md §8.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Consolas Windows con codepage legacy: forzar UTF-8 en la salida.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

# --- Patrones estructurales (públicos: no revelan ningún dato en sí mismos) ---
GENERIC_PATTERNS: list[tuple[str, str]] = [
    ("ruta de usuario Windows", r"[A-Za-z]:[\\/]+Users[\\/]+\w+"),
    ("ruta OneDrive", r"OneDrive[\\/]"),
    ("RUC con dígito verificador", r"\b\d{6,8}-\d\b"),
    ("RUC en contexto", r"\bRUC\b[^\n\[]{0,15}\d"),
    ("CI en contexto", r"(?:\bC\.?I\.?\b|c[eé]dula de identidad)[^\n\[]{0,15}\d"),
    ("correo electrónico", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    ("teléfono paraguayo", r"(?:\+?595\s?|\b0)9\d{2}[\s.\-]?\d{3}[\s.\-]?\d{3}\b"),
    ("expediente en contexto", r"\bExpte\.?\s*N?[°º]?\s*[:.]?\s*\d"),
    ("matrícula en contexto", r"\bmatr[ií]cula\b[^\n\[]{0,20}\d{3,}"),
]

# Correos que sí pueden aparecer (atribuciones públicas / ejemplos).
EMAIL_ALLOWLIST = {
    "noreply@anthropic.com",
}
EMAIL_ALLOW_DOMAINS = {"example.com", "ejemplo.com"}

LOCAL_PATTERNS_FILE = ".sensitive-patterns.local"

# Extensiones que no se escanean (binarios).
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico", ".woff",
              ".woff2", ".ttf", ".eot", ".docx", ".xlsx", ".pptx"}


def repo_root() -> Path:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, check=True)
    return Path(out.stdout.strip())


def load_local_patterns(root: Path) -> list[tuple[str, str]]:
    """Lee `.sensitive-patterns.local` (un regex por línea; # comenta).

    El archivo es local y gitignoreado: contiene los nombres que no deben
    aparecer (clientes, estudio, usuario). Nunca se versiona.
    """
    f = root / LOCAL_PATTERNS_FILE
    patterns: list[tuple[str, str]] = []
    if f.exists():
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                re.compile(line, re.IGNORECASE)
            except re.error as e:
                print(f"[check_sensitive] patrón local inválido (línea {i}): {e}",
                      file=sys.stderr)
                sys.exit(2)
            patterns.append((f"patrón local #{i}", line))
    return patterns


def email_allowed(match_text: str) -> bool:
    m = match_text.lower()
    if m in EMAIL_ALLOWLIST:
        return True
    return any(m.endswith("@" + d) or m.endswith("." + d) for d in EMAIL_ALLOW_DOMAINS)


def scan_text(label: str, text: str, patterns: list[tuple[str, str]]) -> list[str]:
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pat in patterns:
            for m in re.finditer(pat, line, re.IGNORECASE):
                if name == "correo electrónico" and email_allowed(m.group(0)):
                    continue
                findings.append(f"  {label}:{lineno}  [{name}]  …{line.strip()[:110]}")
    return findings


def staged_content(root: Path) -> list[tuple[str, str]]:
    """Devuelve (ruta, contenido staged) de los archivos en el índice."""
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                         capture_output=True, text=True, check=True, cwd=root)
    files = [f for f in out.stdout.splitlines() if f.strip()]
    result = []
    for f in files:
        if Path(f).suffix.lower() in BINARY_EXT:
            continue
        blob = subprocess.run(["git", "show", f":{f}"], capture_output=True, cwd=root)
        try:
            result.append((f, blob.stdout.decode("utf-8")))
        except UnicodeDecodeError:
            continue  # binario no listado por extensión
    return result


def tracked_content(root: Path) -> list[tuple[str, str]]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         check=True, cwd=root)
    result = []
    for f in out.stdout.splitlines():
        p = root / f
        if not p.is_file() or p.suffix.lower() in BINARY_EXT:
            continue
        try:
            result.append((f, p.read_text(encoding="utf-8")))
        except (UnicodeDecodeError, OSError):
            continue
    return result


def install_hook(root: Path) -> int:
    subprocess.run(["git", "config", "core.hooksPath", "scripts/hooks"],
                   check=True, cwd=root)
    print("[check_sensitive] hook instalado: core.hooksPath = scripts/hooks")
    print("El pre-commit correrá esta guarda sobre cada commit.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Guarda de datos sensibles")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="escanear el índice (pre-commit)")
    mode.add_argument("--all", action="store_true", help="escanear todos los archivos versionados")
    mode.add_argument("--files", nargs="+", help="escanear archivos puntuales")
    mode.add_argument("--install", action="store_true", help="configurar el hook pre-commit")
    args = ap.parse_args()

    root = repo_root()
    if args.install:
        return install_hook(root)

    patterns = GENERIC_PATTERNS + load_local_patterns(root)

    if args.staged:
        targets = staged_content(root)
    elif args.all:
        targets = tracked_content(root)
    else:
        targets = []
        for f in args.files:
            p = Path(f)
            if p.is_file() and p.suffix.lower() not in BINARY_EXT:
                targets.append((f, p.read_text(encoding="utf-8", errors="replace")))

    findings: list[str] = []
    for label, text in targets:
        findings.extend(scan_text(label, text, patterns))

    if findings:
        print("BLOQUEADO: posibles datos sensibles detectados "
              f"({len(findings)} hallazgo(s)).\n")
        for f in findings:
            print(f)
        print("\nSi es un falso positivo, ajustá el patrón o el texto; si es un dato"
              "\nreal, quitalo ANTES de commitear (el historial público es inmutable)."
              "\nMétodo: docs/seguridad-y-privacidad.md §8.")
        return 1

    n = len(targets)
    print(f"[check_sensitive] OK: sin hallazgos ({n} archivo(s) escaneado(s), "
          f"{len(patterns)} patrones).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
