---
name: inconstitucionalidad
description: Impugnación de inconstitucionalidad paraguaya (excepción y acción, Sala Constitucional de la CSJ) con test de admisibilidad previo. Usar ante normas o resoluciones judiciales que violen la Constitución.
---

# Skill · Impugnación de inconstitucionalidad (Paraguay)

> **Fuentes.** CN arts. 132, 259 inc. 5 y 260; Ley N° 609/1995 (`verified`, art. 11 con el
> texto según Ley 7307/2024) y CPC (Ley 1337/1988, `verified`) arts. 538-564 y 582,
> verificados contra fuente primaria el 2026-07-18 (`verification-log.md`). Criterios de
> tribunales: `jurisprudencia.yaml` (`control_concentrado_via_reservada`,
> `admisibilidad_fundamentacion_concreta`, `diferimiento_por_accion_pendiente`). La Sala
> Constitucional NO tiene fallos con N° de A.I. confirmado en el mapa: esta skill afirma
> criterios por su clave, **nunca** un fallo puntual → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
>
> **Encaje:** el agravio de rango constitucional se detecta en `diagnostico-escritos`; esta
> skill elige la vía (excepción o acción), corre el test de admisibilidad bloqueante y guía el
> planteo. El cómputo fino del plazo va a `plazos`; la estructura del escrito, a
> `escritos-judiciales`.

## 1. Encuadre — control concentrado

En Paraguay el control de constitucionalidad es **concentrado**: solo la Corte Suprema de
Justicia declara la inconstitucionalidad de normas y de resoluciones judiciales (art. 132 CN;
art. 259 inc. 5 CN), y la ejerce por su **Sala Constitucional** (art. 260 CN; competencia del
art. 11 de la Ley N° 609, texto según Ley 7307/2024). La declaración tiene efecto **solo inter
partes** — no deroga la norma con alcance general (art. 555 CPC).

En supuestos especiales la competencia es del **pleno** de la Corte, no de la Sala: las
acciones y recursos contra resoluciones del TSJE (art. 3 inc. i, Ley N° 609) y el enjuiciamiento
de magistrados (Ley 3759/09 art. 33 [VERIFICAR VIGENCIA]); la declaración **de oficio** del
art. 563 CPC exige la integración del art. 16 de la Ley N° 609.

Consecuencia operativa (criterio `control_concentrado_via_reservada`): **nunca** pedir a un
juzgado o tribunal de apelación que "declare inconstitucional" una norma. La única vía es la
excepción o la acción ante la Sala. Ante un planteo adverso mal dirigido a un tribunal
ordinario, atacar la vía antes que el fondo.

## 2. Datos mínimos de entrada

Sin estos datos no se avanza: si falta uno, marcar `[VACÍO FÁCTICO]` y pedirlo.

- Resolución o norma impugnada (individualizada).
- Órgano que la dictó e instancia.
- Fecha y **forma** de notificación (de ella depende el cómputo del plazo).
- Recursos ordinarios interpuestos contra la resolución y su resultado.
- Norma, derecho o garantía constitucional infringida y **perjuicio concreto** al cliente.
- Si se opuso excepción de inconstitucionalidad y en qué oportunidad.
- Asiento del juzgado (fija dónde y ante quién se plantea).

## 3. Elección de vía

| Vía | Cuándo usarla | Base |
|---|---|---|
| **Excepción** de inconstitucionalidad | Defensa dentro de un juicio en trámite: la norma que la contraparte invoca o el juez aplicaría es inconstitucional. Se opone según el rol procesal. | 538-549 |
| **Acción** contra actos normativos | Impugnar en abstracto una ley, decreto, reglamento u otro acto normativo de autoridad. | 550-555 |
| **Acción** contra resoluciones judiciales | Atacar una resolución judicial ya dictada que viola la Constitución (o se funda en norma inconstitucional). | 556-561 |
| **Consulta** de constitucionalidad — vía **del juez**, no de parte | El órgano, de oficio y con la providencia de autos **ejecutoriada**, remite el expediente a la CSJ cuando a su juicio una norma aplicable puede ser contraria a la Constitución; el litigante solo puede **sugerirla**. La resolución que la dispone debe exponer en modo **concreto y preciso** los motivos de la duda. | 18 inc. a |

