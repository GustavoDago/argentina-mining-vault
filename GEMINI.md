# GEMINI.md - Constitución de la Wiki Compuesta

Este documento rige la operación del agente de IA dentro de este repositorio. **Obsidian es el IDE; el LLM es el programador; la Wiki es el código base.** El objetivo es la acumulación, refinamiento y compilación sistemática del conocimiento sobre minería y energía en Argentina.

## 1. Arquitectura del Repositorio

| Capa | Directorio | Propietario | Regla de Oro |
| :--- | :--- | :--- | :--- |
| **Raw Sources** | `raw/` | Humano | **INMUTABLE.** El agente solo lee. Prohibido escribir aquí. |
| **The Wiki** | `wiki/` | Agente IA | **ESPACIO DE SÍNTESIS.** El agente mantiene y evoluciona este grafo. |
| **The Schema** | Raíz (`/`) | Ambos | Define las reglas de gobernanza (`GEMINI.md`, `JULES_SCHEDULED_TASK.md`). |

### Estructura de la Wiki (`wiki/`)
- `01 Projects/`: Entidades específicas (Proyectos mineros, empresas, yacimientos).
- `02 Frameworks/`: Conceptos transversales, leyes, regímenes (ej. RIGI, Ley de Glaciares).
- `03 Analysis/`: Síntesis complejas, comparativas y respuestas de alto valor ("Filing Back").
- `04 Daily/`: Log cronológico de operaciones y reportes de progreso.

---

## 2. Estándares Técnicos Obligatorios

### YAML Frontmatter
Todas las páginas en `wiki/` (excepto diarios) DEBEN incluir el siguiente bloque:
```yaml
---
type: [project | framework | analysis | daily]
tags: [mining | energy | lithium | copper | oil-gas | regulatory]
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

### Protocolo de Ingesta (El Efecto Ripple)
Al procesar una nueva fuente en `raw/`:
1. **Extraer:** Identificar hitos, datos numéricos y entidades.
2. **Resumir:** Crear/actualizar la nota correspondiente en `wiki/04 Daily/` como reporte.
3. **Propagar:** Actualizar TODAS las notas relacionadas en `01 Projects` y `02 Frameworks`. Si se menciona un nuevo proyecto, crearlo.
4. **Indexar:** Asegurar que las nuevas notas estén conectadas al grafo principal.

### Protocolo de Consulta y "Filing Back"
Las respuestas complejas generadas durante la interacción no deben morir en el chat. Si una síntesis aporta valor estratégico o comparativo, el agente debe **"Filing Back"**: crear una nueva página en `wiki/03 Analysis/` con dicha información.

### Protocolo de Salud (Linting)
El agente debe identificar periódicamente:
- **Contradicciones:** Datos nuevos que chocan con registros anteriores.
- **Gaps:** Conceptos mencionados en `[[ ]]` que aún no tienen archivo (páginas fantasma).
- **Huérfanos:** Notas sin conexiones entrantes o salientes.

---

## 4. Trazabilidad y Control
- **Git:** Cada sesión de trabajo debe terminar con un commit descriptivo. No se deben "stagear" cambios sin revisión si el usuario lo solicita, pero se recomienda el versionado frecuente para auditoría.
- **Logs:** `wiki/04 Daily/` es el registro histórico de la evolución de la Wiki.
