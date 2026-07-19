# paraguay-litigacion

Plugin de **litigación civil, comercial y laboral paraguaya**. Es el MVP 3 de Claude for Legal
Paraguay. Depende de `paraguay-legal-core` (reglas inmodificables, diagnóstico, citación, fuentes,
plazos) y **no lo duplica**: lo extiende con la redacción de escritos judiciales y la guía procesal
de los juicios más frecuentes.

> Toda salida de este plugin se rige por el agente `asistente-paraguay` del núcleo: no inventar
> normas ni jurisprudencia, marcadores de incertidumbre, gramática de autoridad y **diagnóstico
> previo antes de modificar cualquier escrito** (regla nº 9 del núcleo).

---

## Alcance procesal

- **Norma procesal base:** Código Procesal Civil (Ley N° 1337/1988), `verified` en el mapa de
  autoridad con texto consolidado local (modificatorias hasta la Ley 7424/2025).
- **Fuero laboral:** el procedimiento se rige por el Código Procesal del Trabajo (Ley N° 742/1961),
  también `verified`. Las diferencias críticas (excepciones taxativas del art. 119 CPT; ejecución
  laboral arts. 356/357 CPT) están señaladas en `escritos-judiciales`.
- **Jurisprudencia:** ninguna cita de fallo entra a una salida sin verificación contra PJ/CSJ.
  Donde el argumento la necesite, se emite `[INSERTAR JURISPRUDENCIA VERIFICADA]`.

## Skills del plugin

| Skill | Función | Estado |
|---|---|---|
| `escritos-judiciales` | Base de todo escrito judicial paraguayo: estructura forense común, demanda y contestación civil/comercial (proceso ordinario), excepciones previas, reconvención, y las estructuras laborales **portadas** de la skill `escrito-laboral` (atribución Miguel Fernando Díaz, Apache-2.0). | ✅ **estable v0.2** — evals `evals/procesal/` aprobados 2026-07-19 (formato forense verificado en p-02 r4) |
| `juicio-ejecutivo` | Juicio ejecutivo del CPC (arts. 439-475): verificación del título, preparación de la vía, intimación/embargo, excepciones, sentencia de remate y cumplimiento. Perfila ejecutante y ejecutado. | ✅ **estable v0.2** — eval `caso-01-pagare-no-protestado` aprobado 2026-07-19; incisos del 462 anclados tras la corrida |
| `diagnostico-escritos` | Diagnóstico procesal profundo (extiende el `diagnostico` del núcleo): chequeo formal por fuero/etapa, matriz pretensión-elementos-prueba con lista de vacíos, y triage de escritos adversos con opciones de respuesta. Patrón del upstream `litigation-legal` (element chart + demand triage). | ✅ **estable v0.2** — evals `caso-02`/`caso-03` aprobados 2026-07-19 |
| `incidentes-nulidades` | Nulidades procesales e incidentes (CPC 111-117, 180-191, 404-409): elección de vía, test de viabilidad bloqueante (trascendencia, convalidación, protección) y trámite, para nulidicente o contraparte. Criterios reales de tribunales en `jurisprudencia.yaml`. | ✅ **estable v0.2** — eval `caso-04-nulidad-notificacion` aprobado 2026-07-19 |
| `inconstitucionalidad` | Impugnación de inconstitucionalidad (CPC 538-564; Ley 609/1995 y modificatorias): elección de vía, test de admisibilidad bloqueante (art. 12 Ley 609: rechazo in límine) y flujo de la acción contra resoluciones judiciales. Criterio de admisibilidad de la Sala Constitucional verificado contra el portal oficial en `jurisprudencia.yaml`. | ✅ **estable v0.2** — los 3 evals de `evals/constitucional/` aprobados 2026-07-19 (corrección aplicada: régimen 145-150 llevado a la skill `plazos` del núcleo) |

> Las skills quedan namespaced: `/paraguay-litigacion:escritos-judiciales`, etc.

## Dependencias

- **`paraguay-legal-core`** (obligatoria): reglas, diagnóstico, citación, fuentes, plazos.
- Mapa de autoridad (`shared/authorities/`): CPC (Ley 1337/1988), CPT (Ley 742/1961), Código Civil
  (Ley 1183/1985), Org. Judicial (Ley 879/1981), honorarios (Ley 1376/1988) — todos `verified`.

## Relación con skills privadas

El entorno de algunos abogados puede tener la skill privada `escrito-laboral`. **Este plugin no
depende de ella**: su contenido fue portado a `escritos-judiciales` y viaja con el marketplace.
