---
name: plazos
description: 'Marco para el cómputo de plazos procesales paraguayos. Conoce los inhábiles estructurales verificados (feria judicial de todo enero, art. 362 Ley 879/1981; feriados nacionales de la Ley 7544/2025 con su regla de feriados móviles trasladables a lunes), el régimen de cómputo civil del CPC verificado (arts. 145 perentoriedad, 147 cómputo desde la notificación, 149 ampliación por distancia y 150 gracia hasta las 09:00 del día hábil siguiente) y un catálogo verificado de plazos laborales del Código Procesal del Trabajo (Ley 742/1961) y sustantivos del Código del Trabajo (Ley 213/1993). Deriva a fuente oficial lo coyuntural (decretos de traslado anuales, asuetos y acordadas de la CSJ). NO afirma un vencimiento como definitivo: encuadra el plazo, da la duración legal, aplica los inhábiles conocidos como referencia y advierte la criticidad. Usar cuando haya un plazo en juego.'
---

# Skill · Plazos procesales

> Skill del núcleo (`paraguay-legal-core`).
>
> **Qué sabe y qué no.** Esta skill conoce (a) los **días inhábiles estructurales** del derecho
> paraguayo (feria de enero y feriados nacionales, verificados contra fuente oficial) y (b) un
> **catálogo verificado de duraciones de plazos laborales** —procesales del CPT (Ley 742/1961) y
> sustantivos del CT (Ley 213/1993)— en [`references/plazos-laborales-cpt.md`](references/plazos-laborales-cpt.md).
> Lo que **no** hace todavía es producir un cómputo de días hábiles cerrado y afirmar una **fecha de
> vencimiento como definitiva**, porque eso depende además de la forma de notificación y de
> **decretos/acordadas que cambian cada año**. Da la **duración legal** (artículo + días); la **fecha
> final** la deriva a verificación. Ante un plazo fatal, **advierte y deriva**: es preferible eso a
> arriesgar una fecha (regla nº2 de `CLAUDE.base.md`: no inventar plazos).

---

## 1. Función

- **Encuadrar** la consulta: tipo de plazo, norma que lo regula, desde cuándo corre.
- **Aplicar los inhábiles estructurales conocidos** (sección 3) como referencia del cómputo.
- **Identificar** qué inhábiles dependen de fuente coyuntural (decreto/acordada) y derivarlos.
- **Advertir** la criticidad: si hay riesgo de caducidad o prescripción, marcarlo de inmediato.
- **No** afirmar un vencimiento como definitivo sin confirmar el código procesal y los inhábiles del
  año contra fuente oficial.

---

## 2. Las tres capas de días inhábiles (con su certeza)

| Capa | Qué es | Certeza | Fuente |
|---|---|---|---|
| **Estructural permanente** | Feria judicial de **todo enero** | **Verificada** | Ley 879/1981, art. 362 |
| **Feriados nacionales** | Lista fija de la ley; algunos móviles | **Verificada** (lista); el traslado del año, no | Ley 7544/2025 |
| **Coyuntural** | Traslados anuales por decreto, asuetos, acordadas CSJ | **No verificable de antemano** | Decretos PE / Acordadas Digitales CSJ |

La skill afirma las dos primeras como referencia y **deriva** la tercera. Nunca da el traslado
concreto de un año ni un asueto como cierto sin confirmarlo.

---

## 3. Inhábiles estructurales verificados

### 3.1. Feria judicial — todo enero
- **Ley 879/1981 (Cód. Org. Judicial), art. 362:** *«Se establece el mes de enero como feria judicial.»*
  Verificado contra fuente local (`codigo_organizacion_judicial_879_1981.md`).
- **Art. 363:** la feria **no rige** para los **Jueces de Paz** ni los de **Instrucción en lo Criminal**;
  la CSJ regula la atención de asuntos urgentes durante la feria.
- Efecto: durante enero, los plazos procesales ordinarios **se suspenden** (salvo habilitación de
  feria o las excepciones del art. 363). Confirmar el alcance exacto según el código procesal y la
  instancia.

### 3.2. Feriados nacionales — Ley 7544/2025
Feriados nacionales (además de los domingos), **art. 1**:

