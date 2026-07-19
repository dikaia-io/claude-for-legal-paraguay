---
name: escritos-judiciales
description: Genera y estructura escritos judiciales paraguayos (demandas, contestaciones, excepciones, reconvención e interrogatorios) para los fueros civil, comercial y laboral, conforme al CPC (Ley 1337/1988) y al CPT (Ley 742/1961)
---

# Skill · Escritos judiciales (Paraguay)

> **Origen y atribución.** El núcleo laboral de esta skill fue **portado** de la skill `escrito-laboral`
> de Miguel Fernando Díaz e incorporado al repositorio bajo Apache-2.0, generalizado aquí como base de
> todo escrito judicial. Las normas citadas están `verified` en `shared/authorities/leyes.yaml`
> (`codigo_procesal_civil`, `codigo_procesal_trabajo`, `codigo_trabajo`, `codigo_civil`).
>
> **Disciplina aplicada.** Antes de **modificar** un escrito existente, corre el diagnóstico previo de
> la skill `diagnostico` del núcleo (regla nº 9). Toda cita normativa aplica la disciplina de
> citación del núcleo: gramática de autoridad (fuente/fecha/tipo/certeza) y plantillas de
> `shared/authorities/formatos-de-cita.yaml` (referencia completa: skill `citacion`).
> Jurisprudencia sin fuente PJ/CSJ verificada → `[INSERTAR JURISPRUDENCIA VERIFICADA]`.

## Flujo de trabajo

1. **Identificar fuero y tipo de escrito.** Civil/comercial (CPC) o laboral (CPT). Si es una etapa del
   juicio ejecutivo → derivar a la skill `juicio-ejecutivo` de este plugin.
2. **Datos del abogado.** Tomarlos de `legal.local.md` (nombre, matrícula C.S.J., domicilio procesal).
   Si no existe, pedirlos; **nunca** inventarlos ni dejarlos en blanco silencioso.
3. **Datos de las partes.** Cliente (nombre, C.I./RUC, domicilio real) y contraparte. Si el usuario
   pega material de un caso real, verificar que esté anonimizado antes de procesar.
4. **Datos del caso.** Según tipo de escrito (ver secciones). Todo dato determinante faltante →
   `[VACÍO FÁCTICO]`; afirmación sin respaldo documental → `[VACÍO PROBATORIO]`.
5. **Generar el escrito** con la estructura del fuero correspondiente y guardarlo con nombre
   descriptivo (p. ej. `demanda ordinaria [cliente].docx`), usando el script de conversión del
   proyecto si existe.

## Estructura forense común (todo escrito paraguayo)

```
JUICIO: "[ACTOR] C/ [DEMANDADO] S/ [OBJETO]"        ← solo si el juicio ya está caratulado

OBJETO: [VERBO EN INFINITIVO + PRETENSIÓN].          ← p. ej. PROMOVER DEMANDA ORDINARIA...

SEÑOR/A JUEZ/A [fuero, si se estila]:

[NOMBRE ABOGADO], Abogado/a (Mat. C.S.J. N° [MATRÍCULA]), en representación de [PARTE],
conforme [carta poder que adjunto / personería ya acreditada en autos], con domicilio real
en [DOMICILIO REAL] y constituyendo domicilio procesal en [DOMICILIO PROCESAL], a V.S.
respetuosamente digo:

[CUERPO: hechos → derecho → prueba, según el tipo de escrito]

PETITORIO: Por lo expuesto, a V.S. solicito:
1. Tener por reconocida mi personería y por constituido el domicilio procesal.
2. [Pretensión principal del escrito.]
3. [Pretensiones accesorias: intereses, costas...]  Protesto costas.

PROVEER DE CONFORMIDAD, SERÁ JUSTICIA.
```

Convenciones: lenguaje formal forense, montos en guaraníes con letras y cifras, fechas completas,
cada documento ofrecido se individualiza. Primera mención normativa relevante → gramática de
autoridad de la skill `citacion`.

