# Guía rápida de uso — Claude for Legal Paraguay

Cómo poner a trabajar el asistente jurídico paraguayo, sin ser técnico. Elegí la vía que te
quede más cómoda:

- **Vía A — Claude Project** (más simple, sin instalar nada): ideal para empezar hoy mismo en claude.ai.
- **Vía B — Plugin de Claude Code** (más integrada): si ya usás Claude Code en tu equipo.

> El asistente trabaja **solo bajo derecho paraguayo**. En laboral usa orientación **patronal**
> (empleadores); en contratos pregunta qué parte representás antes de revisar o redactar; en
> litigación pregunta tu posición procesal (actor/demandado, ejecutante/ejecutado) y **diagnostica
> antes de redactar**. No reemplaza tu criterio profesional: su salida es un **borrador** que vos
> revisás y firmás.

---

## Antes de empezar: una regla de oro

**Anonimizá los datos reales antes de pegarlos.** Aunque uses un cliente local, el contenido viaja a
los servidores de Anthropic. Reemplazá nombres, RUC, CI, domicilios y expedientes por marcadores:
`[CLIENTE_EMPRESA]`, `[TRABAJADOR_1]`, `[RUC]`, `[CI]`, `[EXPEDIENTE]`, etc.
(Marco legal: Ley N.º 7593/2025 de Protección de Datos. Ver el protocolo de seguridad en
`shared/templates/CLAUDE.base.md` §6.)

---

## Vía A — Usar como Claude Project (recomendada para empezar)

Un Claude Project tiene **dos lugares** para cargar contenido, y no son lo mismo:

| Dónde | Qué va | Para qué |
|---|---|---|
| **Instrucciones del proyecto** | `CLAUDE.base.md` + tu `legal.local.md` | Las **reglas** que el asistente sigue siempre. |
| **Knowledge** (archivos) | El authority map, el glosario y las skills | El **conocimiento** que consulta al trabajar. |

### Paso 1 — Tu perfil (`legal.local.md`)
1. Copiá `shared/templates/legal.local.md.template` a un archivo nuevo `legal.local.md`.
2. Completá los `[COMPLETAR]` (firma, matrícula CSJ, circunscripción, rol y posiciones opcionales).
3. Guardalo en tu carpeta privada. **Nunca lo subas a git** (contiene tus datos personales).

### Paso 2 — Crear el Project
En claude.ai → **Projects** → **Create project**. Nombre sugerido: `Legal Paraguay`.

### Paso 3 — Cargar las Instrucciones
En el campo **"Instrucciones del proyecto"**, pegá:
1. Todo el contenido de `shared/templates/CLAUDE.base.md`.
2. Un separador `---`.
3. Todo el contenido de tu `legal.local.md`.

### Paso 4 — Cargar el Knowledge
**No subas los archivos a mano.** Como todas las skills se llaman `SKILL.md`, colisionarían en el
Knowledge. Corré este script una vez y te deja todo listo en una carpeta:

```bash
# desde la raíz del repo
python scripts/build_project_knowledge.py
```

Genera `build/project-knowledge/` con el authority map, el glosario y las skills ya renombradas a
`SKILL-<nombre>.md`. **Arrastrá el contenido de esa carpeta al Knowledge** del Project.

> Este renombrado es **solo** una limitación del Knowledge de Claude Project (sube archivos planos).
> En la **Vía B (plugin)** no hace falta: ahí las skills se identifican por su carpeta, no por el
> nombre del archivo. Si usás el plugin, ignorá este paso.

### Paso 5 — Trabajar
Abrí una conversación en el Project y pedile lo que necesités (ver "Ejemplos" abajo).

---

## Vía B — Usar como plugin de Claude Code

Si usás Claude Code, instalá el marketplace **a nivel usuario** (no de proyecto, para que pueda leer
tus archivos de trabajo):