`1 ene` Año Nuevo · `1 mar` Héroes de la Patria · **Jueves y Viernes Santo** · `1 may` Día del
Trabajador · `14 y 15 may` Independencia Nacional · `12 jun` Paz del Chaco · `20 jun` Jura de la
Constitución · `15 ago` Fundación de Asunción · `29 set` Batalla de Boquerón · `8 dic` Virgen de
Caacupé · `25 dic` Navidad.

**Feriados móviles** (art. 2-3): solo **1 mar, 12 jun, 20 jun y 29 set** pueden ser **trasladados al
lunes** (anterior o siguiente) por **decreto anual** del Poder Ejecutivo. **Los demás NO se mueven.**

**Feriados adicionales** (art. 4): el Ejecutivo puede fijar por decreto **hasta 3 días** más por año.

**Asuetos** (art. 7): son **días hábiles** y **no** tienen efecto de feriado — **salvo** que un plazo
venza el día del asueto, en cuyo caso **el vencimiento se traslada al día hábil siguiente**.

> Esta ley **derogó el régimen anterior de feriados**: no citar las normas anteriores como vigentes.

---

## 4. Lo que se deriva a fuente oficial (no se afirma de antemano)

- **Traslado efectivo de un feriado móvil en un año concreto** → depende del **decreto anual** del PE.
  Hasta verlo, tratar la fecha base como referencia y marcar `[VERIFICAR VIGENCIA]` sobre el traslado.
- **Feriados adicionales del año** (los hasta 3 del art. 4) → por decreto; verificar.
- **Asuetos** → por decreto del PE; recordar que son hábiles salvo para el vencimiento que cae ese día.
- **Calendario fino de días hábiles, suspensiones y ferias extraordinarias del fuero** → **Acordadas
  Digitales (PJ/CSJ)**. El mapa marca `tasas_judiciales_y_plazos` como norma inestable. Usar la skill
  `fuentes-oficiales` para ubicarlas.

---

## 5. Datos mínimos que pide (sin estos, no se encuadra el plazo)

1. **Tipo de plazo:** procesal / sustantivo (caducidad o prescripción) / administrativo.
2. **Norma o acto que lo origina:** artículo, recurso, traslado, vista, intimación, etc.
3. **Fuero / materia:** civil-comercial (CPC, Ley 1337/1988) / laboral (Proc. Trabajo, Ley 742/1961) /
   administrativo / otro.
4. **Forma de cómputo:** días hábiles / corridos / meses / años (a confirmar contra la norma).
5. **Fecha de inicio del cómputo:** notificación, conocimiento del acto, o hecho que dispara el plazo.
6. **Instancia y circunscripción.**

Si falta alguno de estos datos determinantes → `[VACÍO FÁCTICO]` y pedirlo antes de seguir.

---

## 6. Salida

Ante una consulta de plazo, devolver:

1. **Encuadre:** tipo de plazo + norma probable que lo regula (del mapa). Primera mención normativa
   no verificada en sesión → `[VERIFICAR VIGENCIA]`.
2. **Inhábiles aplicables:** señalar si el período toca **enero** (feria) o **feriados nacionales** de
   la lista (sección 3), advirtiendo cuáles podrían estar **trasladados** ese año (a confirmar por decreto).
3. **Datos faltantes:** los de la sección 5 no aportados, como `[VACÍO FÁCTICO]`.
4. **Alerta de criticidad** si corresponde:
   `[ALERTA PLAZO FATAL] tipo — norma — inicio del cómputo — confirmar vencimiento contra fuente oficial`.
5. **Cómputo:** entregarlo **como estimación referencial**, nunca como fecha definitiva, indicando qué
   falta verificar (decreto de traslado del año, acordadas, código procesal) y derivando a `fuentes-oficiales`.

> `[ALERTA PLAZO FATAL]` es marcador interno de esta skill (señaliza criticidad), no una cita.

---

## 7. Disciplina (de `CLAUDE.base.md`)

- **No inventar** plazos ni reglas de cómputo (regla nº2). Lo verificado (feria de enero, lista de
  feriados) se afirma; lo coyuntural (traslados del año, asuetos, acordadas) se deriva.
- **No dar una fecha de vencimiento como cierta** sin confirmar código procesal + inhábiles del año.
- Ante riesgo de pérdida de derecho, **priorizar la advertencia** sobre la precisión.

