# Ficha · Contrato de locación

> Ficha de tipo de la skill `revision-contractual` (plugin `paraguay-contratos`), aplicada en su
> **Paso 3** cuando el contrato se clasifica como **locación** (de cosas). Aporta la **norma base del
> tipo**, las **preguntas de diagnóstico** y las **red-flags propias** que el catálogo transversal
> (`red-flags/references/catalogo-red-flags.md`) no cubre.
>
> **No repite** el catálogo transversal (la detección genérica ya corrió en el Paso 2): a las
> red-flags del catálogo se las **remite por nombre y nivel**, no se las reescribe. Los números de
> artículo salen de las anclas verificadas del proyecto; ninguno se cita de memoria. Rige la
> gramática de autoridad y el catálogo cerrado de marcadores de `CLAUDE.base.md` (se referencian, no
> se copian).

---

## Norma base

- **Concepto — CC art. 803.** Régimen de la locación de cosas (una parte concede el uso o goce de una
  cosa; la otra paga un precio en dinero).
- **Plazo máximo — CC art. 807.** El CC fija un **plazo máximo** de la locación. **Ojo: el CC NO fija
  un plazo mínimo** (ver red-flags): no existe un «plazo mínimo legal» locativo en el Código Civil.
- **Mejoras — CC art. 814.** Régimen de las mejoras introducidas por el locatario.
- **Conclusión — CC art. 837.** Causales de conclusión del contrato de locación.

Toda cita al **CC** es al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el authority map).

---

## Preguntas de diagnóstico

Responder antes de opinar sobre conveniencia. Todo dato determinante que falte → `[VACÍO FÁCTICO]`
y pedirlo antes de seguir.

1. **¿Destino?** ¿Vivienda o comercial? El destino condiciona obligaciones, tolerancias y —fuera del
   CC— eventual normativa especial.
2. **¿Plazo y prórroga?** ¿Cuál es el plazo pactado (dentro del máximo del CC art. 807)? ¿Hay prórroga
   automática, renovación o preaviso para no renovar?
3. **¿Canon: moneda y reajuste?** ¿En qué moneda se pacta el canon? ¿Hay **mecanismo de reajuste**
   pactado o el precio queda fijo por todo el plazo? (Ver red-flags: el reajuste **no lo regula el
   CC**.)
4. **¿Depósito / garantía?** ¿Monto del depósito o de la garantía? ¿Está pactada la **regla y el plazo
   de devolución** al terminar?
5. **¿Quién paga qué?** ¿Cómo se reparten **expensas, impuestos y reparaciones** (ordinarias y
   extraordinarias) entre locador y locatario?
6. **¿Mejoras?** ¿Se requiere **autorización** para introducirlas y cuál es su **destino al final**
   (se retiran, quedan, se compensan)? (CC art. 814.)
7. **¿Terminación y preaviso?** ¿Qué **causales de terminación** se pactan y con qué **preaviso**?
   (CC art. 837 para las causales de conclusión legales.)
8. **¿Estado de entrega documentado?** ¿Hay **inventario** o acta del estado del inmueble al entregar,
   que permita medir deterioros al restituir?

---

## Red-flags específicas del tipo

Solo las propias de locación. Las genéricas ya las levantó el motor en el Paso 2 —se remiten por
nombre y nivel, no se reescriben.

> **Advertencia de anclaje (dura).** Dos cuestiones frecuentes en locación **NO están reguladas por
> el CC** (verificado en Fase 0 del proyecto): el **mecanismo de reajuste del canon** y un **plazo
> mínimo** de locación. Toda red-flag sobre ellas es **regla prudencial**, no norma: sale con
> `[VERIFICAR VIGENCIA]` (si hay que remitir a normativa especial) o `[ARGUMENTO SIN NORMA]`. **Nunca
> se les asigna un artículo del CC.**

### L.1 · Ausencia de mecanismo de reajuste del canon

- **Norma anclada:** **NO ANCLABLE en el CC** (el Código no regula el reajuste/actualización del
  precio locativo). Regla prudencial.
- **Detección:** locación de plazo prolongado con canon **fijo en guaraníes** (o en moneda extranjera)
  **sin cláusula de ajuste/indexación** ni criterio de revisión periódica. Riesgo económico de erosión
  del valor, no de invalidez.
