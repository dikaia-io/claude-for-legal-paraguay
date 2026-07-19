---
name: juicio-ejecutivo
description: Guía y redacta escritos del juicio ejecutivo civil paraguayo (CPC, Ley 1337/1988, arts. 439-475) — verificación del título, preparación de la vía ejecutiva, intimación de pago y embargo, excepciones, sentencia de remate y cumplimiento — para ejecutante o ejecutado
---

# Skill · Juicio ejecutivo (Paraguay)

> **Fuentes.** Articulado verificado contra el texto consolidado local del CPC (Ley N° 1337/1988,
> `verified` en `shared/authorities/leyes.yaml`; verificación 2026-07-05 en `verification-log.md`).
> Estructura de práctica contrastada con los modelos del estudio (03_EJECUTIVO). Sin jurisprudencia
> cargada: donde el argumento la requiera → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
>
> **Ámbito.** Ejecución **civil/comercial** por el CPC. La ejecución **laboral** se rige por los
> arts. 356-357 CPT (ver `escritos-judiciales` → `references/escritos-laborales.md`). La ejecución
> de sentencias judiciales tiene su propio régimen (arts. 519 y ss. CPC).

## Paso 0 — Perfil de la parte

Preguntar si el cliente es **ejecutante** (acreedor que cobra) o **ejecutado** (deudor que se
defiende). Todo el análisis posterior cambia de lado. Con cliente empresa, aplicar el perfil del
núcleo: contingencia económica, conveniencia transaccional y mala fe procesal (regla nº 10).

## Paso 1 — Verificación del título (antes de redactar nada)

Procede la vía ejecutiva si un **título que trae aparejada ejecución** documenta una **obligación
exigible de dar cantidad líquida de dinero** (art. 439). Chequear:

1. **¿El título está en la lista del art. 448?** a) instrumento público; b) instrumento privado
   suscripto por el obligado, reconocido judicialmente o con firma autenticada por escribano con
   intervención del obligado y registrada; c) crédito por alquileres o arrendamientos de inmuebles;
   d) confesión de deuda líquida y exigible ante juez competente; e) cuenta aprobada o reconocida
   por preparación; f) letra de cambio, factura conformada, vale o pagaré y cheque rechazado,
   protestados cuando correspondiere o reconocidos en juicio; g) póliza de fletamento, conocimiento,
   carta de porte o análogo; h) demás títulos con fuerza ejecutiva legal sin procedimiento especial.
   También: crédito por expensas comunes con sus recaudos (art. 449).
2. **¿Exigible?** Plazo vencido y obligación no sujeta a condición pendiente.
3. **¿Líquida?** Si el título arroja una parte líquida y otra ilíquida, se ejecuta la líquida
   (art. 441).
4. **¿Garantía real?** Hipoteca → ejecución hipotecaria (arts. 503-507, con prelación sobre el bien
   gravado, art. 507). Prenda → ejecución prendaria (arts. 508-510). Ambas siguen supletoriamente el
   juicio ejecutivo.
5. Si el documento **no** se basta por sí solo (privado no reconocido, alquileres sin recibo,
   obligación sin plazo o condicional, contrato bilateral, sueldos no laborales) → **preparación de
   la vía ejecutiva** (art. 443).
6. El actor siempre puede **optar por el conocimiento ordinario** (art. 440) — evaluarlo si el
   título es débil: en el juicio ejecutivo no puede discutirse la causa de la obligación (art. 465).

Si el título no encaja y no es preparable → advertirlo y proponer la vía ordinaria. No forzar la
ejecutiva: la inhabilidad de título es excepción del art. 462 inc. d).

## Paso 2 — Escritos que esta skill genera

