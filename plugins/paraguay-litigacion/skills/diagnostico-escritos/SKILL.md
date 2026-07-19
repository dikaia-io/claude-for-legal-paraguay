---
name: diagnostico-escritos
description: Diagnóstico procesal profundo de escritos de litigación paraguaya. Extiende el diagnóstico del núcleo con tres módulos - chequeo procesal formal (requisitos, etapa, preclusión, fuero), matriz pretensión-elementos-prueba con lista de vacíos como salida prioritaria, y triage de escritos adversos (mérito, plazos reales, opciones de respuesta con recomendación). No redacta - diagnostica
---

# Skill · Diagnóstico de escritos de litigación (Paraguay)

> **Origen del método.** La estructura de auditoría es la de la skill `diagnostico` del núcleo
> (regla nº 9). Los módulos procesales combinan dos referencias — patrón conceptual, no contenido:
> el upstream `anthropics/claude-for-legal` (`litigation-legal`: element chart y triage de
> demandas) y el fork argentino `claude-for-legal-argentina` de Cristian Aboitiz
> (`diagnostico-SKILL.md`: peticiones sin fundamento, observaciones estructurales, alerta de plazo
> fatal y síntesis con veredicto). Normas: solo anclajes `verified` del authority map
> (verificación 2026-07-05 en `verification-log.md`).

## Regla de encaje (no duplicar el núcleo)

**Paso 0 — siempre:** correr la skill `diagnostico` de `paraguay-legal-core` (las 12 secciones).
Esta skill **no repite** esa auditoría: la asume hecha y agrega la capa procesal. Se activa cuando:
- hay **expediente en trámite** o etapa procesal identificable;
- el escrito a diagnosticar es **de la contraparte** (demanda, excepciones, intimación recibida);
- el abogado pide evaluar **viabilidad probatoria** de una demanda/contestación antes de presentarla.

Si no hay litigio en juego, el diagnóstico del núcleo basta; no invocar esta skill.

Como todo diagnóstico: **no redacta, no modifica, no concluye el mérito**. Recomienda con supuestos
explícitos; el abogado decide. La redacción posterior es de `escritos-judiciales` o
`juicio-ejecutivo`, previa instrucción expresa.

## Módulo 1 — Chequeo procesal formal

Sobre el escrito (propio o ajeno), en este orden:

1. **Tipo de escrito y requisitos del fuero.** Contrastar contra la estructura correspondiente de
   `escritos-judiciales` (demanda: art. 215 CPC; contestación: arts. 234-235 CPC y sus cargas;
   excepciones previas: arts. 223-224 CPC; ejecutivo: skill `juicio-ejecutivo`). Todo requisito
   ausente se lista con su artículo.
2. **Fuero correcto.** Verificar que el régimen procesal invocado sea el del fuero: excepciones
   civiles (art. 224 CPC) ≠ laborales (art. 119 CPT, taxativo) ≠ ejecución civil (art. 462 CPC) ≠
   ejecución laboral (arts. 356-357 CPT). Un cruce de fuero es hallazgo crítico.
3. **Etapa procesal y preclusión.** ¿El planteo llega en la etapa que lo admite? (p. ej. documental
   fuera de los supuestos del art. 221 CPC; hechos no articulados que se pretenden probar,
   art. 247; reconvención fuera de la contestación, art. 237; excepción ejecutiva fuera del plazo
   de 5 días, art. 460). Los cómputos concretos se derivan a la skill `plazos` del núcleo.
4. **Riesgo de nulidad** — en ambos sentidos: vicios que la contraparte podría invocar contra
   nuestro escrito, y vicios del procedimiento aprovechables (en ejecutivo: art. 463 CPC y trámites
   irrenunciables del art. 461; en laboral: art. 357 CPT).
