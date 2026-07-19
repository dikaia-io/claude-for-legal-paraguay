# Catálogo de red-flags contractuales (Paraguay)

> Referencia de la skill `red-flags` (plugin `paraguay-contratos`). El **SKILL.md** define el
> marcador, el orden de ejecución y la categoría previa de invalidez metodológica; **este archivo
> es el catálogo**. Se recorre entero, siempre (no detenerse en la primera red-flag).
>
> **Cada red-flag declara 4 campos:** título · norma anclada · cómo se detecta · marcador a emitir.
>
> **Regla de anclaje (dura).** Los números de artículo salen del authority map
> (`shared/authorities/leyes.yaml`) y de las anclas verificadas en la Fase 0 del proyecto
> (`shared/authorities/verification-log.md`). **Ningún artículo se cita de memoria.** Cuando una
> red-flag no tiene ancla verificada, el marcador lleva un marcador de incertidumbre del catálogo
> cerrado de `CLAUDE.base.md` (§3) —`[VERIFICAR VIGENCIA]`, `[ARGUMENTO SIN NORMA]`,
> `[VACÍO PROBATORIO]`, `[INSERTAR JURISPRUDENCIA VERIFICADA]`, `[FUENTE OFICIAL PENDIENTE]`— y
> **nunca** un número de artículo suelto.
>
> El marcador `[RED FLAG — …]` señaliza criticidad; **no es una cita**. La cita al cliente la
> arma la skill que llama, aplicando la gramática de autoridad de `CLAUDE.base.md` (§4).

Todas las citas al **CC** son al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el
authority map). Las citas a leyes especiales se identifican por su número.

---

## Nivel 1 — Nulidad / ineficacia

Cláusulas o vicios que pueden privar de efectos al contrato o a la cláusula. Son los de mayor
criticidad: si aparece uno, encabeza el informe.

### 1.1 · Renuncia a derechos irrenunciables

- **Norma anclada:** sin ancla de artículo verificada para "derechos irrenunciables" en materia
  civil. Apoyo conceptual en el límite del **CC art. 9** (orden público y buenas costumbres) y en
  los requisitos del **CC art. 673**; el artículo concreto que fulmine la renuncia **no está
  verificado** en la tabla de anclajes.
- **Cómo se detecta:** cláusulas del tipo "la parte renuncia a todo reclamo/acción/derecho",
  "renuncia irrevocable a…", renuncia anticipada a garantías legales, a la prescripción, o a
  derechos que la ley declara indisponibles. En relaciones de consumo o laborales, cualquier
  renuncia del contratante débil.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: renuncia a un derecho posiblemente irrenunciable — CC art. 9 (orden público) [VERIFICAR VIGENCIA]]`

### 1.2 · Objeto o causa ilícita

- **Norma anclada:** sin ancla de artículo verificada específica para objeto/causa ilícita.
  Apoyo en **CC art. 9** (los actos no pueden dejar sin efecto leyes de orden público / buenas
  costumbres) y en **CC art. 673** (el objeto es requisito esencial del contrato). El artículo que
  sanciona la ilicitud del objeto o la causa **no está en la tabla de anclajes** → marcador.
- **Cómo se detecta:** objeto prohibido por la ley, contrario a la moral o al orden público;
  prestación imposible o indeterminable; finalidad ilícita encubierta (p. ej. simular una
  operación para eludir una prohibición legal).
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: posible objeto o causa ilícita — CC arts. 9 y 673 [ARGUMENTO SIN NORMA]]`
  (usar `[ARGUMENTO SIN NORMA]` si se afirma la ilicitud sin poder precisar el artículo sancionatorio concreto).

### 1.3 · Cláusulas abusivas en contrato de adhesión con consumidor

- **Norma anclada:** **Ley N° 1334/1998** de Defensa del Consumidor y del Usuario (`verified` en
  el authority map). **Los artículos concretos NO están verificados** en la tabla de anclajes →
  citar la ley **sin número de artículo**, o con `[VERIFICAR VIGENCIA]` si se necesita precisar.
