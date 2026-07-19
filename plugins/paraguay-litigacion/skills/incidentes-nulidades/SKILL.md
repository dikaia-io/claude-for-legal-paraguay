---
name: incidentes-nulidades
description: Nulidades procesales e incidentes en la litigación paraguaya (CPC arts. 111-117, 180-191, 404-409) - elige la vía correcta (incidente, recurso, acción autónoma o régimen especial de ejecución), corre un test de viabilidad bloqueante antes de redactar y guía el trámite, para el nulidicente o para quien contesta
---

# Skill · Incidentes y nulidades procesales (Paraguay)

> **Fuentes.** Articulado del CPC (Ley 1337/1988, `verified`) verificado contra el texto
> consolidado local el 2026-07-05 (`verification-log.md`). Criterios de tribunales:
> `jurisprudencia.yaml` → `nulidad_ejecucion_trascendencia` y `nulidad_oficiosa_alzada`
> (verificados contra fallos reales; carátulas pendientes de PJ/CSJ).
>
> **Encaje:** el vicio normalmente se detecta en `diagnostico-escritos` (módulo 1, punto 4);
> esta skill decide la vía, valida la viabilidad y guía el planteo o su contestación. Los
> cómputos finos van a `plazos`; la estructura del escrito, a `escritos-judiciales`.

## Paso 1 — Elegir la vía (art. 117 CPC)

La nulidad se pide por **incidente o recurso según dónde vive el vicio**: incidente para vicios
en las **actuaciones** (se deduce en la instancia donde el vicio se produjo); recurso de nulidad
para vicios en las **resoluciones**. Elegir mal la vía es un error técnico frecuente.

| El vicio está en... | Vía | Base |
|---|---|---|
| Una actuación (notificación defectuosa, audiencia mal practicada, traslado omitido) | **Incidente de nulidad**, en la instancia del vicio | 117; trámite 180-191 |
| Una resolución (S.D. o A.I. dictados con violación de formas o solemnidades) | **Recurso de nulidad** — implícito en la apelación | 404-405 |
| Una sentencia **firme** que perjudica a un **tercero** en indefensión | **Acción autónoma de nulidad** (residual: solo si falsedad de la ejecutoria o inhabilidad de título no alcanzan) | 409 (texto según Ley 4419/2011) |
| El procedimiento del **juicio ejecutivo civil** | Excepción de nulidad (hasta la citación) → régimen propio | 463 → skill `juicio-ejecutivo` |
| La **ejecución laboral** | Excepción hasta la citación de remate; incidente después | 357 CPT → `escritos-laborales.md` |

Declarada la nulidad de actuaciones, caen también las resoluciones que sean su consecuencia
(117, 2º párr.); la nulidad no se extiende a actos precedentes ni a los posteriores
independientes (115), y el juez debe ordenar la renovación de los actos anulados cuando sea
posible (116).

## Paso 2 — Test de viabilidad (bloqueante: sin esto no se redacta)

Correr **antes** de redactar cualquier planteo de nulidad. Si un punto falla, informarlo y no
redactar (o reencuadrar la defensa):

1. **Especificidad (111).** ¿La nulidad está conminada por ley, o el acto carece de un requisito
   formal o material *indispensable*? Vicios menores no alcanzan.
2. **Finalidad (111 in fine).** Si el acto, aunque irregular, **alcanzó su fin**, no procede la
   anulación (p. ej. notificación defectuosa pero la parte contestó en plazo).
3. **Trascendencia (criterio verificado).** Vicio + **perjuicio cierto y concreto** + indicar
   **qué defensas se vieron impedidas**. "No procede la nulidad por la nulidad misma" — criterio
   uniforme de los Tribunales de Apelación (`nulidad_ejecucion_trascendencia`, aplicado por las
   salas con cita de Alsina y Tellechea).
4. **Protección (112).** Solo la pide la parte perjudicada **que no contribuyó al vicio**. Quien
   generó o consintió el acto no puede invocarlo (salvo nulidad de oficio, 113).
