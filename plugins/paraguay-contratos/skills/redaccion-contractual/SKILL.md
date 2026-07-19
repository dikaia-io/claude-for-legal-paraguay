---
name: redaccion-contractual
description: Redacción de contratos civiles y comerciales NUEVOS bajo derecho paraguayo, con estructura forense paraguaya auténtica. Corre un diagnóstico previo, arma el borrador sobre la estructura canónica y la plantilla del tipo (servicios, locación, compraventa, NDA) y controla el propio borrador con el motor red-flags antes de entregarlo. No cita artículos por número ni redacta si faltan datos determinantes. Usar cuando el abogado necesita generar un contrato desde cero; si lo que trae es un contrato ya hecho para analizar, deriva a revision-contractual.
---

# Skill · Redacción contractual (Paraguay)

> Skill del plugin `paraguay-contratos`. Es la **cara visible de la redacción**: entrevista,
> arma el borrador sobre la estructura forense paraguaya y la plantilla del tipo, y **se
> autocontrola con el motor red-flags** antes de entregar. **La detección la hace el motor
> `red-flags`** (de este mismo plugin); esta skill NO repite el catálogo ni reescribe normas.
>
> **Redacción ≠ revisión.** Si el usuario aporta un contrato ya hecho para analizarlo antes de
> firmar o negociar, esto **no** es trabajo de esta skill: **derivar a `revision-contractual`**.
> Acá se genera contrato **nuevo**.
>
> Se rige por las reglas inmodificables y la **gramática de autoridad** de `CLAUDE.base.md`, por el
> **diagnóstico previo** y la skill `citacion` del núcleo (no reproduce sus reglas: las
> **referencia**), y por la **perspectiva neutral según quién consulta** del plugin: antes de
> redactar se sabe qué parte representa el abogado, y los defaults de las cláusulas críticas se
> calibran a esa parte.

---

## 1. Función

- **Entrevistar** antes de redactar (paso 1): sin los datos estructurales no se escribe una línea.
- **Armar** el borrador sobre la **estructura canónica paraguaya** (paso 2) y la **plantilla del
  tipo** si existe (paso 3) — no improvisa una estructura de memoria.
- **Autocontrolar** el borrador con el motor `red-flags` completo (paso 4) antes de entregar: un
  borrador nuestro que dispararía la propia revisión es un bug, no un producto.
- **Cerrar** con el **Estado del análisis** (paso 5): la interfaz que consumen las tareas
  siguientes y los evals.
- **No recalcular** el catálogo de `red-flags`, **no citar artículos por número** y **no redactar**
  con vacíos fácticos determinantes.

**Regla de oro normativa:** esta skill **no cita artículos por número**. Las anclas normativas
viven en `references/estructura-canonica.md` y en las plantillas por tipo; no se reproducen acá.
Si es inevitable mencionar una norma fuera de esas fuentes, sale con `[VERIFICAR VIGENCIA]` —
nunca un artículo pelado de memoria. Cuando una cláusula del borrador deba justificarse con una
cita para el abogado, la cita aplica la disciplina de citación del núcleo — los 4 controles de
autoridad (fuente / fecha de verificación / tipo de autoridad / nivel de certeza) y las plantillas
de `shared/authorities/formatos-de-cita.yaml` (referencia completa: skill `citacion`).

---

## 2. Qué es un "determinante" (para no bloquear de más)

Un **determinante** es un dato sin el cual el contrato no puede redactarse honestamente. Son:

- Los **estructurales comunes**, siempre: **tipo de contrato, partes, objeto, precio/
  contraprestación, plazo**.
- Los que **la plantilla del tipo** declare como **obligatorios en su encabezado** (sección
  «Determinantes obligatorios» de cada plantilla). Ejemplos del criterio: compraventa →
  individualización del bien y si es registrable; locación → destino del inmueble y garantía;
  NDA → qué información se protege y si es uni/bilateral; servicios → obligación de medios o de
  resultado.

**Regla dura:** si falta un determinante, **no se redacta**: se emite `[VACÍO FÁCTICO]` y se pide
el dato. **Todo lo demás** (lo secundario) puede salir en el borrador con marcadores para
completar — no se bloquea la redacción por lo accesorio.

---

## 3. Flujo de trabajo (5 pasos)

### Paso 1 — Diagnóstico previo (~12 preguntas)

Antes de redactar, entrevistar. Las **preguntas estructurales 1-5** se hacen **SIEMPRE si no
surgen del pedido** (son determinantes; sin ellas no se redacta). Las **6-12** pueden salir con
marcadores en el borrador si el abogado no las contesta, salvo que la plantilla del tipo las
declare determinantes.

1. **¿Qué tipo de contrato?** Uno de los 4 con plantilla (servicios · locación · compraventa ·
   NDA/confidencialidad) o, si no encaja, **estructura canónica genérica** (paso 3).
2. **¿Quiénes son las partes?** Físicas o jurídicas; **C.I. / RUC**; nacionales o extranjeras;
   **quién firma y con qué representación** (poder, órgano, mandato). La individualización
   deficiente es una red-flag: se resuelve preguntando, no rellenando.
