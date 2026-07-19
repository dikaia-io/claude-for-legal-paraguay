---
name: despidos
description: Clasifica y analiza despidos bajo derecho laboral paraguayo desde la perspectiva del empleador. Antes de recomendar un despido, evalúa la causal (art. 81 CT, taxativo), su gravedad, contemporaneidad y prueba documental. Guía el procedimiento de desvinculación (despido justificado, injustificado y abandono de trabajo) y las obligaciones administrativas (IPS, MTESS, certificado de trabajo). No recomienda despedir sin evaluar la prueba. Usar cuando el empleador evalúa, decide o ejecuta una desvinculación.
---

# Skill · Despidos y desvinculación (empleador)

> Skill del plugin `paraguay-laboral`, **orientación patronal**. Evalúa la viabilidad de un despido y
> guía el procedimiento de desvinculación. Se rige por el agente `asistente-paraguay` y por el perfil
> patronal del README (regla nº10 y "no recomendar despido sin evaluar prueba documental").
>
> Procedimiento basado en práctica real de desvinculación paraguaya (anonimizada). Citas verificadas
> contra el Código del Trabajo (Ley 213/93).

---

## 1. Función

Antes de un despido, responder: **¿hay causal? ¿está probada? ¿conviene?** Y si se procede, guiar el
**procedimiento correcto** para que la desvinculación no genere contingencia evitable.

Regla dura del perfil patronal: **no se recomienda un despido justificado sin evaluar la prueba
documental**. Un despido justificado mal probado se convierte en injustificado + indemnización +
complementaria (art. 82 CT).

---

## 2. Clasificación de la causal (despido justificado)

El **art. 81 CT enumera taxativamente** las causas justificadas de despido por voluntad del empleador
(incisos a-q). No puede invocarse ningún motivo fuera de esa lista. Consultar el artículo (vía
`citacion`); no inventar causales.

Para cada causal invocada, evaluar tres filtros (si falla uno, el despido justificado es riesgoso):

| Filtro | Pregunta | Si falla |
|---|---|---|
| **Gravedad** | ¿El hecho encuadra en una causal del art. 81 y es suficientemente grave? | Reclasificar o no despedir con causa. |
| **Contemporaneidad** | ¿El despido es inmediato al hecho/su conocimiento? ¿No hubo consentimiento tácito? | Correr el plazo de caducidad del **art. 401 CT** (30 días desde el conocimiento) con la skill `plazos`. |
| **Prueba** | ¿Hay prueba documental contemporánea del hecho? | `[VACÍO PROBATORIO]`: sin prueba, no recomendar despido justificado. |

> **Caducidad / condonación (art. 401 CT):** el derecho a despedir con justa causa **prescribe a los 30 días**
> desde que el empleador tuvo conocimiento de la causa (art. 401 CT, "condonación de falta"). **No confundir
> con el art. 82 CT**, que regula la improcedencia de indemnizaciones y la complementaria, no el plazo.
> Encuadrar con la skill `plazos` antes de decidir. La falta de contemporaneidad presume renuncia a la causal.

---

## 3. Las tres vías de desvinculación

### 3.1. Despido justificado (art. 81 CT)
Procedimiento patronal recomendado:
1. **Recopilar evidencias** del hecho (documentos contemporáneos, testigos, actas).
2. **Parecer jurídico** previo: solidez de la prueba, adecuación de la causal a los hechos, viabilidad
   legal, riesgos y recomendación. (Esta skill produce ese parecer; puede formalizarse vía `dictamenes`.)
3. **Decisión** del tipo de despido (justificado / injustificado) según el parecer.
4. **Notificación** al trabajador por nota con las **causales invocadas** (fundamental: la causal debe
   constar por escrito y ser fehaciente).
5. **Liquidación** según el tipo (sin indemnización si es justificado y probado) — vía `liquidaciones`.

### 3.2. Despido injustificado
- Sin causal del art. 81 (o con causal no probada). Genera indemnización (art. 91), preaviso, etc.
- A veces es la **opción estratégica más segura** cuando la prueba del justificado es débil: pagar la
  indemnización es más barato que perder un juicio con complementaria. Evaluar con `estrategias-empleador`.

