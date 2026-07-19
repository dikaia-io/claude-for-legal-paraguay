---
titulo: Acción de inconstitucionalidad contra sentencia laboral con rubro agregado (ultra petita) — vía, admisibilidad y plazo
---
## Rúbrica · caso-01-accion-contra-sentencia-laboral

> Verificar cada cita contra el CPC (Ley N° 1337/1988) y la Ley N° 609/1995 consolidados
> localmente antes de puntuar; el cómputo del plazo se contrasta contra el ejemplo trabajado de
> `references/vias-y-plazos.md` de la propia skill (notificación en viernes → hoy hábil 6 →
> vencimiento hábil 9 → gracia del día siguiente).
>
> **Nota de numeración:** el diagnóstico previo es la **regla 9** de `shared/templates/CLAUDE.base.md`
> y el perfil empleador la **regla 10** (no "regla 8"; se cita por el número real del archivo).

### Obligatorios

- [ ] **Test de admisibilidad corrido ANTES de redactar, con salida cerrada `ADMISIBLE`:** recorre
  los pasos del test (§4 de la skill) — justiciabilidad y agravio concreto (el rubro agregado sin
  fundamentación como vicio propio de la resolución, no mera disconformidad con lo resuelto),
  legitimación de [CLIENTE_EMPRESA], plazo, agotamiento (561), barrera del 562 y descarta
  trivialmente el supuesto del 564 (no es resolución de la propia CSJ) — y concluye
  expresamente el estado. No debe quedar en `INDETERMINADO`: los datos del caso alcanzan.
- [ ] **Vía y encuadre:** acción contra resoluciones judiciales (arts. 556-560 CPC), no excepción
  del art. 538 (el juicio ya terminó, no hay proceso en trámite en el que oponerla) ni un recurso
  ordinario adicional. Encuadra en el **art. 556.a** (la resolución es por sí violatoria de la CN
  — defensa en juicio y debido proceso, por el rubro incorporado sin fundamentación), **no** en el
  556.b (no hay norma inconstitucional invocada por la contraparte que la resolución haya
  aplicado).
- [ ] **Agotamiento (art. 561 CPC) verificado:** identifica que el propio Acuerdo y Sentencia
  resolvió los recursos de apelación y nulidad contra la sentencia de 1ª instancia y que no queda
  recurso ordinario pendiente ni disponible contra él — es la resolución que "causa estado"; el
  plazo del 556.a corre desde su notificación.
- [ ] **Barrera del art. 562 CPC — análisis correcto de que NO aplica:** explica que el 562 rige
  únicamente para el supuesto del 556.b y exige la concurrencia **acumulativa** de sus tres
  requisitos (oportunidad de oponer la excepción del 538, norma invocada por la contraparte,
  resolución que la aplicó). Como [TRABAJADOR_1] nunca invocó una norma cuya constitucionalidad se
  discuta, ninguno de los tres concurre. Debe decirlo explícitamente y **no tratar el 562 como una
  preclusión general** que alcance también al 556.a.
- [ ] **Cómputo exacto del plazo de 9 días (art. 557, régimen del art. 147):** desde la
  notificación por cédula del **viernes 2 de octubre de 2026** (día de la diligencia, no
  computable), sin contar los fines de semana: **hoy, lunes 12 de octubre, es el día hábil 6**;
  quedan los hábiles 7 (martes 13), 8 (miércoles 14) y **9** (**jueves 15 de octubre de 2026** —
  vencimiento). Menciona la **gracia del art. 150**: el escrito todavía se admite hasta las
  **09:00 del viernes 16 de octubre de 2026**. No corresponde ampliación por distancia del
  art. 149 (el tribunal y la Sala Constitucional tienen el mismo asiento: Asunción).
- [ ] **Efecto suspensivo automático (art. 559 CPC):** por tratarse de una sentencia definitiva de
  segunda instancia, la sola interposición suspende de pleno derecho, sin necesidad de pedirlo.
- [ ] **Ninguna cita de fallo puntual de la Sala Constitucional no cargado en
  `jurisprudencia.yaml`:** si invoca una tendencia, lo hace **por clave** (p. ej.
  `control_concentrado_via_reservada`, `admisibilidad_fundamentacion_concreta`) y no como un
  Acuerdo y Sentencia o Auto Interlocutorio con carátula o número; para un fallo puntual usa
  `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
- [ ] **Contingencia de costas (art. 53 inc. a CPC):** como parte del perfil empleador (**regla
  10** de `CLAUDE.base.md`), advierte que un planteo débil expone a costas y que la repetición de
  impugnaciones rechazadas con costas agrava el riesgo de ejercicio abusivo.
- [ ] **Diagnóstico previo (regla 9 de `CLAUDE.base.md`):** no pasa directo a "sí, presentamos" —
  entrega o deriva explícitamente un diagnóstico del agravio antes de encarar cualquier
  redacción.

### Deseables

- [ ] Deriva a `diagnostico-escritos` para armar la matriz del agravio (identificar el rubro
  agregado sin fundamentación como agravio de rango constitucional, distinto de una simple
  disconformidad con lo resuelto).
- [ ] Menciona el **art. 12 de la Ley N° 609** (rechazo in límine de planteos con fundamentación
  insuficiente) como el estándar que la propia demanda debe superar.
- [ ] Aclara que, de prosperar, el resultado es la **nulidad de la resolución y el reenvío** al
  tribunal siguiente en orden de turno para que falle de nuevo (art. 560) — no la desaparición
  automática de toda la condena laboral, que puede subsistir en lo no viciado.
- [ ] Señala expresamente que la vía de **excepción** (538) no es aplicable a este caso porque el
  juicio ya concluyó (no hay proceso en trámite en el que oponerla).

### Ausentes esperados

- [ ] **No** debe redactar la demanda de inconstitucionalidad directamente sin haber corrido y
  declarado antes el test de admisibilidad.
- [ ] **No** debe afirmar que una declaración favorable tendría efecto **erga omnes** o alcance
  general: el control concentrado paraguayo es siempre inter partes (encuadre de la skill, §1;
  art. 555 CPC para el supuesto de normas) — sobre una resolución judicial, un resultado
  favorable se traduce en nulidad y reenvío (art. 560), no en la derogación de nada con alcance
  general.
- [ ] **No** debe tratar el art. 562 CPC como un bloqueo automático o una preclusión general
  aplicable a cualquier planteo tardío: solo opera, y de forma acumulativa, en el supuesto del
  556.b.
- [ ] **No** debe recomendar la vía de excepción del art. 538 CPC (es para juicio en trámite; acá
  ya no lo hay) ni el recurso de nulidad del art. 404 CPC (ese es el cauce para vicios de forma de
  la resolución, no para la violación constitucional de fondo).
- [ ] **No** debe citar un Acuerdo y Sentencia o Auto Interlocutorio puntual de la Sala
  Constitucional sin verificación PJ/CSJ (`[INSERTAR JURISPRUDENCIA VERIFICADA]`).
- [ ] **No** debe usar categorías o instituciones de otras jurisdicciones (recurso extraordinario
  federal, certiorari, control difuso "a la americana", casación laboral, etc. — Paraguay tiene
  control concentrado ante la Sala Constitucional de la CSJ).
