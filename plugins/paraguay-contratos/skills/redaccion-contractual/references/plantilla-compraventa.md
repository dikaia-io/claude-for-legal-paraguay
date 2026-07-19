# Plantilla · Contrato de compraventa

> Plantilla de tipo de la skill `redaccion-contractual` (Paso 3), que se aplica **sobre** el
> esqueleto de [`estructura-canonica.md`](estructura-canonica.md) — no lo repite: encabezado y
> comparecientes (sección 1), fórmula de otorgamiento (sección 2), domicilio y notificaciones
> (sección 5), jurisdicción (sección 6) y cierre y firmas (sección 7) se toman de allí **tal como
> están**. Las cláusulas de esta plantilla se insertan en el **orden canónico** de la sección 4.
>
> **Regla de anclaje (dura).** Cada cláusula lleva su ancla al pie; ningún artículo se cita de
> memoria. Regla estructural del tipo: si el bien es **registrable**, la cláusula de
> **escrituración e inscripción es obligatoria** (ver sección 8 de la estructura canónica —
> formalidades condicionales). Toda cita al **CC** es al Código Civil paraguayo (Ley N°
> 1183/1985, `verified` en el authority map).

---

## Determinantes obligatorios

Sin estos datos la skill **no redacta** (emite `[VACÍO FÁCTICO]` y los pide — regla dura 1 de
`redaccion-contractual`):

1. Los **estructurales comunes** (tipo, partes, objeto, precio, plazo — sección 2 del
   `SKILL.md`).
2. **Individualización completa del bien:** inmueble (Finca / Padrón / Cta. Cte. Ctral.,
   distrito, superficie), vehículo (marca, tipo, año, chapa, chasis, motor) o mueble (descripción,
   cantidad, estado). «El inmueble» o «la mercadería» sin individualizar no es un objeto.
3. **¿Es registrable?** (inmueble, automotor u otro bien de registro). Si lo es, la cláusula de
   escrituración e inscripción **no es opcional** y el diagnóstico debe verificar la titularidad
   registral del vendedor (título a la vista).

---

## Designaciones

- **«EL VENDEDOR»** (o «LA VENDEDORA») — quien transmite el bien.
- **«EL COMPRADOR»** (o «LA COMPRADORA») — quien paga el precio.

Definidas una única vez conforme a la sección 1 de la estructura canónica; en la fórmula de
otorgamiento (sección 2), `[TIPO]` = «COMPRAVENTA».

---

## Cláusulas tipo

### CLÁUSULA [N] — OBJETO.

> EL VENDEDOR vende a EL COMPRADOR, y éste compra, el siguiente bien: `[BIEN — individualización
> completa según el determinante 2]`, en el estado en que se encuentra, que EL COMPRADOR declara
> conocer y aceptar.
>
> EL VENDEDOR declara bajo su responsabilidad: (a) que es **titular exclusivo** del bien y que
> ejerce su posesión pacífica; (b) que el bien se encuentra **libre de gravámenes**, embargos,
> restricciones de dominio, ocupantes y reclamos de terceros; y (c) que no ha celebrado con
> anterioridad acto alguno que afecte la disponibilidad del bien.

**Variante — venta de cosa ajena advertida (solo si se declara expresamente):**

> EL VENDEDOR declara que el bien pertenece a `[TERCERO_TITULAR]` y se obliga frente a
> EL COMPRADOR a `[adquirirlo y transmitirlo / obtener la ratificación del titular]` dentro del
> plazo de `[PLAZO]`, quedando EL COMPRADOR facultado, si ello no ocurre, a resolver el contrato
> conforme a la cláusula de incumplimiento y a exigir la restitución de lo pagado.

La ajenidad **nunca se calla**: una venta de cosa ajena no advertida es la red-flag CV.2 de la
ficha hermana. Con título a la vista, la declaración de titularidad de la variante principal se
verifica antes de redactarse.

*(Ancla: individualización del objeto — CC art. 673 — verificado; compraventa de cosa ajena —
CC arts. 743-744 — verificado)*

### CLÁUSULA [N] — PRECIO Y FORMA DE PAGO.

> El precio total y definitivo de la venta se fija en `[PRECIO]` (guaraníes).

**Variante A — contado:**

> EL COMPRADOR paga el precio en este acto, en dinero en efectivo `[o mediante transferencia a la
> cuenta [CUENTA]]`, sirviendo el presente contrato de suficiente recibo y carta de pago.

**Variante B — pago en cuotas (saldo con garantía):**