3. **¿Objeto exacto?** y, cuando aplica, **¿obligación de medios o de resultado?** (define el
   estándar de cumplimiento y la responsabilidad).
4. **¿Precio / contraprestación?** Monto, **moneda**, forma y plazos de pago, y **cláusula de
   reajuste** si es de tracto largo.
5. **¿Plazo?** Inicio, vencimiento, prórroga, y si es de **tracto sucesivo**.
6. **¿Hay consumidor? ¿es contrato de adhesión?** Activa el régimen de defensa del consumidor y
   de cláusulas abusivas (que el QC del paso 4 vigila vía `red-flags`).
7. **¿Riesgo de relación laboral?** Si el vínculo tiene **exclusividad + horario + subordinación**,
   **NO se redacta como contrato civil**: se marca y se **deriva** a `contrato-trabajo` / plugin
   `paraguay-laboral` (ver Regla dura). No se disfraza una relación laboral bajo forma civil.
8. **¿Garantías?** Tipo (fianza, prenda, hipoteca, aval…) y si requieren **forma o registro** para
   ser oponibles.
9. **¿Rescisión / resolución?** Causales, **intimación previa** y **plazo de subsanación**. Un
   pacto comisorio sin intimación ni plazo es red-flag.
10. **¿Confidencialidad?** Alcance y, **siempre, PLAZO** — nunca sin plazo determinado (Regla dura).
11. **¿Cláusula penal?** Monto y **proporcionalidad**. Una pena manifiestamente excesiva es
    red-flag; se propone un tope proporcional.
12. **¿Jurisdicción y ley aplicable?** **Ciudad concreta** (no «tribunales de ______»), si hay
    **arbitraje pactado** y si el abogado quiere una **mediación previa opcional**. La prórroga de
    jurisdicción o el arbitraje extranjero son red-flags.

Cualquier **determinante** que falte → `[VACÍO FÁCTICO]` y pedirlo **antes de seguir**. Lo
secundario que falte → marcador en el borrador.

### Paso 2 — Estructura canónica paraguaya

Todo borrador se arma sobre **[`references/estructura-canonica.md`](references/estructura-canonica.md)**
(esqueleto forense paraguayo: encabezado con lugar y fecha, comparecientes individualizados,
fórmula de otorgamiento, declaraciones/antecedentes, cláusulas numeradas en ordinales, domicilio
especial, jurisdicción con fórmula paraguaya, cierre y firmas). Es **obligatorio para TODO
contrato**, tenga o no plantilla propia.

> **Degradación honesta.** Si `references/estructura-canonica.md` no está presente en la sesión,
> decirlo explícitamente y **NO
> improvisar una estructura de memoria** (una estructura inventada es autoridad incorrecta).
> Pedir el archivo, o marcar `[FUENTE OFICIAL PENDIENTE]` de estructura y dejarlo constar en el
> Estado del análisis. No se entrega un borrador «completo» apoyado en una estructura no anclada.

### Paso 3 — Plantilla por tipo

- **Si el tipo tiene plantilla** en `references/`, usarla, **respetando sus «Determinantes
  obligatorios»** (paso 1 / sección 2). Las plantillas previstas son:
  - [`references/plantilla-servicios.md`](references/plantilla-servicios.md)
  - [`references/plantilla-locacion.md`](references/plantilla-locacion.md)
  - [`references/plantilla-compraventa.md`](references/plantilla-compraventa.md)
  - [`references/plantilla-nda.md`](references/plantilla-nda.md)
- **Si no hay plantilla para el tipo** → **estructura canónica genérica** (paso 2) + **marcadores**
  en las cláusulas específicas del tipo (las que una plantilla habría anclado).

> **Degradación honesta.** Si la plantilla del tipo no está presente en la sesión, no inventar su
> contenido ni sus anclas normativas: seguir con la **estructura canónica genérica** + marcadores, y
> **dejar constancia** en el Estado del análisis de que la plantilla del tipo aún no estuvo
> disponible.

### Paso 4 — QC obligatorio de red-flags sobre el propio borrador (innegociable)

**Antes de entregar CUALQUIER borrador**, correr el catálogo **completo** de la skill `red-flags`
**SOBRE EL PROPIO BORRADOR**, en su **orden obligatorio y sin recortar**:

1. **Invalidez metodológica primero.** Un borrador **nuestro** con terminología foránea
   (siglas de otra jurisdicción, montos en moneda ajena sin aclaración, bloques
   REUNIDOS/EXPONEN calcados) es un **bug grave**: se corrige de inmediato, no se entrega.
2. **Nivel 1 — Nulidad / ineficacia** — completo.
3. **Niveles 2 y 3 — Riesgo alto y medio** — completos.

El motor **corre entero**, no se detiene en la primera señal. **Nunca se entrega un borrador que
dispararía la propia revisión.** Si el QC encuentra algo: **corregir el borrador y re-correr** el
catálogo, hasta que quede limpio o hasta que el hallazgo residual sea una decisión consciente del
abogado documentada en el Estado del análisis. El resultado del QC (limpio / hallazgos corregidos)
va **siempre** al paso 5.

