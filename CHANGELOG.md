# Changelog

Todas las novedades relevantes de **Claude for Legal Paraguay** se registran en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [No publicado]

### Añadido

**Empaquetado — correcciones de instalación desde el marketplace (auditoría 2026-07-21)**
- **`shared/` ahora viaja con cada plugin instalado**: enlace simbólico `shared/` en la raíz de
  los 4 plugins apuntando a `../../shared`. Al instalar desde el marketplace, Claude Code
  dereferencia el enlace y copia el contenido (authority map, plantillas, glosario) dentro de la
  caché del plugin. Antes, un plugin instalado desde GitHub quedaba **sin el mapa de autoridad**
  (las referencias `shared/authorities/...` de las skills no resolvían fuera del clon del repo) —
  la falla era silenciosa y anulaba justamente el mecanismo de control de autoridad.
- **Dependencia del núcleo declarada**: `paraguay-laboral`, `paraguay-contratos` y
  `paraguay-litigacion` declaran `dependencies: ["paraguay-legal-core"]` en su `plugin.json`.
  Instalar un vertical instala (y habilita) el núcleo automáticamente; antes un usuario podía
  instalar solo el vertical y operar degradado sin advertencia.
- **Marca beta visible al instalar**: `paraguay-contratos` y `paraguay-litigacion` llevan
  `[BETA — evals pendientes]` en la descripción que el usuario ve en el marketplace y en el
  `plugin.json`, no solo en el README.

**Seguridad — guarda de datos sensibles para el repo público**
- `scripts/check_sensitive.py`: barrida del contenido staged (o de todo el árbol con `--all`)
  contra patrones estructurales de datos sensibles (RUC, CI, correos, teléfonos, rutas de
  usuario, expedientes, matrículas) más una lista privada de patrones en
  `.sensitive-patterns.local` (gitignoreada, nunca se versiona).
- Hook `pre-commit` versionado en `scripts/hooks/` (instalación:
  `python scripts/check_sensitive.py --install`).
- Método de trabajo documentado en `docs/seguridad-y-privacidad.md` §8: borrador fuera del
  repo, casos de eval **sintéticos primero**, anonimizar = sustituir **y** alterar, commit
  atómico revisado, mensajes de commit estériles, protocolo de incidente.

### Corregido

- **Versiones alineadas en 0.2.1 para los 4 plugins y el marketplace.** Con `version` declarado,
  Claude Code fija el plugin a ese string y los usuarios instalados solo reciben actualizaciones
  cuando cambia: dejar `paraguay-laboral`/`paraguay-contratos` en 0.1.0 habría dejado a los
  usuarios sin estas correcciones. Regla adoptada: **se bumpea la versión en cada release que
  toque el contenido del plugin**; la madurez se señala con la marca beta en la descripción, no
  congelando el número de versión.
- `metadata.pluginRoot` removido del `marketplace.json`: redundante (las entradas ya usan rutas
  completas `./plugins/...`).
- Versiones declaradas alineadas con la 0.2.0: `metadata.version` del marketplace y los
  `plugin.json` de `paraguay-legal-core` y `paraguay-litigacion` seguían en 0.1.0.
- Descripción de `paraguay-litigacion` actualizada: diagnóstico de escritos, incidentes/nulidades
  e inconstitucionalidad ya no son "fases siguientes", están implementadas y estables.

## [0.2.0] — 2026-07-19

Segunda versión: plugin de contratos implementado (evals pendientes: sus skills siguen en v0.1)
y MVP de litigación **completo** — las 5 skills de `paraguay-litigacion` entran como **estables**
con sus 7 evals corridos contra el plugin real (headless) y cada cita verificada contra fuente
primaria. Primera versión pública del repositorio (historial re-publicado desde un commit inicial
limpio; el detalle evolutivo previo vive en este CHANGELOG).

### Añadido

**MVP contratos — `paraguay-contratos`**
- Plugin de contratos civiles/comerciales paraguayos con 3 skills: `red-flags`,
  `revision-contractual` y `redaccion-contractual`.
- Redacción contractual con estructura canónica paraguaya, 4 plantillas base y QC obligatorio del
  propio borrador con `red-flags`.
- Sección opcional "Posiciones del estudio — contratos" en `legal.local.md.template`.
- Cláusula de mediación previa documentada como **opcional**: no se incluye por defecto.

