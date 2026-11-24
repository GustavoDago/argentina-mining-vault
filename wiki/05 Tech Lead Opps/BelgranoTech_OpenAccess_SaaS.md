---
type: tech-lead-opp
tags: [logistics, railway, mining, lithium, open-access, saas, belgrano-cargas]
sources:
  - [[raw/2026-09-30_batch_news_mining_energy.md]]
  - [[raw/2026-09-01_news_mining_energy.md]]
  - [[raw/2026-09-03_news_mining_energy.md]]
  - [[raw/2026-11-03_news_mining_energy.md]]
  - [[raw/2026-11-24_news_mining_energy.md]]
confidence: high
last_update: 2026-11-24
---

# BelgranoTech — SaaS de Optimización Ferroviaria (Open Access)

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🔴 MUY ALTA (licitación 11/nov/2026).

## El Gatillo Factual

El **30 de septiembre de 2026**, el Ministerio de Economía emitió la **Resolución 1350/2026** convocando a Licitación Pública Nacional e Internacional para la concesión por **50 años** de las líneas ferroviarias General Belgrano, General San Martín y General Urquiza bajo modalidad **open access** (acceso abierto a la infraestructura por cualquier operador habilitado).

- **Período de consultas al pliego:** cerrado a finales de octubre de 2026.
- **Apertura de ofertas técnicas/económicas:** prorrogada del 11 de noviembre al **21 de diciembre de 2026** (con flexibilización de requisitos financieros para consorcios).
- **Condición clave:** Inclusión de beneficios RIGI para inversiones en modernización de vías y material rodante.

### Actualización Crítica (Noviembre 2026 — Res. 1984/2026)
1. **Reglamentación Open Access (Resolución 1984/2026, BO 16/11/2026):** Economía formalizó las reglas de acceso abierto: fija **30 días hábiles** para aprobar o rechazar solicitudes de acceso, **60 días corridos** para firmar el convenio, reserva de capacidad garantizada para inversores en vía y control sancionatorio de la **CNRT**, tipificando presunción de competencia desleal ante desvíos **>15%** en horarios preferenciales o **>10%** en peajes (ver [[Open Access Ferroviario Res 1984-2026 CNRT]]).
2. **Baja de Grupo México:** GMX desistió de participar al no concedérsele exclusividad de vía. Esto confirma que el concesionario final operará bajo acceso abierto estricto, requiriendo un árbitro tecnológico neutral para la asignación de capacidad.
3. **Adenda Obligatoria Ramal C-14:** Acuerdo Nación–Salta eliminó la optatividad de las obras en la traza andina. Las obras de rehabilitación del Ramal C-14 son ahora contractuales y vinculantes para el consorcio ganador (sumando esquemas internacionales para el C-15).
4. **Restricción Física Extrema:** El C-14 opera en vía única con pendientes pronunciadas (viaducto La Polvorilla, zig-zags). Un error en la asignación de slots o en los tiempos de retorno de material rodante genera parálisis total.

### Contexto Crítico
El litio del NOA (Salta, Jujuy, Catamarca) y el cobre de [[Taca Taca]] dependen estructuralmente de esta infraestructura para sus rutas de exportación hacia Antofagasta/Mejillones.

## El Play Tech

**Plataforma SaaS B2B** de gestión de capacidad ferroviaria y auditoría regulatoria en régimen open access:

### Módulo 1 — Slot Management
Sistema de reserva y subasta de slots de capacidad de transporte (wagons/tolvas) en tiempo real. Análogo a un GDS aéreo pero para trenes mineros: las operadoras de litio y cobre reservan capacidad con anticipación y el sistema optimiza el uso del material rodante.

### Módulo 2 — Routing & Interoperability  
Motor de optimización de rutas multimodal (tren + camión + puerto) para exportaciones de litio desde los salares del NOA (Paso de Jama, Sico, Susques) hasta Bahía Blanca / Rosario / Antofagasta. Integra restricciones físicas (pendientes, peso por eje, puentes).

### Módulo 3 — Auditoría Anti-Discriminación CNRT & SLA Tracker (Res. 1984/2026)
Módulo forense de cumplimiento normativo que monitorea los SLAs legales de **30 días hábiles** (respuesta) y **60 días corridos** (convenio), y detecta estadísticamente desvíos superiores al **15%** en horarios preferenciales o al **10%** en tarifas de peaje, generando evidencia auditable ante la CNRT y protegiendo la reserva de capacidad de inversores en vía.

### Módulo 4 — Compliance & Trazabilidad
Certificados de cadena de custodia (CoC) para litio de batería grado exportación + manifiestos de aduana digitalizados. Integración con el middleware eTIR para cruce de frontera automatizado. **Complementa y extiende [[Middleware_eTIR_Bioceanico]]**.

## Tech Stack
- Algoritmo de slot-allocation con restricciones físicas (MIP / CP-SAT)
- GIS ferroviario (OpenRailwayMap + datos concesionario)
- API AFIP/ARCA para manifiestos aduaneros y reporte regulatorio CNRT
- Integration Layer Open Access (estándar TAF-TSI europeo adaptado + reglas Res. 1984/2026)
- ERP Integration: SAP Ariba, Coupa (mismos que usan las operadoras mineras)

## Riesgo Crítico
Aunque la **Resolución 1984/2026** dio el marco normativo esperado, la **CNRT** carece hoy de telemetría unificada para auditar peajes y horarios en tiempo real, y la prórroga al **21 de diciembre de 2026** puede sufrir nuevas extensiones si los consorcios no cierran financiamiento.

## Apalancamiento Regulatorio
- Los proyectos bajo RIGI y los inversores en obras de vía tienen reserva de capacidad garantizada por la Res. 1984/2026 → el software que certifique esta prioridad y audite desvíos >15% / >10% se convierte en herramienta obligatoria para operadoras y concesionario.
- Potencial de calificación como software de alta tecnología bajo Súper RIGI (compre local).

## Próximo Movimiento
Presentar el diseño de arquitectura del módulo de slot allocation y del auditor anti-discriminación CNRT (Res. 1984/2026) a los consorcios oferentes antes de la nueva apertura del **21 de diciembre de 2026**, y a CAEM/Secretaría de Transporte.

---
**Backlinks:** [[Middleware_eTIR_Bioceanico]], [[AndesLogistics_Puna_Logistica]], [[Litio]], [[Taca Taca]], [[RIGI]], [[Belgrano Cargas]], [[Open Access Ferroviario Res 1984-2026 CNRT]].