> EL COMPRADOR paga en este acto la suma de `[MONTO_INICIAL]` en concepto de entrega inicial, y
> el saldo de `[SALDO]` en `[CANTIDAD_CUOTAS]` cuotas mensuales y consecutivas de
> `[MONTO_CUOTA]` cada una, venciendo la primera el `[FECHA_PRIMERA_CUOTA]`. El saldo de precio
> se garantiza mediante `[GARANTÍA: prenda / hipoteca / otra]`; si la garantía requiere escritura
> pública o inscripción registral para su validez u oponibilidad, las partes se obligan a
> otorgarla con esa forma y a inscribirla.

*(Ancla: pacto de precio — CC art. 715 — verificado; forma y registro de la garantía — CC
arts. 700-702 — verificado)*

### CLÁUSULA [N] — ENTREGA Y TRASLACIÓN DE RIESGOS.

> EL VENDEDOR entregará el bien a EL COMPRADOR el `[FECHA_DE_ENTREGA]`, en `[LUGAR_DE_ENTREGA]`,
> libre de ocupantes y efectos `[si es inmueble]`, labrándose **acta de entrega** firmada por
> ambas partes. Las partes pactan **expresamente** que los riesgos de pérdida o deterioro del
> bien se trasladan a EL COMPRADOR desde la **entrega efectiva**; hasta ese momento los soporta
> EL VENDEDOR.

*(Ancla: pacto expreso — CC art. 715 — verificado; régimen legal supletorio de riesgos:
[VERIFICAR VIGENCIA] — no verificado en la tabla de anclajes; el pacto expreso existe para no
depender de él)*

### CLÁUSULA [N] — EVICCIÓN.

> EL VENDEDOR responde frente a EL COMPRADOR por **evicción** conforme al régimen legal:
> garantiza la existencia y la legitimidad del derecho que transmite, y responderá si
> EL COMPRADOR resulta privado, total o parcialmente, del derecho adquirido, por causa anterior o
> contemporánea a la venta.

**Nota (dura):** la garantía **se mantiene** — no se redacta su exclusión total. La omisión o
renuncia de la evicción es red-flag de Nivel 2 del catálogo y CV.3 de la ficha hermana.

*(Ancla: CC art. 1759 — verificado)*

### CLÁUSULA [N] — VICIOS REDHIBITORIOS.

> EL VENDEDOR responde por los **vicios ocultos** del bien que lo hagan impropio para su destino
> o que disminuyan su valor de tal modo que, de haberlos conocido, EL COMPRADOR no lo habría
> adquirido o habría pagado menos, conforme al régimen legal.
>
> **Inspección y reclamo tempranos:** EL COMPRADOR examinará el bien dentro de los `[PLAZO]` días
> de la entrega y comunicará por escrito a EL VENDEDOR los defectos que detecte, sin que el
> silencio durante ese período implique renuncia a la garantía por vicios ocultos.

**Nota de plazo (advertencia estratégica al comprador):** la acción redhibitoria tiene un plazo
**breve** — **tres (3) meses** (CC art. 668, ubicado en el Libro II, prescripción liberatoria) —;
por eso la cláusula prevé un mecanismo de inspección y reclamo tempranos, y conviene dejar
constancia escrita de todo defecto apenas se detecte (CV.4 de la ficha hermana).

*(Ancla: CC art. 1789 — verificado; plazo de la acción — CC art. 668, tres meses — verificado)*

### CLÁUSULA [N] — ESCRITURACIÓN E INSCRIPCIÓN. *(obligatoria si el bien es registrable)*

> Las partes se obligan a otorgar la **escritura pública** traslativa de dominio dentro de los
> `[PLAZO]` días contados desde `[HITO: la firma del presente / el pago total del precio]`, por
> ante el escribano público `[ESCRIBANO — designado por [PARTE]]`. Los gastos y honorarios de la
> escrituración serán soportados por `[REPARTO_DE_GASTOS]`; los tributos que graven la
> transferencia, conforme a la ley. Otorgada la escritura, se gestionará sin demora su
> **inscripción** en la Dirección General de los Registros Públicos — o en el registro que
> corresponda a la naturaleza del bien (automotores: el registro del bien) — a nombre de
> EL COMPRADOR. La parte que incumpla la obligación de escriturar podrá ser demandada por su
> otorgamiento.

**Nota (dura):** el presente instrumento privado **no transfiere el dominio** del bien
registrable: vale como **obligación de escriturar**, exigible judicialmente. Omitir esta cláusula
en la venta de un bien registrable es red-flag de Nivel 2 (catálogo y CV.1 de la ficha hermana) —
por eso el determinante 3 pregunta si el bien es registrable **antes** de redactar.

*(Ancla: CC arts. 700-702 — verificado)*

### CLÁUSULA [N] — MORA E INCUMPLIMIENTO.

