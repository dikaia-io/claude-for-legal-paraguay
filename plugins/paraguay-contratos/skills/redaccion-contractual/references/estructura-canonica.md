# Estructura canónica del contrato privado paraguayo

> Reference de la skill `redaccion-contractual` (plugin `paraguay-contratos`). Es el **esqueleto
> forense** que el Paso 2 de esa skill aplica a **todo** borrador, tenga o no plantilla propia por
> tipo (`references/plantilla-*.md`). Las plantillas por tipo se cuelgan de esta estructura: citan
> "sección N de la estructura canónica" y agregan solo su contenido específico — **no repiten**
> este esqueleto.
>
> **Regla de anclaje (dura).** Las únicas anclas normativas de este archivo son **CC arts.
> 700-702** (escritura pública) y la **Ley N° 7561/2025** (arbitraje) — ambas `verified` en el
> authority map. Ningún otro número de artículo aparece acá. Todo otro fundamento se remite al
> **catálogo de red-flags** (`plugins/paraguay-contratos/skills/red-flags/references/catalogo-red-flags.md`)
> o sale con `[VERIFICAR VIGENCIA]`.

---

## 1. Encabezado / comparecientes

Todo contrato abre identificando **lugar, fecha y partes** antes de cualquier cláusula.

**Lugar y fecha en letras:**

> "En la ciudad de `[CIUDAD]`, República del Paraguay, a los `[DÍA]` días del mes de `[MES]` del
> año `[AÑO EN LETRAS]`…"

**Individualización completa de cada parte**, sin excepción:

- Nombre y apellido (persona física) o razón social (persona jurídica).
- **C.I. N.º `[C.I.]`** (persona física) o **RUC `[RUC]`** (persona jurídica o física con actividad
  gravada).
- Nacionalidad.
- Estado civil, si es persona física.
- **Domicilio real `[DOMICILIO]`.**
- Si actúa por representación (apoderado, representante legal, órgano societario): identificar el
  **instrumento del poder** o el **carácter invocado**, y verificar que el poder sea **suficiente**
  para el acto (facultad expresa cuando el acto la requiera). No se asume representación: se
  identifica su fuente.

**Designación abreviada:** cada parte recibe una designación entre comillas y en mayúsculas,
definida una única vez y usada de manera consistente en todo el resto del documento — por ejemplo
"EL PRESTADOR", "EL COMITENTE", "LA LOCADORA". No se alterna entre la designación abreviada y el
nombre completo salvo en el encabezado y el bloque de firmas.

---

## 2. Fórmula de otorgamiento

Cierra el encabezado y abre las cláusulas con una fórmula de convenio, no con un bloque de
"reunión" o "exposición":

> "…convienen en celebrar el presente CONTRATO DE `[TIPO]`, que se regirá por las cláusulas y
> condiciones siguientes:"

Variante admisible: "han convenido en celebrar…".

**Advertencia de estilo (no de fondo):** los bloques **REUNIDOS / EXPONEN** o **INTERVIENEN /
MANIFIESTAN**, propios de otros moldes notariales, **no son de práctica paraguaya** y no se usan
acá — ver "Señales de plantilla foránea" más abajo.

---

## 3. Declaraciones / antecedentes (opcional)

Sección **opcional**, a incluir solo cuando el contexto del negocio lo justifica (operaciones
complejas, alianzas, antecedentes que condicionan el objeto). Fórmula breve:

> "DECLARAN: Que…"

Se usa para dejar constancia de hechos o antecedentes relevantes — no para sustituir cláusulas: lo
que deba obligar a las partes va en las cláusulas numeradas (sección 4), no en las declaraciones.

---

## 4. Cláusulas en ordinales — orden canónico

**Numeración:** ordinales en mayúscula (PRIMERA, SEGUNDA, TERCERA…), cada una con un título
temático breve en mayúsculas seguido de guion: por ejemplo, "PRIMERA — OBJETO.".

**Orden canónico** de las cláusulas sustantivas:

1. **Objeto.**
2. **Precio y forma de pago.**
3. **Plazo / vigencia.**
4. **Obligaciones de cada parte**, detalladas una por una — nunca por remisión genérica a "las
   obligaciones que correspondan según la ley" o equivalente.
5. **Rescisión / resolución e incumplimiento.** **Siempre** con intimación previa fehaciente y
   plazo de subsanación antes de resolver — un pacto comisorio sin intimación ni plazo es una
   red-flag de Nivel 2 (ver catálogo de `red-flags`, no se repite acá).
6. **Garantías**, si el contrato las lleva. Si la garantía requiere forma o registro para ser
   oponible, la cláusula debe decirlo expresamente (ver también sección 8).
7. **Cláusulas propias del tipo de contrato**: confidencialidad, propiedad intelectual, cláusula
   penal, no competencia, u otras según la naturaleza del negocio.
8. **Caso fortuito / fuerza mayor**, si el negocio lo justifica.
9. **Domicilio especial y notificaciones** (desarrollo en sección 5).
10. **Mediación previa voluntaria** (desarrollo en sección 6) — **solo si el abogado la pacta
    expresamente**; si no, se omite.
11. **Jurisdicción y competencia** (desarrollo en sección 6) — **siempre** la última cláusula
    sustantiva del cuerpo, antes del cierre.

**Nota normativa (rescisión):** el régimen de resolución por incumplimiento del Código Civil exige
intimación previa; las anclas concretas viven en el catálogo de red-flags de este plugin — este
reference no las repite ni cita el artículo por número.

---

## 5. Domicilio y notificaciones

Cada parte **constituye domicilio especial** a los efectos del contrato — distinto, si corresponde,
de su domicilio real declarado en el encabezado — y las partes pactan el **medio de notificación
fehaciente** que regirá entre ellas (carta documento, telegrama colacionado, correo electrónico con
acuse, u otro medio verificable, según lo que acuerden).