### 3.3. Abandono de trabajo (art. 81 inc. q)
Es causal justificada, pero **requiere procedimiento estricto** para ser fehaciente:
1. **Intimación fehaciente** (telegrama colacionado) a reintegrarse, con plazo **no menor a 3 días**.
2. **Aviso de retorno:** conservar la constancia de entrega del telegrama. Sin ella —o si consta no
   entregado— la intimación **no es fehaciente** y el abandono no queda configurado.
3. Domicilio de difícil identificación (zona rural, sin numeración) → intimar por **acta notarial**.
4. Vencido el plazo sin justificación/respuesta → **segundo telegrama** declarando configurado el
   abandono y notificando que la liquidación está disponible.
5. Desvincular en IPS y MTESS como **despido justificado** con la causal correspondiente.

---

## 4. Obligaciones administrativas (contingencia patronal)

Toda desvinculación, cualquiera sea la causa, exige cumplir plazos ante IPS y MTESS. Su omisión es
multa y costo concreto:

- **IPS — comunicación de salida:** Declaración Jurada de Movimientos del Empleado, indicando el motivo
  (renuncia / despido justificado / injustificado). Plazos: **3 días hábiles (zona urbana) / 10 días
  hábiles (zona rural)** desde la fecha del movimiento. *Si no se comunica a tiempo, el empleador sigue
  obligado a abonar aportes como si el trabajador estuviera activo.* `[VERIFICAR VIGENCIA]` de las
  resoluciones de IPS (Res. C.A. 045-001/10 y comunicación de motivos de salida).
- **MTESS — comunicación de salida:** comunicar la baja del trabajador por el sistema **REOP** dentro de
  los **30 días hábiles** desde la fecha en que dejó de prestar servicios, declarando el motivo (Art. 78 /
  81 / 84 CT o despido / retiro injustificado). Base: **Decreto N° 1989/2024** (deroga el antiguo Decreto
  8304/17) y **Res. MTESS N° 991/2024**, Anexo N° 2, Cap. III, art. 11. La omisión es pasible de multa
  (1 a 3 jornales mínimos según la mora, art. 22 del Decreto 1989/2024). *No confundir el plazo de
  comunicación con la escala de multa.* Fuente oficial: [resoluciones MTESS](https://www.mtess.gov.py/?page_id=31671).
- **Certificado de trabajo (art. 93 CT):** al término de la relación, **cualquiera sea la causa**, el
  empleador debe entregar certificado con fecha de ingreso y egreso, tipo de trabajo y salario
  percibido. Se entrega junto con la liquidación final.

---

## 5. Renuncia (para distinguirla del despido)

No es despido, pero la skill la reconoce porque cambia la liquidación:
- Debe ser **voluntaria y fehaciente**: firmada ante escribano, autoridad administrativa del
  trabajo, secretario del Juzgado Laboral, o **dos testigos** del acto. *Sin esa formalidad, se presume que la
  extinción fue involuntaria* (riesgo de que se reclame como despido).
- **Anclaje normativo (art. 78 inc. b CT):** esa forma fehaciente está en el art. 78 inc. b, que la exige
  literalmente para el **mutuo consentimiento**; en la práctica paraguaya se aplica también a la renuncia
  unilateral para tenerla por fehaciente. El art. 78 **no tiene un inciso autónomo de "renuncia voluntaria"**
  (el inc. j es despido del empleador; el art. 84 es *retiro justificado* del trabajador, distinto). Por eso
  un papel firmado solo por el trabajador, sin escribano/autoridad/testigos, no alcanza el estándar del inc. b.
- Preaviso del trabajador (art. 87 CT) según antigüedad.

---

## 6. Relación con otras skills

- **`estrategias-empleador`** — decide si conviene despedir (justificado vs injustificado) según contingencia.
- **`liquidaciones` / `calculo-laboral`** — calcula la liquidación del tipo de despido elegido.
- **`plazos`** (núcleo) — caducidad del art. 401 CT y plazos IPS/MTESS.
- **`dictamenes`** — formaliza el parecer jurídico del despido.
- **`citacion`** (núcleo) — cita el art. 81/82/93 CT y las resoluciones IPS/MTESS con sus controles.

---

## 7. Qué NO hace esta skill

- No recomienda despido justificado sin prueba documental: marca `[VACÍO PROBATORIO]`.
- No inventa causales fuera del art. 81 ni plazos: los consulta o los marca.
- No calcula la liquidación (la deriva) ni redacta los telegramas/notas (los deriva).
- No decide por el abogado: evalúa la viabilidad y guía el procedimiento.