5. **Peticiones sin desarrollo en fundamentos.** Cada punto del petitorio debe tener su desarrollo
   argumental y normativo en el cuerpo. Casos típicos: daños pedidos sin cuantificación ni norma
   habilitante; cautelares sin acreditar verosimilitud del derecho y peligro en la demora; recursos
   sin agravio preciso; costas sin principio aplicable. Etiqueta interna de auditoría (misma
   categoría que `[CONTRADICCIÓN]`, no es marcador de cita): `[PETICIÓN SIN FUNDAMENTO] "texto de
   la petición" — qué falta desarrollar`.
6. **Alerta de plazo fatal.** Si el escrito o la posición involucra una acción o recurso sujeto a
   caducidad o prescripción (p. ej. caducidad de medidas preparatorias, art. 447 CPC; ordinario
   posterior, art. 471; prescripción laboral, art. 399 CT), destacarlo **al inicio del
   diagnóstico** — norma, plazo, inicio del cómputo — y derivar el cómputo exacto a la skill
   `plazos`. Un diagnóstico impecable entregado después del vencimiento no sirve de nada.
7. **Observaciones estructurales (máx. 5, en prosa).** Lo que no encaja en las categorías
   anteriores: secciones obligatorias ausentes (demanda sin ofrecimiento de documental, art. 219
   CPC; contestación sin negativa categórica, art. 235), **orden de argumentos que debilita la
   posición** (defensa de fondo desarrollada antes que la nulidad o la excepción de previo
   pronunciamiento), extensión desproporcionada para el tipo de escrito, argumentos repetidos que
   conviene unificar.
8. **Chicanas esperables.** Anticipación estratégica: qué incidencias dilatorias o planteos de mala
   fe puede intentar la contraparte sobre este escrito, y qué exposición tiene la posición propia
   bajo los arts. 51-56 CPC (buena fe, art. 51; mala fe tipificada, art. 52; ejercicio abusivo,
   art. 53 — p. ej. tres incidentes perdidos con costas; sanciones con presunción en contra, costas
   al culpable aunque venza y responsabilidad conjunta del profesional, arts. 54-56). En laboral,
   el equivalente son los arts. 30 y 51 CPT (ver `escritos-laborales.md`).

## Módulo 2 — Matriz pretensión → elementos → prueba

El corazón del diagnóstico probatorio. Formato completo, estados y ejemplo:
`references/matriz-elementos.md`.

Resumen del método:
1. Por cada **pretensión o defensa** del escrito, descomponer en **elementos** que hay que probar.
   Los elementos salen de la **norma citada en el escrito o del authority map** — nunca de memoria.
   Elemento sin ancla verificada → `[ARGUMENTO SIN NORMA]` o `[FUENTE OFICIAL PENDIENTE]`.
2. Por cada elemento: **prueba que lo respalda** (con cita puntual: fs., anexo, testigo),
   **prueba en contra** (la vulnerabilidad de la fila) y **estado**.
3. **Salida prioritaria: la lista de vacíos.** El diagnóstico vale por lo que falta, no por lo que
   sobra. Cada vacío indica qué prueba lo cerraría y en qué etapa todavía se puede producir.
4. **Sesgo a marcar:** no marcar un vacío real es una puerta de un solo sentido (demanda que se
   pierde, defensa precluida); marcar de más se limpia en revisión. Ante la duda, marcar.
5. **Prohibido rellenar:** prueba insuficiente = `[VACÍO PROBATORIO]`, nunca completar con
   conocimiento del modelo ni con "cómo suelen salir estos casos".

## Módulo 3 — Triage de escrito adverso

Cuando lo diagnosticado es un escrito **recibido** (demanda notificada, excepciones opuestas,
intimación, carta documento):

1. **Extracción de campos:** quién (parte, patrocinio), qué pide (pretensiones y montos), plazo que
   declara, base legal que cita, amenazas/apercibimientos.
