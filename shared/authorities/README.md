# Authority map (`shared/authorities/`)

Mapa de autoridad normativa paraguaya. Separa los **datos normativos** del prompt y controla el
riesgo nº1 del dominio: la **autoridad incorrecta** (cita válida en el país equivocado, artículo
desactualizado, acordada que no aplica).

## Archivos

| Archivo | Contenido |
|---|---|
| `leyes.yaml` | Normas base, con bloque `verification` por entrada. |
| `tribunales.yaml` | Órganos jurisdiccionales y competencias (incl. Sala Constitucional). |
| `fuentes-oficiales.yaml` | Qué portal/repositorio es autoridad por materia + fallback. |
| `normas-inestables.yaml` | Normas/temas que exigen verificar vigencia en cada uso. |
| `formatos-de-cita.yaml` | Plantillas de cita + controles obligatorios de autoridad. |
| `verification-log.md` | Bitácora de verificaciones contra fuente oficial/local. |
| `../../schemas/authority.schema.json` | Esquema que valida `leyes.yaml`. |

## Ciclo de vida de una entrada

```
draft  ──(verificar contra fuente oficial/local + fila en verification-log)──>  verified
                                                                                   │
                                                          (norma reemplazada)  ──> deprecated
```

- **draft** — dato sin confirmar (proviene de inferencia o uso común).
- **verified** — confirmado contra fuente oficial (BACN/PJ), repositorio local normalizado, o
  conector Legal Data Hunter, con `verified_at` y `verified_against` completos.
- **deprecated** — norma reemplazada o derogada; no se usa para citar.

## Regla dura (la hace cumplir el validador)

> Una **skill estable** NO puede citar una norma con `verification.status: draft` o `deprecated`.
> Si la usa, debe emitir `[VERIFICAR VIGENCIA]` o `[FUENTE OFICIAL PENDIENTE]` y no presentarla
> como confirmada.

Además, una norma puede estar `verified` y aun así figurar en `normas-inestables.yaml`: en ese caso
hay que **verificar vigencia en cada uso** (p. ej. salario mínimo, artículos del CPC con modificatorias).

## Orden de preferencia de fuentes (de `fuentes-oficiales.yaml`)

1. **Repositorios locales normalizados** — repositorio local de legislación en Markdown con frontmatter (ruta configurable en `legal.local.md`; preferente para citar artículos textuales).
2. **Portal oficial** — BACN (legislación), PJ/CSJ (jurisprudencia y acordadas), MTESS, IPS, DNIT, SEDECO.
3. **Conector MCP Legal Data Hunter** — cuando no se tiene el archivo local; entrega cita verificable.

Si nada verifica → `[FUENTE OFICIAL PENDIENTE]`. **Nunca** rellenar con memoria del modelo.

## Validación

`scripts/validate_authorities.py` (pendiente de escribir) debe fallar el CI si:
1. Una entrada no cumple `authority.schema.json` (falta `verification`, status inválido, etc.).
2. Una skill estable cita una norma `draft`/`deprecated`.
3. Una skill cita una ley ausente de `leyes.yaml`.
4. Una entrada es `verified` pero con `official_source_checked: false`, `verified_at: null` o `verified_against: null`.
