---
name: energon-intel
description: >-
  Ejecuta el ciclo completo de inteligencia, búsqueda web en vivo, ingesta y
  actualización de la bóveda de Minería y Energía en Argentina (Energon). Úsese
  cuando el usuario pida buscar noticias, correr la ronda de inteligencia,
  actualizar la bóveda del día o ejecutar el nuevo flujo de recolección con
  Antigravity.
---

# Skill: Ronda de Inteligencia y Síntesis de Alto Impacto (`energon-intel`)

Este procedimiento reemplaza al antiguo recolector asincrónico (Jules) por un flujo unificado e interactivo ejecutado íntegramente por **Antigravity**.

## Propósito Rector (North Star)
Operar como un **Radar de Oportunidades Tecnológicas B2B de Alto Apalancamiento (*High-Leverage Tech Plays*)**: detectar fricciones operativas, cuellos de botella logísticos/energéticos y procesos burocráticos reales en Minería y Energía (Oil & Gas) en Argentina para diseñar, refinar y someter a *Red Team* tesis de negocio en software (SaaS, Shadow APIs, RegTech, FinTech, IA/IoT).

---

## Paso 1: Investigación Web en Vivo (`search_web`) — Cero Simulación

1. **Verificación Temporal:** Antes de buscar, revisa la última entrada en [`log.md`](../../../log.md) y el último archivo en `raw/` para identificar la ventana temporal exacta que debes cubrir hasta la fecha actual.
2. **Regla de Veracidad Absoluta:**
   - Utiliza exclusivamente la herramienta `search_web` para obtener noticias, resoluciones y datos reales.
   - **Prohibido simular, extrapolar o inventar noticias.** Cada ítem recolectado debe incluir su URL real verificable y fecha de publicación.
   - Si en alguno de los 5 vectores no hubo novedades relevantes verificables en el período, decláralo explícitamente (*"Sin novedades de alto impacto verificadas en el período"*).
3. **Estrategia de Búsqueda Dual (Macro-Hitos + Dolor Operativo/Regulatorio):**
   Ejecuta búsquedas focalizadas sobre los 5 vectores troncales priorizando **resoluciones del Boletín Oficial, licitaciones, cuellos de botella de proveedores, multas, clausuras y fricciones normativas**:
   - **Vector 1 — Vaca Muerta & Oil/Gas:** Producción, etapas de fractura, oleoductos/gasoductos ([[VMOS]], Argentina LNG, Duplicar), logística de arenas/agua de producción y tensiones operadoras vs. PyMEs Tier 2/3 (FECENE, GAPP).
   - **Vector 2 — Cobre (San Juan, Salta, Mendoza):** [[Distrito Vicuña]] ([[Josemaría]], Filo del Sol, [[Lunahuasi]]), [[Los Azules]], [[Taca Taca]], [[El Pachón]], [[San Jorge]]; cuellos de botella logísticos de alta montaña, líneas de 500 kV y licencias ambientales (DIA/EIA).
   - **Vector 3 — Litio (NOA: Catamarca, Salta, Jujuy):** Proyectos activos y en construcción ([[Posco]], [[Tres Quebradas]], [[Cauchari-Olaroz]], [[Rincón]], Fénix, Mariana, [[Hombre Muerto Oeste]]); tecnologías DLE, balance hídrico y choques por leyes de compre y empleo local (REPEM / Regla 80/20).
   - **Vector 4 — RIGI & Marco Regulatorio:** Adhesiones y aprobaciones PEELP, operatoria aduanera ([[Aduana Green Channel]]), resoluciones de Economía/AFIP/CAMMESA/ENRE y conflictos de competencia Nación-Provincias.
   - **Vector 5 — Infraestructura & Corredor Bioceánico:** Licitación y concesión *Open Access* del Ferrocarril Belgrano Cargas (Ramal C-14), pasos fronterizos ([[Paso de Jama]], Sico), rutas críticas (RN 51, Ruta de las Arenas) y almacenamiento BESS/SADI.
4. **Fuentes Prioritarias:**
   `econojournal.com.ar`, `boletinoficial.gob.ar`, `panorama-minero.com`, `mase.lmneuquen.com`, `vacamuertanews.com`, `argenports.com`, `mineriaenergia.com`, `tiempodesanjuan.com`, `fuerzaminera.com`, `rumbominero.com`, y comunicados oficiales de operadoras (TSX/ASX/NYSE).

---

## Paso 2: Creación del Reporte Crudo en `raw/` (Append-Only)

