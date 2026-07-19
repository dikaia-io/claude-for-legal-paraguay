# paraguay-contratos

Plugin de **contratos civiles y comerciales bajo derecho paraguayo**. Es el MVP 2 de Claude for
Legal Paraguay. Depende de `paraguay-legal-core` (reglas inmodificables, diagnóstico, citación y
fuentes oficiales) y **no lo duplica**: lo extiende con revisión contractual, red flags y redacción
de borradores.

> Toda salida de este plugin se rige por el agente `asistente-paraguay` del núcleo: no inventar
> normas ni jurisprudencia, usar marcadores de incertidumbre, aplicar gramática de autoridad y pedir
> datos determinantes antes de concluir o redactar.

---

## Perfil de práctica · Contratos paraguayos

Este plugin opera con **perspectiva neutral según la parte representada**. A diferencia del MVP
laboral, no asume una orientación fija: antes de revisar o redactar pregunta si el abogado representa
al comprador/vendedor, locador/locatario, prestador/cliente, parte divulgante/receptora, u otra.

Variables que condicionan el análisis:
- **Parte representada:** define severidad, defaults de redacción y propuestas de ajuste.
- **Tipo contractual:** servicios, locación, compraventa, confidencialidad/NDA u otro contrato civil o
  comercial.
- **Régimen especial:** consumidor, adhesión, relación laboral encubierta, garantías registrables,
  arbitraje o ley/jurisdicción extranjera.
- **Posiciones del estudio:** si `legal.local.md` trae la sección "Posiciones del estudio —
  contratos", las skills calibran contra ella; si no, operan en modo neutral y lo declaran.

---

## Skills del plugin

| Skill | Función |
|---|---|
| `red-flags` | Motor transversal: detecta plantilla foránea y 20 red flags por nivel de riesgo. Lo consumen revisión y redacción. |
| `revision-contractual` | Orquesta revisión: clasifica, corre `red-flags`, aplica ficha por tipo, compara contra posiciones del estudio y arma informe completo o resumido. |
| `redaccion-contractual` | Redacta contratos nuevos: diagnóstico previo, estructura canónica paraguaya, plantilla por tipo, QC con `red-flags` y Estado del análisis. |

> Las skills quedan namespaced: `/paraguay-contratos:revision-contractual`,
> `/paraguay-contratos:redaccion-contractual`, etc.

---

## Revisión contractual

La revisión sigue un flujo fijo:
1. Clasificación inicial por títulos/anexos y datos determinantes.
2. Detección de invalidez metodológica y red flags.
3. Ficha específica si corresponde: servicios, locación, compraventa o confidencialidad/NDA.
4. Informe con doble severidad: riesgo jurídico y fricción comercial.
5. Propuesta quirúrgica de redacción alternativa cuando hay hallazgos.

Si el contrato llega con pedido de modificación directa, primero se entrega el informe. No se edita
antes de que el abogado lo lea.

---

## Redacción contractual

La redacción usa una entrevista de diagnóstico. Sin datos determinantes no redacta: marca
`[VACÍO FÁCTICO]` y pide completar.

Plantillas disponibles:
- Servicios profesionales.
- Locación.
- Compraventa.
- Confidencialidad/NDA.

Los demás contratos usan la estructura canónica genérica con placeholders y marcadores. Todo borrador
pasa por QC obligatorio con `red-flags` antes de entregarse.

La **mediación previa** es una cláusula **opcional**: no se incluye por defecto. Solo se incorpora si
el abogado la pacta expresamente, con centro/plazo definidos y sin bloquear medidas urgentes ni
cautelares.

---

## Dependencias

- **`paraguay-legal-core`** (obligatoria): reglas, diagnóstico, citación y fuentes oficiales.
- Mapa de autoridad (`shared/authorities/`): Código Civil, Ley del Comerciante, Defensa del
  Consumidor, Pacto de Retroventa, Cheque de Pago Diferido, Arbitraje y Protección de Información no
  Divulgada, según estado `verified` registrado en `verification-log.md`.
