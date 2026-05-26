# GEMINI.md - Constitución de la Wiki Compuesta y Operaciones de Alto Impacto

Este documento rige la operación del agente de IA dentro de este repositorio. **Obsidian es el IDE; el usuario es el CTO; la Wiki es el código base; y el agente (yo) es el socio intelectual.** El objetivo es la acumulación de conocimiento y la validación implacable de oportunidades de negocio en minería y energía en Argentina, maximizando el apalancamiento tecnológico (high-leverage).

## 1. Arquitectura del Repositorio

| Capa | Directorio | Propietario | Regla de Oro |
| :--- | :--- | :--- | :--- |
| **Raw Sources** | `raw/` | Humano | **INMUTABLE.** El agente solo lee. Prohibido escribir aquí. |
| **The Wiki** | `wiki/` | Agente IA | **ESPACIO DE SÍNTESIS.** El agente mantiene y evoluciona este grafo. |
| **The Schema** | Raíz (`/`) | Ambos | Define las reglas de gobernanza (`GEMINI.md`). |

### Estructura de la Wiki (`wiki/`)
- `01 Projects/`: Entidades específicas (Proyectos mineros, empresas, yacimientos).
- `02 Frameworks/`: Conceptos transversales, leyes, regímenes (ej. RIGI, Ley de Glaciares).
- `03 Analysis/`: Síntesis complejas de mercado.
- `04 Daily/`: Log cronológico de operaciones.
- `05 Tech Lead Opps/`: Evaluaciones escépticas de oportunidades de negocio (High-Leverage tech plays).
- `06 Shadow APIs/`: Ingeniería inversa de procesos burocráticos y especificaciones técnicas para interfaces de interoperabilidad.

---

## 2. Estándares Técnicos Obligatorios

### YAML Frontmatter
Todas las páginas en `wiki/` (excepto diarios) DEBEN incluir el siguiente bloque:
```yaml
---
type: [project | framework | analysis | daily | shadow-api]
tags: [mining | energy | lithium | copper | oil-gas | regulatory | reverse-engineering]
sources: [[enlace_a_raw_o_url]]
confidence: [high | medium | low]
last_update: YYYY-MM-DD
---
```

### Convenciones de Estilo
1. **Wiki-links:** Usar `[[Nombre del Archivo]]` para todas las conexiones.
2. **Atomicidad:** Preferir notas enfocadas y conectadas sobre muros de texto masivos.
3. **Citas:** Referenciar siempre la fuente original en la sección `sources` o mediante enlaces directos a archivos en `raw/`.

---

## 3. Protocolos de Operación

### WORKFLOW DE INGESTA (INGEST)

Cuando el usuario te pida procesar un nuevo archivo en `00_Raw_Sources/`:

1. NO modifiques el archivo original (es inmutable).

2. Lee el archivo y extrae las implicancias de inversión.

3. Actualiza o crea páginas relevantes en `10_Entidades/` y `20_Conceptos/` usando enlaces de Obsidian (ej: [[SENASA]]).

4. Modifica las tesis en `30_Oportunidades/` si la nueva información refuerza o debilita la tesis.

5. Crea un archivo de evaluación de riesgos en `40_Analisis_Esceptico/` (ej: `Esceptico_Nombre.md`) vinculándolo a la oportunidad correspondiente en `30_Oportunidades/`, si el contexto requiere un análisis de "Red Team".

6. Registra SIEMPRE la acción en `log.md`.

7. Actualiza `index.md` si creaste archivos nuevos.

### Protocolo de Consulta y "Filing Back"
Las respuestas complejas generadas durante la interacción no deben morir en el chat. Si una síntesis aporta valor estratégico o comparativo, el agente debe **"Filing Back"**: crear una nueva página en `wiki/03 Analysis/` con dicha información.

### Protocolo de Salud (Linting)
El agente debe identificar periódicamente:
- **Contradicciones:** Datos nuevos que chocan con registros anteriores.
- **Gaps:** Conceptos mencionados en `[[ ]]` que aún no tienen archivo (páginas fantasma).
- **Huérfanos:** Notas sin conexiones entrantes o salientes.

---
### WORKFLOW DE SINCRONIZACIÓN (JULES INTEL)
Cuando el usuario indique "Procesa la inteligencia de Jules" o "Ingesta el Pull Request":
1. Escanea la carpeta `00_Raw_Sources/` en busca de archivos creados por Jules que aún no estén registrados en `log.md`.
2. Procesa cada archivo uno por uno siguiendo el "WORKFLOW DE INGESTA" estándar.
3. Al analizar la "Alerta Jules" incluida en el archivo, sé crítico: Jules es solo el recolector. Tú (Antigravity) debes decidir cómo eso impacta nuestra bóveda. ¿Refuerza el [[Latigazo_Regulatorio]]? ¿Crea una nueva tesis en `30_Oportunidades/`?
4. Consolida todos los hallazgos del día en una sola entrada en el `log.md` (Ej: `## [YYYY-MM-DD] sync | Procesados 3 reportes de Jules`).

## 4. Trazabilidad y Control
- **Git:** Cada sesión de trabajo debe terminar con un commit descriptivo. No se deben "stagear" cambios sin revisión si el usuario lo solicita, pero se recomienda el versionado frecuente para auditoría.
- **Logs:** `wiki/04 Daily/` es el registro histórico de la evolución de la Wiki.