## Fuero civil y comercial (proceso de conocimiento ordinario)

Etapas, plazos y artículos verificados: ver `references/proceso-ordinario.md`.

### Demanda (art. 215 CPC)
Contenido obligatorio: **a)** nombre y domicilio real del demandante; **b)** ídem del demandado;
**c)** designación precisa de lo que se demanda; **d)** los hechos en que se funde, explicados
claramente; **e)** el derecho expuesto sucintamente; **f)** petición en términos claros y positivos.
Debe precisar el **monto reclamado** (salvo las excepciones del propio art. 215, 2º párrafo).
La **prueba documental** en poder del actor se acompaña con la demanda; la que no tenga a
disposición se individualiza (art. 219 CPC). El juez puede rechazar de oficio la demanda defectuosa
(art. 216) y el actor puede modificarla antes de la notificación (art. 217).

### Contestación (arts. 234-235 CPC)
Plazo: **18 días** desde la notificación del traslado (arts. 222 y 234). Cargas del art. 235:
reconocer o **negar categóricamente cada hecho**, la autenticidad de los documentos atribuidos y la
recepción de cartas/telegramas (el silencio o la negativa general puede estimarse reconocimiento);
especificar los hechos de la defensa; observar los requisitos del art. 215 en lo pertinente.
En la contestación se oponen todas las defensas no previas (art. 233: medios generales de defensa).

### Excepciones previas (arts. 223-224 CPC)
Se oponen **en un solo escrito, dentro del plazo para contestar**, y su oposición **interrumpe** el
plazo de contestación (art. 223). Lista taxativa del art. 224: incompetencia; falta de personería;
falta de acción manifiesta; litispendencia; defecto legal; cosa juzgada; pago, transacción,
conciliación, desistimiento de la acción y prescripción (cuando puedan resolverse como de puro
derecho); convenio arbitral; arraigo; defensas temporarias. Con el escrito se agrega toda la prueba
documental (art. 227; traslado por 6 días). Las de los incs. d), f), g) y h) exigen documental o
indicación del expediente (art. 228).

### Reconvención (arts. 237-240 CPC)
Solo en el escrito de contestación, en la forma prescripta para la demanda (art. 237). Requisitos
del art. 238: competencia del mismo juez, conexidad con la relación jurídica de la demanda, y que el
proceso sea de conocimiento ordinario. No hay reconvención de la reconvención (art. 239).

## Fuero laboral

Estructuras completas portadas de `escrito-laboral` (demanda, contestación, interrogatorio de
testigos): ver `references/escritos-laborales.md`. Reglas que **nunca** se cruzan de fuero:

| Etapa | Civil/comercial | Laboral |
|---|---|---|
| Excepciones en conocimiento | Art. 224 CPC (lista amplia, incl. arraigo y convenio arbitral) | **Art. 119 CPT, taxativo**: incompetencia, falta de personería, litis pendencia, cosa juzgada, transacción, prescripción. **No existe** la excepción de pago: el pago es defensa de fondo |
| Excepciones en ejecución | Art. 462 CPC (ver skill `juicio-ejecutivo`) | **Arts. 356-357 CPT**: pago total posterior al título documentado, prescripción; nulidad por vicios (excepción hasta la citación de remate, incidente después) |
| Plazo contestación | 18 días (art. 234 CPC) | Según CPT; verificar en `plazos` del núcleo |

## Qué NO hace esta skill

- No calcula liquidaciones (motor `calculo-laboral` del plugin `paraguay-laboral`).
- No tramita el juicio ejecutivo civil (skill `juicio-ejecutivo` de este plugin).
- No inventa jurisprudencia, acordadas ni artículos: si un dato procesal no está verificado en el
  authority map ni en fuente primaria en sesión → `[VERIFICAR VIGENCIA]` o `[FUENTE OFICIAL PENDIENTE]`.