**MVP litigación — `paraguay-litigacion`** (partes 1-4 de la fase 5)
- `escritos-judiciales`: base de todo escrito judicial paraguayo — estructura forense común,
  demanda/contestación/excepciones previas/reconvención del proceso ordinario (CPC), y las
  estructuras laborales **portadas** de la skill `escrito-laboral` (atribución Miguel Fernando
  Díaz, Apache-2.0), con la disciplina de no cruzar regímenes de excepciones entre fueros
  (art. 224 CPC ≠ art. 119 CPT ≠ art. 462 CPC ≠ arts. 356-357 CPT).
- `juicio-ejecutivo`: verificación del título (arts. 448-449), preparación de la vía (443-447),
  intimación/embargo, excepciones taxativas, sentencia de remate y cumplimiento; ejecuciones
  hipotecaria/prendaria/dar cosa mueble referenciadas; perfila ejecutante y ejecutado.
- `diagnostico-escritos`: extiende el `diagnostico` del núcleo con chequeo procesal formal por
  fuero/etapa, **matriz pretensión-elementos-prueba** con lista de vacíos como salida prioritaria,
  y **triage de escritos adversos** (tres relojes de plazo, mérito con escala cerrada, opciones
  con recomendación). Patrones del upstream `litigation-legal` y del fork argentino de
  Cristian Aboitiz (peticiones sin fundamento, alerta de plazo fatal, síntesis con veredicto).
- `incidentes-nulidades`: elección de vía (art. 117: incidente/recurso/acción autónoma 409),
  **test de viabilidad bloqueante** (especificidad, finalidad, trascendencia, protección,
  convalidación de 5 días, costo del art. 53) y trámite completo (arts. 180-191, 404-411).
- 4 evals nuevos en `evals/procesal/` (pagaré no protestado, contestación con excepciones,
  diagnóstico de demanda adversa, nulidad de notificación) — **pendientes de correr**.
- `inconstitucionalidad`: impugnación por excepción y por acción (CPC 538-564; Ley 609/1995
  con modificatorias 7307/2024 y 7615/2025 verificadas), test de admisibilidad bloqueante con
  salida cerrada (art. 12 Ley 609) y flujo desarrollado de la acción contra resoluciones
  judiciales. Criterio de admisibilidad de la Sala Constitucional
  (`admisibilidad_fundamentacion_concreta`) verificado contra el portal oficial CSJ;
  los rulings puntuales quedaron pendientes por OCR ilegible del N° de A.I.
- Ajustes de praxis a `inconstitucionalidad` (consulta constitucional 18.a, naturaleza cautelar
  de la suspensión 553, matiz 543, legitimación acreditada, supuestos de pleno y nota 137 in
  fine), calibrados con dos publicaciones del PJ verificadas contra fuente primaria;
  modificatorias 600/1995 y 4542/2011 cargadas al mapa.

**Authority map**
- `leyes.yaml`: 36 entradas (28 verificadas). CPC con las modificatorias que faltaban
  (Leyes 5330/2014, 6059/2018, 6979/2022 y 7424/2025) y anclajes verificados del proceso
  ordinario, el juicio ejecutivo completo (arts. 439-475, 501-502) y el régimen de nulidades
  (111-117, 180-191, 404-411) contra el texto consolidado local.
- `jurisprudencia.yaml`: 4 criterios nuevos verificados contra el texto completo de fallos
  reales de los Tribunales de Apelación (2024-2025): trascendencia de la nulidad de la ejecución,
  alcance e incompatibilidad de la inhabilidad de título, requisitos del pago documentado, y
  análisis de oficio de la nulidad en la Alzada. Se afirman como tendencia; carátulas pendientes
  de cotejo con PJ/CSJ antes de citar fallos puntuales.
- Hallazgos documentados en `verification-log.md`: epígrafe erróneo del art. 470 CPC en la copia
  local; **laguna de transcripción en el art. 114 inc. b** presente en dos copias del mismo
  linaje (lección: dos copias coincidentes no son verificación cruzada); los modelos de La Ley
  Paraguay se usan solo como contraste (copyright), sin cargar sus citas de jurisprudencia.

