---
name: calculo-laboral
description: Calcula liquidaciones laborales paraguayas (despido injustificado, renuncia, retiro justificado, mutuo acuerdo, despido justificado, fin de plazo) y rubros salariales corrientes (horas extras diurnas 50%, nocturnas 30%, extras nocturnas 100% y feriados 100%, art. 234 CT) según el Código del Trabajo (Ley 213/93) y el Código Procesal del Trabajo (Ley 742/61). Pide los datos mínimos, aplica las escalas de preaviso (art. 87), vacaciones (art. 218) e indemnización (art. 91), el descuento IPS 9%, y muestra el cálculo detallado en guaraníes. Es el motor de cálculo del que depende la skill liquidaciones.
---

# Skill · Cálculo de liquidaciones laborales (Paraguay)

> **Origen y atribución.** Contenido portado de la skill `calculo-laboral` de Miguel Fernando Díaz, incorporado al repositorio bajo Apache-2.0. Las normas citadas (Ley 213/93 y Ley 742/61) están `verified` en el mapa de autoridad (`leyes.yaml`: `codigo_trabajo`, `codigo_procesal_trabajo`).
>
> **Disciplina aplicada.** Toda cifra de tasa o de práctica judicial se presenta como **estimación**,
> no como dato legal. La tasa de interés es jurisprudencial (no legal): se proyecta sujeta a la tasa
> BCP vigente. Ver reglas del agente `asistente-paraguay`.

Calcula liquidaciones conforme al Código del Trabajo paraguayo (Ley 213/93) y el Código Procesal del
Trabajo (Ley 742/61).

## Tipos de terminación del contrato

1. **Despido injustificado** — el empleador despide sin causa válida.
2. **Renuncia voluntaria** — el trabajador renuncia por su voluntad.
3. **Retiro justificado** (art. 84 CT) — el trabajador se retira por culpa del empleador.
4. **Mutuo acuerdo** (art. 78 inc. b) — ambas partes acuerdan terminar.
5. **Despido justificado** (art. 81 CT) — el empleador despide con causa válida.
6. **Término de contrato a plazo** — vence el contrato de plazo fijo.

## Flujo de trabajo

### Paso 1 — Identificar tipo de terminación
Preguntar cómo terminó la relación laboral.

### Paso 2 — Datos básicos
- Fecha de ingreso.
- Fecha de salida/despido.
- Salario base mensual (en guaraníes).

### Paso 3 — Salarios para promedios
Últimos 6 meses de salario (meses enteros), del más reciente completo hacia atrás.
Si falta algún dato determinante → `[VACÍO FÁCTICO]` y pedirlo antes de calcular.

### Paso 4 — Datos adicionales según el caso
- **Aguinaldo proporcional:** total percibido en el año calendario hasta la fecha de salida.
- **¿Liquidación en sede judicial?** Si el cliente quiere saber el monto **en juicio**, se agregan los
  rubros judiciales (compensatoria y complementaria). Si es liquidación extrajudicial/de cese, NO.
  - Si va a juicio — **Compensatoria:** ¿el empleador pagó la liquidación oportunamente? (Sí/No).
  - Si va a juicio — **Complementaria:** ¿el empleador imputó una causal que no logró probar?

## Descuento obligatorio: aporte obrero al IPS (9%)

**Siempre** se calcula el descuento del aporte del trabajador al Instituto de Previsión Social.

- **Tasa:** **9%** (aporte obrero del régimen general).
- **Base:** se descuenta sobre **todos los rubros remuneratorios e indemnizatorios de la liquidación,
  EXCEPTO el aguinaldo** (el aguinaldo no integra la base de aporte).
- **Fórmula:** `Aporte IPS = (Total liquidación − Aguinaldo proporcional) × 0,09`. Se muestra como
  **descuento** (resta) en la liquidación.
- **Base normativa (verificada):** **art. 17° inc. a) del Decreto-Ley N° 1860/1950** (Carta Orgánica
  del IPS, aprobado por Ley 375/1956), en la redacción dada por el **art. 2° de la Ley N° 98/1992**:
  *«La cuota mensual de los trabajadores, que será el 9% (nueve por ciento) de sus salarios»*.
  Para trabajo doméstico, el 9% obrero está en la Ley 5407/2015.
- **Reparto total del aporte** (referencia; lo que importa para el descuento al trabajador es el 9%):
  - **Trabajador: 9%** (lo que se descuenta de la liquidación).
  - **Empleador: 16,5%** = 14% IPS (art. 17 inc. b) + **2,5% adicional** destinado a **SENEPA** y **SNPP**.
  - **Estado: 1,5%** (art. 17 inc. c).
  - El 2,5% patronal (SENEPA/SNPP) `[VERIFICAR VIGENCIA]` de la norma puntual que lo fija.

