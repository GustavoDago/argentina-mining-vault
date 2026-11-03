---
type: tech-lead-opp
tags: [logistics, railway, mining, lithium, open-access, saas, belgrano-cargas]
sources:
  - [[raw/2026-09-30_batch_news_mining_energy.md]]
  - [[raw/2026-09-01_news_mining_energy.md]]
  - [[raw/2026-09-03_news_mining_energy.md]]
  - [[raw/2026-11-03_news_mining_energy.md]]
confidence: high
last_update: 2026-11-03
---

# BelgranoTech — SaaS de Optimización Ferroviaria (Open Access)

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🔴 MUY ALTA (licitación 11/nov/2026).

## El Gatillo Factual

El **30 de septiembre de 2026**, el Ministerio de Economía emitió la **Resolución 1350/2026** convocando a Licitación Pública Nacional e Internacional para la concesión por **50 años** de las líneas ferroviarias General Belgrano, General San Martín y General Urquiza bajo modalidad **open access** (acceso abierto a la infraestructura por cualquier operador habilitado).

- **Período de consultas al pliego:** cerrado a finales de octubre de 2026.
- **Apertura de ofertas técnicas/económicas:** noviembre de 2026.
- **Condición clave:** Inclusión de beneficios RIGI para inversiones en modernización de vías y material rodante.

### Actualización Crítica (Noviembre 2026)
1. **Baja de Grupo México:** GMX desistió de participar al no concedérsele exclusividad de vía. Esto confirma que el concesionario final operará bajo acceso abierto estricto, requiriendo un árbitro tecnológico neutral para la asignación de capacidad.
2. **Adenda Obligatoria Ramal C-14:** Tras el reclamo de la Provincia de Salta y las mineras ([[Taca Taca]], litio), se eliminó la optatividad de las obras en la traza andina. Las obras de rehabilitación del Ramal C-14 son ahora contractuales y vinculantes para el consorcio ganador.
3. **Restricción Física Extrema:** El C-14 opera en vía única con pendientes pronunciadas (viaducto La Polvorilla, zig-zags). Un error en la asignación de slots o en los tiempos de retorno de material rodante genera parálisis total. El slot-management algorítmico es una necesidad física, no un lujo administrativo.

### Contexto Crítico
El litio del NOA (Salta, Jujuy, Catamarca) depende estructuralmente de esta infraestructura para sus rutas de exportación. Con 7 proyectos de salmueras en producción activa y al menos 12 más aprobados bajo RIGI, el Belgrano Cargas es el cuello de botella logístico definitivo del sector. La creciente dependencia ya fue alertada recurrentemente en el `raw/` desde septiembre de 2026 por CAEM, FAPM e incluso el BID.

## El Play Tech

**Plataforma SaaS B2B** de gestión de capacidad ferroviaria en régimen open access:

### Módulo 1 — Slot Management
Sistema de reserva y subasta de slots de capacidad de transporte (wagons/tolvas) en tiempo real. Análogo a un GDS aéreo pero para trenes mineros: las operadoras de litio y cobre reservan capacidad con anticipación y el sistema optimiza el uso del material rodante.

### Módulo 2 — Routing & Interoperability  
Motor de optimización de rutas multimodal (tren + camión + puerto) para exportaciones de litio desde los salares del NOA (Paso de Jama, Sico, Susques) hasta Bahía Blanca / Rosario. Integra restricciones físicas (pendientes, peso por eje, puentes).

### Módulo 3 — Compliance & Trazabilidad
Certificados de cadena de custodia (CoC) para litio de batería grado exportación + manifiestos de aduana digitalizados. Integración con el middleware eTIR para cruce de frontera automatizado. **Complementa y extiende [[Middleware_eTIR_Bioceanico]]**.

## Tech Stack
- Algoritmo de slot-allocation con restricciones físicas (MIP / CP-SAT)
- GIS ferroviario (OpenRailwayMap + datos concesionario)
- API AFIP/ARCA para manifiestos aduaneros
- Integration Layer Open Access (estándar TAF-TSI europeo adaptado)
- ERP Integration: SAP Ariba, Coupa (mismos que usan las operadoras mineras)

## Riesgo Crítico
El modelo open access es **inédito en Argentina**. El concesionario puede resistir activamente la digitalización del acceso de terceros para preservar poder de mercado. La regulación de acceso de terceros debe estar explícita en el pliego — si no lo está, la oportunidad se retrasa 2-3 años.

## Apalancamiento Regulatorio
- Los proyectos bajo RIGI tienen prioridad de despacho implícita → el software que certifique esta prioridad se convierte en herramienta obligatoria para las operadoras.
- Potencial de calificación como software de alta tecnología bajo Súper RIGI (compre local).

## Próximo Movimiento
Presentar el diseño de arquitectura del módulo de slot allocation y simulación de tráfico en vía única (Ramal C-14) a los 3 consorcios oferentes y a CAEM/Secretaría de Transporte. Posicionar el software no sólo como herramienta para el concesionario, sino como la plataforma que las mineras ([[Taca Taca]], Zijin, Posco, Rio Tinto) exigirán contractualmente para auditar la equidad de acceso y evitar abusos de posición dominante.

---
**Backlinks:** [[Middleware_eTIR_Bioceanico]], [[AndesLogistics_Puna_Logistica]], [[Litio]], [[Taca Taca]], [[RIGI]], [[Belgrano Cargas]].
