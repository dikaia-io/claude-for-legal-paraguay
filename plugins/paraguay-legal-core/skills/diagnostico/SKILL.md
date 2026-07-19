---
name: diagnostico
description: 'Diagnóstico jurídico preliminar antes de redactar o reescribir cualquier escrito o consulta paraguaya. Audita un escrito ya redactado (argumentos sin norma, hechos no probados, citas sin verificar, contradicciones) o estructura una consulta fáctica (hechos faltantes, prueba, riesgos, estrategia, próximo paso). No modifica el escrito: solo identifica problemas. Usar antes de cualquier modificación, y de forma automática ante un escrito largo pegado sin instrucción clara.'
---

# Skill · Diagnóstico jurídico preliminar

> Skill transversal del núcleo (`paraguay-legal-core`). Opera con o sin perfil de materia cargado.
> Es la **puerta de entrada** de cualquier trabajo: nada se redacta ni se modifica antes de pasar por acá.
> Da cumplimiento a la **regla inmodificable nº8** de `CLAUDE.base.md`.

---

## 1. Función

Analizar lo que aporta el abogado —un **escrito** ya redactado o una **consulta fáctica**— y devolver
un **diagnóstico estructurado** que identifica problemas, vacíos y riesgos **antes** de producir o
modificar nada.

El diagnóstico **no modifica** el escrito ni resuelve la consulta. Solo audita. La redacción o la
modificación ocurren en una **segunda etapa**, después de que el abogado da la instrucción de proceder.

Esto es disciplina de práctica, no encaje de normas: el valor está en el **método** (qué mirar y en
qué orden), no en citar artículos. Las normas se consultan del mapa de autoridad solo cuando hacen
falta (punto 4 más abajo).

---

## 2. Cuándo se activa

- **Explícito:** el abogado escribe «diagnosticá esto», «corré el diagnóstico» o invoca
  `/paraguay-legal-core:diagnostico`.
- **Automático antes de redactar:** si el abogado pega un escrito y pide modificarlo
  («mejorá los fundamentos», «ampliá esto»), **primero** se corre el diagnóstico y **luego** se
  pregunta si procede con la modificación o si quiere revisar el diagnóstico antes. No se modifica
  un escrito sin diagnóstico previo.
- **Automático ante escrito largo sin instrucción:** ante un texto jurídico extenso pegado en el
  chat sin instrucción clara de qué hacer con él, ofrecer correr el diagnóstico.

> La **activación automática real** (hook / agente) se cablea en la fase de empaquetado del plugin.
> Esta skill define el comportamiento; el disparo se conecta después.

---

## 3. Dos modos según la entrada

El esqueleto es común; cambia el **énfasis** según lo aportado.

- **Modo ESCRITO** (demanda, contestación, recurso, carta, acta…): prioriza la **auditoría** del
  texto — argumentos sin norma, hechos no probados, citas sin verificar, contradicciones internas.
- **Modo CONSULTA** (relato fáctico de un caso, sin escrito todavía): prioriza la **estructuración**
  del caso — hechos relevantes y faltantes, prueba necesaria, riesgos, estrategia, próximo paso.

Si no está claro cuál es, preguntar antes de continuar. Una consulta puede traer fragmentos de
escrito: en ese caso, correr ambos énfasis.

---

## 4. Reglas de disciplina (no negociables)

Estas gobiernan todo el diagnóstico y derivan de `CLAUDE.base.md`; no se repiten ahí, se aplican acá.

1. **No inventar** normas, artículos, plazos, acordadas ni criterios de tribunales.
2. **No agregar jurisprudencia** que el abogado no haya aportado. Si hace falta un fallo, se pide.
3. **No citar de memoria.** Las normas del punto 4.4 salen del mapa de autoridad
   (`shared/authorities/leyes.yaml`); si una norma no está en el mapa → `[FUENTE OFICIAL PENDIENTE]`.
4. Toda norma del mapa con `verification.status: draft` se menciona **siempre** con `[VERIFICAR VIGENCIA]`.
5. **No concluir** sobre la base de hechos no aportados: pedirlos con `[VACÍO FÁCTICO]`.
6. Usar **solo** el catálogo cerrado de marcadores (sección 6). No crear marcadores nuevos.
7. El diagnóstico **no decide** por el abogado: recomienda y explicita los supuestos.

---

## 5. Estructura del diagnóstico

Se entrega en un **bloque único**, en este orden. **No omitir secciones.** Si una no tiene
observaciones, escribir «Sin observaciones» y continuar. Adaptar el énfasis al modo (sección 3).

### 1. Identificación
- Modo (escrito / consulta).
- Si es escrito: tipo (demanda / contestación / recurso / alegato / carta / acta / otro), rama del
  derecho inferida, fuero y circunscripción si se deducen, parte que suscribe (actor / demandado /
  tercero / indeterminado).
- Si es consulta: materia inferida y rol del cliente (si surge del relato).
- Si algún dato esencial no puede determinarse, indicarlo y preguntar antes de seguir.

### 2. Hechos relevantes aportados
- Resumen ordenado de los hechos que el material efectivamente trae. Solo lo aportado; no completar.

