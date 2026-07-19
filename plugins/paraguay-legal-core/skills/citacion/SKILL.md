---
name: citacion
description: Formato de cita jurídica paraguayo y control de autoridad. Construye la cita de una norma, acordada, resolución o fallo usando las plantillas oficiales del mapa de autoridad, y exige los cuatro controles de autoridad (fuente oficial, fecha de verificación, tipo de autoridad, nivel de certeza). Bloquea la cita de normas en estado draft sin marcador, y de normas ausentes del mapa. Usar siempre que haya que citar una norma o jurisprudencia.
---

# Skill · Cita y control de autoridad

> Skill transversal del núcleo (`paraguay-legal-core`). Se invoca siempre que una salida cite una
> norma o un fallo. Es el control que evita el riesgo nº1 del proyecto: la **autoridad incorrecta**
> (cita válida en el país equivocado, artículo desactualizado, acordada que no aplica).
> No duplica el mapa de autoridad: lo **consulta**.
>
> **Nota de diseño (evals fase 5, 2026-07-19).** Con el agente `asistente-paraguay` activo, esta
> skill opera en la práctica como **referencia, no como invocación**: el agente ya impone la
> gramática de autoridad y el uso del mapa (`CLAUDE.base.md` §4-§5), y el modelo consulta
> `formatos-de-cita.yaml` directamente. Es comportamiento esperado, no un defecto — las skills se
> seleccionan por *tarea*, y citar es una *propiedad de la salida*, no una tarea (verificado
> empíricamente: 0 invocaciones en 8 corridas de eval, con disciplina de cita perfecta en las 7
> corridas con agente). En superficies **sin** el agente la disciplina se degrada y esta skill
> **tampoco se autoinvoca**: la mitigación real es activar el agente (settings del plugin), o
> invocarla manualmente (`/paraguay-legal-core:citacion`). Detalle del experimento en
> `PLAN-fase-5-mvp-litigacion.md`, notas de la parte 5.

---

## 1. Función

Producir una cita jurídica **bien formada y verificable**, y acompañarla de la **gramática de
autoridad** obligatoria. La skill responde a una pregunta simple antes de dejar pasar cualquier cita:

> ¿De dónde sale esta cita, está vigente, qué tipo de autoridad es y con qué certeza la afirmo?

Si no puede responder las cuatro, la cita no se presenta como confirmada: se marca.

---

## 2. Fuentes que consulta (no las duplica)

- **`shared/authorities/leyes.yaml`** — título oficial, cita corta, URL de fuente, y el bloque
  `verification` (`status`, `verified_at`, `verified_by`, `official_source_checked`).
- **`shared/authorities/formatos-de-cita.yaml`** — plantillas (`formats`), controles obligatorios
  (`controls.required_with_citation`), notas de formato (`format_notes`), y unidades (`units`).
- **`shared/authorities/fuentes-oficiales.yaml`** — qué portal es autoridad para qué materia
  (para declarar la fuente oficial). Si hace falta ubicar la fuente, deriva a la skill `fuentes-oficiales`.

> Toda la regla de autoridad vive en `CLAUDE.base.md` §5 y en el mapa. Esta skill solo la **aplica**.

---

## 3. Plantillas de cita (de `formatos-de-cita.yaml`)

Usar la plantilla que corresponda al tipo de norma; no improvisar formato.

| Tipo | Plantilla |
|---|---|
| Ley con artículo | `{official_title}, art. {art}` |
| Ley corta | `{short_cite}` — p. ej. `Ley N° 213, art. {art}` |
| Ley con año | `Ley N° {num}/{anio}` |
| Decreto | `Decreto N° {num}/{anio}` |
| Resolución MTESS | `Resolución MTESS N° {num}/{anio}` |
| Resolución SEDECO | `Resolución SEDECO N° {num}` |
| Acordada | `Acordada N° {num}/{anio} CSJ` |
| Jurisprudencia | `{tribunal}, "{caratula}", Ac. y Sent. N° {num}, {fecha}` |

**Notas de formato vigentes** (de `format_notes`): el formato de **acordadas** y el formato canónico
de **jurisprudencia** (`Ac. y Sent.` = Acuerdo y Sentencia, uso forense) están marcados `[VERIFICAR]`
contra PJ/CSJ. Mientras tanto, citarlos con `[VERIFICAR VIGENCIA]`.

Montos en guaraníes (`₲ / Gs.`), según `units`.

---

## 4. Gramática de autoridad (los 4 controles obligatorios)

Toda cita con contenido normativo declara —junto a la cita, no en una nota al pie lejana— los cuatro
controles de `controls.required_with_citation`:

| Control | Qué declarar |
|---|---|
| **Fuente oficial** | BACN / PJ-CSJ / fuente local en disco / documento aportado en sesión. |
| **Fecha de verificación** | Cuándo se contrastó; o explícitamente «no verificado en esta sesión». |
| **Tipo de autoridad** | Ley / acordada / resolución / jurisprudencia. |
| **Nivel de certeza** | Alto / medio / bajo. |

Formato sugerido de salida:

```
Ley N° 213/1993 - Código del Trabajo, art. 9
  · Fuente: BACN (leyes-paraguayas/2608) + copia local verificada
  · Verificación: 2026-06-06 · Tipo: ley · Certeza: alta
```

---

## 5. Reglas de bloqueo (lo que esta skill impide)

Antes de emitir una cita, pasar este control:

1. **¿La norma está en `leyes.yaml`?**
   - **No** → no citar de memoria. Emitir `[FUENTE OFICIAL PENDIENTE]` y, si corresponde, derivar a
     `fuentes-oficiales` para ubicarla.
2. **¿Su `verification.status` es `verified`?**
   - `draft` → se puede mencionar, pero **siempre** con `[VERIFICAR VIGENCIA]`. Nunca presentarla como
     confirmada. (Una skill marcada como *estable* no debe apoyar una conclusión en una norma `draft`.)
   - `deprecated` → no usar como vigente. Señalar que fue reemplazada y marcar `[VERIFICAR VIGENCIA]`.
   - `verified` → citar con los 4 controles (sección 4), declarando `verified_at` como fecha.
3. **¿Es jurisprudencia?**
   - Solo se cita si el fallo fue **aportado o consultado en la sesión** (regla nº1 de `CLAUDE.base.md`).
   - Si la conclusión necesita un fallo no aportado → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
   - Nunca inventar carátula, sala, número ni año.
4. **¿Es acordada o resolución cuyo formato aún no se fijó?** → citar con `[VERIFICAR VIGENCIA]` por la
   nota de formato pendiente (sección 3).

---

## 6. Flujo de trabajo

1. Identificar el **tipo** de autoridad a citar (ley / acordada / resolución / jurisprudencia).
2. Buscar la entrada en el mapa (`leyes.yaml`) o, si es fallo, confirmar que fue aportado en sesión.
3. Aplicar el **control de bloqueo** (sección 5).
4. Construir la cita con la **plantilla** correspondiente (sección 3).
5. Adjuntar los **4 controles** de autoridad (sección 4).
6. Si algo no se pudo confirmar, anteponer el **marcador** que corresponda del catálogo de `CLAUDE.base.md`.

---

## 7. Qué NO hace esta skill

- No verifica normas contra la fuente oficial (eso es trabajo de verificación que actualiza el mapa y
  el `verification-log.md`); solo **refleja** el `status` que el mapa ya tiene.
- No ubica fuentes: para eso está `fuentes-oficiales`.
- No computa plazos ni interpreta el fondo: solo gobierna **cómo se cita** y **con qué garantías**.
- No rellena con memoria del modelo: ante la duda, marca y deriva.
