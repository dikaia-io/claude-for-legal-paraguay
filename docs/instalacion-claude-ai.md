# Instalá el asistente jurídico paraguayo en claude.ai (sin terminal)

> **Para quién:** abogados, sin necesidad de perfil técnico. **Tiempo estimado:** 15 minutos.
> **Necesitás:** una cuenta en [claude.ai](https://claude.ai) (la gratuita alcanza para empezar;
> el plan Pro se recomienda por capacidad) y un navegador.

## Los 5 pasos

1. **Descargá el paquete.** Abrí este enlace (siempre apunta a la última versión):
   <https://github.com/dikaia-io/claude-for-legal-paraguay/releases/latest/download/paquete-claude-ai.zip>
2. **Descomprimilo.** Clic derecho sobre `paquete-claude-ai.zip` → «Extraer todo…». Adentro vas a
   encontrar esta guía (`LEEME-PRIMERO.md`), `instrucciones-del-proyecto.md`, `manifiesto.json`,
   `LICENSE`, `NOTICE` y una carpeta `knowledge/`.
3. **Creá el Project.** En claude.ai → **Projects** → **Create project**. Nombre sugerido:
   `Legal Paraguay`.
4. **Pegá las instrucciones.** Abrí `instrucciones-del-proyecto.md` (doble clic: se abre con el
   Bloc de notas), seleccioná todo (Ctrl+A), copialo (Ctrl+C) y pegalo en el campo
   **Instructions / Instrucciones del proyecto**.
5. **Cargá el conocimiento.** Entrá a la carpeta `knowledge/`, seleccioná TODOS los archivos
   (Ctrl+A) y arrastralos juntos al área **Knowledge** del Project.

**Primer mensaje sugerido:** escribí `Configurá mi perfil`. El asistente te hace 4 preguntas
(abogado responsable, matrícula CSJ, circunscripción, rol predominante) y te entrega un archivo
`perfil-del-abogado.md` para que lo guardes y lo subas al Knowledge. Con eso queda personalizado.

## Regla de oro antes de usarlo

**Anonimizá los datos reales antes de pegarlos.** Todo lo que pegás viaja a los servidores de
Anthropic. Reemplazá nombres, RUC, CI, domicilios y expedientes por marcadores:
`[CLIENTE_EMPRESA]`, `[TRABAJADOR_1]`, `[RUC]`, `[CI]`, `[EXPEDIENTE]`. Marco legal: Ley
N.º 7593/2025 de Protección de Datos Personales. Detalle: `seguridad-y-privacidad.md` (está en
`knowledge/`).

## Materias incluidas y su estado

| Materia | Estado |
|---|---|
| Núcleo transversal (setup, diagnóstico, plazos, citación, fuentes) | ✅ estable |
| Laboral (orientación patronal) | ✅ estable |
| Litigación (escritos, ejecutivo, incidentes, inconstitucionalidad) | ✅ estable |
| Contratos (revisión, red flags, redacción) | ⚠️ **beta — evals pendientes**: sus skills llevan un banner de advertencia; verificá la salida con especial rigor |

## ¿Cómo actualizo a una versión nueva?

1. Volvé a descargar el paquete (mismo enlace del paso 1).
2. En el Project, reemplazá el contenido de **Instructions** por el nuevo
   `instrucciones-del-proyecto.md`.
3. En **Knowledge**, borrá los archivos del paquete anterior y arrastrá los nuevos de `knowledge/`.
4. **Conservá `perfil-del-abogado.md`** — es tu perfil, no viene en el paquete: no lo borres.

¿Qué versión tenés? Preguntale al asistente: «¿qué versión del paquete tenés?» (lee el sello al
pie de sus instrucciones).

## ¿Problemas?

Abrí un issue en <https://github.com/dikaia-io/claude-for-legal-paraguay/issues>, o pegá el
«instalador conversacional» (`docs/instalador-conversacional.md`) en cualquier chat de Claude
para que te guíe paso a paso.

---
Contrato de instalación v1 — si cambiás los pasos de este archivo, subí este número y actualizá
la landing y el prompt instalador (spec §10).