- **Cómo se detecta:** primero, que sea **contrato de adhesión** (cláusulas predispuestas, no
  negociadas) y que una parte sea **consumidor/usuario final**. Luego, cláusulas que desequilibran:
  facultad unilateral de modificar el contrato, inversión de la carga de la prueba en contra del
  consumidor, exoneración de responsabilidad del proveedor, prórroga de jurisdicción que lo
  perjudica, adhesión a condiciones no informadas.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: posible cláusula abusiva en contrato de adhesión con consumidor — Ley N° 1334/1998 [VERIFICAR VIGENCIA]]`

### 1.4 · Limitación o exoneración de responsabilidad por dolo

- **Norma anclada:** **sin ancla de artículo verificada** en la tabla para la nulidad de la
  dispensa del dolo → marcador. (Conceptualmente se conecta con el orden público del CC art. 9,
  pero el artículo que fulmina la cláusula que exonera el dolo no está verificado.)
- **Cómo se detecta:** cláusulas que eximen o topan la responsabilidad de una parte "en todos los
  casos", "cualquiera sea la causa", incluso por incumplimiento intencional; renuncia previa a
  reclamar daños; topes de indemnización redactados sin excluir el dolo/culpa grave.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: limitación de responsabilidad que podría alcanzar el dolo — CC art. 9 [VERIFICAR VIGENCIA]]`

### 1.5 · Lesión

- **Norma anclada:** **CC art. 671** (lesión). La ventaja "manifiestamente injustificada y
  desproporcionada" obtenida explotando la necesidad, ligereza o inexperiencia de la otra parte
  habilita a demandar nulidad o modificación equitativa dentro de dos años; la notable
  desproporción hace presumir la explotación (salvo prueba en contrario).
- **Cómo se detecta:** desproporción evidente entre las prestaciones (precio muy por debajo/encima
  del valor real), plazos o penas leoninas, aprovechamiento de la posición de una parte. Requiere
  contrastar los valores; si faltan datos para medir la desproporción, marcar además el vacío
  fáctico.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: posible lesión (desproporción manifiesta) — CC art. 671]`
  (si falta el dato de valor para medir la desproporción, agregar `[VACÍO FÁCTICO]`).

### 1.6 · Simulación de relación laboral bajo contrato civil

- **Norma anclada:** **sin ancla civil verificada** en la tabla; la calificación laboral y sus
  consecuencias corresponden al **plugin laboral** (Código del Trabajo). Esta red-flag **detecta y
  deriva**, no califica.
- **Cómo se detecta:** un contrato civil/comercial (servicios, locación de obra, "monotributista",
  "profesional independiente") que en los hechos presenta **exclusividad + horario/jornada fijos +
  subordinación** (instrucciones, control, provisión de herramientas, integración a la estructura de
  la empresa, pago periódico como salario). Cuantos más indicadores, más fuerte la señal.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 1: posible simulación de relación laboral bajo forma civil — derivar al plugin laboral]`
  y, dado que la calificación depende de prueba de los hechos, agregar **`[VACÍO PROBATORIO]`**
  (exclusividad/horario/subordinación deben acreditarse). No afirmar la laboralidad como certeza:
  derivar a la skill laboral competente.

---

## Nivel 2 — Riesgo alto

Cláusulas válidas pero peligrosas, u omisiones que dejan a la parte expuesta. No anulan el
contrato, pero pueden costar caro.

### 2.1 · Cláusula penal manifiestamente excesiva

- **Norma anclada:** **CC arts. 454 y 459.** El art. 454 hace que la pena sustituya la
  indemnización de daños (no hay que probar el perjuicio); el **art. 459** permite al juez
  **reducir equitativamente** la pena cuando es manifiestamente excesiva o cuando la obligación fue
  cumplida en parte o irregularmente.
