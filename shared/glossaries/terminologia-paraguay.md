# Terminología jurídica paraguaya

> **Propósito.** Normalizar el lenguaje jurídico paraguayo del asistente, evitar argentinismos y
> dar fórmulas de cita y denominaciones de órganos correctas.
>
> **Disciplina de fuentes.** Cada entrada lleva un estado:
> - ✅ **verificado** — confirmado contra fuente oficial (BACN / PJ-CSJ) en la fecha indicada.
> - 🟡 **draft** — proviene del mapa de autoridad o de uso común, sin confirmar; tratar con `[VERIFICAR VIGENCIA]`.
> - ⬜ **pendiente** — `[COMPLETAR con fuente]`, no usar de memoria.
>
> Las entradas ✅ de esta versión fueron verificadas vía el conector **Legal Data Hunter**
> (fuente `PY/BACN` y `PY/LeyesParaguayas`) el **2026-06-06**.

---

## 1. Órganos e instituciones

| Término | Denominación oficial | Estado |
|---|---|---|
| CSJ | Corte Suprema de Justicia | 🟡 draft |
| Sala Constitucional | Sala Constitucional de la Corte Suprema de Justicia (competencia de control de constitucionalidad, Ley N° 609/1995) | ✅ verificado (Ley 609/1995, 2026-06-06) |
| Sala Civil y Comercial | Sala Civil y Comercial de la CSJ | 🟡 draft |
| Sala Penal | Sala Penal de la CSJ | 🟡 draft |
| MTESS | Ministerio de Trabajo, Empleo y Seguridad Social | 🟡 draft |
| IPS | Instituto de Previsión Social (administra el seguro social; incluye el Fondo de Jubilaciones y Pensiones) | ✅ verificado (Ley 4933/2013, 2026-06-06) |
| DNIT | Dirección Nacional de Ingresos Tributarios | 🟡 draft |
| BACN | Biblioteca y Archivo Central del Congreso de la Nación (fuente oficial de legislación) | 🟡 draft |
| TSJE | Tribunal Superior de Justicia Electoral | ✅ verificado (fuente PY/TSJE, 2026-06-06) |
| Tribunales de Apelación | Tribunales de Apelación (por fuero y circunscripción) | 🟡 draft |
| Juzgados de Primera Instancia | Juzgados de Primera Instancia (por fuero y circunscripción) | 🟡 draft |
| Ministerio Público | Ministerio Público | 🟡 draft |

---

## 2. Normas base (con número y año verificados)

| Materia | Norma | Estado |
|---|---|---|
| Trabajo | **Ley N° 213** que establece el Código del Trabajo — promulgada **29-06-1993**, publicada 29-10-1993 (deroga el código anterior, Ley 729/1961) | ✅ verificado (BACN 2608, 2026-06-06) |
| Procesal civil | **Ley N° 1337/88** — Código Procesal Civil (con modificaciones: Ley 4419/2011 art. 409; Ley 4867/2013 art. 173) | ✅ verificado (BACN, 2026-06-06) |
| Organización CSJ | **Ley N° 609/1995** que organiza la Corte Suprema de Justicia (modificada por Ley 3986/2010 y Ley 7307/2024, art. 11 inc. a) | ✅ verificado (BACN 2333, 2026-06-06) |
| Estabilidad sindical | **Ley N° 1172/1985** — estabilidad en el trabajo del dirigente sindical | ✅ verificado (BACN 2611, 2026-06-06) |
| Protección de datos | **Ley N° 7593/2025** — Protección de Datos Personales | 🟡 draft (pendiente confirmar art. y vigencia) |

> El resto de las normas base (Constitución, Código Civil 1183, Código Penal 1160/1997, CPP 1286,
> Ley 6715, Ley 879) está en el mapa de autoridad en estado `draft`; ver `shared/authorities/leyes.yaml`.

---

## 3. Fórmulas de cita

| Tipo | Formato | Estado |
|---|---|---|
| Ley con artículo | `Ley N° {num}, art. {art}` | 🟡 draft |
| Ley con año | `Ley N° {num}/{año}` (p. ej. *Ley N° 1337/88*) | ✅ uso confirmado en fuentes BACN |
| Código del Trabajo | `Ley N° 213, art. {art}` (Código del Trabajo) | ✅ verificado |
| Acordada CSJ | `Acordada N° {num}/{año} CSJ` | ⬜ pendiente confirmar formato exacto |
| Jurisprudencia | `{tribunal}, "{carátula}", Ac. y Sent. N° {num}, {fecha}` | ⬜ pendiente confirmar formato exacto |

> "Ac. y Sent." (Acuerdo y Sentencia) es el formato de uso común; **confirmar contra fuente PJ/CSJ**
> antes de marcarlo ✅. Ver `shared/authorities/formatos-de-cita.yaml`.

---

## 4. Moneda y unidades

| Término | Uso | Estado |
|---|---|---|
| Guaraní (₲ / Gs.) | Moneda nacional; los montos en juicios se expresan en guaraníes | ✅ verificado (Ley 7614/2025, 2026-06-06) |
| Salario mínimo | Se ajusta por decreto; **verificar valor vigente** antes de toda liquidación | 🟡 norma inestable |
| Jornal mínimo | Unidad de referencia laboral; verificar valor vigente | ⬜ pendiente |

---

## 5. Lista negra de argentinismos (NO usar)

El asistente **no** debe usar estos términos/siglas argentinos. Si aparecen en un documento aportado,
señalarlos como ajenos a la jurisdicción paraguaya.

| Argentinismo | Por qué no aplica | Equivalente/criterio paraguayo |
|---|---|---|
| LCT (Ley de Contrato de Trabajo) | Norma argentina | Código del Trabajo (Ley N° 213) |
| CCCN (Código Civil y Comercial de la Nación) | Norma argentina | Código Civil (Ley N° 1183), separado del comercial |
| CPCCN / CPCCBA | Códigos procesales argentinos | Código Procesal Civil (Ley N° 1337/88) |
| CNAT (Cámara Nacional de Apelaciones del Trabajo) | Órgano argentino | Tribunales de Apelación del fuero laboral |
| SCBA / CSJN | Órganos argentinos | Corte Suprema de Justicia (Paraguay) |
| AAIP | Autoridad de datos argentina | Régimen de la Ley N° 7593/2025 (PY) |
| IGJ / ARCA / ARBA | Órganos argentinos | Organismos paraguayos según materia |
| Ley 25.326 | Datos personales (Argentina) | Ley N° 7593/2025 (Paraguay) |
| "fuero" como tribunal | Uso argentino ambiguo | Usar denominación paraguaya del órgano |

---

## 6. Cómo se mantiene este glosario

1. Toda entrada nueva nace en ⬜ pendiente o 🟡 draft.
2. Pasa a ✅ verificado solo tras confirmarse contra BACN / PJ-CSJ, anotando la fecha de consulta.
3. Las verificaciones contra fuente oficial se registran también en
   `shared/authorities/verification-log.md` cuando afectan normas del mapa de autoridad.
4. Este glosario es **complementario** al mapa de autoridad (`shared/authorities/`): los datos
   normativos estructurados viven allí; aquí vive la **terminología y el uso del lenguaje**.
