---
name: revision-contractual
description: 'Revisión de contratos civiles y comerciales bajo derecho paraguayo, según la parte que representa el abogado. Clasifica el contrato por sus títulos, corre el motor red-flags completo, aplica la ficha del tipo (servicios, locación, compraventa, confidencialidad) y arma un informe con doble severidad (riesgo jurídico y fricción comercial) y propuestas de redacción quirúrgicas. No cita artículos por número ni recalcula el catálogo: orquesta. Usar cuando el cliente aporta un contrato para analizar antes de firmar o negociar.'
---

# Skill · Revisión contractual (orquestación)

> Skill del plugin `paraguay-contratos`. Es la **cara visible de la revisión**: clasifica, invoca al
> motor, aplica la ficha del tipo y arma el informe. **La detección la hace el motor `red-flags`** (de
> este mismo plugin); esta skill NO repite el catálogo ni redacta normas.
>
> Se rige por las reglas inmodificables y la **gramática de autoridad** de `CLAUDE.base.md`, por el
> **diagnóstico previo** y la skill `citacion` del núcleo (no reproduce sus reglas: las **referencia**),
> y por la **perspectiva neutral según quién consulta** del README del plugin.

---

## 1. Función

- **Clasificar** el contrato aportado (paso 1) antes de mirar cláusula por cláusula.
- **Invocar** al motor `red-flags` en su orden completo (paso 2) — no lo duplica ni lo interrumpe.
- **Aplicar** la ficha del tipo si existe en `references/` (paso 3) y, si hay posiciones del estudio
  cargadas, calibrar la severidad contra ellas.
- **Armar** el informe de revisión con el formato fijo (paso 4) — la interfaz de las fichas y evals.
- **No recalcular** el catálogo, **no citar artículos por número** y **no modificar** el contrato
  aportado antes de entregar el informe.

**Regla de oro normativa:** esta skill **no cita artículos por número**. Las normas viven ancladas en el
catálogo de `red-flags` y en las fichas por tipo. Si es inevitable mencionar una norma fuera de esas
fuentes, sale con `[VERIFICAR VIGENCIA]` — nunca un artículo pelado de memoria. Cuando una red-flag se
convierta en observación citable para el cliente, la cita aplica la disciplina de citación del núcleo:
los 4 controles de autoridad y las plantillas de `shared/authorities/formatos-de-cita.yaml`
(referencia completa: skill `citacion`) — acá no se reproduce esa gramática.

---

## 2. Flujo de trabajo (4 pasos)

### Paso 1 — Clasificación inicial (siempre, antes del análisis fino)

Antes de leer cláusula por cláusula, fijar el encuadre. Todo dato determinante que falte para clasificar
→ `[VACÍO FÁCTICO]` y **pedirlo antes de seguir**.

1. **Tipo de contrato — por los títulos del documento y sus anexos, NO por keywords del cuerpo.** Un
   contrato de 40 páginas con la palabra «confidencial» por todas partes no es un NDA. Se lo ubica en uno
   de los **4 tipos con ficha** (servicios · locación · compraventa · confidencialidad/NDA) o, si no
   encaja, se corre el **motor genérico sin ficha** (solo `red-flags` + análisis contra la ley).
2. **Parte representada.** ¿A quién representa el abogado? (comprador/vendedor, prestador/cliente,
   locador/locatario, divulgante/receptor…). **Preguntarlo SIEMPRE si no surge del contexto**: el análisis
   y los defaults se adaptan a la parte. Sin esto, no se opina sobre conveniencia.
3. **¿Consumidor? ¿Adhesión o paritario?** Detectarlo activa el régimen de defensa del consumidor y de
   cláusulas abusivas **vía el catálogo de `red-flags`** (no se resuelve acá).
4. **¿Relación laboral encubierta?** Si hay indicios de subordinación, **marcarlo y derivar al plugin
   laboral** (`paraguay-laboral`) — no se resuelve en esta skill.
5. **¿Ley aplicable o arbitraje extranjero?** Solo se **detecta** para clasificar; la red-flag y su
   consecuencia viven en el catálogo.
6. **Datos faltantes determinantes** para clasificar → `[VACÍO FÁCTICO]` y pedirlos antes de avanzar.

### Paso 2 — Motor `red-flags` (barrido completo, sin detenerse en la primera)

Invocar la skill `red-flags` **en su orden obligatorio**, sin omitir ni recortar el catálogo:

1. **Invalidez metodológica primero** (plantilla de jurisdicción extranjera). Si aparece, **informarla de
   entrada** y **reclasificar el régimen** (el análisis se hará contra derecho paraguayo) **antes** del
   análisis fino.
