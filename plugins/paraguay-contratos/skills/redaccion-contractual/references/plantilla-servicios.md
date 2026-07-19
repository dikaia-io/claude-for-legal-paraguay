# Plantilla · Contrato de servicios

> Plantilla de tipo de la skill `redaccion-contractual` (Paso 3), que se aplica **sobre** el
> esqueleto de [`estructura-canonica.md`](estructura-canonica.md) — no lo repite: encabezado y
> comparecientes (sección 1), fórmula de otorgamiento (sección 2), domicilio y notificaciones
> (sección 5), jurisdicción (sección 6) y cierre y firmas (sección 7) se toman de allí **tal como
> están**. Las cláusulas de esta plantilla se insertan en el **orden canónico** de la sección 4.
>
> **Regla de anclaje (dura).** Cada cláusula lleva su ancla al pie. Los números de artículo salen
> de las anclas verificadas del proyecto; ninguno se cita de memoria. Lo que no tiene ancla
> verificada sale con un marcador del catálogo cerrado de `CLAUDE.base.md` (se referencia, no se
> copia). Toda cita al **CC** es al Código Civil paraguayo (Ley N° 1183/1985, `verified` en el
> authority map).

---

## Determinantes obligatorios

Sin estos datos la skill **no redacta** (emite `[VACÍO FÁCTICO]` y los pide — regla dura 1 de
`redaccion-contractual`):

1. Los **estructurales comunes** (tipo, partes, objeto, precio, plazo — sección 2 del `SKILL.md`).
2. **¿Obligación de medios o de resultado?** Define la variante de la cláusula de objeto y el
   estándar de cumplimiento. Si toda la economía del negocio es un resultado determinado, el tipo
   puede ser **obra** (CC art. 852 y ss.) y no servicios: reclasificar antes de redactar.
3. **Alcance del servicio:** descripción concreta de las actividades comprendidas (y, si es de
   resultado, el resultado exigido). «Los servicios que se convengan» no es un alcance.

---

## Designaciones

- **«EL PRESTADOR»** — quien se obliga a prestar el servicio.
- **«EL COMITENTE»** — quien encarga el servicio y paga los honorarios.

Definidas una única vez conforme a la sección 1 de la estructura canónica; en la fórmula de
otorgamiento (sección 2), `[TIPO]` = «PRESTACIÓN DE SERVICIOS».

---

## Cláusulas tipo

### CLÁUSULA [N] — OBJETO Y ALCANCE.

> EL PRESTADOR se obliga a prestar a favor de EL COMITENTE el servicio de `[SERVICIO]`,
> comprensivo de las siguientes actividades: `[ALCANCE]`, conforme a las especificaciones del
> **Anexo A**, firmado por las partes e integrante del presente contrato.

**Variante A — obligación de medios (default del tipo):**

> La obligación asumida por EL PRESTADOR es de **medios**: se compromete a desplegar la actividad
> descripta con la diligencia, la pericia y el cuidado exigibles a un profesional de su
> especialidad, sin garantizar la obtención de un resultado determinado.

**Variante B — obligación de resultado (debe decirse expresamente):**

> Las partes dejan expresa constancia de que EL PRESTADOR asume una obligación de **resultado**:
> se obliga a alcanzar `[RESULTADO]`, y el cumplimiento se verificará contra la obtención de ese
> resultado, conforme a los criterios de aceptación del Anexo A.

*(Ancla: CC arts. 845-851 — verificado; deslinde con la obra: CC art. 852 y ss. — verificado)*

### CLÁUSULA [N] — HONORARIOS Y FORMA DE PAGO.

> EL COMITENTE pagará a EL PRESTADOR, en concepto de honorarios, la suma de `[PRECIO]`
> (guaraníes), pagadera `[MODALIDAD: contado / por hito cumplido / mensual]`, contra presentación
> de la factura correspondiente, dentro de los `[PLAZO]` días de recibida.
>
> **Aceptación objetiva:** EL COMITENTE dispondrá de `[PLAZO]` días hábiles desde cada entrega o
> presentación para formular observaciones fundadas y por escrito; vencido ese plazo sin
> observaciones, la prestación del período se tendrá por aprobada y el pago será exigible.
>
> **Cambios de alcance:** toda tarea no comprendida en la cláusula de objeto requerirá acuerdo
> previo y escrito de ambas partes sobre su contenido, su plazo y su precio, instrumentado por
> adenda firmada. Ninguna parte podrá imponer unilateralmente una ampliación o reducción del
> alcance.

