# Ficha · Contrato de confidencialidad (NDA)

> Ficha de tipo de la skill `revision-contractual` (plugin `paraguay-contratos`), aplicada en su
> **Paso 3** cuando el contrato se clasifica como **confidencialidad / NDA**. Aporta la **norma base
> del tipo**, las **preguntas de diagnóstico**, un **triage semáforo** propio (el corazón de la ficha)
> y las **red-flags propias** que el catálogo transversal
> (`red-flags/references/catalogo-red-flags.md`) no cubre.
>
> **No repite** el catálogo transversal (la detección genérica ya corrió en el Paso 2): a las
> red-flags del catálogo se las **remite por nombre y nivel**, no se las reescribe. Los números de
> artículo salen de las anclas verificadas del proyecto; ninguno se cita de memoria. Rige la
> gramática de autoridad y el catálogo cerrado de marcadores de `CLAUDE.base.md` (se referencian, no
> se copian).

---

## Norma base (stack del NDA)

- **Base contractual — CC arts. 715 y 673**, con el límite del **CC art. 9** (orden público y buenas
  costumbres). El art. 715 da fuerza obligatoria al pacto; el art. 673 fija los requisitos esenciales;
  el art. 9 marca el techo de lo pactable.
- **Protección sustantiva de secretos — Ley N° 3283/2007, Cap. I, arts. 1, 2, 3.B, 5 y 8** (`verified`
  en el authority map). El art. 3.B nombra expresamente el incumplimiento de cláusulas de
  confidencialidad. **Reserva dura:** **NO citar el plazo de 3 años del art. 7** de esta ley —está
  anclado a la presentación ante la autoridad sanitaria y **no se traslada** a un NDA civil genérico.
  La **aplicación de esta ley a NDAs genéricos** (fuera del supuesto sanitario) es interpretativa: si
  se afirma, requiere **`[INSERTAR JURISPRUDENCIA VERIFICADA]`**.
- **No competencia / competencia desleal (conexión indirecta) — Ley N° 1034/1983 arts. 106 y 108
  inc. d.** El art. 106 (pacto de no competencia: zona + actividad + tope de 5 años) es relevante si el
  «NDA» incorpora obligaciones de no competencia; el art. 108 inc. d es la cláusula abierta de
  competencia desleal.
- **Palanca penal complementaria — CP arts. 147-149** (`verified` en el authority map; el art. 148
  según su redacción por la Ley N° 3440/2008). **Es de acción penal a instancia de la víctima**, no de
  oficio. La **conexión NDA → CP art. 147** (revelación de secretos) es **interpretativa**: al usarla,
  **`[VERIFICAR VIGENCIA]`**; nunca afirmar aplicación judicial concreta sin
  **`[INSERTAR JURISPRUDENCIA VERIFICADA]`**. La dimensión penal se usa **solo como advertencia
  informativa**, jamás como amenaza redactada.

Toda cita al **CC** es al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el authority map).

---

## Preguntas de diagnóstico

Responder antes de opinar sobre conveniencia. Todo dato determinante que falte → `[VACÍO FÁCTICO]`
y pedirlo antes de seguir.

1. **¿Uni o bilateral?** ¿Solo una parte divulga (unilateral) o ambas intercambian (bilateral)? Define
   quién carga con las obligaciones.
2. **¿Qué información cubre y cómo se identifica?** ¿La información confidencial está **definida y
   marcada** (por rótulo, por listado, por confirmación escrita), o se define en forma total/circular?
3. **¿Exclusiones estándar?** ¿Excluye lo que debe: información **pública**, **conocida previamente**,
   **recibida de un tercero legítimo**, **desarrollada independientemente** y **requerida por
   autoridad** competente?
4. **¿Plazo determinado y razonable?** ¿Fija un **plazo de duración** de la obligación, y es
   **razonable para el tipo de información** de que se trata?
5. **¿Cláusula penal proporcional?** Si hay pena por incumplimiento, ¿el monto es **proporcional**?
   (Régimen y morigeración: **CC arts. 454 y 459**.)
6. **¿Devolución o destrucción al terminar?** ¿Se pacta **devolver o destruir** la información al
   concluir, y qué pasa con **copias y backups**?

---

## Triage semáforo (el corazón de la ficha)

El NDA se resuelve con un **veredicto de tres estados**. El veredicto se **refleja en el informe** de la
skill `revision-contractual`.

### VERDE — pasa todas las posiciones del estudio

**Definición.** El NDA **pasa todas las posiciones del estudio** cargadas y no arrastra marcadores
pendientes.

**REGLAS DURAS (no se suspenden en sesión):**

- **(a)** **NO se emite verde** si las **«Posiciones del estudio»** de `legal.local.md` **no están
  cargadas / revisadas por el abogado**. El **default honesto es AMARILLO**: sin posiciones cargadas,
  el triage no puede afirmar conformidad.
- **(b)** **NO se emite verde** si **alguna norma del análisis quedó con un marcador pendiente**
  (`[VERIFICAR VIGENCIA]`, `[INSERTAR JURISPRUDENCIA VERIFICADA]`, `[FUENTE OFICIAL PENDIENTE]`,
  `[VACÍO FÁCTICO]`, `[VACÍO PROBATORIO]`, `[ARGUMENTO SIN NORMA]`).
- **(c)** El **verde NO es aprobación legal final.** Significa **conformidad con las posiciones cargadas
  y las fuentes verificadas en sesión**; la **decisión de firmar es siempre del abogado**.

