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
