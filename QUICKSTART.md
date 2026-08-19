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

**Sin terminal, sin instalar nada.** Funciona incluso con la cuenta gratuita de claude.ai
(hasta 5 proyectos; el plan Pro se recomienda por capacidad).

1. Descargá [`paquete-claude-ai.zip`](https://github.com/dikaia-io/claude-for-legal-paraguay/releases/latest/download/paquete-claude-ai.zip)
   de la [última release](https://github.com/dikaia-io/claude-for-legal-paraguay/releases/latest).
2. Seguí los 5 pasos de la guía incluida (`LEEME-PRIMERO.md`, que es
   [`docs/instalacion-claude-ai.md`](docs/instalacion-claude-ai.md)): descomprimir → crear el
   Project → pegar `instrucciones-del-proyecto.md` → arrastrar `knowledge/` → primer mensaje
   `Configurá mi perfil`.
3. Tu perfil queda en `perfil-del-abogado.md` (Knowledge). Al actualizar el paquete, ese archivo
   **se conserva**; el resto se reemplaza (detalle en la guía, sección «¿Cómo actualizo?»).

> **Para desarrolladores:** el paquete lo construye el CI en cada release. Para generarlo local:
> `python scripts/build_project_knowledge.py --zip` (sale en `build/`).

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

Tras instalar, activá los plugins en la sesión y dejá las actualizaciones configuradas:

```bash
/reload-plugins            # activar en la sesión actual (o reiniciar Claude Code)
```

> **Actualizaciones:** para marketplaces de terceros como este, el auto-update viene
> **desactivado por defecto**. Activalo una vez: `/plugin` → **Marketplaces** →
> `claude-for-legal-paraguay` → **Enable auto-update**. Alternativa manual:
> `/plugin marketplace update claude-for-legal-paraguay` cuando quieras traer la última versión.

> **Instalación gráfica (sin comandos):** si usás Claude en el navegador o Cowork con plan pago,
> podés instalar sin terminal: **Customize → Plugins → Add marketplace** →
> `dikaia-io/claude-for-legal-paraguay` → instalar los plugins. *(Camino en validación: hasta
> confirmar que las reglas del núcleo gobiernan esa superficie, la vía recomendada sigue siendo
> la A o los comandos de Claude Code.)*

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
