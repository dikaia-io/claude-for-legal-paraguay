---
name: dictamenes
description: Elabora dictámenes jurídicos formales en el contexto laboral paraguayo (también civil/comercial/tributario, excluyendo penal). Produce un documento estructurado (consulta, análisis, desarrollo, conclusiones, recomendaciones) con fundamentación normativa precisa, análisis de riesgos cuantificado y recomendaciones orientadas al beneficio del cliente dentro del marco legal. Usar cuando el cliente pide una opinión legal formal o dictamen escrito, o para formalizar el análisis de estrategias-empleador en un documento entregable.
---

# Skill · Dictámenes jurídicos (Paraguay)

> **Origen y atribución.** Contenido portado de la skill `dictamenes-juridicos-py` de Miguel Fernando
> Díaz, incorporado al repositorio bajo Apache-2.0. Auditado: sin datos de clientes reales (metodología
> y referencias normativas genéricas).
>
> Skill del plugin `paraguay-laboral`. Se rige por el agente `asistente-paraguay` (no inventar normas
> ni jurisprudencia, marcadores, gramática de autoridad). **Formaliza** en un documento entregable el
> análisis que produce `estrategias-empleador`; no recalcula ni reaudita.

---

## 1. Función

Producir un **dictamen jurídico formal**: una opinión legal escrita, estructurada y fundamentada, que
analiza una situación, cuantifica riesgos y concluye con recomendaciones prácticas orientadas al
beneficio del cliente **dentro del marco legal**.

Es la cara "documento" de la asesoría: donde `estrategias-empleador` entrega el análisis de decisión,
esta skill lo **redacta como dictamen** entregable al cliente.

---

## 2. Cuándo se usa

- El cliente pide una **opinión legal formal** o un dictamen escrito.
- Hay que **formalizar** el análisis de contingencia (`estrategias-empleador`) en un documento.
- Se necesita evaluación de riesgos **cuantificada** con recomendaciones estratégicas por escrito.

No es para penal (queda fuera del alcance).

---

## 3. Estructura del dictamen

Sigue esta estructura (las secciones intermedias se integran según la complejidad del caso):

1. **Encabezado:** PARA / ATN / DE / FECHA / ASUNTO (datos del abogado desde `legal.local.md`).
2. **Consulta planteada:** los hechos relevantes en prosa conectada; identificar los puntos jurídicos
   a analizar. Si faltan hechos determinantes → `[VACÍO FÁCTICO]`.
3. **Análisis:** marco legal aplicable; vincular hechos con normas (citadas vía skill `citacion`);
   implicaciones prácticas; escenarios, considerando posible mala fe de la contraparte.
4. **Desarrollo** (casos complejos): profundizar; detallar riesgos con montos cuando corresponda
   (el cálculo lo provee `calculo-laboral`, no se inventa).
5. **Conclusiones:** posición jurídica clara y fundamentada.
6. **Recomendaciones:** soluciones concretas, medidas preventivas, pasos a seguir, relación
   costo-beneficio — priorizando el interés del cliente dentro del marco legal.
7. **Cierre formal.**

> Plantilla y frases jurídicas de apoyo en `assets/` (template y frases en prosa forense paraguaya).

---

## 4. Análisis de riesgos (metodología)

Reutilizable también por `estrategias-empleador`. Cuatro pasos:

1. **Identificar contingencias:** escenarios adversos, considerando mala fe de la contraparte.
2. **Cuantificar:** montos de indemnizaciones (arts. 91-92 CT) u otras contingencias —**vía el motor
   `calculo-laboral`**, nunca a ojo.
3. **Proponer mitigación:** acciones concretas para minimizar el riesgo.
4. **Contexto paraguayo:** prácticas del MTESS, tribunales laborales e IPS.

---

## 5. Principios de redacción

- **Prosa continua**, sin viñetas, con conectores lógicos (estilo dictamen forense paraguayo).
- **Formal pero accesible**: profesional y objetivo.
- **Fundamentación:** cita específica de artículo/inciso/norma (jerarquía: Constitución → leyes →
  decretos → resoluciones). Jurisprudencia y doctrina solo si están verificadas/aportadas
  (regla del núcleo: no inventar fallos).
- **Enfocado en soluciones:** todo análisis conduce a una recomendación práctica.
- Datos del abogado (firma, matrícula) desde `legal.local.md`, nunca incrustados en la skill.

---

## 6. Relación con otras skills

- **`estrategias-empleador`** — provee el análisis de contingencia que este dictamen formaliza.
- **`calculo-laboral` / `liquidaciones`** — proveen los montos; el dictamen los cita, no los recalcula.
- **`citacion`** (núcleo) — gobierna cómo se citan las normas del dictamen.
- **`diagnostico`** (núcleo) — si el dictamen parte de un escrito, se audita primero.

---

## 7. Qué NO hace esta skill

- No inventa normas, montos ni jurisprudencia: los toma de las skills de cálculo/cita o los marca pendientes.
- No emite dictámenes penales (fuera de alcance).
- No reemplaza la firma profesional: el dictamen es un borrador que el abogado revisa y suscribe.
