---
name: liquidaciones
description: 'Recoge las variables mínimas de una liquidación laboral paraguaya (fecha de ingreso y egreso, salario, forma de extinción, preaviso, vacaciones, aguinaldo, pagos parciales) y delega el cálculo al motor calculo-laboral. No recalcula: valida que no falten datos, pide los que falten con VACÍO FÁCTICO, y orquesta. Pregunta si la liquidación es extrajudicial o en sede judicial. Usar cuando el cliente pide cuánto corresponde pagar o cobrar en una terminación laboral.'
---

# Skill · Liquidaciones laborales (orquestación)

> Skill del plugin `paraguay-laboral`. Es la **cara visible** del cálculo de liquidación: entrevista,
> valida y delega. **El cálculo lo hace el motor `calculo-laboral`** (de este mismo plugin); esta skill
> NO repite fórmulas ni escalas.
>
> Se rige por el agente `asistente-paraguay` del núcleo (no inventar, marcadores, gramática de
> autoridad) y por el **perfil patronal** del README del plugin.

---

## 1. Función

- **Pedir** las variables mínimas (sección 3), una tanda a la vez, sin abrumar.
- **Validar:** si falta un dato determinante para el tipo de terminación, **no calcular** → `[VACÍO FÁCTICO]`.
- **Determinar el escenario:** liquidación **extrajudicial / de cese** (la habitual) o **en sede
  judicial** (agrega compensatoria y complementaria).
- **Delegar** el cálculo al motor `calculo-laboral` y presentar su resultado.
- **No recalcular** ni alterar las fórmulas del motor.

---

## 2. Flujo de trabajo

1. **Identificar la forma de extinción** (despido injustificado / renuncia / retiro justificado /
   mutuo acuerdo / despido justificado / fin de plazo). Determina qué rubros corresponden.
2. **Recoger las variables mínimas** (sección 3). Pedir solo lo que el tipo de terminación requiere.
3. **Chequear vacíos:** todo dato determinante que falte → `[VACÍO FÁCTICO]` y pedirlo **antes** de
   calcular. No estimar a ciegas.
4. **Preguntar el escenario:** ¿la liquidación es **de cese/extrajudicial** o se quiere el monto **en
   juicio**? (Solo en juicio se suman compensatoria y complementaria — ver motor.)
5. **Delegar a `calculo-laboral`**: pasarle las variables; el motor aplica escalas (preaviso art. 87,
   vacaciones art. 218, indemnización art. 91), el **descuento IPS 9%** (sobre todo menos aguinaldo) y
   arma la tabla.
6. **Presentar** el resultado del motor + advertencias del diagnóstico (riesgos, vacíos).

---

## 3. Variables mínimas

Sin estas, no se calcula (las que falten → `[VACÍO FÁCTICO]`):

- **Fecha de ingreso.**
- **Fecha de egreso.**
- **Salario mensual** (en guaraníes) y, si se requiere promedio, los **últimos 6 meses**.
- **Forma de extinción.**
- **Preaviso** otorgado o no.
- **Vacaciones** gozadas o no (y desde el último aniversario).
- **Aguinaldo** pagado o no, y total percibido en el año.
- **Pagos parciales** ya realizados (se descuentan del total).
- **Documentos respaldatorios** (si faltan → lo señala el diagnóstico como `[VACÍO PROBATORIO]`).
- **Solo si va a juicio:** ¿el empleador pagó la liquidación a tiempo? ¿imputó una causal que no probó?

---

## 4. Disciplina (perfil patronal)

- **No calcular** sin salario, antigüedad, fecha de ingreso y de egreso (regla del perfil patronal).
- El **descuento IPS 9%** se aplica **siempre** (lo hace el motor); recordarlo en la salida.
- La **compensatoria (20%)** y la **complementaria** **no** van en la liquidación de cese: solo si el
  cliente pide el monto **en juicio**. No inflar la liquidación extrajudicial con rubros judiciales.
- Las cifras de **práctica judicial** son **criterio jurisprudencial o estimación**, no datos legales (lo
  marca el motor). La **complementaria (art. 82)** ya tiene criterio verificado: rango **1-2 meses** de
  salario (`jurisprudencia.yaml` → `complementaria_art82_quantum`). La **tasa de interés** sigue siendo
  estimación a confirmar.
- Para cliente empleador, encuadrar el número dentro de la **estrategia**: el monto es insumo de la
  decisión de negociar / ofrecer / litigar (ver skill `estrategias-empleador`).

---

## 5. Relación con otras skills

- **`calculo-laboral`** (motor) — hace el cálculo. Esta skill lo invoca; no lo duplica.
- **`diagnostico`** (núcleo) — corre antes si hay un escrito o si faltan hechos/prueba.
- **`estrategias-empleador`** — toma el monto y lo convierte en recomendación de contingencia.
- **`citacion`** (núcleo) — gobierna cómo se citan las normas del cálculo (213/93, 742/61, IPS).

---

## 6. Qué NO hace esta skill

- No recalcula ni cambia las fórmulas/escalas del motor.
- No inventa montos ni asume datos faltantes: pide con `[VACÍO FÁCTICO]`.
- No mezcla la liquidación de cese con la judicial: pregunta el escenario primero.
- No decide la estrategia: entrega el número; la estrategia es `estrategias-empleador`.
