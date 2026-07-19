# Ficha · Contrato de servicios

> Ficha de tipo de la skill `revision-contractual` (plugin `paraguay-contratos`), aplicada en su
> **Paso 3** cuando el contrato se clasifica como **servicios**. Aporta la **norma base del tipo**,
> las **preguntas de diagnóstico** y las **red-flags propias** que el catálogo transversal
> (`red-flags/references/catalogo-red-flags.md`) no cubre.
>
> **No repite** el catálogo transversal (la detección genérica ya corrió en el Paso 2): a las
> red-flags del catálogo se las **remite por nombre y nivel**, no se las reescribe. Los números de
> artículo salen de las anclas verificadas del proyecto; ninguno se cita de memoria. Rige la
> gramática de autoridad y el catálogo cerrado de marcadores de `CLAUDE.base.md` (se referencian,
> no se copian).

---

## Norma base

- **Contrato de servicios — CC arts. 845-851.** Régimen del contrato por el que una parte se obliga
  a prestar un **servicio** (una actividad) a cambio de una retribución. El **CC art. 846** fija que
  la prestación es **personal e incesible salvo pacto** en contrario. El **CC art. 851** regula la
  **terminación por justos motivos**.
- **Distinción con la obra — CC art. 852 y ss.** El criterio de deslinde es el **objeto de la
  obligación**: en **servicios** se debe una **actividad** (medios); en **obra** se debe un
  **resultado determinado**. La calificación cambia el régimen de riesgos, de pago y de recepción,
  así que fijarla es el primer paso de la ficha.

Toda cita al **CC** es al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el authority map).

---

## Preguntas de diagnóstico

Responder antes de opinar sobre conveniencia. Todo dato determinante que falte → `[VACÍO FÁCTICO]`
y pedirlo antes de seguir.

1. **¿Medios o resultado?** ¿La obligación central es desplegar una **actividad diligente**
   (servicios) o **entregar un resultado determinado** (obra)? De esto depende el régimen aplicable
   (CC arts. 845-851 vs. 852 y ss.) y quién carga con el riesgo del no logro.
2. **¿Prestación personal o cesible?** ¿El contrato respeta el default del **CC art. 846** (personal
   e incesible) o **pacta** expresamente la sustitución/subcontratación del prestador? Si guarda
   silencio, rige el default.
3. **¿Exclusividad, horario y herramientas?** ¿Se pacta exclusividad? ¿Horario o jornada fijos?
   ¿Quién provee las **herramientas/medios** (el prestador o el comitente)? ¿El prestador se integra
   a la organización del comitente? (Insumo directo del test de subordinación — ver red-flags.)
4. **¿Quién es dueño del entregable / la PI?** ¿El contrato define la **titularidad** de lo producido
   (informes, código, diseños, material) y de los derechos de propiedad intelectual? Si calla, la
   titularidad queda en zona gris.
5. **¿Cómo se determinan los honorarios y los cambios de alcance?** ¿Precio fijo, por hora, por hito?
   ¿Hay procedimiento para **cambios de alcance** (scope creep) y su repricing? ¿La aprobación/pago
   depende de un criterio objetivo o de la mera **satisfacción del cliente**? (Ver red-flags.)
6. **¿Terminación por justos motivos pactada?** ¿El contrato prevé la **terminación por justos
   motivos** (CC art. 851) y sus consecuencias (preaviso, liquidación de lo devengado)?

---

## Red-flags específicas del tipo

Solo las propias de servicios. Las genéricas ya las levantó el motor en el Paso 2 —se remiten por
nombre y nivel, no se reescriben.

### S.1 · Relación laboral encubierta (subordinación bajo forma de servicios)

- **Detección — test de subordinación.** Indicios acumulables: **exclusividad** + **horario/jornada
  fijos** + **herramientas y medios provistos por el comitente** + **integración a la organización**
  (instrucciones, control, supervisión jerárquica, pago periódico tipo salario). Cuantos más
  indicadores concurran, más fuerte la señal.
