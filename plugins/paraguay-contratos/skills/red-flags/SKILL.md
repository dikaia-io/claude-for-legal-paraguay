---
name: red-flags
description: 'Motor de detección de cláusulas problemáticas en contratos civiles y comerciales bajo derecho paraguayo, organizado por nivel de riesgo (nulidad/ineficacia, riesgo alto, riesgo medio) más una categoría previa de invalidez metodológica (plantilla de jurisdicción extranjera). Lo invocan las skills de revisión y de redacción de este plugin (como control de calidad del borrador) y también es invocable directo sobre cualquier contrato. NO recalcula ni redacta: recorre el catálogo completo y emite marcadores de criticidad para que la skill que lo llama decida.'
---

# Skill · Red-flags contractuales (Paraguay)

> Skill motor del plugin `paraguay-contratos`.
>
> **Qué es.** Un **motor transversal de detección**: un catálogo cerrado de cláusulas
> problemáticas ordenado por severidad, aplicable a cualquier contrato civil o comercial
> paraguayo. No clasifica el contrato ni lo redacta; **recorre el catálogo y señaliza**.
>
> **Quién lo usa.** Lo consumen `revision-contractual` (como paso de detección de su flujo) y
> `redaccion-contractual` (como **control de calidad del propio borrador**, antes de entregarlo).
> También es **invocable directo** sobre un contrato suelto que el abogado quiera auditar.
>
> **Qué NO hace (regla de no-duplicación).** No reescribe las reglas inmodificables ni la
> gramática de autoridad de `CLAUDE.base.md`, ni los datos del authority map: los **referencia**.
> El catálogo con las 4 columnas de cada red-flag vive en
> [`references/catalogo-red-flags.md`](references/catalogo-red-flags.md), no acá.

---

## 1. El marcador que produce (interfaz para las skills que llaman)

El motor no emite citas: emite **señales de criticidad**. El marcador interno es:

```
[RED FLAG — NIVEL N: descripción — norma]
```

y, para la categoría previa que no encaja en la escala de nulidad:

```
[RED FLAG — INVALIDEZ METODOLÓGICA: descripción]
```

- `N` es 1, 2 o 3 (los tres niveles del catálogo).
- `descripción` = qué cláusula/omisión se detectó, en una línea.
- `norma` = el ancla del catálogo (p. ej. `CC art. 459`), o un **marcador de incertidumbre** del
  catálogo cerrado de `CLAUDE.base.md` (`[VERIFICAR VIGENCIA]`, `[ARGUMENTO SIN NORMA]`, etc.)
  cuando la red-flag no tiene ancla verificada.

**Este marcador señaliza criticidad; NO es una cita.** Convive con el catálogo cerrado de
marcadores de incertidumbre de `CLAUDE.base.md` (§3) y con su **gramática de autoridad** (§4):
cuando la skill que llama transforme una red-flag en una observación citable para el cliente,
aplica esos controles (fuente / fecha de verificación / tipo de autoridad / nivel de certeza).
No los repito acá: rigen tal como están en `CLAUDE.base.md`.

---

## 2. Orden de ejecución (obligatorio — no detenerse en la primera)

El motor **corre el catálogo entero, siempre**. No se detiene en la primera red-flag: un contrato
con una nulidad puede además tener tres omisiones de nivel 3, y todas importan para el informe.

El orden es:

1. **Invalidez metodológica** (§3 de esta skill) — se evalúa **primera**, antes que nada.
2. **Nivel 1 — Nulidad / ineficacia** — completo.
3. **Nivel 2 — Riesgo alto** y **Nivel 3 — Riesgo medio** — completos.

Recién con el barrido completo se devuelve la lista de marcadores a la skill que llamó.

---

## 3. Categoría previa: invalidez metodológica (plantilla de jurisdicción extranjera)

**No es una causal de nulidad** y por eso va aparte, antes del catálogo. Es el **riesgo nº1 del
proyecto**: que el contrato esté redactado sobre **derecho ajeno** y que analizarlo con normas
paraguayas produzca autoridad incorrecta. Un modelo extranjero adaptado a medias invalida la
**base normativa del análisis**, aunque el contrato en sí pueda ser válido.

**Indicadores de plantilla extranjera** (señales concretas a buscar en el texto):

- Siglas/figuras de otra jurisdicción: **AFP, NIT, N.I.F., C.P.** (código postal), **comuna**,
  **CUIT**, **"Registro Mercantil"**, **"Ilustre Notario"**, **"boleta de honorarios"**.
- Montos en **$ / "pesos"** u otra moneda de otro país sin conversión ni aclaración.
- Bloques de encabezado calcados sin adaptar: **REUNIDOS / EXPONEN** (España),
  **INTERVIENEN / MANIFIESTAN**, u otra fórmula que no sea la práctica paraguaya.
- Remisiones a códigos, tribunales o registros de otra jurisdicción.

**Qué hacer al detectarla** (en este orden):

1. **Informarla de entrada**, antes de correr el catálogo por niveles, con
   `[RED FLAG — INVALIDEZ METODOLÓGICA: descripción]`.
2. **Reclasificar el régimen aplicable**: advertir que el análisis se hará bajo derecho
   paraguayo (`CLAUDE.base.md` §1) y que las cláusulas deben releerse contra el CC/leyes PY,
   no contra las normas de origen del modelo.
3. **Recién entonces correr el catálogo** de los tres niveles sobre el texto reencuadrado.

Si el contrato no muestra ninguno de estos indicadores, se anota que la base normativa es
coherente con derecho paraguayo y se sigue con el Nivel 1.

---

## 4. El catálogo

El catálogo completo —cada red-flag con sus **4 campos** (título · norma anclada · cómo se
detecta · marcador a emitir), agrupado en Nivel 1 / Nivel 2 / Nivel 3— vive en:

**[`references/catalogo-red-flags.md`](references/catalogo-red-flags.md)**

Regla de anclaje del catálogo: **ningún número de artículo se cita de memoria**. Solo se usan
las anclas verificadas del authority map (`shared/authorities/leyes.yaml`) y de la Fase 0 del
proyecto. Lo que no tiene ancla verificada sale con el marcador de incertidumbre que
corresponda de `CLAUDE.base.md` (§3), nunca con un artículo pelado.