Esta skill **no interpreta ni reescribe** los marcadores del motor: los recibe, corrige el borrador
y re-corre. No duplica el catálogo (vive en `red-flags`).

### Paso 5 — Estado del análisis (cierre obligatorio de todo borrador)

Todo borrador cierra con este bloque de formato fijo (interfaz que consumen las tareas siguientes y
los evals); se respetan sus cuatro ítems aun cuando alguno quede en «Ninguno»:

```
### Estado del análisis
- Marcadores pendientes: [cada dato concreto que falta para completar el borrador]
- Normas con [VERIFICAR VIGENCIA]: [listado, o "Ninguna"]
- Decisiones estructurales por defecto que el abogado debe confirmar: [listado, o "Ninguna"]
- Resultado del QC de red-flags: [limpio / hallazgos corregidos: cuáles]
```

---

## 4. Reglas duras de la skill (el usuario no las suspende en sesión)

1. **No se redacta sin determinantes.** Falta un determinante (sección 2) → `[VACÍO FÁCTICO]` y se
   pide; **no se redacta**. Lo secundario sí puede salir con marcadores.
2. **Confidencialidad siempre con plazo determinado.** No se redacta una cláusula de
   confidencialidad **sin plazo**. Si el abogado pide **plazo indefinido**, **informar el riesgo**
   (una obligación perpetua tiende a ser inejecutable / desproporcionada) y **proponer un plazo
   determinado con renovación**. No se entrega confidencialidad abierta.
3. **Riesgo laboral → derivar, no redactar como civil.** Si el diagnóstico (pregunta 7) muestra
   indicios de subordinación, **marcarlo y derivar** a `contrato-trabajo` / plugin
   `paraguay-laboral`. No se disfraza una relación laboral bajo forma de contrato civil (es una
   nulidad del catálogo, y además un riesgo para el propio cliente).
4. **Posiciones del estudio como default de las cláusulas críticas.** Si el archivo **local no
   versionado** `legal.local.md` tiene la sección **«Posiciones del estudio — contratos»**, usar la
   posición **Preferida** como default de las cláusulas críticas (limitación de responsabilidad,
   jurisdicción/arbitraje, mediación previa opcional, cláusula penal, plazo de confidencialidad,
   reajuste, garantías).
   **Degradar bien:** si el archivo o la sección **no existen**, no fallar: aplicar **defaults
   neutrales** calibrados a la parte que se representa y **registrarlos como «decisiones por
   defecto»** en el Estado del análisis, para que el abogado los confirme.
5. **Placeholders canónicos.** Los campos variables del borrador se dejan con placeholders
   uniformes: `[PARTE_A]`, `[PARTE_B]`, `[C.I.]`, `[RUC]`, `[DOMICILIO]`, `[PRECIO]`, `[PLAZO]`,
   `[CIUDAD]`. Los datos personales del abogado (firma, matrícula) nunca se hardcodean: viven en
   `legal.local.md`.
6. **Regla de oro normativa.** No se citan artículos por número (las anclas viven en la estructura
   canónica y las plantillas). Mención normativa inevitable fuera de esas fuentes →
   `[VERIFICAR VIGENCIA]`.

> El **diagnóstico previo** (heredado del núcleo) y la **gramática de autoridad** de
> `CLAUDE.base.md`, más el control de citas de la skill `citacion`, **rigen tal como están** — esta
> skill los referencia, no los copia.

---

## 5. Relación con otras skills

- **`red-flags`** (motor, este plugin) — hace la detección; esta skill lo corre como **QC del
  propio borrador** (paso 4). No lo duplica.
- **`revision-contractual`** (este plugin) — revisa contratos aportados. **Destino de la
  derivación** si el usuario trae un contrato ya hecho para analizar (redacción ≠ revisión).
- **`diagnostico`** (núcleo) — el diagnóstico previo obligatorio; su disciplina rige el paso 1.
- **`citacion`** (núcleo) — gobierna cómo se cita una norma cuando una cláusula debe justificarse
  ante el abogado.
- **`contrato-trabajo`** / **`paraguay-laboral`** — destino de la derivación si el diagnóstico
  detecta relación laboral (pregunta 7 / Regla dura 3). No se redacta el vínculo laboral acá.

---

## 6. Qué NO hace esta skill

- No revisa contratos aportados: eso es de `revision-contractual` (deriva).
- No recalcula ni reescribe el catálogo de `red-flags`: lo corre completo como QC y corrige el
  borrador con su salida.
- No cita artículos por número ni normas de memoria: usa las anclas de la estructura canónica y las
  plantillas, o `[VERIFICAR VIGENCIA]`.
- No redacta con vacíos fácticos determinantes (Regla dura 1) ni confidencialidad sin plazo
  (Regla dura 2).
- No redacta relaciones laborales encubiertas: las marca y deriva (Regla dura 3).
- No inventa el contenido de una estructura o plantilla que aún no existe: lo dice y degrada
  (pasos 2 y 3), dejándolo constar en el Estado del análisis.