2. **Nivel 1 — Nulidad/ineficacia.** Si hay una nulidad estructural, **decirlo ANTES del detalle**: no
   gastar el análisis fino en un contrato inviable. Igual se completa el barrido.
3. **Niveles 2 y 3 completos.** El motor devuelve la lista completa de marcadores.

**Nunca** omitir el catálogo ni frenar en el primer hallazgo: un contrato con una nulidad puede además
tener varias omisiones de nivel 3, y todas van al informe. Esta skill **no interpreta ni reescribe** los
marcadores del motor; los recibe y los ordena en el informe.

### Paso 3 — Ficha por tipo + posiciones del estudio

1. **Ficha del tipo.** Si el tipo clasificado tiene ficha en `references/`, aplicarla. Las fichas
   aportan la norma base del tipo, sus preguntas de diagnóstico y sus red-flags específicas. Se cargan
   **si están presentes**:
   - `references/ficha-servicios.md`
   - `references/ficha-locacion.md`
   - `references/ficha-compraventa.md`
   - `references/ficha-confidencialidad.md`

   > Si el archivo de la ficha del tipo no está presente en la sesión, no inventar su contenido:
   > seguir con el **motor genérico** (paso 2 + análisis contra la ley) y **dejar constancia en el
   > informe** de que la ficha del tipo no estuvo disponible. La ficha de confidencialidad aporta un
   > **triage semáforo** (verde/amarillo/rojo) cuyo veredicto se refleja en el informe.

2. **Posiciones del estudio (playbook local liviano).** Si el archivo **local no versionado**
   `legal.local.md` del abogado tiene la sección **«Posiciones del estudio — contratos»**, comparar cada
   cláusula relevante contra la posición declarada y **clasificar la brecha** en una de estas cuatro:
   - **falta** — la cláusula que el estudio querría no está en el contrato.
   - **más débil que la preferida** — está, pero por debajo de la posición preferida (dentro de lo
     aceptable).
   - **fuera de lo aceptable** — cae por debajo del rango de fallback aceptable.
   - **inaceptable** — choca con una línea roja («nunca aceptar»).

   La severidad se **calibra contra las posiciones propias del estudio**, no contra un «estándar de
   mercado» genérico.

   > **Degradar bien:** si el archivo o la sección no existen, no fallar.

3. **Modo neutral (sin posiciones cargadas).** Si no hay posiciones del estudio disponibles, operar en
   **modo neutral**: analizar contra la ley, apoyado en la parte que se representa (paso 1.2), y
   **declararlo explícitamente en el informe** («Posiciones del estudio: no cargadas — modo neutral»).

### Paso 4 — Informe de revisión

Armar el informe con el **formato fijo** de la sección 3. Es la **interfaz** que consumen las fichas y los
evals: se respetan todas sus secciones y sus títulos, aun cuando una sección quede en «Ninguna».

### Paso 4-bis — Modo resumido (opcional, a pedido)

**Cuándo se usa:** solo si el abogado lo pide **expresamente** («revisión rápida», «resumido», «solo lo
crítico» o equivalente). **El default sigue siendo el informe completo** de la sección 3; esta skill nunca
cambia de formato por iniciativa propia.

**Formato del modo resumido:**

```
## Revisión rápida · [tipo] · [fecha]
**Veredicto:** [2-3 líneas: qué es, para quién se revisa, riesgo de fondo]
**Crítico:** [invalidez metodológica si existe + red-flags Nivel 1, una línea c/u con su marcador]
**Riesgo alto:** [red-flags Nivel 2, una línea c/u]
**Pendientes:** [n.º de marcadores pendientes y cuáles]
_Informe completo disponible a pedido._
```

**Reglas duras del modo resumido:**

a. **Nunca omite** la invalidez metodológica ni las red-flags de Nivel 1 — resumir no es callar nulidades.
b. El catálogo se corre **completo igual**: lo resumido es el **output**, no el análisis (pasos 1-3 no se
   recortan).
c. Si el contrato llegó con instrucción de **modificación directa**, el modo resumido **no reemplaza** al
   informe completo — sigue rigiendo la regla inmodificable 1 (informe completo antes de modificar).
d. Las **posiciones del estudio** y la **doble severidad** se aplican igual; solo se comprime la
   presentación, no el criterio.

---

## 3. Formato del Informe de revisión (interfaz fija)

