# Escritos laborales — estructuras portadas (fuero del trabajo, Ley N° 742/1961)

> **Portado** de la skill `escrito-laboral` de Miguel Fernando Díaz (Apache-2.0). Normas `verified`
> en el authority map: `codigo_trabajo` (Ley 213/1993), `codigo_procesal_trabajo` (Ley 742/1961).
> La liquidación de rubros (COSA DEMANDADA) se delega al motor `calculo-laboral` del plugin
> `paraguay-laboral`; esta referencia solo aporta la estructura del escrito.

## Datos a recopilar

- **Demanda:** fecha de ingreso y de despido/salida, cargo, salario mensual (Gs.), hechos, causal
  invocada por el empleador (si la hubo), documentos disponibles.
- **Contestación:** carátula del juicio, resumen del reclamo, versión del demandado, documentos.
- **Interrogatorio:** hechos a probar y testigos **ofrecidos y admitidos** en la providencia de
  apertura/admisión de pruebas (verificarlo antes: testigo no admitido → advertir riesgo de objeción).

## Estructura de DEMANDA LABORAL

```
OBJETO: PROMOVER DEMANDA LABORAL POR [TIPO] Y COBRO DE GUARANÍES.

SEÑOR JUEZ:

[NOMBRE ABOGADO], Abogado (MAT. C.S.J. N° [MATRÍCULA]), en representación de [NOMBRE CLIENTE],
con C.I. N° [CI], [estado civil], [nacionalidad], profesión [profesión], con domicilio real en
[domicilio real], conforme a la carta poder que adjunto a esta presentación, constituyendo
domicilio procesal en [domicilio procesal], y muy respetuosamente me presento a V.S. y digo:-

QUE, siguiendo expresas instrucciones de mi mandante, vengo a promover DEMANDA LABORAL [TIPO]
COBRO DE GUARANÍES, contra [demandado], con RUC N° [RUC], domiciliada en [domicilio demandado],
por los argumentos de hecho y derecho que paso a exponer:-

HECHOS
[Relato detallado con argumentación jurídica.]

COSA DEMANDADA:
[Liquidación detallada de rubros en tabla — delegar cálculo a calculo-laboral.]
TOTAL RECLAMADO: GUARANÍES [monto en letras].

RECLAMO DE INTERESES
[La tasa es jurisprudencial (promedio BCP), no legal — presentarla como estimación.]

DERECHO
FUNDO la presente acción en los artículos [arts. aplicables] del Código del Trabajo y los
arts. [arts.] del Código Procesal del Trabajo y concordantes.-

POR consiguiente, a V.S. PIDO:-
1. TENER por reconocida mi personería y por constituido mi domicilio.-
2. TENER por iniciada la presente demanda laboral contra [DEMANDADO], más costos, intereses
   y costas.-
3. OPORTUNAMENTE, previos trámites de rigor, dictar Sentencia haciendo lugar a la demanda.
   Protesto costas.-

Proveer de conformidad, y SERÁ JUSTICIA.
```

## Estructura de CONTESTACIÓN DE DEMANDA

```
JUICIO: "[ACTOR] C/ [DEMANDADO] S/ [OBJETO]"

OBJETO: TOMAR INTERVENCIÓN Y CONTESTAR DEMANDA.

SEÑOR/A JUEZ/A:

[NOMBRE ABOGADO], Abogado de la Matrícula N° [MATRÍCULA], en representación de [CLIENTE],
conforme al Poder General que acompaño, fijando domicilio real en [domicilio real] y procesal
en [domicilio procesal], a V.S. digo:

Por el presente, vengo a tomar intervención y a contestar la demanda iniciada por [ACTOR],
solicitando desde ya su rechazo por notoria improcedencia, conforme a los fundamentos siguientes:

Negativa: Es falso todo cuanto se expresa en el escrito de demanda, así como los documentos
acompañados que no sean reconocidos de manera expresa en el presente escrito.

Contestación de la demanda.
[Negación punto por punto de las afirmaciones del actor.]

COSA RECLAMADA: Se rechaza el reclamo de Gs. [monto]. [Detalle de cada rubro rechazado.]

LA VERDAD DE LOS HECHOS:
[Versión del demandado.]

INSTRUMENTALES: [Lista de documentos adjuntos.]

PETITORIO: personería y domicilios; demanda contestada; instrumentales ofrecidas (con desglose
y devolución de originales previa autenticación); rechazo de la demanda con costas.

PROVEER DE CONFORMIDAD Y SERÁ JUSTICIA.
```

### Excepciones en el juicio laboral de conocimiento — art. 119 CPT (taxativo)

Solo son admisibles: **a)** incompetencia de jurisdicción; **b)** falta de personería;
**c)** litis pendencia; **d)** cosa juzgada; **e)** transacción; **f)** prescripción.

Implicancias al contestar:
1. **No existe la "excepción de pago"** en el fuero laboral: el pago se invoca como **defensa de
   fondo** en el cuerpo de la contestación, con recibos firmados y comprobantes. Escribir "opongo
   excepción de pago" es un error técnico.
2. Tampoco existen como excepciones laborales: falta de acción, falta de legitimación, defecto
   legal, arraigo ni ninguna otra figura del CPC — se canalizan como negativa o defensa sustantiva.
3. Las seis excepciones del art. 119 se oponen de modo expreso, según el trámite previsto.
4. Pago, improcedencia del rubro, falsedad de los hechos, finiquito liberatorio, recibí conforme:
   argumentos defensivos de fondo, no excepciones.