```bash
# agregar el marketplace (directo desde GitHub)
/plugin marketplace add dikaia-io/claude-for-legal-paraguay

# (alternativa: desde un clon local del repo)
/plugin marketplace add /ruta/a/claude-for-legal-paraguay

# instalar los plugins de práctica (cada uno declara su dependencia sobre el
# núcleo paraguay-legal-core, que se instala solo si falta)
/plugin install paraguay-laboral@claude-for-legal-paraguay
/plugin install paraguay-contratos@claude-for-legal-paraguay
/plugin install paraguay-litigacion@claude-for-legal-paraguay
```

> **Dónde queda `shared/` al instalar.** Cada plugin lleva en su raíz un enlace `shared/` al
> mapa de autoridad, las plantillas y el glosario. Al instalar desde el marketplace, Claude Code
> copia ese contenido dentro de cada plugin en la caché, así las referencias de las skills a
> `shared/authorities/...` resuelven igual que en el repo. `paraguay-contratos` está marcado
> **beta** hasta correr sus evals.

Para desarrollo/prueba de un solo plugin:
```bash
claude --plugin-dir ./plugins/paraguay-legal-core
/reload-plugins   # recargar tras editar skills
```

Las skills quedan disponibles con su nombre: `/paraguay-laboral:liquidaciones`,
`/paraguay-contratos:revision-contractual`, `/paraguay-contratos:redaccion-contractual`,
`/paraguay-legal-core:diagnostico`, etc. La primera vez, corré `/paraguay-legal-core:setup` para
generar tu `legal.local.md` por entrevista.

---

## Ejemplos de uso (qué pedirle)

El asistente está pensado para que le hables como a un colega. Algunos ejemplos:

**Calcular una liquidación:**
> "Calculá la liquidación de un [TRABAJADOR_1] despedido sin causa: ingresó el 01/02/2020, egresó el
> 30/06/2026, salario Gs. 6.000.000, sin preaviso, vacaciones no gozadas, aguinaldo impago."

→ Pide los datos que falten, aplica las escalas (preaviso/vacaciones/indemnización), descuenta el
**IPS 9%** y te da la liquidación neta. Si querés el monto en juicio, agregá "decime también cuánto
sería en juicio" (suma compensatoria y complementaria).

**Calcular horas extras:**
> "Cuánto le debo a un trabajador por 20 horas extras diurnas y 10 nocturnas, salario Gs. 3.000.000."

→ Aplica los recargos del art. 234 (50% / 30% / 100%) y te advierte si falta el registro de horas.

**Evaluar un despido:**
> "Quiero despedir a un empleado por faltas. Tengo un memo interno sin firma. ¿Me conviene?"

→ Evalúa causal, contemporaneidad y **prueba**; te advierte el riesgo de reclasificación y te da una
recomendación estratégica.

**Diagnóstico antes de redactar:**
> "Diagnosticá este borrador de contestación de demanda laboral: [pegás el texto anonimizado]."

→ Audita el escrito (argumentos sin norma, hechos no probados, citas a verificar) **antes** de tocarlo.

---

## Qué esperar (y qué no)

El asistente **sí**:
- Pide los datos faltantes en vez de inventarlos (`[VACÍO FÁCTICO]`, `[VACÍO PROBATORIO]`).
- Aplica el descuento IPS y los recargos correctos sin que se lo recuerdes.
- Advierte las obligaciones IPS/MTESS y las contingencias.
- Marca con `[VERIFICAR VIGENCIA]` toda norma que no esté confirmada contra la fuente oficial.

El asistente **no**:
- No inventa normas, plazos ni jurisprudencia: si no tiene fuente, lo dice (`[FUENTE OFICIAL PENDIENTE]`).
- No reemplaza tu firma profesional: entrega borradores para que vos revises y decidas.

> ¿Querés validar que funciona con casos concretos antes de usarlo en serio? Hay 10 casos de prueba
> con su rúbrica en `evals/laboral/`.
