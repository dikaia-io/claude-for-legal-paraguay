---
name: sumarios-mtess
description: Habilidad especializada para contestar sumarios administrativos del Ministerio de Trabajo, Empleo y Seguridad Social (MTESS) de Paraguay. Se utiliza cuando el usuario solicita elaborar contestaciones de sumarios administrativos por infracciones laborales, preparar defensas contra resoluciones del MTESS, oponer excepciones (especialmente prescripción), o analizar imputaciones laborales. Aplica para todo tipo de infracciones documentales, salariales, de jornada, seguridad e higiene, y seguridad social.
---

# Contestación de Sumarios Administrativos del MTESS

> **Origen y atribución.** Contenido portado de la skill `sumarios-mtess` de Miguel Fernando Díaz, incorporado bajo Apache-2.0. Se rige por el agente `asistente-paraguay` del núcleo (no inventar normas/jurisprudencia, marcadores de incertidumbre, gramática de autoridad, diagnóstico previo). Las normas se referencian contra el authority map (`leyes.yaml`).

Esta habilidad permite elaborar contestaciones profesionales de sumarios administrativos instruidos por el Ministerio de Trabajo, Empleo y Seguridad Social de Paraguay, con fundamentación jurídica precisa, análisis estratégico de defensas y estructura procesal adecuada al contexto legal paraguayo.

> **Diagnóstico previo:** Antes de actuar sobre cualquier escrito o estrategia, delegá el diagnóstico general en la skill `/paraguay-legal-core:diagnostico`. Esta skill agrega el análisis específico del sumario administrativo (prescripción, vicios procesales, estrategia defensiva ante el MTESS) a ese diagnóstico base.

## Cuándo Usar Esta Habilidad

Utilizar esta habilidad cuando el usuario:
- Solicite contestar un sumario administrativo del MTESS
- Necesite oponer excepción de prescripción
- Requiera analizar las imputaciones de una resolución de instrucción de sumario
- Solicite evaluar estrategias defensivas para infracciones laborales
- Necesite preparar expresión de agravios contra resolución definitiva del MTESS
- Requiera asesoramiento sobre documentación probatoria a presentar

## Proceso de Trabajo

### Paso 1: Análisis Inicial
Antes de comenzar la redacción, SIEMPRE leer los archivos de referencia:
- `references/procedimiento_sumario.md` - Para conocer el procedimiento completo
- `references/infracciones_defensas.md` - Para identificar defensas específicas por tipo de infracción

### Paso 2: Análisis de la Resolución
Analizar minuciosamente la Resolución de Instrucción de Sumario o documentación proporcionada:

1. **Identificar datos procesales:**
   - Número de sumario
   - Fecha de inspección laboral
   - Fecha de notificación de la resolución de instrucción
   - Juez instructor asignado
   - Matrícula patronal fiscalizada

2. **Verificar prescripción INMEDIATAMENTE:**
   - Calcular tiempo transcurrido entre inspección y notificación
   - Si excede 1 año: La prescripción es la defensa principal
   - Incluir excepción de prescripción en la contestación

3. **Analizar cada imputación:**
   - Identificar artículos citados
   - Determinar tipo de infracción
   - Verificar si especifica trabajadores afectados
   - Buscar vicios en la imputación

4. **Identificar vicios procesales:**
   - Incompetencia territorial
   - Falta de individualización de trabajadores
   - Errores en identificación de empresa/sucursal
   - Confusión de matrículas patronales

### Paso 3: Estrategia Defensiva
Determinar las defensas aplicables según `references/infracciones_defensas.md`:

**Defensas de Forma (Prioritarias):**
- Excepción de prescripción (si aplica)
- Incompetencia territorial
- Falta de individualización de trabajadores afectados
- Indefensión por falta de claridad en imputaciones

**Defensas de Fondo:**
- Cumplimiento sustancial de las obligaciones
- Presentación de documentación probatoria
- Interpretación restrictiva de normas sancionadoras
- Primacía de la realidad sobre formalidades
- Jurisprudencia favorable

### Paso 4: Recopilación de Documentación

Asesorar al cliente sobre documentación necesaria según cada infracción:
- Crear lista específica de documentos a presentar
- Explicar qué prueba cada documento
- Indicar cómo debe organizarse
- Sugerir documentación que pueda generarse aún si no existe