5. **Prescripción** es la de mayor uso defensivo (plazo general de 1 año, art. 399 CT — verificar
   fecha de cese vs. fecha de promoción). **Transacción** exige acuerdo homologado o instrumentado
   conforme a derecho (no confundir con recibí conforme).

Fórmula para alegar el pago (dentro del rubro correspondiente):

> "En lo que respecta al rubro [X] reclamado, el mismo se halla íntegramente pagado, conforme
> acredita el recibo N° [X] firmado por la propia parte actora en fecha [fecha], cuya copia se
> acompaña, así como el comprobante bancario obrante a fs. [X]. Mal puede pretenderse el cobro de
> un crédito extinguido por pago, conducta que configura plus petitio manifiesta y mala fe procesal
> en los términos de los arts. 30 y 51 del C.P.T. y art. 31 de la Ley 1376/88."

### Excepciones en la ejecución laboral — arts. 356 y 357 CPT (taxativos)

En la etapa de ejecución **no** rige el art. 119; solo son oponibles:
- **Pago total** (art. 356 inc. a): **posterior al título ejecutivo** y **justificado por
  documentos**. El pago anterior al título debió alegarse en el conocimiento; el pago parcial no es
  excepción (se imputa en la liquidación).
- **Prescripción** (art. 356 inc. b).
- **Nulidad de la ejecución por vicios del procedimiento** (art. 357): como **excepción** hasta la
  citación de remate; por **vía de incidente** desde ese momento hasta la realización de los bienes.

| Etapa procesal laboral | Norma | Excepciones admisibles |
|---|---|---|
| Contestación (conocimiento) | Art. 119 CPT | Incompetencia, falta de personería, litis pendencia, cosa juzgada, transacción, prescripción |
| Oposición a la ejecución | Arts. 356-357 CPT | Pago total posterior documentado, prescripción, nulidad por vicios |

## Estructura de CUESTIONARIO (INTERROGATORIO) PARA TESTIGOS

Reglas de la práctica forense paraguaya:
1. Preguntas numeradas en **ordinales escritos en negrita** (PRIMERA, SEGUNDA, … VIGÉSIMA PRIMERA…).
2. Orden fijo: **PRIMERA POR SUS DATOS PERSONALES.** / **SEGUNDA POR LAS GENERALES DE LA LEY.**
   (fórmulas escuetas) → desde la TERCERA, preguntas de fondo, una por hecho → la última es siempre
   **POR LA RAZÓN DE SUS DICHOS.**
3. Cada pregunta de fondo empieza con *"Diga el testigo si sabe y le consta que…"*, en sentido
   afirmativo y favorable a la parte oferente.
4. **No** incluir "reserva en sobre cerrado" (eso es del pliego de posiciones) ni enumerar a los
   testigos en el cuerpo (ya constan en el ofrecimiento y en la providencia de admisión).
5. Si las audiencias ya están señaladas → *"en las audiencias señaladas por V.S."* (no pedir nuevo
   señalamiento).
6. Pliego común por defecto; pregunta que solo conste a un testigo → aclaración en cursiva
   *"(Pregunta dirigida principalmente a [Nombre].)"*.

```
JUICIO: "[ACTOR] C/ [DEMANDADO] S/ [OBJETO]"

OBJETO: ACOMPAÑAR INTERROGATORIO PARA TESTIGOS.

SEÑOR JUEZ EN LO LABORAL:

[NOMBRE ABOGADO], abogado, Matrícula C.S.J. Nº [MATRÍCULA], en representación de [CLIENTE],
conforme personería acreditada en autos, en el juicio del epígrafe, a V.S. digo:

Que, conforme al Código Procesal del Trabajo (Ley 742/61) y supletoriamente al Código Procesal
Civil, vengo a acompañar el INTERROGATORIO a tenor del cual deberán declarar, bajo juramento o
promesa de decir verdad, los testigos oportunamente ofrecidos y admitidos por mi parte, en las
audiencias señaladas por V.S.

INTERROGATORIO PARA TESTIGOS

PRIMERA POR SUS DATOS PERSONALES.
SEGUNDA POR LAS GENERALES DE LA LEY.
TERCERA: Diga el testigo si sabe y le consta que [primer hecho a probar].
[... una pregunta por hecho ...]
[ÚLTIMA]: POR LA RAZÓN DE SUS DICHOS.

PETITORIO: tener por acompañado el interrogatorio; recibir la declaración testimonial en las
audiencias señaladas por V.S., bajo apercibimiento de ley.

PROVEER DE CONFORMIDAD, SERÁ JUSTICIA.
```

## Anclas normativas laborales de uso frecuente (verificadas)

- **CT (Ley 213/93):** arts. 78-81 (terminación y causales), 82 (improcedencia de indemnizaciones +
  complementaria), 87 (preaviso), 91 (indemnización), 93 (certificado de trabajo), 218-221
  (vacaciones), 399 (prescripción general 1 año), 401 (caducidad de la causal, 30 días).
- **CPT (Ley 742/61):** art. 28 (requisitos de la demanda) `[VERIFICAR VIGENCIA]` en primera
  mención; art. 119 (excepciones); arts. 227 y 232 (intereses — la tasa es jurisprudencial, no
  legal); art. 233 (compensatoria ≤20%); arts. 356-357 (ejecución).
- No citar el art. 234 CPT para la compensatoria (regula la cuota-litis) ni el art. 235 CPT como
  norma de intereses (enumera recursos).
