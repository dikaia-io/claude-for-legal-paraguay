# Claude for Legal Paraguay

Asistente jurídico para práctica profesional paraguaya, construido como **marketplace de plugins de Claude Code**. Orientado inicialmente a **derecho laboral empresarial**, **contratos civiles/comerciales** y **litigación**.

<!-- project-status:start -->
> ✅ **Estado del código: v0.3.1** (publicada).
> Núcleo, laboral y litigación están **estables**; contratos permanece en **beta** hasta cerrar sus evals.
> **Evals versionados:** 27 casos — 17 aprobados y 10 pendientes de cierre formal.
> **Gate de publicación:** habilitado. El árbol y el historial alcanzable pasan las guardas de datos sensibles.
> Las normas `draft` y toda primera mención no verificada en sesión llevan `[VERIFICAR VIGENCIA]`.
<!-- project-status:end -->
>
> **¿Cómo lo uso?** → ver [`QUICKSTART.md`](QUICKSTART.md) (vía Claude Project o plugin de Claude Code).
>
> **¿Sos abogado y querés usarlo sin terminal?** Descargá
> [`paquete-claude-ai.zip`](https://github.com/dikaia-io/claude-for-legal-paraguay/releases/latest/download/paquete-claude-ai.zip)
> y seguí la [guía en español](docs/instalacion-claude-ai.md). No hace falta instalar programas
> ni conocer GitHub: la cuenta gratuita de Claude alcanza.

## Qué es

Claude opera como asistente jurídico paraguayo disciplinado: trabaja bajo derecho paraguayo, no inventa normas/plazos/jurisprudencia, pide datos faltantes, detecta vacíos probatorios, evalúa contingencias y propone estrategia.

Diseño **skills-first, sources-first, citation-first**: el riesgo principal a controlar no es solo la alucinación, sino la **autoridad incorrecta** (cita válida en el país equivocado o norma desactualizada).

## Estructura

```
claude-for-legal-paraguay/
├── .claude-plugin/marketplace.json   # marketplace propio
├── plugins/
│   ├── paraguay-legal-core/          # núcleo transversal
│   ├── paraguay-laboral/             # MVP 1 (empleadores)
│   ├── paraguay-litigacion/          # MVP 3 (incl. inconstitucionalidad)
│   └── paraguay-contratos/           # MVP 2
├── schemas/                          # JSON Schema del authority map
├── shared/
│   ├── authorities/                  # leyes, tribunales, fuentes, citas, jurisprudencia
│   ├── templates/                    # CLAUDE.base.md, legal.local.md.template
│   └── glossaries/                   # terminología jurídica paraguaya
├── evals/                            # casos de prueba por materia
├── scripts/                          # validación de frontmatter, links, authorities
├── docs/                             # arquitectura, privacidad, política de citas
└── examples/                         # casos anonimizados
```

## Instalación

Desde Claude Code, directo desde GitHub:

```bash
/plugin marketplace add dikaia-io/claude-for-legal-paraguay
/plugin install paraguay-laboral@claude-for-legal-paraguay
/plugin install paraguay-contratos@claude-for-legal-paraguay
/plugin install paraguay-litigacion@claude-for-legal-paraguay
```

> Instalar **a nivel usuario** para no bloquear la lectura de archivos fuera del proyecto.
> Cada plugin de práctica declara su dependencia sobre `paraguay-legal-core`: el núcleo se
> instala y habilita automáticamente si falta. `paraguay-contratos` está en **beta**
> (corrida preliminar 8 verdes + 1 observación; cierre formal pendiente); litigación tiene
> 7/7 evals aprobados y laboral 10/11, con el caso extraterritorial pendiente.

### Desarrollo local

```bash
# desarrollo del plugin principal
claude --plugin-dir ./plugins/paraguay-legal-core

# o agregando el marketplace desde un clon local
/plugin marketplace add /ruta/local/claude-for-legal-paraguay
```

## Seguridad y privacidad

- **Anonimizá** todo material real antes de ingresarlo. Incluso un cliente local envía el contexto a los servidores de Anthropic.
- La configuración con datos personales/del estudio vive en `legal.local.md`, que **no se versiona** (ver `.gitignore`).
- Marco rector: **Ley N.º 7593/2025** de Protección de Datos Personales (Paraguay). Detalle en [`docs/seguridad-y-privacidad.md`](docs/seguridad-y-privacidad.md).
- **Agent Skills (API) y MCP connector no están cubiertos por Zero Data Retention.**

Ver [`SECURITY.md`](SECURITY.md).

## Aviso jurídico

Esta herramienta **no constituye asesoramiento legal**. Toda salida debe ser revisada por un abogado matriculado, y toda referencia normativa verificada contra la fuente oficial (BACN / Poder Judicial – CSJ) antes de su uso profesional.

## Licencia

[Apache-2.0](LICENSE). Ver [`NOTICE`](NOTICE) para atribución de diseño.
