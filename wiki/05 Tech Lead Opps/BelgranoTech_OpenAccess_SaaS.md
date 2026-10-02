---
type: tech-lead-opp
tags: [logistics, railway, mining, lithium, open-access, saas, belgrano-cargas]
sources:
  - [[raw/2026-09-30_batch_news_mining_energy.md]]
  - [[raw/2026-09-01_news_mining_energy.md]]
  - [[raw/2026-09-03_news_mining_energy.md]]
confidence: high
last_update: 2026-10-02
---

# BelgranoTech — SaaS de Optimización Ferroviaria (Open Access)

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🔴 MUY ALTA (licitación 11/nov/2026).

## El Gatillo Factual

El **30 de septiembre de 2026**, el Ministerio de Economía emitió la **Resolución 1350/2026** convocando a Licitación Pública Nacional e Internacional para la concesión por **50 años** de las líneas ferroviarias General Belgrano, General San Martín y General Urquiza bajo modalidad **open access** (acceso abierto a la infraestructura por cualquier operador habilitado).

- **Período de consultas al pliego:** hasta el 28 de octubre de 2026.
- **Apertura de ofertas técnicas/económicas:** 11 de noviembre de 2026.
- **Condición clave:** Inclusión de beneficios RIGI para inversiones en modernización de vías y material rodante.

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
Analizar el pliego publicado (plazo hasta 28/oct) para verificar si se especifican APIs de acceso de terceros. Presentar PoC de slot management a CAEM y FAPM durante el período de consultas. Contactar al concesionario ganador en diciembre de 2026.

---
**Backlinks:** [[Middleware_eTIR_Bioceanico]], [[AndesLogistics_Puna_Logistica]], [[Litio]], [[Taca Taca]], [[RIGI]], [[Belgrano Cargas]].