> Estas normas (Decreto-Ley 1860/50, Ley 98/92, Ley 5407/2015) todavía no son entradas propias de
> `leyes.yaml`; conviene cargarlas para que `citacion` las dé por `verified` (texto del art. 17 inc. a
> confirmado en sesión, 2026-06-30).

## Bases de cálculo por rubro

| Rubro | Base de cálculo | Fórmula |
|-------|-----------------|---------|
| Salario del mes (días trabajados) | Salario base | Salario base / 30 × días trabajados |
| Indemnización por despido | Promedio 6 meses | Promedio × (15 días por año) |
| Preaviso | Promedio 6 meses | Promedio × días según escala art. 87 (30/45/60/90) |
| Vacaciones causadas | Último salario | Último salario / 30 × días según escala |
| Vacaciones proporcionales | Último salario | Último salario / 30 × días proporcionales |
| Aguinaldo proporcional | Total año / 12 | (Total percibido en año) / 12 |
| **Aporte IPS (−9%)** | **Total liq. − aguinaldo** | **(Total − aguinaldo) × 0,09 (se resta)** |
| Compensatoria (20%) — *solo en juicio* | Subtotal adeudado | Subtotal × 0,20 |
| Complementaria — *solo en juicio* | 1-2 meses (criterio jurisp.) | Promedio × meses (rango real 1-2; tope legal 12) |

## Rubros salariales corrientes: horas extras, nocturnas y feriados (art. 234 CT)

> **Distinto de la liquidación de cese.** Estos rubros son salario **devengado durante la relación**
> (lo que se le adeuda al trabajador por horas trabajadas), no parte de la indemnización por terminación.
> Se calculan por separado y pueden sumarse a un reclamo o a una liquidación mensual.

**Base de cálculo (salario hora):** `salario hora = salario mensual / 30 / 8`
(30 días, jornada de 8 horas; art. 194 CT, jornada diurna). Para jornada nocturna la base ordinaria
ya lleva el +30% (ver abajo).

> **Divisor uniforme = 8 (criterio del estudio):** aunque la jornada nocturna ordinaria es de 7 h/día
> (art. 196 CT), el `salario hora` base se calcula **siempre con divisor 8**, también para los recargos
> nocturnos. Es el criterio conservador para el empleador (no infla la base nocturna). El art. 234 no
> impone un divisor; usar 7 para la base nocturna sería más favorable al trabajador pero requeriría
> respaldo jurisprudencial. Si aparece un fallo que exija divisor 7, revisar esta decisión.

**Jornadas (arts. 194-196 CT):** diurna 06:00-20:00 (máx. 8 h/día, 48 h/sem); nocturna 20:00-06:00
(máx. 7 h/día, 42 h/sem); mixta (máx. 7,5 h/día, 45 h/sem), pagada según el tramo diurno/nocturno.

**Recargos del art. 234 CT (verificados contra el Código del Trabajo):**

| Concepto | Recargo (art. 234) | Factor sobre salario hora | Fórmula |
|---|---|---|---|
| Hora extra diurna | +50% | × 1,5 | hora × 1,5 |
| Trabajo nocturno (ordinario) | +30% sobre el diurno | × 1,3 | hora × 1,3 |
| Hora extra nocturna | +100% sobre la hora ordinaria nocturna | × 1,3 × 2 | hora × 1,3 × 2 |
| Feriado trabajado (diurno) | +100% sobre la hora ordinaria de día hábil | × 2 | hora × 2 |
| Feriado trabajado nocturno | nocturno + feriado, ambos sobre extra *(criterio combinado del estudio)* | × 1,3 × 2 × 2 | hora × 1,3 × 2 × 2 |

> El art. 234 CT fija expresamente los cuatro primeros (50% extra, 30% nocturno, 100% extra-nocturna,
> 100% feriado). El **feriado nocturno** combina recargos; el art. 234 no da una fórmula única para esa
> combinación, así que se usa el criterio práctico (×1,3×2×2). Señalarlo como tal, no como texto legal.

**Flujo:** pedir el salario mensual y la **cantidad de horas** de cada concepto → multiplicar por el
factor → sumar todos los conceptos + salario base = **subtotal bruto** → aplicar **descuento IPS 9%**
(sobre todo menos aguinaldo) → **total a cobrar**. Si falta la cantidad de horas de un concepto →
`[VACÍO FÁCTICO]`.

