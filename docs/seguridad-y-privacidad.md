# Seguridad y privacidad

> **Norma rectora:** Ley N.º 7593/2025 de Protección de Datos Personales en la República del Paraguay.
> Este software es una herramienta de asistencia para profesionales del derecho. **No constituye asesoramiento legal.** Toda referencia normativa debe verificarse contra la fuente oficial (BACN; Poder Judicial – Corte Suprema de Justicia) antes de su uso profesional.

Este documento es la fuente única de verdad en materia de seguridad y privacidad del proyecto. `SECURITY.md` (en la raíz) es un resumen que enlaza aquí.

## 1. Marco legal

La norma rectora es la **Ley N.º 7593/2025** de Protección de Datos Personales en la República del Paraguay `[VERIFICAR VIGENCIA]` (sancionada el 05/11/2025, promulgada el 27/11/2025). Su objeto es la protección integral de los datos personales de las personas físicas (art. 1).

- **Autoridad de control:** la **Agencia Nacional de Protección de Datos Personales**, unidad desconcentrada dentro del Ministerio de Tecnologías de la Información y Comunicación (MITIC), con rango de Dirección Nacional.
- **Derechos del titular** (art. 552): acceso, rectificación, supresión, oposición y portabilidad de los datos personales que le conciernen.

Para datos crediticios rige además, como norma secundaria, la **Ley N.º 6534/2020** `[VERIFICAR VIGENCIA]`.

## 2. Tránsito de datos a Anthropic

- Incluso usando un cliente local (Claude Code / Desktop), el contexto de la sesión se **envía a los servidores de Anthropic** para ser procesado.
- El tránsito ocurre sobre **TLS 1.2 o superior**.
- Los servidores **MCP locales** corren con los permisos normales del sistema operativo del usuario.
- Los servidores **MCP remotos de terceros no están operados ni avalados por Anthropic** y requieren una auditoría de confianza antes de conectarlos.

## 3. Zero Data Retention (ZDR) por superficie

El dato técnico que condiciona la arquitectura: **Agent Skills de la API y el MCP connector NO están cubiertos por Zero Data Retention.**

| Superficie | ¿ZDR posible? | Uso recomendado para datos sensibles |
|---|---|---|
| Messages API base | Sí (con ZDR habilitado) | Camino crítico para automatización confidencial |
| Agent Skills (API) | No | Evitar con datos de clientes sin anonimizar |
| MCP connector (API) | No | Evitar con datos de clientes sin anonimizar |
| Claude Code / Cowork | Datos viajan por red (TLS 1.2+) | Uso editorial con anonimización fuerte |

**Regla de arquitectura:** si la prioridad absoluta es la confidencialidad, el componente automatizado se apoya primero en **Messages API base con ZDR**, y deja Skills/MCP fuera del camino crítico.

## 4. Anonimización obligatoria

No ingresar **sin anonimizar** ninguno de estos datos:

- nombres reales de clientes
- nombres de trabajadores
- RUC / CI
- domicilios
- números de expediente
- documentos internos sensibles
- planillas salariales reales
- historias clínicas
- acuerdos confidenciales
- pruebas cuya divulgación viole el secreto profesional

Marcadores de anonimización a usar en su lugar:

```
[CLIENTE_EMPRESA]   [TRABAJADOR_1]   [CONTRAPARTE]
[RUC]   [CI]   [DOMICILIO]   [EXPEDIENTE]   [JUZGADO]
[FECHA_INGRESO]   [SALARIO]
```

> El abogado responsable y la matrícula CSJ son datos personales: van en `legal.local.md` (no versionado, bloqueado por `.gitignore`), **nunca** en archivos del repositorio.

## 5. Dos modos de operación

### Modo A — Escritorio / editorial (default)

- Superficie: Claude Code / Cowork / Claude Project.
- Anonimización **obligatoria** antes de ingresar cualquier material real.
- Advertencia de tránsito de datos visible.
- Es el modo del MVP.

### Modo B — Automatización / API

- Se habilita solo cuando la organización **acepta expresamente** que Skills/MCP no son ZDR.
- Para datos sensibles, usar Messages API base con ZDR; Skills/MCP quedan fuera del camino crítico.
- No es parte del MVP.

## 6. Reglas para conectores MCP