- **Cómo se detecta:** penalidades desproporcionadas frente al valor de la prestación o del
  incumplimiento (multas diarias que superan el capital, penas que se acumulan sin tope,
  "cláusula penal" que en realidad encubre un interés usurario). Señal: la pena excede
  holgadamente el daño previsible.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: cláusula penal posiblemente excesiva, sujeta a morigeración judicial — CC arts. 454 y 459]`

### 2.2 · Pacto comisorio / rescisión sin intimación previa ni plazo de subsanación

- **Norma anclada:** **CC arts. 724-729** (resolución por incumplimiento / pacto comisorio). El
  régimen exige, para el comisorio, un mecanismo de intimación a cumplir en un plazo antes de
  resolver; el art. 724 además excluye la resolución cuando el incumplimiento es de escasa
  importancia.
- **Cómo se detecta:** cláusulas que autorizan a una parte a resolver o rescindir "de pleno
  derecho", "sin necesidad de interpelación", "en forma automática", sin conceder plazo para
  subsanar; o que permiten resolver por cualquier incumplimiento, incluso insignificante.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: rescisión/pacto comisorio sin intimación ni plazo de subsanación — CC arts. 724-729]`

### 2.3 · Confidencialidad sin plazo determinado

- **Norma anclada (stack NDA):** protección sustantiva de secretos en la **Ley N° 3283/2007
  Cap. I** (arts. 1, 2, 3.B, 5 y 8: el art. 3.B nombra expresamente el incumplimiento de cláusulas
  de confidencialidad); régimen de no competencia / competencia desleal anexo en la **Ley N°
  1034/1983** (art. 106 pacto de no competencia con tope de 5 años; art. 108 inc. d como cláusula
  abierta); base contractual en el **CC art. 715** (fuerza obligatoria). **Reservas:** NO citar el
  plazo de 3 años del **art. 7 de la Ley 3283/2007** (está anclado a la presentación ante la
  autoridad sanitaria, no se traslada a un NDA civil genérico); la conexión con el **CP arts.
  147-149** (revelación de secretos) es palanca penal complementaria y su aplicación a un NDA
  civil es interpretativa → `[VERIFICAR VIGENCIA]`; no afirmar aplicación judicial concreta sin
  `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
- **Cómo se detecta:** cláusula de confidencialidad/NDA que no fija **plazo de duración** de la
  obligación ("las partes guardarán confidencialidad" sin decir por cuánto tiempo, ni desde
  cuándo, ni hasta cuándo), o que la extiende de forma perpetua e indeterminada.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: cláusula de confidencialidad sin plazo determinado — Ley N° 3283/2007 Cap. I]`
  (si además se invoca la palanca penal, agregar la remisión al CP arts. 147-149 con `[VERIFICAR VIGENCIA]`).

### 2.4 · Prórroga de jurisdicción o arbitraje en el extranjero

- **Norma anclada:** **Ley N° 7561/2025** de Arbitraje (`verified` en el authority map; deroga la
  Ley 1879/2002 salvo sus arts. 53-67). El sometimiento a arbitraje o a tribunales del exterior
  debe leerse bajo este régimen (y, si hay consumidor de por medio, contra la Ley 1334/1998).
- **Cómo se detecta:** cláusulas que someten los conflictos a **tribunales o árbitros de otro
  país**, a reglas de arbitraje extranjeras, o que fijan sede/ley aplicable fuera de Paraguay,
  cuando el contrato y las partes son locales. Señal frecuente en plantillas importadas (ver
  también invalidez metodológica en el SKILL.md).
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: prórroga de jurisdicción o arbitraje en el extranjero — Ley N° 7561/2025]`

### 2.5 · Ausencia de mecanismo de reajuste en contratos de larga duración

- **Norma anclada:** **NO ANCLABLE.** El CC no regula un mecanismo de reajuste/actualización del
  precio (verificado en Fase 0: sin resultado en el Cap. III de Locación ni en disposiciones
  generales). Es una **regla prudencial**, no una norma → marcador.
- **Cómo se detecta:** contratos de tracto sucesivo y **larga duración** (locación, suministro,
  servicios plurianuales) con precio fijo en guaraníes y **sin cláusula de ajuste/indexación** ni
  criterio de revisión periódica. Riesgo económico de erosión del valor, no de invalidez.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: contrato de larga duración sin mecanismo de reajuste del precio — [ARGUMENTO SIN NORMA]]`
  (regla prudencial; si se necesita afirmar una regla de reajuste, usar `[VERIFICAR VIGENCIA]` / `[FUENTE OFICIAL PENDIENTE]`).