```
## Informe de revisión · [tipo de contrato] · [fecha]

### Resumen ejecutivo
[2-3 frases: qué es, para quién se revisa, y el veredicto de fondo]

### Clasificación
- Tipo: ... · Adhesión/paritario: ... · Consumidor: sí/no/a verificar
- Parte representada: ...
- Relación laboral encubierta: sí/no/a verificar · Derecho/arbitraje extranjero: sí/no
- Posiciones del estudio: cargadas / no cargadas (modo neutral)

### Invalidez metodológica
[Ninguna detectada / desarrollo]

### Red-flags Nivel 1 — Nulidad/ineficacia
[Ninguna / por ítem: cláusula textual o paráfrasis + norma + consecuencia]

### Red-flags Nivel 2 — Riesgo alto
[por ítem, con propuesta de redacción alternativa]

### Red-flags Nivel 3 — Riesgo medio
[listado con nota breve]

### Análisis por tipo (ficha)
[hallazgos propios del tipo; brecha vs. posiciones del estudio si existen]

### Hallazgos — severidad
[por hallazgo: riesgo jurídico (alto/medio/bajo) ∥ fricción comercial (alta/media/baja) — un hallazgo legalmente válido pero comercialmente ruinoso se reporta]

### Propuestas de redacción
[redlines QUIRÚRGICOS: palabra > frase > oración; cláusula entera solo como último recurso, avisándolo]

### Estado del análisis
- Marcadores pendientes: [dato que falta para resolverlos]
- Normas con [VERIFICAR VIGENCIA]: [listado]
- Decisiones por defecto que el abogado debe confirmar: [o "Ninguna"]
```

**Cómo se llenan las secciones sensibles:**

- **Invalidez metodológica** refleja el resultado del paso 2.1; si el motor la detectó, va acá y ya se
  reclasificó el régimen.
- **Red-flags Nivel 1/2/3** ordenan los marcadores del motor por nivel. Cada ítem describe la cláusula
  (textual o parafraseada) + la norma **anclada en el catálogo** (no un artículo de memoria) + la
  consecuencia. La stack normativa que el catálogo ancle a una red-flag (p. ej. en confidencialidad) se
  cita **desde el campo «norma anclada» del catálogo**, no de memoria.
- **Análisis por tipo** trae los hallazgos propios de la ficha y, si hay posiciones cargadas, la brecha
  clasificada (paso 3.2). Si la ficha del tipo aún no existe, se anota acá.
- **Hallazgos — severidad** asigna a cada hallazgo la **doble severidad**: **riesgo jurídico**
  (alto/medio/bajo) ∥ **fricción comercial** (alta/media/baja). Un hallazgo legalmente válido pero
  comercialmente ruinoso **se reporta igual**.
- **Estado del análisis** cierra con los marcadores pendientes (qué dato falta para resolverlos), las
  normas con `[VERIFICAR VIGENCIA]` y las decisiones por defecto a confirmar (o «Ninguna»).

---

## 4. Reglas inmodificables de la skill (el usuario no las suspende en sesión)

1. **Informe primero, modificación después.** Si el contrato llega con instrucción de modificarlo
   directamente, **primero se entrega el informe completo** y se **pregunta antes de modificar**. No se
   toca el contrato antes de que el abogado lea el informe.
2. **Redacción a la menor granularidad posible.** Las propuestas de redacción son **quirúrgicas**:
   reemplazar una **palabra** antes que una **frase**; una **frase** antes que una **oración**; una
   **cláusula entera solo como último recurso**, cuando editar quirúrgicamente dejaría el texto ilegible
   — **y avisándolo** en el informe.
3. **No citar artículos por número.** Las normas viven en el catálogo de `red-flags` y en las fichas.
   Cualquier mención normativa inevitable fuera de esas fuentes → `[VERIFICAR VIGENCIA]`.

> El **diagnóstico previo** (heredado del núcleo) y la **gramática de autoridad** de `CLAUDE.base.md`, más
> el control de citas de la skill `citacion`, **rigen tal como están** — esta skill los referencia, no los
> copia.

---

## 5. Relación con otras skills

- **`red-flags`** (motor, este plugin) — hace la detección. Esta skill lo invoca en su orden; no lo duplica.
- **`redaccion-contractual`** (este plugin) — redacta contratos nuevos; comparte el motor `red-flags` como QC.
- **`diagnostico`** (núcleo) — el diagnóstico previo obligatorio; corre antes de tocar cualquier escrito.
- **`citacion`** (núcleo) — gobierna cómo se cita una norma cuando una red-flag se vuelve observación citable.
- **`paraguay-laboral`** — destino de la derivación si se detecta relación laboral encubierta (paso 1.4).

---

## 6. Qué NO hace esta skill

- No recalcula ni reescribe el catálogo de `red-flags`: lo invoca completo y ordena su salida.
- No cita artículos por número ni normas de memoria: usa las anclas del catálogo/fichas o `[VERIFICAR VIGENCIA]`.
- No modifica el contrato aportado antes de entregar el informe (regla inmodificable 1).
- No inventa el contenido de una ficha que aún no existe: degrada al motor genérico y lo deja constar.
- No resuelve la relación laboral encubierta ni redacta el contrato: deriva y orquesta.