**Prueba (perfil patronal):** las horas extras deben estar **registradas** (art. 206 CT exige registro
de horas extraordinarias). Si el empleador no tiene registro, marcar `[VACÍO PROBATORIO]`: en juicio,
la falta de registro suele perjudicar la posición patronal.

## Escala de vacaciones (art. 218 CT)

| Antigüedad | Días de vacaciones |
|------------|-------------------|
| 1 a 5 años | 12 días hábiles corridos |
| 5 a 10 años | 18 días hábiles corridos |
| Más de 10 años | 30 días hábiles corridos |

## Escala de preaviso (art. 87 CT)

| Antigüedad | Días de preaviso |
|------------|-----------------|
| Período de prueba | Sin preaviso |
| Hasta 1 año | 30 días |
| 1 a 5 años | 45 días |
| 5 a 10 años | 60 días |
| Más de 10 años | 90 días |

## Indemnización por despido (art. 91 CT)

- **15 días de salario** por cada año de servicio o fracción superior a 6 meses.
- Base: promedio de los salarios devengados durante los últimos seis meses de vigencia del contrato
  (o fracción menor si el término fue más corto).

## Vacaciones proporcionales

**Corresponden en:** despido injustificado · retiro justificado (art. 84 CT).
**NO corresponden en:** renuncia voluntaria · despido justificado · mutuo acuerdo (salvo pacto).

**Cálculo:** días transcurridos desde el último aniversario laboral, proporcional a los días de
vacaciones según escala.

Ejemplo (1 año 7 meses): vacaciones causadas 12 días (primer año cumplido) + proporcionales 7 días
(7 meses adicionales).

## Rubros SOLO en sede judicial (liquidación en juicio)

> La compensatoria y la complementaria **no integran la liquidación extrajudicial / de cese**: ambas
> presuponen un **juicio ya iniciado**. Solo se agregan cuando el cliente pide saber el monto **en
> sede judicial**. En la liquidación común no se calculan.

### Indemnización compensatoria (20%) — solo en juicio

- **Cuándo aplica:** solo si **hay juicio** y el empleador NO pagó la liquidación oportunamente al despedir.
- **Base:** 20% del subtotal de rubros adeudados.
- **Fundamento:** art. 233 del Código Procesal del Trabajo (Ley 742/61): cuando el juicio se debió a
  la negativa injustificada del deudor, el juez puede fijar una indemnización compensatoria que no
  supere el 20% de la condena. *(No citar el art. 234 CPT: regula la cuota-litis.)*

### Indemnización complementaria (art. 82, 2º párrafo CT) — solo en juicio

- **Cuándo aplica:** solo en **sede judicial**, cuando el empleador imputa una justa causa de despido
  que no resulta judicialmente probada.
- **Regla legal:** salarios desde la presentación de la reclamación judicial hasta que la sentencia
  quede ejecutoriada, con tope de un año de salario (de ahí el rango práctico de 1 a 12 meses). El juez
  puede reducirla por equidad. *(No citar el art. 83 CT: regula contratos a plazo fijo u obra.)*
- **Criterio jurisprudencial (verificado, no regla legal):** los Tribunales de Apelación del Trabajo la
  fijan en un **rango bajo de 1 a 2 meses** de salario por equidad; el tope de 1 año **no se aplica** en
  la práctica relevada. En litigios muy prolongados con alta antigüedad algún tribunal eleva el monto sin
  llegar al máximo. Ver `jurisprudencia.yaml` → `criteria: complementaria_art82_quantum` (verificado contra
  RAG local de fallos 2023-2025; carátulas individuales pendientes de confirmar contra PJ/CSJ).
- **Mostrar opciones:** presentar el cálculo con **1 y 2 meses** (rango típico) para que el usuario elija;
  ofrecer un escenario mayor solo si el caso tiene litigio prolongado/alta antigüedad, marcándolo como excepcional.

## Rubros según tipo de terminación

> En **todos** los tipos se aplica el **descuento IPS 9%** (sobre todo menos el aguinaldo).
> La **compensatoria** y la **complementaria** se listan abajo **solo si la liquidación es en juicio**.

### Despido injustificado
✅ Salario del mes · ✅ Indemnización por despido (15 días/año) · ✅ Preaviso · ✅ Vacaciones causadas ·
✅ Vacaciones proporcionales · ✅ Aguinaldo proporcional · ➖ Descuento IPS 9% ·
⚖️ Compensatoria (solo en juicio, si no pagó a tiempo) · ⚖️ Complementaria (solo en juicio, si negó el despido).

