# Ficha · Contrato de compraventa

> Ficha de tipo de la skill `revision-contractual` (plugin `paraguay-contratos`), aplicada en su
> **Paso 3** cuando el contrato se clasifica como **compraventa**. Aporta la **norma base del tipo**,
> las **preguntas de diagnóstico** y las **red-flags propias** que el catálogo transversal
> (`red-flags/references/catalogo-red-flags.md`) no cubre.
>
> **No repite** el catálogo transversal (la detección genérica ya corrió en el Paso 2): a las
> red-flags del catálogo se las **remite por nombre y nivel**, no se las reescribe. Los números de
> artículo salen de las anclas verificadas del proyecto; ninguno se cita de memoria. Rige la
> gramática de autoridad y el catálogo cerrado de marcadores de `CLAUDE.base.md` (se referencian, no
> se copian).

---

## Norma base

- **Compraventa de cosa ajena — CC arts. 743-744.** Régimen de la venta de una cosa que no pertenece
  al vendedor.
- **Escritura pública — CC arts. 700-702.** Actos que exigen escritura pública (inmuebles y demás
  actos registrables): el instrumento privado deficiente vale como obligación de escriturar (art. 701)
  y su otorgamiento puede demandarse (art. 702). El contrato privado, por sí, **no transfiere el
  dominio** del bien registrable.
- **Evicción — CC art. 1759.** El adquirente a título oneroso responde si es privado del derecho
  adquirido.
- **Vicios redhibitorios — CC art. 1789.** Vicios ocultos que hacen la cosa impropia para su destino.
  **Plazo de la acción redhibitoria: CC art. 668 (tres meses)** — ubicado en el **Libro II
  (prescripción liberatoria)**, no junto al art. 1789.
- **Pacto de retroventa — Ley N° 701/1995** (`verified` en el authority map). Régimen del pacto por el
  que el vendedor se reserva recuperar la cosa vendida.

Toda cita al **CC** es al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el authority map).

---

## Preguntas de diagnóstico

Responder antes de opinar sobre conveniencia. Todo dato determinante que falte → `[VACÍO FÁCTICO]`
y pedirlo antes de seguir.

1. **¿Bien mueble o inmueble/registrable?** ¿Qué se vende y bajo qué régimen de transmisión? Define si
   se exige escritura pública e inscripción (CC arts. 700-702).
2. **¿El vendedor es titular?** ¿Hay **título a la vista** que acredite la titularidad del vendedor?
   (Riesgo de venta de cosa ajena, CC arts. 743-744.)
3. **¿Gravámenes verificados?** ¿Se comprobó la existencia de **hipoteca, embargo, prenda** u otros
   gravámenes sobre el bien?
4. **¿Precio?** ¿Moneda, forma de pago, y si hay saldo, con qué **garantía**?
5. **¿Entrega y traslación de riesgos?** ¿Están pactadas la **entrega** y el momento de **traslación de
   los riesgos** de la cosa?
6. **¿Evicción y vicios?** ¿Las garantías de **evicción (CC art. 1759)** y **vicios redhibitorios
   (CC art. 1789)** se mantienen, se amplían o se excluyen?
7. **¿Pactos especiales?** ¿Hay **retroventa (Ley N° 701/1995)** u otros pactos especiales sobre la
   operación?

---

## Red-flags específicas del tipo

Solo las propias de compraventa. Las genéricas ya las levantó el motor en el Paso 2 —se remiten por
nombre y nivel, no se reescriben.

### CV.1 · Bien registrable sin cláusula de escrituración e inscripción

- **Norma anclada:** **CC arts. 700-702.** El **contrato privado NO transfiere el dominio** de un bien
  registrable: hace nacer la **obligación de escriturar** (art. 701), exigible judicialmente (art. 702).
- **Detección:** compraventa de **inmueble o vehículo** (u otro bien registrable) que **no prevé la
  escrituración ni la inscripción registral** a favor del comprador, o no fija quién y cuándo debe
  otorgar la escritura/transferir el registro.
- **Consecuencia:** el comprador que paga contra un contrato privado **no adquiere el dominio** hasta
  escriturar e inscribir. Recomendar cláusula de escrituración con plazo y responsable.
- **Marcador:**
  `[RED FLAG — NIVEL 2: compraventa de bien registrable sin cláusula de escrituración/inscripción — CC arts. 700-702]`