### 3. Hechos faltantes
- Datos determinantes que faltan para concluir. Uno por línea.
- Formato: `[VACÍO FÁCTICO] hecho que falta — por qué es determinante`.
- **Ambigüedad dirimente** *(énfasis modo consulta)*: si un término clave de la consulta
  admite dos lecturas fácticas que conducen a respuestas jurídicas **opuestas**, señalarla
  acá **antes** de todo análisis normativo, con `[VACÍO FÁCTICO]`, y estructurar el resto
  del diagnóstico **por escenarios** (uno por lectura) hasta que el abogado aclare.
  No elegir una lectura en silencio: una respuesta impecable sobre el escenario equivocado
  es inútil. *Ejemplo real: «prestación 100% extraterritorial» puede significar que el
  trabajador vive y trabaja en el exterior (activa el art. 57 CT y el conflicto de leyes)
  o que teletrabaja desde Paraguay para beneficiarios del exterior (relación laboral local
  ordinaria) — el lugar de prestación es donde se ejecuta el trabajo, no donde se
  aprovecha su resultado.*

### 4. Documentos y prueba necesarios
- Prueba documental que respaldaría la posición y que no se ve en el material.
- Formato: `[VACÍO PROBATORIO] afirmación o posición — prueba que correspondería`.
- En **modo escrito**, marcar además cada afirmación fáctica que el texto da por probada sin prueba
  ofrecida o producida.

### 5. Argumentos sin norma de respaldo *(énfasis modo escrito)*
- Cada afirmación jurídica del escrito que no está respaldada por una norma citada.
- Formato: `[ARGUMENTO SIN NORMA] "paráfrasis del argumento" — norma que correspondería: [del mapa / indeterminado]`.
- La norma sugerida sale del mapa de autoridad; si no está en el mapa → `[FUENTE OFICIAL PENDIENTE]`.

### 6. Normas aplicables a verificar
- Normas relevantes para el caso, tomadas del mapa de autoridad.
- Toda norma en `status: draft` o de **primera mención** → `[VERIFICAR VIGENCIA]`.
- Si el caso depende de un fallo aún no aportado → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.

### 7. Citas jurisprudenciales del escrito *(énfasis modo escrito)*
- Listar toda cita de jurisprudencia que figure en el texto. Para cada una:
  `[VERIFICAR VIGENCIA] "carátula / sala / año" — verificar contra PJ-CSJ antes de presentar`.
- Si el abogado aportó el fallo completo en la sesión, indicarlo como verificado en sesión y resumir
  su doctrina. **Nunca** dar por buena una cita no verificada.

### 8. Contradicciones internas *(énfasis modo escrito)*
- Inconsistencias entre partes del escrito (fechas, montos, calificación jurídica, peticiones).
- Formato: `[CONTRADICCIÓN] sección A: "…" / sección B: "…" — resolución necesaria`.

### 9. Riesgos de la posición del cliente
- Dónde está expuesto el cliente (procesal, probatorio, económico). Para cliente empleador, el perfil
  laboral añade el análisis patronal (mala fe procesal, contingencia, conveniencia transaccional).

### 10. Argumentos esperables de la contraparte
- Qué puede alegar razonablemente la otra parte. No es exhaustivo; es anticipación estratégica.

### 11. Estrategia recomendada
- Recomendación explícita entre las opciones disponibles (p. ej. negociar / intimar / despedir /
  documentar / esperar / conciliar / litigar), con sus supuestos. El abogado decide.

### 12. Próximo paso práctico
- La acción concreta siguiente (qué pedir, qué documento conseguir, qué redactar después del visto
  bueno). Una sola, accionable.

---

## 6. Catálogo de marcadores (cerrado)

Usar **solo** estos. Los seis primeros son los marcadores oficiales de `CLAUDE.base.md`; `[CONTRADICCIÓN]`
es una etiqueta interna de esta skill para ordenar el informe (no es cita).

| Marcador | Uso |
|---|---|
| `[VERIFICAR VIGENCIA]` | Norma o cita cuya vigencia/redacción no fue confirmada contra fuente oficial en sesión, o norma en `status: draft`. |
| `[VACÍO FÁCTICO]` | Falta un hecho determinante; hay que pedirlo antes de concluir. |
| `[VACÍO PROBATORIO]` | Falta prueba documental que respalde una afirmación o posición. |
| `[INSERTAR JURISPRUDENCIA VERIFICADA]` | La conclusión necesita un fallo que aún no fue aportado/verificado. |
| `[FUENTE OFICIAL PENDIENTE]` | No se ubicó la fuente oficial; no se rellena con memoria del modelo. |
| `[ARGUMENTO SIN NORMA]` | Afirmación jurídica sin norma de respaldo identificada, o sin precisar el artículo/inciso concreto. |
| `[CONTRADICCIÓN]` | (auditoría) Inconsistencia interna entre secciones del escrito. |

---

## 7. Qué NO hace esta skill

- No redacta ni reescribe: eso es la segunda etapa, con instrucción expresa del abogado.
- No cita normas de memoria ni completa jurisprudencia: las consulta del mapa o las marca pendientes.
- No asume materia ni rol del cliente: es neutral. El sesgo patronal lo aporta el perfil
  `paraguay-laboral` cuando está cargado.
- No computa plazos: para eso está la skill `plazos`. Si detecta un plazo en juego, lo señala y deriva.