**Calidad — evals de litigación corridos (fase 5, parte 5, 2026-07-19)**
- Los 7 evals (4 procesales + 3 constitucionales) corridos en **headless real** (`claude -p` +
  `--plugin-dir` + `--agent`, workspace aislado con `--setting-sources project`, frontmatter del
  caso excluido del prompt, generación y evaluación separadas) y **aprobados 7/7** con cada cita
  verificada contra fuente primaria en disco. Las 5 skills de `paraguay-litigacion` pasan a
  **estables v0.2**. Streams JSONL guardados como evidencia auditable de skills invocadas,
  lecturas y denegaciones de permisos.
- **Cero jurisprudencia inventada y cero datos de verificación fabricados en 7/7**: toda
  afirmación de autoridad resultó trazable a `leyes.yaml` / `jurisprudencia.yaml` /
  `verification-log.md`.
- Skill `plazos` del núcleo: nueva sección con el **régimen de cómputo civil del CPC verificado**
  (art. 145 perentoriedad, 147 cómputo desde la notificación, 149 ampliación por distancia,
  150 gracia hasta las 09:00 del día hábil siguiente), con advertencia expresa contra el
  instituto argentino de las "dos primeras horas" (CPCCN art. 124).
- Skill `citacion`: nota de diseño — con el agente activo opera como **referencia, no como
  invocación** (verificado empíricamente en 8 corridas; las skills se seleccionan por tarea y
  citar es una propiedad de la salida). En superficies sin agente la disciplina se degrada y la
  mitigación real es activar el agente.

### Corregido

Correcciones detectadas al correr los evals de litigación contra el plugin real (detalle en
`PLAN-fase-5` y `verification-log.md`):
- **Agente `asistente-paraguay`: faltaba `Skill` en su allowlist de tools** — el agente prometía
  invocar las skills del núcleo y su propio frontmatter lo impedía (ninguna skill invocable, en
  headless y en interactivo). Detectado porque la corrida 1 respondió los 7 casos sin disparar
  una sola skill.
- **Renumeración en cascada de las reglas del núcleo** en 8 archivos: "regla nº 8" → **9**
  (diagnóstico previo) y "regla nº 9" → **10** (perfil patronal) — numeración vieja anterior a la
  inserción de `[ARGUMENTO SIN NORMA]` como regla 8.
- `juicio-ejecutivo`: **letras de inciso del art. 462 ancladas** (c = litispendencia; d = falsedad
  **o** inhabilidad — un mismo inciso; f = pago documentado), prevención del error de cita
  detectado en la corrida 3.
- **CPC art. 69: errata de transcripción "hechos ilícitos" → "hechos lícitos"** presente en el
  HTML de BACN y en la copia local (mismo linaje). Resuelta por cotejo convergente: escaneo
  oficial CSJ (OCR con patrón l→i sistemático), CPCCN argentino art. 60 (fuente de redacción),
  doctrina paraguaya independiente y paralelo del art. 235 inc. a. Detectada por el propio eval
  (el modelo citó "lícitos" contra la copia que decía "ilícitos"). Copia local corregida con nota
  de consolidación.
- Frontmatter de 4 evals: `citacion` removida de las skills esperadas (expectativa desalineada
  con el diseño: la disciplina de citación la impone el agente) y reformulada la frase-mandato
  "la cita pasa por la skill `citacion`" a descripción de la disciplina en 3 skills.

### Pendiente (fuera de v0.2)

- **Evals de contratos** (`evals/contratos/`, 8+1 casos diseñados): escribirlos, correrlos con
  el harness headless y recién entonces pasar las skills de `paraguay-contratos` a estables.
- Verificar las 2 entradas `draft` restantes del authority map (CPP, fuera de foco; Ley
  1110/1985, sin fuente oficial disponible — `[FUENTE OFICIAL PENDIENTE]`).
- Carátulas de los criterios de `jurisprudencia.yaml` contra PJ/CSJ (hoy se citan como
  tendencia, nunca como fallo puntual).
- Scripts previstos: `package_plugins.sh`, `validate_frontmatter.py`, `check_official_links.py`;
  CI que corra `validate_authorities.py` + `check_sensitive.py --all` en cada push.
- Publicación: visibilidad pública del repositorio y Release v0.2.0 en GitHub.

## [0.1.0] — 2026-06-30

Primera versión utilizable. Marketplace paraguayo propio (no fork injertado) con núcleo transversal, MVP laboral orientado a empleadores, authority map verificado contra fuente oficial y suite de evals corrida de punta a punta.

### Añadido