### Paso 5: Estructura de la Contestación

La contestación debe seguir esta estructura formal con encabezados en párrafos (no usar formato de markdown con ##):

**OBJETO: CONTESTAR SUMARIO / OPONER EXCEPCIÓN DE PRESCRIPCIÓN Y CONTESTAR SUMARIO**

**SEÑOR/A JUEZ/A INSTRUCTOR/A:**

**I. PERSONERÍA Y REPRESENTACIÓN**
[Identificación del abogado, matrícula, cliente, domicilios]

**II. EXCEPCIÓN DE PRESCRIPCIÓN (si aplica)**
[Desarrollo completo con jurisprudencia]

**III. CONTESTACIÓN DEL SUMARIO**
[Análisis de cada imputación]

**A) [Primera Infracción]**
[Contestación detallada]

**B) [Segunda Infracción]**
[Contestación detallada]

**IV. VICIOS PROCESALES (si aplica)**
[Detalle de vicios que afectan validez]

**V. ARGUMENTACIÓN JURÍDICA GENERAL**
[Principios del derecho administrativo sancionador aplicables]

**VI. PETITORIO**
[Solicitudes concretas]

**PROVEER DE CONFORMIDAD Y SERÁ JUSTICIA**

## Lineamientos de Redacción

### Tono y Estilo
- **Formal y técnico**: Lenguaje jurídico preciso
- **Asertivo sin ser agresivo**: Firme en la defensa, respetuoso con autoridad
- **Fundado**: Cada afirmación debe tener respaldo legal o fáctico
- **Estructurado**: Uso de párrafos con conectores lógicos
- **Sin ambigüedades**: Redacción clara y precisa

### Estructura de Párrafos
- Cada infracción se contesta en sección separada con encabezado claro
- Párrafos conectados lógicamente (En primer lugar... En segundo lugar... Por tanto... En consecuencia...)
- Argumentación progresiva: hecho → derecho → conclusión

### Citas Jurisprudenciales

> **Nota sobre jurisprudencia:** Las citas de Acuerdos y Sentencias de la Corte Suprema de Justicia que aparecen en esta skill (N° 163/2011, 2/2013, 70/2012, 98/2011, 193/2011, 84/2005, y demás) deben verificarse contra el portal oficial del Poder Judicial (pj.gov.py) antes de incluirlas en un escrito definitivo. Aplicá el marcador `[INSERTAR JURISPRUDENCIA VERIFICADA]` cuando no hayas revisado el texto original en sesión.

Cuando se cite jurisprudencia:
- Identificar claramente el acuerdo y sentencia (número y fecha)
- Entrecomillar el texto citado en cursiva
- Destacar en negrita los conceptos clave usando formato **texto**
- Explicar la aplicación al caso concreto

Ejemplo:
```
Al respecto, el Acuerdo y Sentencia Nº 163 de fecha 13 de septiembre de 2011 expresa: 
"*No existe en la ley laboral un plazo máximo entre dicha verificación y la iniciación 
del sumario, imprevisión legal que debe salvarse con la aplicación analógica del art. 399 CT...*"
```

### Citas Normativas
Los artículos citados del Código del Trabajo (Ley 213/1993, clave `codigo_trabajo` en `leyes.yaml`, status `verified`) y del Código Procesal del Trabajo (Ley 742/1961, clave `codigo_procesal_trabajo`, status `verified`) no requieren el marcador `[VERIFICAR VIGENCIA]` para las citas de artículos ya identificados. Citá correctamente: Art. X de la Ley 213/1993 (Código del Trabajo). Para las Resoluciones del MTESS: la **672/2024** está `verified` en el authority map (no requiere el marcador para el número de norma; sí para numerales internos aún no cotejados). La **346/2024** sigue en `draft` (no está en disco ni en LDH) → aplicá `[VERIFICAR VIGENCIA]` en su primera mención.

- Citar artículos completos cuando sea necesario
- Referenciar correctamente: Art. X de la Ley Y, Art. X del Decreto Y
- Explicar la ratio legis de la norma cuando fortalezca la defensa

### Tratamiento de Infracciones