### 2.6 · Garantías sin la forma o el registro exigidos

- **Norma anclada:** **CC arts. 700-702** (actos que exigen escritura pública; el art. 701 hace
  valer el instrumento deficiente como obligación de escriturar; el art. 702 permite demandar el
  otorgamiento). Aplica a las garantías cuya constitución la ley somete a forma/registro.
- **Cómo se detecta:** garantías reales (hipoteca, prenda) o actos que exigen escritura pública
  constituidos en instrumento privado o sin la inscripción registral necesaria; ausencia de la
  formalidad que da oponibilidad a la garantía frente a terceros.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: garantía sin la forma o el registro exigidos por la ley — CC arts. 700-702]`

### 2.7 · Compraventa de bien registrable sin cláusula de escrituración/inscripción

- **Norma anclada:** **CC art. 700** (escritura pública para inmuebles y demás actos registrables)
  y **arts. 701-702** (obligación de escriturar y su ejecución). Para la venta de cosa que no es de
  quien vende, ver además **CC arts. 743-744** (compraventa de cosa ajena).
- **Cómo se detecta:** compraventa de **inmueble o vehículo** (u otro bien registrable) que no
  prevé la **escrituración** ni la **inscripción registral** a favor del comprador, o que no fija
  quién y cuándo debe otorgar la escritura/transferir el registro. Verificar también que el
  vendedor sea el titular registral (riesgo de venta de cosa ajena, arts. 743-744).
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: compraventa de bien registrable sin cláusula de escrituración/inscripción — CC art. 700]`

### 2.8 · Omisión de garantías de evicción y de vicios redhibitorios

- **Norma anclada:** **CC art. 1759** (evicción: el adquirente a título oneroso responde si es
  privado del derecho adquirido) y **CC art. 1789** (vicios redhibitorios: vicios ocultos que hacen
  la cosa impropia para su destino). **Plazo de la acción redhibitoria: CC art. 668** (tres meses;
  está en el Libro II, prescripción liberatoria).
- **Cómo se detecta:** contratos de transmisión a título oneroso (compraventa, permuta) que
  **excluyen o no mencionan** la garantía de evicción y/o la de vicios redhibitorios, o que renuncian
  a ellas sin contrapartida; ausencia de previsión sobre qué pasa si un tercero reclama la cosa o si
  aparece un defecto oculto.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 2: omisión o renuncia de las garantías de evicción y vicios redhibitorios — CC arts. 1759 y 1789 (plazo redhibitoria art. 668)]`

---

## Nivel 3 — Riesgo medio

Omisiones y defectos que conviene corregir; no comprometen la validez pero debilitan la posición o
generan incertidumbre.

### 3.1 · Falta de domicilio especial constituido

- **Norma anclada:** **CC art. 62** (se puede elegir en los actos jurídicos un domicilio especial
  para determinados efectos, lo que importa prorrogar la jurisdicción). **Nota:** la prohibición de
  constituir domicilio especial **fuera de la República** es del art. 1560 y aplica **solo al
  contrato de seguro** — no generalizar a otros contratos.
- **Cómo se detecta:** el contrato no constituye **domicilio especial** de las partes para las
  notificaciones y los efectos del contrato, o lo hace de forma incompleta (sin dirección precisa).
  Dificulta notificar y determinar la jurisdicción.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: falta de domicilio especial constituido — CC art. 62]`

### 3.2 · Moneda extranjera sin cláusula de contingencia

- **Norma anclada:** para el interés moratorio, **CC art. 475** (no pueden estipularse intereses
  ni comisiones superiores a las **tasas máximas del Banco Central del Paraguay**, bajo pena de
  nulidad). El CC **no fija un porcentaje**: remite a la tasa máxima del BCP → **nunca inventar un
  porcentaje**. La cobertura del riesgo cambiario en sí es materia de pacto (regla prudencial).