**Advertencia de alcance:** no corresponde pactar domicilio especial **fuera de la República** en
contratos de **seguro** — es una regla específica de ese tipo contractual; ver el catálogo de
`red-flags` para el detalle y su ancla. No se generaliza esta restricción a otros contratos.

---

## 6. Jurisdicción y competencia — fórmula paraguaya

**Fórmula estándar:**

> "Para todos los efectos derivados del presente contrato, las partes se someten a la jurisdicción
> de los Tribunales Ordinarios de la ciudad de `[CIUDAD]`, República del Paraguay, renunciando
> expresamente a cualquier otro fuero o jurisdicción que pudiera corresponderles."

**Regla dura:** la cláusula **nunca** se deja como "tribunales de ______" sin completar la ciudad —
dejar el espacio en blanco o genérico es una red-flag de Nivel 3 (jurisdicción abierta sin ciudad
fijada).

**Arbitraje:** solo si las partes lo pactan **expresamente**, con una cláusula arbitral propia y
separada de la fórmula de jurisdicción ordinaria de arriba. La cláusula arbitral se ancla en la
**Ley N° 7561/2025 (De Arbitraje) `[VERIFICAR VIGENCIA]`** en su primera mención. No se mezclan
arbitraje y jurisdicción ordinaria para la misma materia dentro del mismo contrato.

**Mediación previa voluntaria (opcional):** no se incluye por defecto. Solo si el abogado la pacta
expresamente, insertar una cláusula adicional **antes** de jurisdicción/arbitraje, con centro y plazo
definidos. Fórmula base:

> "Las partes acuerdan procurar, antes de promover una acción judicial derivada del presente
> contrato, una instancia de mediación voluntaria ante `[CENTRO_DE_MEDIACION]`, en la ciudad de
> `[CIUDAD]`, por un plazo máximo de `[PLAZO_MEDIACION]` días corridos contados desde la solicitud
> escrita de cualquiera de ellas. Vencido dicho plazo sin acuerdo, cualquiera de las partes podrá
> acudir a la jurisdicción pactada. Esta instancia no impedirá solicitar medidas urgentes,
> conservatorias o cautelares cuando resulten necesarias."

Si faltan el centro o el plazo, dejar placeholders y registrar la decisión en el **Estado del
análisis**. No usar mediación abierta, sin plazo o situada fuera de Paraguay salvo instrucción expresa
del abogado.

---

## 7. Cierre y firmas

**Fórmula de conformidad:**

> "En prueba de conformidad, las partes firman el presente contrato en dos ejemplares de un mismo
> tenor y a un solo efecto, en el lugar y fecha indicados en el encabezamiento."

**Bloque de firmas:** cada firmante se identifica con su **designación abreviada** (la definida en
la sección 1) y la **aclaración de nombre y C.I.** correspondiente, debajo de la firma.

---

## 8. Formalidades condicionales (checklist final del redactor)

Antes de cerrar el borrador, revisar:

- **Certificación de firmas** ante escribano público (práctica: Colegio de Escribanos del
  Paraguay). Recomendable en contratos de monto significativo; **obligatoria** cuando la ley o el
  registro que recibirá el instrumento la exige.
- **Escritura pública.** Si el acto está alcanzado por el **CC art. 700** (actos que exigen
  escritura pública — p. ej. inmuebles y demás actos registrables), el contrato privado vale, por
  los **arts. 701-702**, como compromiso de escriturar. En ese caso, la plantilla del tipo debe
  incluir una **cláusula de escrituración e inscripción registral** ante la Dirección General de
  los Registros Públicos (automotores: registro correspondiente al bien).
- **Cantidad de ejemplares** y, si hay anexos, que estén **firmados e identificados**
  individualmente (por ejemplo, "Anexo A — …").

---

## Señales de plantilla foránea

Antes de entregar cualquier borrador armado sobre esta estructura, verificar que no arrastre
terminología de otro molde contractual — como el bloque REUNIDOS/EXPONEN descartado en la sección
2. El **catálogo completo de indicadores** (siglas de otra jurisdicción, monedas extranjeras sin
aclarar, encabezados calcados, y demás señales) y el **procedimiento de reencuadre** viven en la
skill `red-flags`, categoría previa **"Invalidez metodológica (plantilla de jurisdicción
extranjera)"**. Este reference **no repite esa lista**: remite a ella. Cualquier borrador armado
sobre esta estructura pasa igual por el QC completo de `red-flags` (Paso 4 de
`redaccion-contractual`), que corre esa categoría previa antes del catálogo por niveles.

---

## Placeholders canónicos

Los campos variables de esta estructura se completan siempre con los mismos placeholders,
consistentes con los que usa la skill `redaccion-contractual`:

`[PARTE_A]` · `[PARTE_B]` · `[C.I.]` · `[RUC]` · `[DOMICILIO]` · `[PRECIO]` · `[PLAZO]` ·
`[CIUDAD]` · `[CENTRO_DE_MEDIACION]` · `[PLAZO_MEDIACION]`

**Regla:** todo dato que falte y no sea determinante (sección 2 del `SKILL.md` de
`redaccion-contractual`) sale en el borrador como placeholder. Si además el vacío corresponde a un
marcador del catálogo cerrado de `CLAUDE.base.md` (`[VACÍO FÁCTICO]`, `[VACÍO PROBATORIO]`,
`[INSERTAR JURISPRUDENCIA VERIFICADA]`, `[FUENTE OFICIAL PENDIENTE]`, `[VERIFICAR VIGENCIA]`), se
agrega el marcador junto con el placeholder — nunca se rellena de memoria.
