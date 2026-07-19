# Seguridad

Documento de fondo completo: [`docs/seguridad-y-privacidad.md`](docs/seguridad-y-privacidad.md).

## Reporte de vulnerabilidades

Si encontrás una vulnerabilidad de seguridad o una fuga de datos, **no abras un issue público.** Reportala de forma privada a través de **GitHub Security Advisories**: pestaña **Security** del repositorio → **Report a vulnerability**.

Los issues públicos quedan reservados para errores que no exponen datos ni vectores de ataque.

## Privacidad en 5 puntos

1. **Anonimización obligatoria.** No ingreses datos reales (nombres, RUC/CI, domicilios, expedientes, salarios) sin reemplazarlos por marcadores como `[CLIENTE_EMPRESA]`, `[TRABAJADOR_1]`, `[EXPEDIENTE]`. Incluso un cliente local envía el contexto a los servidores de Anthropic.
2. **Zero Data Retention no cubre todo.** Agent Skills (API) y MCP connector **no están cubiertos por ZDR**. Para datos sensibles, el camino crítico se apoya en Messages API base con ZDR.
3. **Marco legal.** La norma rectora es la **Ley N.º 7593/2025** de Protección de Datos Personales (Paraguay).
4. **Datos del abogado.** Firma y matrícula CSJ van solo en `legal.local.md` (no versionado, bloqueado por `.gitignore`), nunca en archivos del repositorio.
5. **Verificación de autoridad.** Toda referencia normativa se verifica contra la fuente oficial (BACN; Poder Judicial – CSJ) antes de su uso profesional.

## Alcance

Este software es una herramienta de asistencia para profesionales del derecho. **No constituye asesoramiento legal.**