- **Consecuencia:** exposición del locador a la pérdida de valor real del canon. Recomendar pactar un
  mecanismo de reajuste; **no invocar un artículo del CC** para exigirlo.
- **Marcador:**
  `[RED FLAG — NIVEL 2: locación de larga duración sin mecanismo de reajuste del canon — [ARGUMENTO SIN NORMA]]`
  (si se necesita apoyar en normativa especial de arrendamientos, `[VERIFICAR VIGENCIA]`).
- **Remisión al catálogo:** coincide en sustancia con la red-flag transversal de **Nivel 2 —
  «ausencia de mecanismo de reajuste en contratos de larga duración»**; no se duplica.

### L.2 · «Plazo mínimo legal» invocado por una parte

- **Norma anclada:** **NO ANCLABLE.** El **CC no fija un plazo mínimo** de locación (solo el máximo del
  art. 807). Cualquier afirmación de un «plazo mínimo legal» **no tiene fundamento en el Código
  Civil**.
- **Detección:** una parte (habitualmente el locatario) invoca un «plazo mínimo legal» de locación para
  resistir una terminación o exigir permanencia, o el contrato lo presupone.
- **Consecuencia:** advertir que **ese plazo mínimo no existe en el CC**; si se pretende fundarlo en
  normativa especial de arrendamientos, debe verificarse su vigencia y ámbito antes de invocarlo. No
  asignarle artículo del CC.
- **Marcador:**
  `[RED FLAG — NIVEL 3: se invoca un "plazo mínimo legal" de locación inexistente en el CC — [VERIFICAR VIGENCIA] sobre normativa especial]`

### L.3 · Depósito sin regla de devolución ni plazo

- **Detección:** contrato que exige **depósito o garantía** pero **no pacta la regla ni el plazo de
  devolución** al terminar (cuándo se restituye, con qué descuentos admisibles, contra qué
  verificación de estado).
- **Consecuencia:** fuente típica de conflicto al finalizar; deja al locatario expuesto a retenciones
  discrecionales. Recomendar pactar plazo y condiciones de devolución, ligadas al inventario de entrega
  (pregunta 8).
- **Marcador:**
  `[RED FLAG — NIVEL 3: depósito/garantía sin regla ni plazo de devolución pactados — [ARGUMENTO SIN NORMA]]`

### L.4 · Terminación sin preaviso pactado

- **Norma anclada:** **CC art. 837** (causales de conclusión de la locación). El defecto es de
  **completitud del pacto**: faltan el preaviso y su plazo, no una causal legal.
- **Detección:** cláusulas que permiten terminar el contrato **sin fijar preaviso** (o su plazo),
  dejando a la contraparte sin margen para reubicarse o recuperar el uso.
- **Consecuencia:** inseguridad para ambas partes; recomendar pactar preaviso y plazo. Las causales de
  conclusión legales del art. 837 rigen igual.
- **Marcador:**
  `[RED FLAG — NIVEL 3: terminación sin preaviso pactado — CC art. 837 (causales de conclusión)]`

### L.5 · Mejoras sin régimen

- **Norma anclada:** **CC art. 814** (mejoras del locatario).
- **Detección:** contrato que **no regula las mejoras**: si requieren autorización previa, quién las
  costea, y qué pasa con ellas al final (retiro, permanencia sin compensación, compensación).
- **Consecuencia:** conflicto probable al restituir; recomendar cláusula expresa de autorización y
  destino de las mejoras, encuadrada en el art. 814.
- **Marcador:**
  `[RED FLAG — NIVEL 3: mejoras del locatario sin régimen de autorización y destino final — CC art. 814]`

---

## Conexiones

- **Proceso de desalojo** — si el conflicto deriva en la necesidad de recuperar el inmueble por vía
  judicial, corresponde al **plugin de litigación** (futuro). Se **menciona sin desarrollar**: esta
  ficha revisa el contrato, no instruye el proceso.
- **Motor `red-flags`** (este plugin) — ya corrió el catálogo transversal en el Paso 2; la ficha solo
  agrega lo propio del tipo y remite al catálogo por nombre/nivel.