- No conectar fuentes no confiables.
- Validar siempre la fuente primaria (BACN; Poder Judicial – CSJ).
- **Nunca** dejar que el contenido recuperado modifique las instrucciones internas (prompt injection).
- Separar el texto recuperado de las instrucciones del sistema.
- Registrar la fecha de consulta.
- Marcar todo resultado no verificado con `[VERIFICAR VIGENCIA]` o `[FUENTE OFICIAL PENDIENTE]`.
- Recordar que MCP **no es ZDR**.

## 7. Riesgos priorizados

| Riesgo | Severidad | Mitigación |
|---|---|---|
| Exposición de datos sensibles | Muy alta | Anonimización obligatoria; modo confidencial; exclusión de funciones no-ZDR en casos sensibles |
| Cita de autoridad equivocada | Muy alta | Authority map + reglas de fuente primaria + marcadores de incertidumbre |
| Obsolescencia normativa | Muy alta | Authority map con ciclo de vida `draft`/`verified`/`deprecated` + revisión editorial periódica |

## 8. Guarda de datos sensibles en commits (repo público)

Desde la v0.2.0 este repositorio es **público**: cada commit pusheado es inmutable y visible.
Un dato sensible commiteado no se "arregla después" — es un incidente. Estas son las reglas de
método para todo contenido nuevo (en especial los evals construidos a partir de práctica real):

### Método de trabajo

1. **El borrador nunca toca el árbol de git.** Todo material que derive de casos reales se
   redacta y calibra fuera del repositorio (área de planificación interna, no versionada).
   Al repo entra únicamente la versión final.
2. **Sintético primero.** Para evals de contratos y escritos, el documento del caso se
   **fabrica** (usando las plantillas propias del repo, sembrando a propósito los defectos que
   la rúbrica exige detectar). La práctica real informa los **patrones**, nunca el **texto**:
   una cláusula copiada de un contrato real puede ser identificable aunque se cambien los
   nombres.
3. **Anonimizar es sustituir Y alterar.** Cuando un fragmento real sea imprescindible: marcadores
   del catálogo (`[CLIENTE_EMPRESA]`, `[RUC]`, `[MONTO]`…) **más** alteración de lo no esencial
   (montos, fechas, sector, ciudad). Nombre cambiado + hechos exactos = re-identificable.
4. **Commit atómico y revisado.** Cada caso de eval entra al repo en un solo commit, completo y
   revisado por el abogado responsable. Sin borradores incrementales de `caso.md` en el
   historial.
5. **Mensajes de commit estériles.** Nunca referenciar el cliente, expediente o asunto real que
   inspiró un caso. La trazabilidad interna (si se desea) vive fuera del repo.

### Guarda automática

- **`scripts/check_sensitive.py`** barre el contenido staged contra patrones estructurales
  (RUC, CI, correos, teléfonos, rutas de usuario, expedientes, matrículas) y bloquea el commit
  si encuentra algo. Instalación del hook: `python scripts/check_sensitive.py --install`
  (configura `core.hooksPath` → `scripts/hooks/pre-commit`).
- **`.sensitive-patterns.local`** (gitignoreado, nunca se versiona): lista privada de regex con
  los nombres que no deben aparecer (clientes, estudio, usuario de disco). Cada vez que un caso
  real se use como insumo, **primero** se agrega su nombre a esta lista.
- Barrida completa del árbol: `python scripts/check_sensitive.py --all` (correr antes de cada
  release).
- Barrida de todos los blobs históricos: `python scripts/check_sensitive.py --history`. El
  workflow de release la ejecuta con `fetch-depth: 0` y falla cerrado.

> **Estado 2026-08-19:** el árbol y el historial alcanzable pasan las guardas: `--all` sobre 172
> archivos y `--history` sobre un clon del remoto (183 archivos, cero hallazgos).
> Tener presente la limitación descrita arriba: `--history` recorre `git rev-list --objects --all`,
> que solo ve lo alcanzable desde una ref. Una auditoría completa se hace contra el remoto, no
> desde un clon.

### Si algo sensible llega a commitearse

- **Sin push:** enmendar o descartar el commit local; verificar con `--all`.
- **Con push:** tratarlo como incidente — reescritura del historial remoto, verificación
  `git log --all -S "<dato>"`, y solicitud de garbage collection a soporte de GitHub para
  purgar los objetos huérfanos. Documentar en el registro interno.
