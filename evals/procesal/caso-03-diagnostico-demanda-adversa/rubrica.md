---
titulo: Diagnóstico de demanda adversa recibida — triage, matriz de elementos y opciones
---
## Rúbrica · caso-03-diagnostico-demanda-adversa

> Verificar cada cita contra el CPC/CC consolidados locales antes de puntuar.

### Obligatorios

- [ ] **No redacta la contestación**: diagnostica primero (regla nº 9 del núcleo) y deja la
  redacción para una segunda etapa con instrucción expresa.
- [ ] **Desarma el plazo declarado**: el "plazo de 9 días" de la contraparte no vincula; el plazo
  legal del traslado de demanda ordinaria es **18 días** (arts. 222 y 234 CPC). Informa los tres
  relojes: plazo declarado / plazo legal real (computado desde la notificación, derivando el
  cómputo fino a la skill de plazos) / plazo interno de decisión.
- [ ] **Matriz pretensión-elementos-prueba** del actor con lista de vacíos como salida prioritaria.
  Debe detectar al menos: el **monto del daño sin respaldo documental** (elemento en `vacío` — la
  documental debía acompañar la demanda, art. 219 CPC) y la **fecha del hecho sin articular**
  ("se probará en autos" — los hechos no articulados no se prueban después, art. 247 CPC; además la
  demanda debe explicar claramente los hechos, art. 215 inc. d).
- [ ] **Verifica la base legal ajena en vez de darla por buena**: el "art. 1833 CC y concordantes"
  queda marcado `[VERIFICAR VIGENCIA]` / a contrastar contra el texto local antes de asumir que
  funda la responsabilidad invocada — verificar la cita de la contraparte es parte del triage.
- [ ] **Carga de la prueba**: recuerda que prueba quien afirma (art. 249 CPC) — los vacíos del
  actor son defensa del demandado, no problema propio.
- [ ] **Opciones de respuesta con recomendación única**: al menos contestar el fondo con negativa
  categórica hecho por hecho (art. 235 CPC), evaluar **excepciones previas** (art. 224 — p. ej.
  defecto legal por la forma de proponer la demanda, según lo que el análisis sostenga) recordando
  que su oposición interrumpe el plazo (art. 223), y la vía transaccional. Recomienda una con
  fundamentos.

### Deseables

- [ ] Califica el mérito con la escala cerrada (sólido / discutible / débil / temerario) y lo
  presenta como triage, no como dictamen.
- [ ] Señala la exposición del actor a los arts. 51-56 CPC si la demanda altera la verdad
  (mala fe, art. 52 inc. a) y el efecto en costas del allanamiento oportuno (art. 198) si algo
  fuera indefendible.
- [ ] Marca los datos faltantes propios con `[VACÍO FÁCTICO]` (fecha exacta de notificación,
  fuero/juzgado, relación previa con el actor) antes de concluir.
- [ ] Ofrece formalizar el análisis como dictamen entregable (skill `dictamenes`) si el cliente lo
  quiere por escrito.

### Ausentes esperados

- [ ] **No** debe aceptar el plazo de 9 días ni recomendar "contestar ya mismo" sin computar el
  plazo real.
- [ ] **No** debe completar los vacíos del actor razonando "cómo suelen probarse estos daños": los
  vacíos ajenos se explotan, no se rellenan.
- [ ] **No** debe validar el art. 1833 CC de memoria ni construir la teoría del caso del actor.
- [ ] **No** debe citar jurisprudencia sin verificación PJ/CSJ (`[INSERTAR JURISPRUDENCIA
  VERIFICADA]`).
- [ ] **No** debe usar categorías argentinas (arts. CPCCN, "excepción de falta de legitimación
  pasiva" como previa civil paraguaya, etc.).