5. **Convalidación (114 y 191).** La nulidad se subsana si el acto cumplió su finalidad, por
   confirmación expresa o **tácita** — no promover el incidente dentro de los **cinco días**
   subsiguientes al conocimiento del acto viciado (art. 114 inc. b) — o por cosa juzgada.
   Concordante con el art. 191 (regla residual de todo incidente: 5 días desde el conocimiento).
   *Nota de fuente: el número del art. 114 inc. b faltaba en las transcripciones disponibles
   (incluido el HTML de BACN); verificado el 2026-07-19 contra el escaneo oficial del texto
   original promulgado (PJ/CSJ).*
6. **Costo estratégico.** Un planteo débil no es neutro: costas, y **tres incidentes perdidos
   con costas en el mismo proceso configuran ejercicio abusivo** (art. 53 inc. b), con las
   sanciones de los arts. 54-56 (presunción en contra, costas aunque venza, responsabilidad
   conjunta del profesional). Ver `diagnostico-escritos` módulo 1.8.

## Paso 3 — Incidente de nulidad (trámite: arts. 180-191)

Requisitos del escrito (183): fundarlo **clara y concretamente en los hechos y en el derecho**
(los tribunales rechazan incidentes sin fundamento normativo o atípicos mal encuadrados),
**ofrecer toda la prueba** y acompañar la documental. Trámite completo, suspensión del principal,
plazos y estrategia: `references/vias-y-tramite.md`.

## Paso 4 — Recurso de nulidad (arts. 404-408)

- Procede contra resoluciones dictadas **con violación de la forma o solemnidades** legales
  (404) — vicios de la resolución misma (incongruencia, falta de fundamentación, vicios de
  constitución del tribunal), no la injusticia de fondo (eso es apelación).
- Se interpone independiente, conjunta o separadamente con la apelación, en la cual está
  **implícito** (405). Criterio verificado (`nulidad_oficiosa_alzada`): la Alzada analiza la
  nulidad **de oficio** aunque el recurso esté desistido o solo se haya fundado la apelación —
  coherente con el art. 113 (nulidades declarables de oficio).
- Si el Tribunal anula, **resuelve también el fondo** (406); no pronuncia la nulidad si puede
  decidir a favor del nulidicente (407: la apelación repara).
- **Costas al juez** si el vicio le es imputable, sin petición de parte; salvo que la otra parte
  se haya opuesto a la declaración, en cuyo caso las carga ella (408).
- Recurso denegado → **queja en 5 días** (410-411).

## Paso 5 — Acción autónoma de nulidad (art. 409)

Vía **excepcional y residual** para **terceros** a quienes una resolución firme perjudica sin
haber sido oídos (indefensión), cuando la falsedad de la ejecutoria o la inhabilidad de título no
alcanzan a reparar el agravio. Se presenta ante el juzgado civil de turno (con las inhibiciones
del propio 409), **solo con sentencia firme y ejecutoriada**. No es una tercera instancia ni una
apelación tardía para quien fue parte: si el cliente fue parte y consintió, la vía está
convalidada. Requiere fundamentación reforzada — antes de redactarla, diagnóstico completo y
advertencia de su carácter excepcional.

## Contestar un planteo de nulidad ajeno

Invertir el test del Paso 2: atacar primero la **falta de trascendencia** (¿qué defensa concreta
se vio impedida? ¿qué perjuicio cierto?), la **convalidación** (¿cuándo conoció el acto? ¿pasaron
los 5 días?), la **protección** (¿contribuyó al vicio?) y la **finalidad** (¿el acto cumplió su
fin?). Pedir costas y, si es un patrón dilatorio, dejar constancia para el art. 53.

## Qué NO hace esta skill

- No decide si hay vicio: eso lo detecta el diagnóstico (`diagnostico` / `diagnostico-escritos`).
- No computa vencimientos: deriva a `plazos` (el plazo de 5 días del art. 191 corre desde el
  **conocimiento** — fijar ese hecho con precisión es parte del caso).
- No tramita la nulidad de la ejecución civil (463 → `juicio-ejecutivo`) ni la laboral (357 CPT).
- No redacta planteos que fallen el test de viabilidad: informa el resultado y las alternativas.
- No cita fallos puntuales: los criterios se afirman como tendencia (`jurisprudencia.yaml`);
  para citar un A. y S. concreto → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.