- **Remisión al catálogo:** coincide con la red-flag transversal de **Nivel 2 — «compraventa de bien
  registrable sin cláusula de escrituración/inscripción»**; no se duplica.

### CV.2 · Venta de cosa ajena sin advertirlo

- **Norma anclada:** **CC arts. 743-744** (compraventa de cosa ajena).
- **Detección:** vendedor que **no es el titular** del bien (o no lo acredita) y el contrato **no
  advierte** esa condición ni prevé cómo se saneará (adquisición previa, ratificación del dueño).
  Verificar contra el título (pregunta 2).
- **Consecuencia:** riesgo para el comprador de no adquirir válidamente. Exigir acreditación de
  titularidad o encuadrar expresamente la operación en el régimen de cosa ajena.
- **Marcador:**
  `[RED FLAG — NIVEL 2: venta de cosa ajena sin advertirlo ni prever su saneamiento — CC arts. 743-744]`

### CV.3 · Exclusión total de evicción y vicios redhibitorios

- **Norma anclada:** **CC art. 1759** (evicción) y **CC art. 1789** (vicios redhibitorios).
- **Detección:** cláusulas que **excluyen o renuncian totalmente** a la garantía de evicción y/o a la
  de vicios redhibitorios, dejando al comprador sin cobertura si un tercero reclama la cosa o si
  aparece un defecto oculto.
- **Consecuencia:** deja al comprador expuesto. **Remitir al catálogo transversal (Nivel 2 — «omisión
  de garantías de evicción y vicios redhibitorios»)** y a la **interpretación restrictiva** de las
  cláusulas que exoneran garantías legales; no se reescribe el catálogo.
- **Marcador:**
  `[RED FLAG — NIVEL 2: exclusión total de evicción y vicios redhibitorios — CC arts. 1759 y 1789 (plazo redhibitoria art. 668)]`

### CV.4 · Plazo corto de la acción redhibitoria (advertencia al comprador)

- **Norma anclada:** **CC art. 668 (tres meses)** — plazo de la acción por vicios redhibitorios,
  ubicado en el **Libro II (prescripción liberatoria)**.
- **Detección:** más que un defecto del texto, es una **advertencia estratégica al comprador**: la
  acción por vicios ocultos tiene un **plazo corto (3 meses, CC art. 668)**, por lo que conviene prever
  un mecanismo de inspección/reclamo temprano y dejar constancia de defectos apenas se detecten.
- **Consecuencia:** el comprador que descubre un vicio tarde puede quedar fuera de plazo. Advertirlo y,
  si se representa al comprador, recomendar cláusula de recepción con período de observación.
- **Marcador:**
  `[RED FLAG — NIVEL 3: plazo corto de la acción redhibitoria (3 meses) — advertir al comprador — CC art. 668]`

### CV.5 · Retroventa sin los límites de la Ley N° 701/1995

- **Norma anclada:** **Ley N° 701/1995** (`verified` en el authority map). El **alcance exacto** de sus
  límites **no está en la tabla de anclajes del proyecto**.
- **Detección:** pacto de **retroventa** que no respeta (o cuyo respeto no puede confirmarse) los
  límites de la Ley N° 701/1995 (p. ej. plazo o condiciones del rescate).
- **Consecuencia:** riesgo de invalidez o ineficacia del pacto. Verificar su encuadre en la ley antes de
  validarlo; **no afirmar el alcance exacto de sus límites sin verificarlo**.
- **Marcador:**
  `[RED FLAG — NIVEL 2: pacto de retroventa cuyo encuadre en la Ley N° 701/1995 no está confirmado — [VERIFICAR VIGENCIA] sobre su alcance exacto]`

---

## Conexiones

- **Régimen de consumidor** — si la compraventa es a **consumidor final**, se activa el régimen de la
  **Ley N° 1334/1998** (defensa del consumidor y cláusulas abusivas en adhesión), que corre **vía el
  catálogo transversal** (Nivel 1 — «cláusulas abusivas en contrato de adhesión con consumidor»). No se
  resuelve en esta ficha: se detecta y se remite al catálogo.
- **Motor `red-flags`** (este plugin) — ya corrió el catálogo transversal en el Paso 2; la ficha solo
  agrega lo propio del tipo y remite al catálogo por nombre/nivel.
