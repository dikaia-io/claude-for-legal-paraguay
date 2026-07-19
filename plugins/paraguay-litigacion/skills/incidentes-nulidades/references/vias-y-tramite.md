# Nulidades e incidentes — trámite detallado y estrategia

> Articulado verificado contra el texto consolidado local del CPC (2026-07-05, ver
> `shared/authorities/verification-log.md`). Criterios de tribunales en
> `shared/authorities/jurisprudencia.yaml`.

## Trámite del incidente (arts. 180-191 CPC)

| Paso | Regla | Base |
|---|---|---|
| Concepto | Toda cuestión accesoria relacionada con el objeto principal, sin procedimiento especial propio | 180 |
| ¿Suspende el principal? | Solo si impide de hecho y de derecho continuar sustanciándolo (se tramita en los mismos autos); si no, **pieza separada sin suspensión** y el juez resuelve en 10 días | 181-182 |
| Escrito | Fundar **clara y concretamente en los hechos y en el derecho** + ofrecer **toda** la prueba + acompañar la documental (o individualizarla) | 183 |
| Filtro | Rechazo **in límine** del incidente manifiestamente improcedente, por decisión fundada; apelable **sin efecto suspensivo** | 184 |
| Traslado | **5 días** a las partes; al contestar ofrecen su prueba; el traslado se notifica por cédula dentro de 3er día | 185 |
| Prueba | Solo si el juez la estima necesaria: **máx. 10 días**; pericial con **un** perito de oficio; **máx. 4 testigos** por parte, declarando en la sede del juzgado | 186-187 |
| Resolución | Sin más trámite, contestado el traslado o producida la prueba; las cuestiones accesorias se deciden en la misma interlocutoria | 188-189 |
| Acumulación | Incidentes suspensivos con causas simultáneas y conocidas → **un mismo escrito**; los promovidos después se desestiman sin trámite | 190 |
| Plazo residual | Sin plazo expreso: **5 días desde conocida la causa** | 191 |

## Comparativa de vías de nulidad

| | Incidente (117/180-191) | Recurso (404-408) | Acción autónoma (409) |
|---|---|---|---|
| Vicio en | Actuaciones | Resoluciones | Proceso ya firme (visto por un tercero) |
| Quién | Parte perjudicada que no contribuyó (112) | Apelante (implícito en la apelación, 405) | **Tercero** en indefensión |
| Cuándo | 5 días desde el conocimiento (191; convalidación 114) | Con la apelación (plazos del recurso) | Sentencia firme y ejecutoriada |
| Ante quién | La instancia donde se produjo el vicio | El superior | Juzgado civil de turno (con inhibiciones del 409) |
| Efecto si prospera | Caen el acto y sus consecuencias (115-117); renovación (116) | El tribunal anula **y resuelve el fondo** (406) | Repara el agravio del tercero |
| Válvulas de escape | Finalidad cumplida (111), convalidación (114), falta de trascendencia | No se pronuncia si la apelación repara (407); de oficio aunque desistido (`nulidad_oficiosa_alzada`) | Residual: solo si falsedad/inhabilidad no alcanzan |

## Vicios típicos y su vía (práctica)

| Vicio | Vía y observaciones |
|---|---|
| Notificación de la demanda en domicilio equivocado | Incidente en primera instancia; el perjuicio es autoevidente si hubo rebeldía, pero igual articularlo (defensas impedidas). Si el demandado igual compareció en plazo → finalidad cumplida (111), no hay nulidad |
| Traslado omitido / audiencia sin notificar | Incidente; medir convalidación: ¿cuándo se conoció efectivamente? |
| Sentencia incongruente (extra/ultra/citra petita) o sin fundamentación | Recurso de nulidad (404), implícito en la apelación |
| Vicios de la intimación de pago o citación en ejecutivo | Excepción de nulidad del 463 (skill `juicio-ejecutivo`), no incidente del 180 |
| Tercero afectado por sentencia firme en juicio del que no fue parte | Acción autónoma (409), previa verificación de que falsedad/inhabilidad no alcanzan |
| "Incidente" atípico sin base legal (p. ej. tacha de testigos como incidente autónomo) | Los tribunales lo juzgan igual por el filtro del 183/184: sin fundamento normativo claro → rechazo con costas |

## Estrategia

**Nulidicente:**
- El planteo se escribe alrededor de la **trascendencia**: primero el perjuicio y la defensa
  impedida, después el vicio. Un párrafo que no pueda contestar "¿qué habría cambiado?" es un
  planteo perdido.
- Fijar con prueba la **fecha de conocimiento** del vicio (el reloj del 191 corre desde ahí).
- Si el vicio está en una actuación **y** contaminó la resolución, la vía es el incidente en la
  instancia (117); la nulidad de la resolución cae por arrastre (117, 2º párr.). No "guardarse"
  el vicio de actuación para la Alzada: se convalida.
- Presupuestar el riesgo: costas + contador del art. 53 inc. b.

**Contra el nulidicente:**
- Orden de ataque: trascendencia → convalidación (5 días) → protección (112) → finalidad (111).
- Documentar el patrón dilatorio (fechas de cada incidente, resultado y costas) para pedir la
  declaración de ejercicio abusivo (arts. 53-56) y la tramitación conjunta del 190 contra la
  dosificación de incidentes.

**En la Alzada (cualquier posición):** aunque nadie funde la nulidad, el tribunal puede
declararla de oficio (113; criterio `nulidad_oficiosa_alzada`) — al apelar o contestar agravios,
revisar el expediente con ojos de nulidad antes que el adversario o el tribunal lo hagan.

> Para citar un A. y S. concreto sobre cualquiera de estos criterios →
> `[INSERTAR JURISPRUDENCIA VERIFICADA]` (carátulas pendientes de cotejo con PJ/CSJ).
