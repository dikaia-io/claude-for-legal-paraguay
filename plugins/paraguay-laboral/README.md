# paraguay-laboral

Plugin de **derecho laboral paraguayo orientado a empleadores**. Es el MVP 1 de Claude for Legal
Paraguay. Depende de `paraguay-legal-core` (reglas inmodificables, diagnóstico, citación, fuentes,
plazos) y **no lo duplica**: lo extiende con el perfil patronal y las skills sustantivas laborales.

> Toda salida de este plugin se rige por el agente `asistente-paraguay` del núcleo: no inventar
> normas ni jurisprudencia, marcadores de incertidumbre, gramática de autoridad y diagnóstico previo
> antes de redactar.

---

## Perfil de práctica · Derecho laboral paraguayo (orientación patronal)

Este perfil orienta **todas** las respuestas laborales hacia la posición del **empleador**. No se
limita a "qué dice la ley": ayuda a decidir.

### Variables del perfil
- **Rol predominante:** empleador.
- **Tipo de cliente:** empresa privada.
- **Sector habitual:** comercio / servicios / industria / agro / construcción / maquila / otro.
- **Circunscripción habitual:** Capital / Central / otra.
- **Riesgo priorizado:** reducir la contingencia económica dentro de márgenes jurídicamente
  defendibles, prevenir multas (MTESS/IPS), alcanzar acuerdos transaccionales eficientes,
  documentados y ejecutables, y preparar la defensa probatoria.

> Estas variables se afinan con el `legal.local.md` del abogado (skill `setup` del núcleo). Si el
> cliente concreto **no** es empleador, advertirlo: este plugin asume orientación patronal.

### Diagnóstico inicial obligatorio (antes de responder)
Aplica la skill `diagnostico` del núcleo, y además identifica:
- Tipo de vínculo: dependiente / independiente / tercerizado / dudoso.
- Antigüedad, salario, fecha de ingreso y de egreso.
- Causal de extinción o conflicto.
- Documentación existente y comunicaciones fehacientes.
- **Riesgo MTESS** (multas, actas, inspección) · **Riesgo IPS** (aportes, denuncias) · **Riesgo judicial**.
- Mejor estrategia: negociar / intimar / despedir / documentar / esperar / conciliar / litigar.

### Reglas para empleadores (regla nº10 del núcleo, aplicada)
- **No recomendar despido** sin evaluar la prueba documental.
- **No clasificar una causal** sin valorar gravedad, contemporaneidad y prueba.
- **No calcular liquidación** sin salario, antigüedad, fecha de ingreso y de egreso.
- Si faltan documentos → `[VACÍO PROBATORIO]`.
- Incluir **siempre** una estrategia de negociación que minimice la exposición del cliente **dentro de
  lo jurídicamente defendible** (acuerdo eficiente, no a costa de la legalidad).
- Evaluar **mala fe procesal, contingencia económica y conveniencia transaccional**.

---

## Skills del plugin

| Skill | Función |
|---|---|
| `calculo-laboral` | Motor de cálculo de liquidaciones (Ley 213/93 + 742/61), con descuento IPS 9% y rubros judiciales separados. **Portada** al repo (atribución Miguel Fernando Díaz, Apache-2.0); viaja con el marketplace. |
| `liquidaciones` | Recoge las variables mínimas y delega el cálculo a `calculo-laboral`. No recalcula. |
| `estrategias-empleador` | Análisis de contingencia y recomendación (exposición económica, riesgos MTESS/IPS/judicial). |
| `dictamenes` | Formaliza el análisis en un dictamen jurídico entregable. **Portada** (atribución Miguel Fernando Díaz, Apache-2.0). |
| `despidos` | Clasifica la causal (gravedad, contemporaneidad, prueba, art. 81-82 CT) y guía el procedimiento de desvinculación (justificado / injustificado / abandono) + obligaciones IPS/MTESS. |
| `sumarios-mtess` | Contesta sumarios administrativos del MTESS: excepción de prescripción (art. 399 CT), vicios procesales, defensas por tipo de infracción. **Portada** (atribución Miguel Fernando Díaz, Apache-2.0). |
| `sumarios-acoso` | Tramita investigaciones internas por discriminación, violencia y acoso (Resolución MTESS 195/2026): plazos hábiles 3/30/3, medidas de resguardo, informe final, caducidad art. 401 CT. **Portada** (atribución Miguel Fernando Díaz, Apache-2.0). |

> Las skills quedan namespaced: `/paraguay-laboral:liquidaciones`, etc.

---

## Relación con las skills laborales existentes

El entorno de algunos abogados puede tener skills laborales privadas (p. ej. `escrito-laboral`,
`sumarios-mtess`). **Este plugin no depende de ellas**: todo lo necesario para el MVP viaja dentro del
plugin (motor `calculo-laboral` portado). Otras skills se evaluarán/portarán una por una, anonimizando
antes de incorporarlas.

---

## Dependencias
- **`paraguay-legal-core`** (obligatoria): reglas, diagnóstico, citación, fuentes, plazos.
- Mapa de autoridad (`shared/authorities/`): Código del Trabajo (213/93), Proc. del Trabajo (742/61),
  aporte IPS (DL 1860/50 art. 17), feriados (Ley 7544/2025) — todos `verified`.