**Declaración obligatoria en el output (textual).** Todo veredicto VERDE incluye en el informe la
leyenda: *«VERDE = conformidad con las posiciones del estudio cargadas y las fuentes verificadas en
sesión; NO es aprobación legal final. La decisión de firmar es del abogado.»*

### AMARILLO — desvíos no fatales o término no cubierto

**Definición.** Hay **desvíos no fatales**, o un **término que las posiciones del estudio no cubren**.
También es AMARILLO el **default honesto** cuando no hay posiciones cargadas (regla dura (a)).

**AMARILLO AUTOMÁTICO (regla operativa dura).** Si el «NDA» contiene **obligaciones más allá de la
confidencialidad** —**no competencia**, **exclusividad**, **cesión de PI**, **mínimos de compra** u
otras—, **es otro contrato disfrazado de NDA**: **sale del triage semáforo** y **va a revisión completa
por `revision-contractual`** (motor `red-flags` completo + ficha del tipo real, p. ej. servicios). El
triage no lo aprueba ni lo rechaza: lo **reclasifica** y lo deriva.

### ROJO — choca con una línea roja o es estructuralmente incompatible

**Definición.** El NDA **choca con una posición «nunca aceptar»** del estudio, **o** tiene una
**estructura incompatible** — por ejemplo, **confidencialidad perpetua sobre información que ya es
pública**, u **obligaciones imposibles de cumplir**.

---

## Red-flags específicas del tipo

Solo las propias del NDA. Las genéricas ya las levantó el motor en el Paso 2 —se remiten por nombre y
nivel, no se reescriben.

### NDA.1 · Confidencialidad sin plazo determinado

- **Norma anclada:** stack del NDA (**Ley N° 3283/2007 Cap. I**; base contractual **CC art. 715**).
- **Detección:** obligación de confidencialidad que **no fija plazo** (ni desde/hasta cuándo) o que la
  extiende de forma perpetua e indeterminada.
- **Consecuencia:** **remitir al catálogo transversal (Nivel 2 — «confidencialidad sin plazo
  determinado»)** y a la **regla de la skill de redacción** sobre plazos razonables por tipo de
  información; no se reescribe el catálogo.
- **Marcador:**
  `[RED FLAG — NIVEL 2: cláusula de confidencialidad sin plazo determinado — Ley N° 3283/2007 Cap. I]`

### NDA.2 · Sin exclusiones estándar

- **Detección:** la definición de información confidencial **no excluye** los supuestos estándar
  (pública / conocida previamente / recibida de tercero legítimo / desarrollada independientemente /
  requerida por autoridad). Sin esas exclusiones, la obligación puede volverse **imposible de cumplir**
  (obliga a proteger lo que ya es público o de conocimiento propio).
- **Consecuencia:** recomendar incorporar el elenco estándar de exclusiones. Ligada a la incompatibilidad
  estructural del ROJO cuando la obligación resulta directamente imposible.
- **Marcador:**
  `[RED FLAG — NIVEL 2: definición de información confidencial sin las exclusiones estándar — [ARGUMENTO SIN NORMA]]`

### NDA.3 · «Información confidencial» circular o total

- **Detección:** la información se define en forma **circular o total** —«toda información
  intercambiada», «cualquier dato al que se acceda»— sin criterio de identificación (rótulo, listado,
  confirmación). Vuelve la obligación inabarcable e incierta.
- **Consecuencia:** recomendar una definición delimitada, con mecanismo de marcado o identificación.
- **Marcador:**
  `[RED FLAG — NIVEL 2: "información confidencial" definida en forma circular o total — [ARGUMENTO SIN NORMA]]`

### NDA.4 · Cláusula penal desproporcionada

- **Norma anclada:** **CC arts. 454 y 459** (la pena sustituye la indemnización; el juez puede
  **reducirla equitativamente** si es manifiestamente excesiva).
- **Detección:** pena por violación de confidencialidad **desproporcionada** frente al perjuicio
  previsible.
- **Consecuencia:** sujeta a morigeración judicial; recomendar un monto proporcional. Coincide con la
  red-flag transversal de **Nivel 2 — «cláusula penal manifiestamente excesiva»**; no se duplica.
- **Marcador:**
  `[RED FLAG — NIVEL 2: cláusula penal por confidencialidad posiblemente excesiva, sujeta a morigeración — CC arts. 454 y 459]`

### NDA.5 · Obligación sobre información ya pública al firmar

- **Detección:** la obligación de confidencialidad **recae sobre información que ya era pública al
  momento de firmar** (o de conocimiento general). Es una obligación **estructuralmente imposible o sin
  objeto protegible**.
- **Consecuencia:** dispara la evaluación de **ROJO** (estructura incompatible). Recomendar excluir lo
  público y delimitar el objeto.
- **Marcador:**
  `[RED FLAG — NIVEL 2: confidencialidad sobre información ya pública al firmar (objeto no protegible) — [ARGUMENTO SIN NORMA]]`

---

## Conexiones

- **No competencia detectada** → si el «NDA» incorpora un **pacto de no competencia**, remitir a la
  **`ficha-servicios.md`** y al **catálogo transversal**, con el encuadre del **art. 106 de la Ley
  N° 1034/1983** (zona + actividad + tope de 5 años). Suele activar además el **AMARILLO AUTOMÁTICO**
  (contrato disfrazado).
- **Dimensión penal** → **solo como advertencia informativa** (acción **a instancia de la víctima**,
  CP arts. 147-149). **Nunca redactar la dimensión penal como amenaza** dirigida a la contraparte.
- **Motor `red-flags`** (este plugin) — ya corrió el catálogo transversal en el Paso 2; la ficha solo
  agrega lo propio del tipo y remite al catálogo por nombre/nivel.