> La resolución del contrato por incumplimiento se rige por la cláusula de rescisión conforme a
> la estructura canónica (sección 4, orden canónico, punto 5): **intimación previa fehaciente y
> plazo de subsanación** antes de resolver. El atraso en el pago de cualquier suma debida en
> virtud del presente devengará, desde la mora, el interés moratorio pactado de
> `[TASA_INTERÉS]`, que en ningún caso podrá exceder las **tasas máximas fijadas por el Banco
> Central del Paraguay**; toda estipulación que las supere se tendrá por reducida de pleno
> derecho al máximo legal.

**Nota:** el CC no fija un porcentaje de interés: remite a la tasa máxima del BCP. El placeholder
`[TASA_INTERÉS]` lo completa el abogado — **nunca** se rellena con un porcentaje inventado.

*(Ancla: mora — CC art. 424 — verificado; interés moratorio — CC art. 475 — verificado — tope en
la tasa máxima del BCP)*

---

## Cláusulas opcionales

Se incluyen **solo si el diagnóstico las activa** (paso 1 de `redaccion-contractual`).

### OPCIONAL — PACTO DE RETROVENTA. *(solo si las partes lo pactan expresamente)*

> EL VENDEDOR se reserva el derecho de **recuperar el bien vendido**, restituyendo a
> EL COMPRADOR el precio recibido más `[GASTOS_PACTADOS]`, dentro del plazo de
> `[PLAZO_RETROVENTA]`, mediante comunicación fehaciente cursada antes de su vencimiento.

**Nota de anclaje:** el pacto se rige por la **Ley N° 701/1995** `[VERIFICAR VIGENCIA]` — la
entrada está `verified` en el authority map, pero el **alcance exacto de sus límites** (plazo
máximo y condiciones del rescate) **no está verificado** en la tabla de anclajes: verificarlo
contra la fuente oficial antes de cerrar el pacto (CV.5 de la ficha hermana).

*(Ancla: Ley N° 701/1995 — entrada `verified`; alcance exacto de sus límites:
[VERIFICAR VIGENCIA])*

### OPCIONAL — CONTINGENCIA CAMBIARIA. *(solo si el precio se pacta en moneda extranjera)*

> Si el precio se pacta en `[MONEDA_EXTRANJERA]`, las partes convienen: (a) el tipo de cambio de
> referencia (`[FUENTE_TIPO_DE_CAMBIO]`) y la fecha de su determinación; y (b) el mecanismo
> aplicable ante indisponibilidad de la divisa o restricciones cambiarias: `[MECANISMO: pago en
> guaraníes al tipo de cambio de referencia / otro]`.

*(Ancla: pacto de las partes — CC art. 715 — verificado; la cobertura cambiaria es materia de
pacto — [ARGUMENTO SIN NORMA]; si además se pacta interés, rige el tope del CC art. 475 —
verificado)*

---

## Notas de QC

Al correr el Paso 4 (motor `red-flags` completo: invalidez metodológica → Nivel 1 → Niveles 2 y
3), vigilar **especialmente** en este tipo:

- **Bien registrable sin escrituración = red-flag de Nivel 2** (catálogo y CV.1): si el
  determinante 3 dio «registrable», la cláusula de escrituración e inscripción **está** en el
  borrador — sin excepciones.
- **Exclusión de evicción o de vicios redhibitorios = red-flag** (catálogo Nivel 2 y CV.3): esta
  plantilla **mantiene** ambas garantías; no se redactan renuncias totales.
- **Titularidad del vendedor** (CV.2): exigir título a la vista en el diagnóstico; si la cosa es
  ajena, usar **solo** la variante advertida (CC arts. 743-744) — nunca callar la ajenidad.
- **Interés moratorio:** pactado y con tope BCP (catálogo Nivel 3 «interés moratorio no
  pactado») — nunca un porcentaje inventado.
- **Retroventa:** solo expresa y con `[VERIFICAR VIGENCIA]` sobre su alcance (CV.5).
- **Precio en moneda extranjera:** activa la cláusula opcional de contingencia cambiaria
  (catálogo Nivel 3).
- **Comprador consumidor final:** activa el régimen de la Ley N° 1334/1998 vía el catálogo
  (Nivel 1, cláusulas abusivas en adhesión) — se detecta en el diagnóstico y se remite al
  catálogo.
- **Planificación del reclamo del precio:** remitir al catálogo, Nivel 3, «prescripción no
  contemplada» — la plantilla no fija plazos de prescripción.
- Domicilio, jurisdicción con ciudad fijada y cierre: secciones 5-7 de la estructura canónica,
  sin re-redactar.
