# Matriz pretensión → elementos → prueba

> Patrón adaptado del *civil element chart* del upstream `anthropics/claude-for-legal`
> (litigation-legal), ajustado a la disciplina de este repo: elementos solo desde norma verificada,
> marcadores del catálogo cerrado, y la matriz como **borrador de trabajo**, nunca conclusión de
> mérito.

## Principios

1. **La matriz es un borrador para el abogado, no un hallazgo.** Cada fila es una pista a verificar
   contra el expediente. Encabezar toda salida con esta advertencia; no ablandarla.
2. **La salida prioritaria es la lista de vacíos.** El resto de la matriz existe para producirla.
3. **Sesgo a marcar.** Un vacío no marcado es una puerta de un solo sentido (pretensión que se
   rechaza, defensa que precluye). Un vacío marcado de más se limpia en revisión. Ante la duda,
   marcar.
4. **Prohibido rellenar.** Prueba insuficiente = estado `vacío`, nunca extrapolar desde el
   conocimiento del modelo, "casos similares" o cómo "suele" fallar un tribunal.
5. **Elementos con ancla.** La descomposición en elementos sale de la norma invocada en el escrito
   (contrastada contra el authority map o el texto local) — no de memoria. Sin ancla verificada →
   `[ARGUMENTO SIN NORMA]` en la fila.

## Estados por elemento (cerrados)

| Estado | Significado |
|---|---|
| `probado` | Prueba directa identificada en el expediente/material, con cita puntual |
| `parcial` | Hay prueba de una parte del elemento; se indica qué parte falta |
| `controvertido` | Hay prueba en ambos sentidos; la fila lista ambas |
| `vacío` | Sin prueba identificada → entra a la lista de vacíos |
| `requiere-prueba` | Cerrable en la etapa actual; se indica el medio (testigo, informe, pericia, absolución) y su plazo de ofrecimiento |

## Formato

Una tabla por pretensión o defensa:

```markdown
### Pretensión: [p. ej. resolución de contrato por incumplimiento + daños]
Base normativa: [norma y arts., estado en authority map] — elementos según [artículo(s)]

| # | Elemento | Prueba a favor (cita puntual) | Prueba en contra | Estado |
|---|---|---|---|---|
| 1 | Existencia del contrato | Contrato de fs. 5-12, firmado | — | probado |
| 2 | Cumplimiento propio | Facturas fs. 15-18 (parcial: falta entrega final) | Nota de fs. 40 niega recepción | controvertido |
| 3 | Incumplimiento de la contraparte | — | — | vacío |
| 4 | Daño y su monto | — (monto afirmado sin respaldo) | — | requiere-prueba (pericia contable; ofrecer en los 10 primeros días, art. 253 CPC) |
```

Seguida de:

```markdown
### Lista de vacíos (salida prioritaria)
1. [VACÍO PROBATORIO] Elemento 3 (incumplimiento) — sin prueba identificada. Cerrable con: [medio].
   Etapa límite para producirla: [etapa/plazo, vía skill plazos].
2. [VACÍO PROBATORIO] Elemento 4 (monto del daño) — afirmado sin respaldo. Cerrable con pericia.
...
```

## Lectura según de quién es el escrito

- **Escrito propio (antes de presentar):** cada `vacío` es un defecto a cerrar **antes** de
  presentar, o una pretensión a reformular/retirar. Recordar: los hechos no articulados en el
  escrito constitutivo no se prueban después (art. 247 CPC) — la matriz se corre **antes** de que
  la demanda/contestación quede fijada.
- **Escrito de la contraparte:** cada `vacío` de ellos es una defensa (la carga de probar el hecho
  es de quien lo afirma, art. 249 CPC) y un blanco para la contestación o el alegato. Cada
  `controvertido` es el campo de batalla probatorio: ahí se concentra el ofrecimiento propio.
- **En ejecutivo:** la matriz se reduce — los "elementos" son los presupuestos del título
  (art. 439/448 CPC: título hábil, obligación exigible, cantidad líquida) y, del lado del
  ejecutado, los presupuestos de la excepción elegida (art. 462: p. ej. pago **documentado**);
  recordar que la carga de la prueba de las excepciones es del ejecutado (art. 468 CPC).

## Encuadre por etapa (misma matriz, distinta lectura)

| Etapa | Qué responde la matriz |
|---|---|
| Antes de demandar/contestar | ¿Cada pretensión/defensa tiene sus elementos cubiertos o cerrables? ¿Conviene reformular? |
| Período probatorio | ¿Qué medio cierra cada vacío y cuál es su plazo de ofrecimiento (art. 253 CPC / 20 días posiciones, art. 277)? |
| Alegatos | La matriz se convierte en el índice del alegato: elemento → prueba producida → valoración pedida (sana crítica, art. 269 CPC) |
| Recursos | ¿Qué elemento quedó sin prueba y fue igualmente acogido/rechazado? — ahí está el agravio |

> Jurisprudencia de apoyo (criterios de valoración, cargas dinámicas, etc.): no cargada en el repo →
> `[INSERTAR JURISPRUDENCIA VERIFICADA]` cuando el análisis la necesite.