### Renuncia voluntaria
✅ Salario del mes · ❌ Indemnización por despido · ❌ Preaviso (lo debe dar el trabajador) ·
✅ Vacaciones causadas · ❌ Vacaciones proporcionales · ✅ Aguinaldo proporcional · ❌ Compensatoria ·
❌ Complementaria.

### Retiro justificado (art. 84 CT)
✅ Salario del mes · ✅ Indemnización por despido · ✅ Preaviso · ✅ Vacaciones causadas ·
✅ Vacaciones proporcionales · ✅ Aguinaldo proporcional · ⚠️ Compensatoria (si aplica) ·
⚠️ Complementaria (solo si al contestar negó la causal).

### Mutuo acuerdo
✅ Salario del mes · ❌ Indemnización por despido (salvo pacto) · ❌ Preaviso · ✅ Vacaciones causadas ·
❌ Vacaciones proporcionales · ✅ Aguinaldo proporcional · ❌ Compensatoria · ❌ Complementaria ·
⚠️ Gratificación extraordinaria (si se acordó).

### Despido justificado (art. 81 CT)
✅ Salario del mes · ❌ Indemnización por despido · ❌ Preaviso · ✅ Vacaciones causadas ·
❌ Vacaciones proporcionales · ✅ Aguinaldo proporcional · ❌ Compensatoria · ❌ Complementaria.

## Formato de salida

```
LIQUIDACIÓN FINAL DE HABERES

Tipo de terminación: [TIPO]
Fecha de ingreso: [FECHA]      Fecha de salida: [FECHA]
Antigüedad: [X años, Y meses, Z días]

Salario base: Gs. [MONTO]
Promedio últimos 6 meses: Gs. [MONTO]      Último salario: Gs. [MONTO]

CONCEPTO                          DÍAS        MONTO Gs.
─────────────────────────────────────────────────────────
Salario del mes                   [X]         [MONTO]
Indemnización por despido         [X]         [MONTO]
Preaviso                          [X]         [MONTO]
Vacaciones causadas               [X]         [MONTO]
Vacaciones proporcionales         [X]         [MONTO]
Aguinaldo proporcional            -           [MONTO]
─────────────────────────────────────────────────────────
Base de aporte (todo menos aguinaldo)         [MONTO]
(−) Aporte IPS 9% (DL 1860/50 art. 17 a)      ([MONTO])
─────────────────────────────────────────────────────────
LIQUIDACIÓN NETA (extrajudicial / de cese)    [MONTO]

— Solo si se pide la liquidación EN JUICIO: —
Indemnización compensatoria (20%)             [MONTO]
Indemnización complementaria (rango jurisp. 1-2 meses):
  - Opción 1 mes / 2 meses                    [MONTO c/u]
─────────────────────────────────────────────────────────
TOTAL ESTIMADO EN JUICIO (según opción)       [MONTO]
─────────────────────────────────────────────────────────
TOTAL (según meses de complementaria elegidos): [MONTO]
```

## Intereses

Si se solicitan, calcular desde la fecha de mora. Base procesal: arts. 227 y 232 CPT (la sentencia
fija el importe o las bases; los intereses se imponen al vencido aunque no se hubiesen solicitado).
**Ninguna norma fija la tasa:** es jurisprudencial. Los juzgados usan el promedio ponderado de las
tasas de préstamos comerciales del BCP. Presentar la cifra como **estimación sujeta a la tasa BCP
vigente**, nunca como tasa legal. *(No citar el art. 235 CPT: enumera los recursos.)*

## Integración

- La skill `liquidaciones` (de este plugin) usa este motor: recoge las variables mínimas y delega aquí
  el cálculo. **No** depende de skills externas a `~/.claude` — este motor viaja con el marketplace.
- Puede alimentar la sección "COSA DEMANDADA" de un escrito laboral (monto total reclamado).

## Legislación de referencia

- **Código del Trabajo** (Ley 213/93): arts. 78-92 (terminación, preaviso, indemnizaciones y base de
  cálculo), 218-221 (vacaciones), 243-244 (aguinaldo).
- **Código Procesal del Trabajo** (Ley 742/61): arts. 227 y 232 (intereses), 233 (compensatoria).

> Ambas leyes están `verified` en `shared/authorities/leyes.yaml`. Aun así, en primera mención en una
> salida al cliente, la skill `citacion` aplica los 4 controles de autoridad.