---

## 8. Catálogo de plazos laborales (verificado)

Para el **fuero laboral** hay un catálogo de duraciones verificado contra fuente en
[`references/plazos-laborales-cpt.md`](references/plazos-laborales-cpt.md): plazos **procesales** del
Código Procesal del Trabajo (Ley 742/1961, arts. cotejados uno a uno contra el texto) y **sustantivos**
del Código del Trabajo (Ley 213/1993: caducidad art. 401, prescripciones arts. 399-400).

- Usá ese catálogo para dar la **duración legal** de un plazo laboral con su artículo (p. ej. contestar
  demanda = 6 días, art. 114; apelar = 3 días, art. 243; perención = 3 meses, art. 217).
- **La duración no es la fecha final.** Sobre esa duración se aplican los inhábiles (§2-4) y las reglas
  de cómputo del propio catálogo (días hábiles vs. corridos). En el **fuero laboral**, los días de
  notificación automática en Secretaría son **martes y jueves**; la regla operativa fue confirmada
  por el abogado responsable y por una providencia laboral actual aportada en sesión, que aplica
  expresamente el **art. 1 de la Ley 1110/1985** `[VERIFICAR VIGENCIA]`. La cautela subsiste solo
  hasta cotejar el texto de esa ley en fuente oficial.
- Para el fuero **civil/comercial**, el régimen general de cómputo del CPC está verificado en la
  sección 9. Para el administrativo todavía no hay catálogo cargado → encuadrar con la norma del
  fuero y `[VERIFICAR VIGENCIA]`.

---

## 9. Régimen de cómputo civil y comercial (CPC, Ley 1337/1988) — verificado

Cotejado artículo por artículo contra el texto consolidado local (consolidación 2026-04-03;
fila 2026-07-19 en `verification-log.md`):

- **Art. 145 — Carácter:** los plazos legales y judiciales son **perentorios e improrrogables**;
  fenecen **por su solo transcurso**, sin necesidad de petición de parte ni declaración judicial.
- **Art. 147 — Cómputo:** corren desde la **notificación** (si son comunes, desde la última); **no se
  computa el día de la diligencia ni los días inhábiles**. Plazos en horas: de momento a momento.
- **Art. 149 — Ampliación por distancia:** para diligencias dentro de la República y fuera del asiento
  del juzgado: **1 día por cada 50 km** (región Oriental) y **1 día por cada 25 km** (Occidental).
  Si tribunal y domicilio comparten asiento (p. ej. ambos en Asunción), **no hay ampliación**.
- **Art. 150 — Plazo de gracia:** el escrito se admite **hasta las 09:00 (nueve horas) del día hábil
  siguiente al último día del plazo**. Después, inadmisible. Es una red de seguridad, no un plan.

> ⚠️ **No confundir la gracia del art. 150 con institutos de otras jurisdicciones** (p. ej. las
> "dos primeras horas del despacho" del CPCCN argentino, art. 124 — **no rige en Paraguay**).

Ejemplo trabajado de este régimen aplicado al plazo de 9 días del art. 557 (acción de
inconstitucionalidad): `paraguay-litigacion` → skill `inconstitucionalidad`,
`references/vias-y-plazos.md`.

## 10. Evolución prevista

1. **v2 (laboral, hecho):** catálogo de duraciones del CPT + reglas de cómputo. Falta el cierre del
   cómputo de días hábiles integrando el decreto anual de traslados de feriados.
2. **v3 (civil, base hecha):** régimen general de cómputo del CPC verificado (sección 9). Pendientes:
   catálogo de duraciones civil/comercial por acto procesal, administrativo, y
   suspensiones/interrupciones y caducidad/prescripción por materia, contra acordadas CSJ
   registradas en `verification-log.md`.

---

## 11. Qué NO hace esta skill

- No afirma un vencimiento definitivo: entrega estimación referencial y deriva la confirmación.
- No conoce el traslado de feriados móviles de un año sin el decreto: lo marca como pendiente.
- No interpreta el fondo del recurso o acción: solo el encuadre temporal.
- No reemplaza el control del abogado sobre un plazo fatal: lo asiste y lo alerta.