- **Consecuencia:** al detectar indicios, **NO resolver la laboralidad en esta ficha** (la
  calificación depende de prueba de los hechos). Emitir **`[VACÍO PROBATORIO]`**
  (exclusividad/horario/subordinación deben acreditarse) y **derivar al plugin `paraguay-laboral`**.
- **Remisión al catálogo:** coincide con la red-flag transversal de **Nivel 1 — «simulación de
  relación laboral bajo contrato civil»**; la ficha no la duplica, la refuerza con el test propio del
  tipo y confirma la derivación.

### S.2 · «Satisfacción del cliente» como condición de pago

- **Detección:** cláusulas que subordinan el pago (o la recepción/aprobación del trabajo) a la
  **satisfacción, conformidad o criterio discrecional del cliente**, sin parámetro objetivo. En un
  contrato de **medios**, esto **convierte de hecho la obligación en una de resultado unilateral**:
  el prestador cumple su actividad diligente pero no cobra hasta que la contraparte declare estar
  satisfecha.
- **Consecuencia:** desnaturaliza el régimen de servicios (CC arts. 845-851) y traslada al prestador
  un riesgo que el tipo no le asigna. Si se representa al **prestador**, proponer un criterio de
  aceptación objetivo (hitos verificables, plazo de observaciones, aprobación tácita por silencio).
  Si se representa al **comitente**, es una cláusula favorable pero de **alta fricción comercial**.
- **Marcador:**
  `[RED FLAG — NIVEL 2: pago sujeto a "satisfacción del cliente" desnaturaliza la obligación de medios — CC arts. 845-851]`

### S.3 · No competencia sin límites de zona, actividad o plazo

- **Norma anclada:** **Ley N° 1034/1983 art. 106** (pacto de no competencia: válido si delimita
  **zona + actividad + plazo**, con **tope de 5 años**). La cláusula abierta sin secretos expresos se
  vincula al **art. 108 inc. d** de la misma ley.
- **Detección:** cláusula de no competencia impuesta al prestador **sin delimitar zona geográfica,
  actividad prohibida o plazo**, o con **plazo superior a 5 años**.
- **Consecuencia:** excede el marco del art. 106 y queda expuesta a invalidación o reducción. Acotar
  a los tres límites y al tope temporal.
- **Marcador:**
  `[RED FLAG — NIVEL 2: pacto de no competencia sin límites de zona/actividad/plazo o mayor a 5 años — Ley N° 1034/1983 art. 106]`

### S.4 · PI del entregable sin cláusula de titularidad

- **Norma anclada:** **sin ancla verificada.** El **régimen de propiedad intelectual sobre el
  entregable no está en la tabla de anclajes del proyecto** → **no citar la ley de derechos de autor
  por número**. Si el contrato calla, la titularidad del entregable y de sus derechos queda en **zona
  gris** (default legal no verificado en el authority map).
- **Detección:** contrato de servicios que produce material susceptible de PI (software, textos,
  diseños, informes, bases de datos) **sin cláusula** que asigne la titularidad de la obra ni de sus
  derechos de explotación.
- **Consecuencia:** al firmar sin cláusula, el comitente puede no adquirir la PI que cree pagar, y el
  prestador puede quedar atado más de lo previsto. Recomendar una cláusula expresa de titularidad y
  cesión. **No afirmar el régimen supletorio sin verificarlo.**
- **Marcador:**
  `[RED FLAG — NIVEL 2: titularidad de la PI del entregable no pactada; régimen supletorio [VERIFICAR VIGENCIA]]`

---

## Conexiones

- **Plugin `paraguay-laboral`** — destino de la derivación si el test de subordinación (S.1) arroja
  indicios de **relación laboral encubierta**. Esta ficha detecta y deriva; no califica la
  laboralidad.
- **Skill `contrato-trabajo`** — si el diagnóstico concluye que lo que corresponde **no es un
  contrato de servicios sino uno laboral**, el instrumento a redactar es un contrato de trabajo: esa
  skill (materia laboral) lo genera. No se resuelve en esta ficha.
- **Motor `red-flags`** (este plugin) — ya corrió el catálogo transversal en el Paso 2; la ficha solo
  agrega lo propio del tipo y remite al catálogo por nombre/nivel.