*(Ancla: retribución del servicio — CC arts. 845-851 — verificado; si se pacta interés por
atraso: CC art. 475 — verificado — tope en la tasa máxima del BCP, nunca un porcentaje
inventado)*

### CLÁUSULA [N] — CARÁCTER DE LA PRESTACIÓN.

**Variante A — personal e incesible (default legal):**

> La prestación a cargo de EL PRESTADOR es **personal e incesible**. EL PRESTADOR no podrá ceder
> el presente contrato ni subcontratar total o parcialmente su ejecución sin la autorización
> previa y escrita de EL COMITENTE.

**Variante B — sustitución pactada (pacto en contrario):**

> EL PRESTADOR podrá valerse de colaboradores o subcontratados de su elección, bajo su exclusiva
> dirección y responsabilidad, permaneciendo como único obligado frente a EL COMITENTE por la
> ejecución íntegra y correcta del servicio.

*(Ancla: CC art. 846 — verificado — prestación personal e incesible salvo pacto en contrario;
la Variante B es el pacto en contrario que el propio artículo admite)*

### CLÁUSULA [N] — INDEPENDENCIA DE LAS PARTES.

> Las partes declaran que el presente es un contrato civil de prestación de servicios y que no
> existe entre ellas relación de dependencia ni subordinación jurídica alguna. En consecuencia:
> (a) EL PRESTADOR organiza libremente su actividad, sus horarios y su método de trabajo, sin
> sujeción a jornada ni horario fijo impuestos por EL COMITENTE; (b) no se pacta exclusividad,
> pudiendo EL PRESTADOR prestar servicios a terceros; (c) EL PRESTADOR ejecuta el servicio con
> sus propias herramientas, equipos y medios, salvo los accesos que EL COMITENTE deba facilitar
> por la naturaleza del encargo, detallados en el Anexo A; (d) EL PRESTADOR asume sus propias
> cargas fiscales y de seguridad social como trabajador independiente.

**Nota de derivación (dura):** esta cláusula **declara, no constituye**. Si los hechos de la
ejecución la contradicen (exclusividad + horario fijo + subordinación efectiva: instrucciones,
control, herramientas del comitente, integración a su organización), **la cláusula no salva la
relación laboral**: el vínculo se rige por su realidad. Ante esos indicios en el diagnóstico, la
skill **no redacta como civil**: marca `[VACÍO PROBATORIO]` y **deriva** al plugin
`paraguay-laboral` / skill `contrato-trabajo` (regla dura 3 de `redaccion-contractual`; red-flag
de Nivel 1 «simulación de relación laboral bajo contrato civil» del catálogo).

*(Ancla: declaración de las partes — CC art. 715 — verificado; su eficacia frente a hechos que
la contradigan: [ARGUMENTO SIN NORMA] — la calificación laboral corresponde al Código del
Trabajo, fuera de esta plantilla)*

### CLÁUSULA [N] — PROPIEDAD INTELECTUAL DEL ENTREGABLE.

**Variante A — cesión al comitente:**

> Todo material producido por EL PRESTADOR en ejecución del presente contrato (informes,
> documentos, diseños, desarrollos, código, bases de datos) pertenecerá a EL COMITENTE desde su
> entrega, cediéndole EL PRESTADOR, en forma exclusiva y sin limitación territorial, todos los
> derechos patrimoniales de utilización y explotación susceptibles de cesión, en la máxima medida
> que permita la ley aplicable. EL PRESTADOR se obliga a suscribir los instrumentos adicionales
> que la formalización de la cesión requiera.

**Variante B — retención del prestador con licencia:**