**Negar expresamente lo no reconocido:**
"Negando todos y cada uno de los hechos que no sean objeto de reconocimiento expreso en el presente escrito"

**Para cada infracción:**
1. Identificar claramente (con número o letra)
2. Describir la imputación
3. Negar o admitir (según estrategia)
4. Argumentar la defensa
5. Ofrecer prueba documental
6. Concluir sobre improcedencia de sanción

**Fórmulas útiles:**
- "No es cierto que la empresa incumpla con esta normativa..."
- "Negamos incumplir con..."
- "Al respecto cabe resaltar que..."
- "Adjuntamos a esta presentación..."
- "Se puede comprobar fehacientemente que..."
- "Por lo que solicito se desestime esta imputación..."

## Excepción de Prescripción - Tratamiento Especial

La excepción de prescripción es la defensa más efectiva y debe incluirse siempre que aplique.

**Estructura completa:**

1. **Introducción y base legal:**
En primer término, vengo a interponer Excepción de Prescripción contra la potestad que tenía el Estado para imponer sanciones administrativas, conforme al art. 399 del Código del Trabajo (Ley 213/1993). En efecto, el Código del Trabajo establece en el artículo 399: "*Las acciones acordadas por este Código o derivadas del contrato individual o colectivo de condiciones de trabajo, prescribirán al año de haber ellas nacido, con excepción de los casos previstos en los artículos siguientes.*"

2. **Criterio jurisprudencial:**

> `[INSERTAR JURISPRUDENCIA VERIFICADA]` — Las citas que siguen deben verificarse contra PJ/CSJ (pj.gov.py) antes de incluirlas en escrito definitivo.

Citar TODOS estos acuerdos `[INSERTAR JURISPRUDENCIA VERIFICADA]` (verificar cada Acuerdo y Sentencia contra PJ/CSJ antes de citarlo en un escrito):
- Acuerdo y Sentencia N° 163/2011 (criterio principal)
- Acuerdo y Sentencia N° 2/2013 (extinción de potestad, no prescripción de acciones)
- Acuerdos y Sentencia N° 249/04 y 64/2010 (confirmación)

3. **Aplicación al caso concreto:**
En el presente caso, mi mandante ha sido objeto de una Inspección laboral realizada por funcionarios inspectores del Ministerio del Trabajo Empleo y Seguridad Social el día [FECHA DE INSPECCIÓN], conforme se puede comprobar con el acta realizada por los funcionarios en cumplimiento de su cometido y que obra a fs. [X] de este Sumario.

Sin embargo, mi mandante fue notificado de la instrucción del sumario administrativo en fecha [FECHA DE NOTIFICACIÓN], es decir, luego de más de un año desde la inspección laboral en donde fueron detectadas las supuestas irregularidades hasta la notificación realizada a mi mandante, por lo que a todas luces se puede comprobar que se ha operado la Prescripción.

4. **Interrupción de la prescripción:**
Cabe resaltar a V.S. que solamente la notificación del Auto de apertura de instrucción del sumario interrumpe esta prescripción, ya que si esta no es conocida por la empresa sumariada, vale decir no es objeto de notificación, no puede tener efecto alguno.

5. **Oportunidad procesal:**
Los tribunales también se expresaron en cuanto a la oportunidad en que debe oponerse la Excepción de Prescripción, estableciendo que debe articularse en la instancia administrativa. En este sentido opinaron los Acuerdos y Sentencias Números 91 del 21-10-13, 241/04, 58/06, 21/09 y 37/14. `[INSERTAR JURISPRUDENCIA VERIFICADA]`

6. **Conclusión:**
Consecuentemente, en el caso de [EMPRESA], si se tiene en cuenta la fecha de inspección de los funcionarios del Ministerio del Trabajo, el [FECHA], a la fecha de notificación del Auto de apertura de instrucción de sumario, el [FECHA], se hallaba operada la prescripción y por ende la extinción de la potestad del estado para imponer las sanciones por las supuestas infracciones encontradas.

## Petitorio

El petitorio debe ser claro, específico y numerado:

**PETITORIO**

Por todo lo precedentemente expuesto, a V.S. solicito provea el siguiente PETITORIO:

1) Tenga por reconocida mi personería en el carácter invocado y por constituido mi domicilio en el lugar señalado;