| Escrito | Base CPC | Notas |
|---|---|---|
| Demanda de preparación de acción ejecutiva | 443-444 | Citación al reconocimiento bajo apercibimiento de tenerlo por confeso |
| Promoción de acción ejecutiva (quirografaria) | 439, 448, 450 | Directa, o dentro de los **20 días** de concluida la preparación (447, caducidad) |
| Promoción de ejecución hipotecaria / prendaria | 503-507 / 508-510 | Excepciones más restringidas (504; 509-510) |
| Oposición de excepciones (defensa del ejecutado) | 460, 462-463 | **5 días**, en un solo escrito, con ofrecimiento de prueba |
| Contestación del traslado de excepciones (ejecutante) | 466 | 5 días, ofrecer prueba |
| Solicitud de cumplimiento de sentencia de remate | 475 (dinero), 476-479 (muebles), 480 y ss. (inmuebles) | Según el bien embargado |
| Liquidación (capital, intereses, costas) y su aprobación | 475, 501-502 | Si el ejecutante no liquida en 5 días, puede hacerlo el ejecutado (501) |
| Ampliación de la ejecución | 458 (antes de sentencia), 459 (después) | Nuevos plazos o cuotas vencidos |

Estructura formal: la común de `escritos-judiciales` (encabezado, personería, cuerpo, petitorio).
En la demanda ejecutiva el relato de hechos es **mínimo**: el título habla por sí; no abrir la
causa de la obligación (art. 465).

## Paso 3 — Reglas duras del procedimiento (no negociables)

- **Trámites irrenunciables** (art. 461): intimación de pago, citación para oponer excepciones y
  sentencia. Su omisión habilita la nulidad (art. 463 inc. a).
- **Pago en tercero día** (art. 460): si el ejecutado paga capital, intereses y gastos dentro de
  3er día de la intimación, se pasa directo a liquidación (art. 475).
- **Excepciones taxativas** (art. 462, con sus incisos): a) incompetencia; b) falta de personería;
  c) litispendencia; d) **falsedad (solo material/adulteración) o inhabilidad del título** (falta de
  acción o documento no ejecutivo) — *un mismo inciso para ambas*; e) prescripción; f) **pago
  documentado, total o parcial**; g) compensación de crédito líquido con fuerza ejecutiva; h) quita,
  espera, remisión, novación y transacción; i) cosa juzgada. Más la
  **nulidad de la ejecución** (art. 463, solo por sus dos causales). Excepción no autorizada o no
  opuesta en forma clara → desestimación sin sustanciación y sentencia de remate (art. 466).
- **Inapelabilidad general** (art. 442): solo son apelables la **sentencia de remate** (en los
  casos del art. 472, en relación y con efecto suspensivo) y el **auto que decide la liquidación**.
- **Caducidades:** medidas preparatorias, 20 días (447); embargo tras nulidad o incompetencia,
  15 días (464).
- **Sentencia de remate** (art. 470): solo puede resolver nulidad del procedimiento, rechazo de la
  ejecución o llevarla adelante en todo o en parte. *(En la copia local el epígrafe del art. 470
  figura como "Juicio posterior"; el contenido citado es el transcripto.)*
- **Juicio ordinario posterior** (art. 471): cualquiera de las partes, dentro de **60 días** de
  notificada la sentencia firme de remate. El ejecutado que opuso excepciones puede exigir **fianza**
  al ejecutante (art. 473, remite al art. 1457 del Código Civil).
- **Costas:** las paga el deudor aunque pague en el acto de la intimación (457); al vencido en
  general, con la regla especial del pago parcial (474).

Flujo completo, plazos con fuente por fila y guía estratégica por posición:
ver `references/flujo-ejecutivo.md`.

## Qué NO hace esta skill

- No ejecuta sentencias laborales (arts. 356-357 CPT → `escritos-judiciales`).
- No liquida rubros laborales (motor `calculo-laboral`).
- No calcula intereses con tasa inventada: la tasa aplicable se pacta en el título o se estima
  sujeta a la tasa máxima BCP (art. 475 del Código Civil, `verified`); presentarla como estimación.
- No cita fallos sin verificar contra PJ/CSJ → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
