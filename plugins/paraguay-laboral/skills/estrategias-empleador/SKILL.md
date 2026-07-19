---
name: estrategias-empleador
description: 'Análisis de contingencia y estrategia laboral para el empleador. Toma el caso (y el monto de liquidación si lo hay) y produce una recomendación de decisión: rango de exposición económica (mínimo/probable/máximo), vacíos probatorios del empleador, riesgo MTESS/IPS/judicial, y la recomendación entre negociar/intimar/despedir/documentar/esperar/conciliar/litigar, con la oferta de menor costo y la comunicación a preparar. Usar cuando el cliente empleador necesita decidir qué hacer, no solo saber qué dice la ley.'
---

# Skill · Estrategia y contingencia (empleador)

> Skill del plugin `paraguay-laboral`, **orientación patronal**. Es donde el sistema deja de "decir la
> ley" y pasa a **recomendar una decisión**. No calcula (eso es `calculo-laboral`/`liquidaciones`) ni
> audita el escrito (eso es `diagnostico`): **integra** todo en una estrategia.
>
> Se rige por el agente `asistente-paraguay` y por el perfil patronal del README del plugin
> (regla nº10: mala fe procesal, contingencia económica, conveniencia transaccional).

---

## 1. Función

Responder la pregunta que de verdad le importa al cliente empleador: **¿qué conviene hacer?** Y
fundamentarlo con: cuánto puede costar, qué prueba falta, qué riesgos hay y cuál es el próximo paso.

No es teoría jurídica: es **análisis orientado a la decisión**, dentro de lo jurídicamente defendible
(nunca a costa de la legalidad).

---

## 2. Insumos que toma

- **El diagnóstico** (`diagnostico` del núcleo): hechos, vacíos fácticos y probatorios, riesgos.
- **El monto** (`liquidaciones` → `calculo-laboral`): la liquidación de cese y, si aplica, la
  estimación en juicio (con compensatoria/complementaria).
- **El perfil patronal** (README): sector, circunscripción, tolerancia al riesgo.

Si falta alguno, lo pide o lo marca: sin liquidación no hay rango económico; sin diagnóstico no hay
mapa de vacíos.

---

## 3. Salida: análisis de contingencia (8 puntos)

Entregar en bloque, en este orden (de `04-mvp-laboral.md` §6):

### 1. Rango de exposición económica
- **Mínimo** (escenario favorable al empleador), **probable**, **máximo** (peor escenario en juicio).
- El mínimo suele ser la liquidación de cese bien pagada; el máximo, la estimación judicial con
  compensatoria (20%) + complementaria + intereses. Las cifras judiciales son **estimaciones** (la
  tasa de interés es jurisprudencial, la complementaria depende del criterio del juez).

### 2. Vacíos probatorios del empleador
- Qué prueba le falta al empleador para sostener su posición → `[VACÍO PROBATORIO]`.
- Típicos: falta de registro de horas extras (art. 206 CT), ausencia de comunicaciones fehacientes,
  causal de despido sin documentación contemporánea, recibos no firmados.

### 3. Argumentos esperables del trabajador
- Qué reclamará razonablemente la contraparte (despido injustificado, horas extras no pagadas,
  diferencias salariales, falta de aportes IPS). No exhaustivo: anticipación estratégica.

### 4. Riesgo MTESS
- Multas, actas de inspección, infracciones (registro, jornada, seguridad e higiene, salario mínimo).
- Si hay sumario o inspección en curso, derivar a la defensa administrativa correspondiente.

### 5. Riesgo IPS
- Aportes adeudados o no declarados, denuncias del trabajador, diferencias de salario declarado.
- Recordar el aporte obrero 9% y patronal 16,5%: la subdeclaración es contingencia concreta.

### 6. Riesgo judicial
- Probabilidad de condena y su magnitud; mala fe procesal de la contraparte; chicanas previsibles;
  solidez probatoria del empleador. Si el empleador está mal documentado, el riesgo sube.

### 7. Recomendación
- Una recomendación **explícita** entre: **negociar / intimar / despedir / documentar / esperar /
  conciliar / litigar**, con sus supuestos. El abogado decide; la skill fundamenta.
- Regla patronal: priorizar el **acuerdo eficiente, documentado y ejecutable** cuando reduce
  exposición sin sacrificar legalidad.

### 8. Oferta de menor costo + comunicación a preparar
- La **oferta sugerida** (monto/condiciones) que minimiza la exposición dentro de lo defendible.
- Qué **comunicación** preparar (intimación, oferta transaccional, acta de acuerdo, telegrama/nota),
  derivando su redacción a la skill correspondiente.

---

## 4. Disciplina

- **No prometer resultados:** el rango es estimación; los montos judiciales dependen de prueba y criterio.
- **No recomendar despido** sin evaluar prueba documental (regla del perfil patronal).
- **No inflar ni minimizar** la exposición: el cliente decide con números honestos.
- Marcadores cuando falte base: `[VACÍO FÁCTICO]` (hecho), `[VACÍO PROBATORIO]` (prueba),
  `[VERIFICAR VIGENCIA]` (norma del cálculo o del plazo).
- La estrategia es **insumo** para el abogado, no asesoramiento definitivo (ver `asistente-paraguay`).

---

## 5. Relación con otras skills

- **`diagnostico`** (núcleo) — provee el mapa de hechos/vacíos/riesgos que esta skill convierte en estrategia.
- **`liquidaciones` / `calculo-laboral`** — proveen el rango económico.
- **`despidos`** — si la decisión incluye despedir, esa skill clasifica la causal y su prueba.
- **`dictamenes`** — **formaliza** este análisis en un dictamen jurídico entregable al cliente. Si el
  cliente pide la estrategia por escrito como opinión legal, derivar a `dictamenes` (que comparte la
  metodología de análisis de riesgos: identificar → cuantificar → mitigar → contexto paraguayo).
- **`plazos`** (núcleo) — si hay un plazo en juego (caducidad del art. 401 CT —30 días desde el conocimiento—
  antes de despido justificado, prescripción), encuadrarlo y advertir.
- **`citacion`** (núcleo) — gobierna cómo se citan las normas invocadas.

---

## 6. Qué NO hace esta skill

- No calcula la liquidación (la pide a `liquidaciones`/`calculo-laboral`).
- No redacta los escritos: deriva su redacción.
- No decide por el abogado: recomienda con fundamento y explicita los supuestos.
- No garantiza el resultado de un juicio: trabaja con rangos y probabilidades, no certezas.