2. **Triage de plazos — tres relojes distintos:** el plazo que la contraparte declara (no vincula),
   el **plazo legal real** (computar vía skill `plazos`; p. ej. traslado de demanda ordinaria:
   18 días, arts. 222/234 CPC; excepciones en ejecutivo: 5 días, art. 460 CPC), y el **plazo
   interno de decisión** (plazo legal menos días de redacción y aprobación). Los tres se informan.
3. **Evaluación de mérito** (lectura estructurada, no opinión definitiva): sus hechos vs. lo que
   sabemos; su base legal ¿aplica al caso?; su mejor versión si litiga; nuestras defensas
   disponibles (encuadradas en el fuero correcto); proporcionalidad entre lo pedido y lo probable;
   credibilidad de la amenaza (¿demanda ya promovida? ¿litigante habitual?).
4. **Calificación cerrada:** `sólido / discutible / débil / temerario`. Sin matices intermedios:
   es triage, no dictamen.
5. **Opciones de respuesta (3-4) con tradeoffs y una recomendación.** Según el caso: contestar el
   fondo / oponer excepciones (previas o ejecutivas según fuero) / allanarse en lo indefendible
   (efecto en costas: art. 198 CPC) / negociar-transar antes de contestar / dejar vencer y asumir
   la rebeldía (casi nunca; explicitar el costo). Cada cita de la contraparte queda etiquetada
   `[VERIFICAR VIGENCIA]` hasta contrastarla — **verificar la cita ajena es parte del triage**: la
   base legal mal citada de una demanda es defensa.

## Salida

Un solo bloque, después del diagnóstico del núcleo: **alerta de plazo fatal** (si existe, siempre
primero) → **Módulo 1** (hallazgos formales, críticos primero) → **Módulo 2** (matriz + lista de
vacíos) → **Módulo 3** (si aplica: campos, relojes, mérito, opciones y recomendación) →
**Síntesis** → **Próximo paso práctico** (uno, accionable).

**Síntesis (máx. 5 líneas):** conteo de hallazgos por categoría + veredicto cerrado sobre el
escrito: `presentable con correcciones menores` / `requiere revisión sustancial` / `problemas que
afectan su viabilidad` — y la observación más urgente. Cierre fijo: *«Diagnóstico completo.
¿Procedemos con las correcciones, o querés revisar algún punto primero?»* Si el abogado ordena
proceder sobre un escrito con contradicciones o peticiones sin fundamento que afectan la
viabilidad, **advertirlo de nuevo antes de modificar** — la instrucción de proceder no borra el
hallazgo.

- Marcadores: solo el catálogo cerrado del núcleo (`[VACÍO FÁCTICO]`, `[VACÍO PROBATORIO]`,
  `[VERIFICAR VIGENCIA]`, `[INSERTAR JURISPRUDENCIA VERIFICADA]`, `[FUENTE OFICIAL PENDIENTE]`,
  `[ARGUMENTO SIN NORMA]`) más las etiquetas internas de auditoría `[CONTRADICCIÓN]` (del núcleo)
  y `[PETICIÓN SIN FUNDAMENTO]` (de esta skill). Las etiquetas internas ordenan el informe; no son
  marcadores de cita y no se crean otras.
- Si el abogado quiere el análisis como **documento entregable al cliente**, se formaliza con la
  skill `dictamenes` (plugin `paraguay-laboral`): ella pone la estructura de dictamen; esta skill
  aporta el contenido. No duplicar el análisis.

## Qué NO hace esta skill

- No redacta ni contesta: eso viene después, con instrucción expresa (`escritos-judiciales` /
  `juicio-ejecutivo`).
- No computa plazos: los deriva a `plazos` y reporta los tres relojes.
- No emite opinión de mérito definitiva: la calificación del triage es para decidir la ruta.
- No valida la base legal ajena de memoria: la contrasta contra el authority map o la marca
  `[VERIFICAR VIGENCIA]`.
- No usa jurisprudencia no verificada: `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