> EL PRESTADOR conserva la titularidad de los derechos sobre el material producido en ejecución
> del presente contrato, y concede a EL COMITENTE una licencia `[EXCLUSIVA / NO EXCLUSIVA]` de
> uso de dicho material, limitada a `[PROPÓSITO]`, por el plazo de `[PLAZO]`.

*(Ancla: [VERIFICAR VIGENCIA] — el régimen legal de la propiedad intelectual sobre el entregable
no está verificado en el authority map y no se cita ley por número; la cláusula expresa existe
precisamente para no depender del régimen supletorio)*

### CLÁUSULA [N] — TERMINACIÓN.

> El presente contrato termina: (a) por vencimiento del plazo pactado o cumplimiento total del
> alcance; (b) por decisión de cualquiera de las partes, comunicada por medio fehaciente con un
> preaviso de `[PLAZO]` días, quedando a salvo el pago de los honorarios devengados hasta la
> fecha efectiva de terminación; (c) por **justos motivos**, entendiéndose por tales los hechos
> graves que hagan inexigible la continuación del vínculo, con derecho de EL PRESTADOR a la
> retribución proporcional a lo ejecutado.
>
> La resolución por **incumplimiento** se rige por la cláusula de rescisión del contrato conforme
> a la estructura canónica (sección 4, orden canónico, punto 5): **intimación previa fehaciente y
> plazo de subsanación** antes de resolver. No se pacta resolución «de pleno derecho» sin
> intimación.

*(Ancla: terminación por justos motivos — CC art. 851 — verificado; resolución por
incumplimiento: remisión a la estructura canónica, cuyas anclas viven en el catálogo de
red-flags)*

---

## Cláusulas opcionales

Se incluyen **solo si el diagnóstico las activa** (paso 1 de `redaccion-contractual`).

### OPCIONAL — NO COMPETENCIA.

> EL PRESTADOR se obliga a no desarrollar, por sí ni por interpósita persona, la actividad de
> `[ACTIVIDAD]`, dentro de `[ZONA]`, por el plazo de `[PLAZO]` — **máximo cinco (5) años** —
> contado desde la terminación del presente contrato.

Los **tres límites** (zona + actividad + plazo, con tope de 5 años) son condición de validez del
pacto: una no competencia sin ellos, o por más de cinco años, dispara la red-flag S.3 de
`ficha-servicios.md` y el catálogo transversal. No se redacta abierta.

*(Ancla: Ley N° 1034/1983 art. 106 — verificado)*

### OPCIONAL — CONFIDENCIALIDAD.

Si el servicio implica acceso a información sensible, **no improvisar acá**: tomar la cláusula de
definición por categorías, exclusiones y **plazo determinado** de
[`plantilla-nda.md`](plantilla-nda.md). Nunca confidencialidad sin plazo (regla dura 2 de
`redaccion-contractual`).

---

## Notas de QC

Al correr el Paso 4 (motor `red-flags` completo: invalidez metodológica → Nivel 1 → Niveles 2 y
3), vigilar **especialmente** en este tipo:

- **Simulación laboral (Nivel 1).** La cláusula de independencia declara, no salva: si el
  diagnóstico muestra exclusividad + horario + subordinación, se deriva al plugin laboral — no se
  entrega el contrato civil.
- **«Satisfacción del cliente» como condición de pago — prohibida** (S.2 de la ficha hermana):
  desnaturaliza la obligación de medios. El mecanismo de aceptación de esta plantilla es
  **objetivo** (plazo de observaciones fundadas + aprobación tácita); no reemplazarlo por la
  conformidad discrecional del comitente.
- **No competencia** solo como opcional y con los tres límites del art. 106 (S.3).
- **PI del entregable:** el borrador siempre lleva una de las dos variantes — callar deja la
  titularidad en zona gris (S.4).
- **Servicios plurianuales con precio fijo:** prever reajuste pactado o dejar constancia de la
  decisión — catálogo, Nivel 2, «ausencia de mecanismo de reajuste en contratos de larga
  duración» (regla prudencial, sin norma).
- Domicilio, jurisdicción con ciudad fijada y cierre: secciones 5-7 de la estructura canónica,
  sin re-redactar.