1. Crea un archivo nuevo en `raw/YYYY-MM-DD_news_mining_energy.md` (usando la fecha real de la corrida).
2. Estructura cada hallazgo con:
   - **Titular y Fecha real de la noticia.**
   - **Fuente y enlace URL directo.**
   - **Síntesis fáctica y dolor operativo/regulatorio detectado.**
3. **Inmutabilidad:** `raw/` funciona en modo *Append-Only*. Una vez creado el archivo del día, queda inmutable para auditoría forense; jamás edites ni sobrescribas archivos previos dentro de `raw/`.

---

## Paso 3: Compilación y Propagación en `wiki/` (Efecto Ripple)

Propaga los hallazgos hacia el grafo de conocimiento respetando los estándares de [`GEMINI.md`](../../../GEMINI.md):

1. **Formato y Metadatos:**
   - Mantén el bloque YAML Frontmatter obligatorio (`type`, `tags`, `sources`, `confidence`, `last_update`).
   - Estandariza toda mención a dólares como `US$` (ej. `US$ 1.500 millones`) para evitar que pares de símbolos `$` disparen el renderizador LaTeX/MathJax de Obsidian.
   - Usa enlaces `[[Nombre de Nota]]` para fortalecer la densidad del grafo.
2. **Entidades y Marcos (`01 Projects/` y `02 Frameworks/`):**
   - Actualiza las páginas de proyectos, empresas, provincias y marcos regulatorios impactados por la evidencia nueva, agregando el archivo `[[raw/YYYY-MM-DD_news_mining_energy.md]]` en `sources` y actualizando `last_update`.
   - Si surge un actor o proyecto relevante que no existe aún, crea su nota atómica.
3. **Síntesis de Mercado (`03 Analysis/Oportunidades y Conexiones.md`):**
   - Actualiza las oportunidades destacadas y el diagrama `mermaid` para reflejar los nuevos hitos y relaciones de dependencia.
4. **Reporte Diario (`04 Daily/YYYY-MM-DD_Daily_Report.md`):**
   - Genera el informe ejecutivo diario cerrando obligatoriamente con la sección **Análisis Escéptico y Oportunidades (Tech Lead POV)** estructurada en los 5 puntos de [`Prompt escéptico.md`](../../../Prompt%20escéptico.md):
     1. **Idea central**
     2. **Trade-offs**
     3. **Riesgos críticos**
     4. **Efectos de segundo orden**
     5. **Próximo movimiento recomendado**

---

## Paso 4: Evolución de Tesis de Negocio (`05`, `06` y `07`) — Umbral de Calidad Estricto

1. **Por defecto (Refinamiento):** Si las noticias refuerzan, matizan o contradicen una tesis existente en `wiki/05 Tech Lead Opps/`, una especificación en `wiki/06 Shadow APIs/` o un análisis en `wiki/07 Analisis Esceptico/`, actualiza dicha página con la nueva evidencia empírica.
2. **Creación Selectiva (Solo ante Señal Fuerte):**
   - Crea una **nueva** nota en `05 Tech Lead Opps/`, `06 Shadow APIs/` o `07 Analisis Esceptico/` **únicamente** cuando la evidencia revele un cuello de botella operativo, resolución burocrática o falla de mercado inédita con verdadero potencial B2B *high-leverage*.
   - Si creas una nueva oportunidad en `05 Tech Lead Opps/`, regístrala también en [`wiki/05 Tech Lead Opps/00_Index_Tech_Lead_Opps.md`](../../../wiki/05%20Tech%20Lead%20Opps/00_Index_Tech_Lead_Opps.md).

---

## Paso 5: Indización, Trazabilidad y Cierre en Git

1. **Catálogo Maestro (`index.md`):** Agrega cualquier archivo nuevo creado en la corrida (incluyendo el `YYYY-MM-DD_Daily_Report`) en su sección correspondiente de [`index.md`](../../../index.md).
2. **Registro de Operaciones (`log.md`):**
   - Inserta en la parte superior de [`log.md`](../../../log.md) (debajo de `# Log de Operaciones`) la entrada consolidada:
     `## [YYYY-MM-DD] intel | Ronda de inteligencia Antigravity: <resumen ejecutivo>`
   - Verifica que el archivo se guarde en codificación UTF-8 limpia (sin caracteres nulos).
3. **Consolidación Git Automática:**
   - Revisa `git status` y `git diff --stat`.
   - Ejecuta `git add .`, realiza un commit descriptivo (`git commit -m "intel(vault): ronda de inteligencia YYYY-MM-DD - <hitos>"`) y sube los cambios a producción (`git push origin main`).