> El reenvío interno del art. 18 inc. a al "art. 200 de la Constitución" apunta a la CN de
> **1967** (el CPC es de 1988); hoy corresponde a los arts. 132/259/260 CN.

Detalle de cada vía (oportunidades, trámite, cómputos) → `references/vias-y-plazos.md`.

## 4. Test de admisibilidad (bloqueante: sin esto no se redacta)

Correr **en orden** antes de redactar. Salida cerrada: **`ADMISIBLE` / `INADMISIBLE` /
`INDETERMINADO`** (esta última siempre con `[VACÍO FÁCTICO]` o `[VACÍO PROBATORIO]`).

a. **Justiciabilidad y agravio concreto.** ¿Hay una norma constitucional **precisada** y una
   **lesión concreta, actual y propia**? El escrito debe autoabastecerse: la mera invocación
   genérica de artículos o el relato de irregularidades procesales no alcanza (arts. 552 y 557
   CPC), y la Sala rechaza **in límine** el planteo insuficiente (art. 12, Ley N° 609). Criterio
   verificado `admisibilidad_fundamentacion_concreta`: el desacuerdo con lo resuelto o el intento
   de reeditar la instancia ordinaria como tercera instancia se rechaza; explicitar caso por caso
   qué perjuicio de rango constitucional sufre el accionante.
b. **Legitimación — invocada y acreditada.** ¿El accionante es titular del derecho lesionado
   (art. 550 CPC)? No basta afirmarla: el examen previo de admisibilidad (art. 12, Ley N° 609)
   controla que esté **acreditada**, no solo invocada — práctica de admisibilidad relevada del
   portal oficial (ver `verification-log.md`).
c. **Plazo.** La acción contra resoluciones se promueve dentro de **9 días** desde la
   notificación (art. 557 CPC), computados con el régimen de plazos y días inhábiles de los
   arts. 145/147/149/150 CPC → el calendario concreto se calcula en `plazos` y
   `references/vias-y-plazos.md`. Vencido, la vía se pierde.
d. **Agotamiento de recursos ordinarios** (solo para el supuesto del art. 556.a): la resolución
   debe estar consentida o los recursos ordinarios agotados (art. 561 CPC).
e. **Barrera del art. 562 CPC — SOLO para el supuesto del art. 556.b.** Veda la acción
   **únicamente** si concurren de forma acumulativa: (i) hubo oportunidad de oponer la excepción
   del art. 538, (ii) la norma fue invocada por la contraparte y (iii) existe resolución que la
   aplicó. Si falta cualquiera de las tres, no hay barrera. **No es una preclusión general** y
   **no bloquea** la acción del art. 556.a.
f. **Resolución de la propia CSJ.** Es inimpugnable por esta vía (art. 564 CPC; art. 17, Ley
   N° 609): las resoluciones de la Corte no se atacan por inconstitucionalidad.
g. **Costo estratégico.** Dos o más impugnaciones rechazadas con imposición de costas en el
   mismo proceso exponen al cliente al art. 53 inc. a CPC (ejercicio abusivo). Un planteo débil
   no es neutro.

Resultado **`INADMISIBLE`** o **`INDETERMINADO`** → informar el déficit puntual y **no
redactar**. Solo `ADMISIBLE` habilita la redacción.

## 5. Acción contra resoluciones judiciales (flujo desarrollado)

- **Supuesto (art. 556 CPC):** 556.a — la resolución en sí es inconstitucional; 556.b — se funda
  en una ley u otro acto normativo inconstitucional. La distinción define qué recaudos aplican
  (recursos agotados en 556.a; barrera del 562 solo en 556.b).
- **Demanda (art. 557 CPC):** individualizar la resolución y el juicio en que recae, constituir
  domicilio y fundar el agravio **clara y concretamente**; se promueve en el plazo de 9 días.