2) [Si hay excepción de prescripción] Tenga por contestado el Sumario y por opuesta la Excepción de Prescripción en los términos del escrito que antecede;

3) [Si hay excepción] Previo trámites de rigor, haga lugar a la Excepción de Prescripción planteada y disponga el sobreseimiento de mi mandante de cualquier multa o sanción que pudiera derivar del presente sumario;

4) [Alternativo o acumulativo] Disponga el sobreseimiento de mi mandante por las razones expuestas en el cuerpo del presente escrito;

5) Disponga el desglose y devolución de los documentos originales presentados previa autenticación de sus copias por parte de la actuaria;

Proveer de conformidad y SERÁ JUSTICIA.

## Aspectos Críticos del Contexto Paraguayo

### 1. Ambiente Adversarial
- Las autoridades laborales suelen tener sesgo pro-trabajador
- Los procedimientos pueden ser arbitrarios
- La fundamentación exhaustiva es esencial
- Anticipar posibles malas interpretaciones

### 2. Aplicación de Multas
- Las multas se calculan por infracción y por trabajador afectado
- Pueden ser cuantiosas
- La prescripción es el mejor escudo
- El allanamiento puede reducir montos pero crea antecedente

### 3. Importancia de la Documentación
- La carga probatoria está en la administración, pero la empresa debe crear duda razonable
- Documentación completa puede lograr sobreseimiento
- Fotografías y constancias firmadas son esenciales

### 4. Jurisprudencia como Escudo
- Los tribunales han sido protectores en varios aspectos (reglamento interno, vacaciones, prescripción)
- Citar jurisprudencia precisa es fundamental, siempre con marcador `[INSERTAR JURISPRUDENCIA VERIFICADA]` hasta confirmar contra PJ/CSJ
- Los jueces instructores suelen seguir criterios consolidados

## Verificaciones Finales

Antes de entregar la contestación, verificar:

- Se calculó la prescripción y se incluyó si aplica
- Se contestaron TODAS las imputaciones una por una
- Se citó jurisprudencia relevante correctamente y con marcador `[INSERTAR JURISPRUDENCIA VERIFICADA]` donde no se verificó en sesión
- Se especificó la documentación probatoria adjunta
- El petitorio es claro y completo
- Se identificó correctamente el número de sumario
- Se incluyó la matrícula del abogado (de `legal.local.md`)
- Los domicilios están completos
- El tono es formal pero asertivo
- La redacción es clara y sin ambigüedades
- Se estructuró en párrafos con conectores
- Se evitaron listas donde no corresponden (usar párrafos con conectores)

## Notas Importantes

- **Matrícula del abogado**: Siempre usar MAT. C.S.J. Nº [MATRÍCULA — de `legal.local.md`]
- **Preferencia por párrafos**: No usar listas numeradas en la contestación salvo en el petitorio
- **Conectores**: Usar "En primer lugar...", "En segundo lugar...", "Por tanto...", "En consecuencia...", "Asimismo..."
- **Negación expresa**: Siempre incluir "negando todos y cada uno de los hechos que no sean objeto de reconocimiento expreso"
- **Sin redundancias**: No repetir información innecesariamente
- **Enfoque en resultados**: Priorizar estrategias que beneficien al cliente
- **Análisis de riesgos**: Cuantificar probabilidades y consecuencias cuando sea posible
- **Mala fe de contrapartes**: Anticipar posibles interpretaciones desfavorables

## Recursos Adicionales

### Para Procedimiento Detallado
Ver `references/procedimiento_sumario.md` - Contiene:
- Todas las etapas del sumario según Resolución MTESS N.° 672/2024 (verificada contra el PDF primario; los plazos/numerales internos, `[VERIFICAR VIGENCIA]` hasta cotejar cada uno)
- Plazos procesales específicos
- Métodos de notificación
- Recursos disponibles
- Jurisprudencia sobre prescripción

### Para Defensas Específicas por Infracción
Ver `references/infracciones_defensas.md` - Contiene:
- Análisis de cada tipo de infracción laboral
- Defensas específicas probadas
- Documentación necesaria por infracción
- Argumentación jurídica para cada caso
- Tabla resumen de infracción → defensa → documentación