- **Cómo se detecta:** precio/obligación en **dólares u otra moneda extranjera** sin prever qué
  pasa ante variaciones del tipo de cambio, indisponibilidad de la divisa o restricciones
  cambiarias; ausencia de mecanismo de conversión o de moneda de pago alternativa.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: obligación en moneda extranjera sin cláusula de contingencia cambiaria — [ARGUMENTO SIN NORMA]]`
  (si se pacta interés, verificar el tope del CC art. 475 → tasa máxima BCP; nunca afirmar un porcentaje).

### 3.3 · Prescripción no contemplada en la planificación del reclamo

- **Norma anclada:** **CC art. 659 inc. e** (plazo general de acciones personales: **diez años**);
  **CC art. 662 inc. b** (**tres años**, precio de mercaderías vendidas entre comerciantes);
  **CC art. 663 inc. e** (**dos años**, precio de mercaderías vendidas a no comerciantes). Régimen
  general de la prescripción liberatoria a partir del **CC art. 633**.
- **Cómo se detecta:** no es un defecto de la cláusula sino de la **estrategia**: verificar que el
  plazo de prescripción de las acciones del contrato esté identificado y que el reclamo se planifique
  dentro de él (según sea acción personal general, entre comerciantes o contra no comerciantes).
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: prescripción no contemplada en la planificación del reclamo — CC arts. 659 inc. e, 662 inc. b, 663 inc. e]`

### 3.4 · Individualización deficiente de las partes o del objeto

- **Norma anclada:** **CC art. 673** (requisitos esenciales del contrato: consentimiento, objeto y
  forma cuando la ley la exige). Un objeto indeterminado o partes mal identificadas afectan un
  requisito esencial.
- **Cómo se detecta:** partes sin datos de identificación suficientes (nombre, documento, calidad
  en que contratan, representación); objeto vago o indeterminado ("los servicios que se convengan",
  "el inmueble" sin individualizarlo, cantidades o especificaciones ausentes).
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: individualización deficiente de las partes o del objeto — CC art. 673]`

### 3.5 · Interés moratorio no pactado

- **Norma anclada:** **CC art. 475** (régimen y tope de los intereses; remite a la tasa máxima del
  BCP, **sin porcentaje legal fijo**). También conecta con la **mora** del **CC art. 424**.
- **Cómo se detecta:** obligaciones de dar sumas de dinero (precio, cuotas) que **no pactan interés
  moratorio** para el caso de atraso, dejando el resarcimiento del retardo librado a lo que fije
  eventualmente un juez.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: interés moratorio no pactado — CC art. 475 (tope: tasa máxima BCP)]`

### 3.6 · Cláusula de jurisdicción abierta sin ciudad fijada

- **Norma anclada:** sin ancla de artículo verificada específica para la cláusula de jurisdicción
  en blanco; se relaciona con el domicilio especial del **CC art. 62** (cuya elección importa
  prorrogar la jurisdicción). El defecto es de **redacción/completitud**, no de validez → marcador.
- **Cómo se detecta:** cláusula que somete los conflictos a "los tribunales de ______", "la
  jurisdicción competente" o deja el espacio en blanco, sin fijar la **ciudad/circunscripción**.
- **Marcador a emitir:**
  `[RED FLAG — NIVEL 3: cláusula de jurisdicción abierta sin ciudad fijada — CC art. 62 [ARGUMENTO SIN NORMA]]`

---

## Cierre — recordatorio de disciplina de cita

Al trasladar cualquiera de estas red-flags a una salida para el cliente, la **primera mención
normativa relevante** lleva `[VERIFICAR VIGENCIA]`, salvo que la fuente primaria haya sido revisada
en la sesión. Es la **regla 3 del proyecto** (`CLAUDE.base.md` §2); **no se reescribe acá**: rige
tal como está. Estas anclas están `verified` en el authority map, pero eso no exime de los cuatro
controles de la gramática de autoridad (fuente / fecha de verificación / tipo de autoridad / nivel
de certeza) cuando la observación se presenta como cita.