- **Efecto suspensivo (art. 559 CPC):** la interposición suspende de pleno derecho solo cuando
  se impugna una **sentencia definitiva** o una interlocutoria con fuerza de tal; en los demás
  casos, la suspensión debe **pedirse** y la decide la Corte.
- **Trámite (art. 558 CPC):** sustanciación ante la Sala (traslado y vista según la norma).
- **Resultado (art. 560 CPC):** si prospera, la Corte declara la **nulidad** de la resolución y
  **reenvía** el expediente al juez o tribunal siguiente de turno para que resuelva de nuevo.

## 6. Excepción y acción contra normas (resumen operativo)

- **Excepción (arts. 538-549 CPC):** se opone según el **rol procesal** y su oportunidad
  (art. 538 CPC): el demandado o reconvenido, **al contestar** la demanda o la reconvención; el
  actor o reconviniente, **dentro de 9 días** desde la notificación de la providencia que tiene
  por contestada la demanda o la reconvención (reacciona a que la contestación se funda en norma
  inconstitucional). En 2ª y 3ª instancia rige el art. 545; en los juicios especiales, el
  art. 546; en los incidentes, el art. 547 (oportunidades detalladas → reference). **No
  suspende** el curso del principal (art. 543 CPC): el juicio avanza **hasta quedar en estado
  de sentencia**, pero el **dictado** de esta espera la resolución de la Corte sobre la
  excepción. Se sustancia en **expediente separado** (art. 539 CPC).
- **Acción contra actos normativos (arts. 550-555 CPC):** impugna la norma ante la Sala; la
  **suspensión de los efectos** de la norma procede solo **a pedido** de parte (art. 553 CPC).
- Detalle de oportunidades por rol, trámite y suspensión → `references/vias-y-plazos.md`.

## 7. Derivaciones y perfil empleador

- El agravio de rango constitucional nace en el diagnóstico → `diagnostico-escritos`.
- La estructura formal del escrito → `escritos-judiciales`; el calendario concreto e inhábiles
  → `plazos`.
- **Nulidad de la resolución vs. inconstitucionalidad:** un vicio de forma de la resolución se
  ataca por el **recurso de nulidad** (art. 404 CPC → `incidentes-nulidades`); la violación
  constitucional, por la **acción del art. 556.a**. Elegir mal la vía es un error técnico.
- **Amparo — fuera de alcance.** Esta skill no tramita amparos; solo la interfaz del art. 582
  CPC: cuando en un amparo sea necesario decidir la constitucionalidad de una norma, el juez
  eleva la cuestión a la Sala, y la declaración procede cuando la inconstitucionalidad sea
  **manifiesta**. (Criterios de contexto disponibles: `amparo_improcedente_accion_pendiente` y
  `falta_comunicacion_accion_no_vicia`.)
- Formalización del análisis en dictamen → `dictamenes`.
- **Perfil empleador (regla 10 de `CLAUDE.base.md`):** evaluar la propia contingencia de costas
  antes de plantear. Ante una acción de inconstitucionalidad de la **contraparte**, valorar su
  efecto práctico —puede diferir de hecho pronunciamientos aunque no haya suspensión formal
  (criterio `diferimiento_por_accion_pendiente`)— y su eventual **finalidad dilatoria**, que se
  **evalúa** por los estándares de los arts. 52-54 CPC (a pedido de parte), **nunca se presume**
  por la mera pendencia.

## 8. Gramática de autoridad

Rigen las reglas inmodificables y el catálogo cerrado de marcadores de `CLAUDE.base.md` (no se
repiten aquí). Toda cita normativa se toma del authority map; la jurisprudencia se afirma solo
como criterio de `jurisprudencia.yaml`. Para citar un Ac. y Sent. o A.I. puntual de la Sala
Constitucional → `[INSERTAR JURISPRUDENCIA VERIFICADA]` (no hay fallos con carátula/N° confirmado
cargados).
