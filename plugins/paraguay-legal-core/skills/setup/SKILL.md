---
name: setup
description: Entrevista de configuración inicial que genera o actualiza el archivo legal.local.md del abogado o estudio a partir de la plantilla. Pregunta identidad profesional, circunscripción, rol predominante, áreas, sector de clientes, preferencias de estilo y posiciones contractuales opcionales, una sección a la vez, y escribe el resultado. Usar en la primera configuración, cuando cambia el perfil, o cuando el abogado pide reconfigurar.
---

# Skill · Setup (configuración local del abogado)

> Skill del núcleo (`paraguay-legal-core`). Genera o actualiza `legal.local.md` — el perfil personal
> que complementa las reglas inmodificables de `CLAUDE.base.md`.
> **No inventa datos:** pregunta, confirma y escribe lo que el abogado responde.

---

## 1. Función

Conducir una **entrevista breve** y, al final, producir el contenido de `legal.local.md` siguiendo la
plantilla `shared/templates/legal.local.md.template`. El archivo resultante guarda el perfil del
abogado/estudio para no volver a preguntar lo mismo en cada sesión.

La skill **no decide** por el abogado ni rellena con valores supuestos: si una respuesta falta, deja
el placeholder `[COMPLETAR]` de la plantilla.

---

## 2. Regla de privacidad (no negociable)

`legal.local.md` contiene **datos personales** (nombre, matrícula CSJ, contacto). Por eso:

- **Nunca se versiona.** Ya está bloqueado por `.gitignore`. Solo el `.template` (con placeholders) va al repo.
- **Nunca incluir** estos datos en archivos del repositorio, en skills, ni en el paquete del plugin
  que se distribuye.
- Recordar al abogado que el contenido de `legal.local.md`, al usarse en sesión, **viaja a Anthropic**
  como cualquier contexto (ver `CLAUDE.base.md` §6 y `docs/seguridad-y-privacidad.md`).
- La matrícula CSJ y el nombre del responsable **no van** en `CLAUDE.base.md` ni en ningún archivo
  versionado: solo en la copia local.

---

## 3. La entrevista

Hacer las preguntas **una sección a la vez**, en este orden. Para cada pregunta, indicar entre
paréntesis las opciones cuando las haya, y **por qué se pregunta** (impacto), para que el abogado
responda con criterio. Aceptar «no aplica» o dejar el campo vacío cuando corresponda.

### Modo exprés (primera configuración rápida)

Si el abogado pide la «configuración exprés» (o llega desde el paquete de claude.ai, cuyo
bootstrap la ofrece en el primer mensaje), preguntar **solo estos 4 campos, en un único
mensaje**: abogado responsable, matrícula CSJ, circunscripción habitual y rol predominante.
El resto de la plantilla queda con `[COMPLETAR]`, y se ofrece la entrevista completa como paso
opcional posterior. La regla de privacidad (sección 2) aplica igual.

### Bloque 1 — Identidad profesional
1. **Firma / estudio.** Nombre del estudio, o «Profesional independiente».
2. **Abogado responsable.** Nombre y apellido.
   *Impacto: encabeza escritos y dictámenes. Es dato personal → solo en `legal.local.md`.*
3. **Matrícula CSJ.** Número de matrícula de la Corte Suprema de Justicia.
   *Impacto: identifica al profesional en escritos. Dato personal.*
4. **Circunscripción habitual.** (Capital / Central / otra — indicar cuál.)
   *Impacto: orienta tribunales y órganos de referencia. La jurisdicción es siempre Paraguay.*

### Bloque 2 — Práctica
5. **Rol predominante.** (empleador / trabajador / mixto.)
   *Impacto: define la orientación por defecto. «empleador» activa el análisis patronal (regla nº10
   de `CLAUDE.base.md`) cuando se cargue el perfil laboral.*
6. **Áreas prioritarias.** (laboral / civil / comercial / litigación / otras — listar.)
   *Impacto: prioriza qué materias y skills se asumen por defecto.*