**Núcleo — `paraguay-legal-core`**
- `CLAUDE.base.md` con identidad de práctica paraguaya, 9 reglas inmodificables y gramática de autoridad (fuente / fecha / tipo / certeza).
- `legal.local.md.template` (datos del abogado fuera del repo, bloqueado por `.gitignore`).
- Glosario `terminologia-paraguay.md` verificado contra BACN.
- 5 skills del núcleo: `setup`, `diagnostico` (8 puntos, disparo previo a redactar), `citacion` (4 controles de autoridad), `fuentes-oficiales` (materia → portal + fallback de 3 capas), `plazos` (3 capas de inhábiles con su nivel de certeza).
- Agente autocontenido `asistente-paraguay` (reglas incrustadas por exigencia de plataforma; disparo automático del diagnóstico como regla, no como hook).

**MVP laboral — `paraguay-laboral`** (orientación patronal)
- 6 skills: `calculo-laboral` (motor: liquidación + horas extras art. 234 CT + descuento IPS 9%), `liquidaciones` (orquestación), `estrategias-empleador` (contingencia, 8 puntos), `dictamenes`, `despidos` (causales + procedimiento de práctica real anonimizado), más perfil patronal completo en el `README`.
- Integración (no duplicación) con las skills laborales preexistentes.

**Authority map — `shared/authorities/`**
- 5 YAML (`leyes`, `tribunales`, `fuentes-oficiales`, `normas-inestables`, `formatos-de-cita`) + `authority.schema.json` + `README` + `verification-log.md`.
- 26 entradas, **19 verificadas** contra BACN / `D:\LEGISLACION\normalizadas\` (incluye Código del Trabajo 213/1993, IPS, feriados Ley 7544/2025, REOP Decreto 1989/2024, Constitución 1992, protección de datos 7593/2025, Res. MTESS 195/2026 y 672/2024) y 5 en borrador.
- Ciclo de vida `draft → verified → deprecated`; una skill estable nunca cita una norma `draft` sin marcador.

**Seguridad y privacidad**
- `docs/seguridad-y-privacidad.md` (Ley N.º 7593/2025, anonimización obligatoria, advertencia ZDR para Skills/MCP) + `SECURITY.md` paraguayo.

**Calidad**
- 10 casos en `evals/laboral/` (5 despido + 3 negociación + 2 liquidación), todos anonimizados, con rúbrica de Obligatorios / Deseables / Ausentes esperados.
- **Los 10 evals corridos contra fuente primaria: 10/10 aprobados.**
- `scripts/validate_authorities.py` (4 reglas del authority map), probado en sentido positivo y negativo.

**Documentación**
- `README.md`, `QUICKSTART.md`, `LICENSE` (Apache-2.0) y `NOTICE` con atribución al upstream `anthropics/claude-for-legal` (patrón de diseño, no contenido).

### Corregido

Correcciones normativas detectadas al correr los evals contra fuente primaria (detalle en `verification-log.md`):
- **Régimen de comunicación de despido**: Decreto MTESS 8304/17 está **derogado** → vigente Decreto 1989/2024 + Res. MTESS 991/2024 (sistema REOP, salida en 30 días hábiles).
- **Caducidad de la falta**: corregida la cita en cascada (art. 401 CT, condonación; no art. 82) en ~12 archivos, preservando el art. 82 donde corresponde (improcedencia + complementaria).
- **Marcador `[ARGUMENTO SIN NORMA]`** incorporado al catálogo cerrado de `CLAUDE.base.md`.
- **Forma de la renuncia** anclada en art. 78 inc. b CT (no art. 84).
- **Divisor del salario hora** unificado en 8 (decisión conservadora del estudio, documentada).
- Criterio jurisprudencial verificado de la complementaria (art. 82, rango 1–2 meses).

### Seguridad
- Datos personales del abogado (firma, matrícula CSJ) y rutas de disco personales saneados fuera del repo versionado.

### Pendiente (fuera de v0.1)
- Plugins `paraguay-contratos` (MVP 2) y `paraguay-litigacion` (MVP 3, con eje constitucional).
- Verificar las 5 leyes `draft` restantes contra BACN.
- `plazos` con cómputo real (hoy esqueleto honesto).
- Empaquetado final como plugin y evaluación de conectores MCP (recordando que MCP no es ZDR).

[0.2.0]: https://github.com/dikaia-io/claude-for-legal-paraguay/releases/tag/v0.2.0