7. **Sector habitual de clientes.** (comercio / servicios / industria / agro / construcción / maquila / otro.)
   *Impacto: contextualiza ejemplos y riesgos típicos.*

### Bloque 3 — Repositorios locales (opcional)
8. **Legislación / jurisprudencia / casos y modelos en disco.** Rutas locales, o vacío si no aplica.
   *Impacto: permite consultar fuentes locales antes que portales web. Los casos/modelos reales son
   confidenciales y deben anonimizarse antes de incorporarse al repo.*

### Bloque 4 — Preferencias de estilo
9. **Estilo de salida.** (formal-estratégico / formal-neutro / didáctico.)
   *Impacto: ajusta el tono. Sobreescribe el estilo por defecto de `CLAUDE.base.md` §7.*
10. **Nivel de detalle por defecto.** (ejecutivo / completo.)

### Bloque 5 — Contacto (opcional, para encabezados)
11. **Domicilio procesal / teléfono / correo.** Cualquiera puede quedar vacío.
    *Impacto: solo se usa si el abogado pide armar el encabezado de un escrito.*

### Bloque 6 — Posiciones del estudio — contratos (opcional)
12. **¿Querés cargar posiciones contractuales del estudio?** (sí / no / dejar placeholders.)
    *Impacto: `revision-contractual` y `redaccion-contractual` pueden calibrar cláusulas críticas
    contra tus posiciones propias; si queda vacío, operan en modo neutral.*
13. Si responde que sí, preguntar por estas cláusulas críticas, una por una, usando el formato
    **Preferida / Aceptable / Nunca aceptar** de la plantilla:
    - Limitación de responsabilidad.
    - Jurisdicción y arbitraje.
    - Mediación previa (**opcional**; no se asume si el abogado no la pacta).
    - Cláusula penal.
    - Plazo de confidencialidad.
    - Reajuste en contratos de tracto largo.
    - Garantías.

### Bloque 7 — Notas internas (opcional)
14. **Convenciones o recordatorios del estudio.** Texto libre. **Nunca se publica ni se cita.**

---

## 4. Confirmación y escritura

1. Al terminar la entrevista, **mostrar un resumen** de lo capturado y pedir confirmación antes de escribir.
2. Generar el contenido respetando **exactamente** las secciones y campos de
   `legal.local.md.template` (Identidad profesional / Práctica / Repositorios locales /
   Preferencias de estilo / Datos de contacto / Posiciones del estudio — contratos / Notas internas).
3. Todo campo sin respuesta queda con su placeholder `[COMPLETAR]` (no inventar).
4. **Escritura del archivo según la superficie:**
   - **Claude Code / Cowork:** ofrecer escribir `legal.local.md` en el workspace (no dentro del
     paquete del plugin). Confirmar la ruta antes de escribir.
   - **Claude Project:** no hay escritura de archivo; entregar el contenido listo para guardar
     como **`perfil-del-abogado.md`** y **subir al Knowledge** del Project. **No pegarlo en las
     instrucciones del proyecto**: ahí se perdería al actualizar el paquete (las instrucciones
     se reemplazan enteras en cada versión; el Knowledge conserva el perfil). Indicar el cómo:
     guardar el bloque con el Bloc de notas como `perfil-del-abogado.md` y arrastrarlo al
     Knowledge.
5. Recordar la **regla de privacidad** (sección 2) al entregar el resultado.

---

## 5. Actualización de un perfil existente

Si ya existe `legal.local.md`, **no rehacer todo**: leer el actual, mostrarlo y preguntar **solo** qué
campos cambian. Reescribir conservando lo demás intacto. Nunca borrar las «Notas internas» sin
confirmación expresa.

---

## 6. Qué NO hace esta skill

- No pide ni guarda datos de **clientes** (eso se anonimiza; ver `CLAUDE.base.md` §6). Solo configura
  el perfil del **abogado/estudio**.
- No versiona ni publica `legal.local.md`.
- No define reglas jurídicas: esas viven en `CLAUDE.base.md` y en el mapa de autoridad.
- No asume valores por defecto no confirmados: ante la duda, deja `[COMPLETAR]`.
