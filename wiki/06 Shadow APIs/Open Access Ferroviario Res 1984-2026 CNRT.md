---
type: shadow-api
tags: [reverse-engineering, regulatory, railway, open-access, belgrano-cargas, cnrt, mining]
sources: [[Corredor Bioceanico]], [[BelgranoTech_OpenAccess_SaaS]], [[raw/2026-11-24_news_mining_energy.md]]
confidence: high
last_update: 2026-11-24
---

# Shadow API: Open Access Ferroviario (Resolución 1984/2026 - CNRT)

Ingeniería inversa normativa y operacional de la **Resolución 1984/2026** del Ministerio de Economía (publicada en el Boletín Oficial el **16 de noviembre de 2026**), que reglamenta la modalidad de acceso abierto (*Open Access*) para el transporte ferroviario de cargas bajo la desintegración vertical del Decreto 67/2025.

---

## 1. Especificación del Proceso (Endpoint)

- **Autoridad Responsable (Backend):** Administrador de Infraestructura Ferroviaria (ADIF / Concesionario de Infraestructura) + **CNRT** (Comisión Nacional de Regulación del Transporte como autoridad fiscalizadora y sancionatoria).
- **Actores Consumidores (Clients):** Operadores ferroviarios habilitados, consorcios cargadores de litio/cobre ([[Taca Taca]], [[Litio]] NOA) y transportistas privados.
- **Input Requerido:**
  - Solicitud formal de acceso a capacidad de vía y asignación de horarios (*slots*).
  - Acreditación técnica de material rodante y tripulación habilitada ante CNRT.
  - En su caso, convenio aprobado de inversión en mejoras de vía (para activar reserva de capacidad).
- **SLAs Legales Obligatorios:**
  - `30 días hábiles`: Plazo máximo para que el administrador de infraestructura resuelva (apruebe o rechace fundadamente bajo criterios técnicos objetivos) la solicitud de acceso.
  - `60 días corridos`: Plazo máximo tras la aprobación para suscribir el convenio de circulación respectivo.
- **Servicios Incluidos en el Peaje Base:** Derecho de paso, acceso a patios ferroviarios 24 hs, armado de rutas y gestión de circulación. *(Servicios adicionales como combustible o reparaciones menores se negocian libremente).*
- **Output Esperado:** `200 OK | Convenio de Circulación Activo + Reserva de Slots & Tarifa de Peaje Auditada`.

---

## 2. Fricciones, Umbrales y Códigos de Error (Auditoria CNRT)

La Resolución 1984/2026 codifica umbrales cuantitativos explícitos para detectar prácticas anticompetitivas o discriminatorias:

- **`ERR_SLOT_DISCRIMINATION` (Umbral > 15%):** Presunción de competencia desleal cuando existan desvíos superiores al **15%** en la asignación de horarios preferenciales respecto de otros operadores en igualdad de condiciones técnicas.
- **`ERR_TOLL_DISCRIMINATION` (Umbral > 10%):** Presunción de trato comercial preferencial injustificado ante diferencias superiores al **10%** en el cobro de peajes de acceso.
- **`ERR_CAPACITY_FORFEITURE_BREACH`:** Violación de la reserva de capacidad garantizada a concesionarios/operadores que ejecutaron obras de mejora en ramales bajo acuerdos avalados por el Estado (blindaje frente a acusaciones de subutilización).
- **`ERR_SILENT_DENIAL`:** Incumplimiento del SLA de 30 días hábiles o rechazo sin respaldo técnico objetivo verificable.

---

## 3. Oportunidad de Abstracción (SFaaS / Clearing Neutral)

La transición del papel al cumplimiento real de la Res. 1984/2026 convierte a la CNRT en árbitro de disputas de peajes y horarios sin herramientas de telemetría unificada:
- **Middleware de Auditoría Anti-Discriminación ([[BelgranoTech_OpenAccess_SaaS]]):** Motor de asignación de slots determinista en vía única (crítico para el **Ramal C-14** en Salta) con registro inmutable de solicitudes, tiempos de respuesta (30/60 días), cálculo transparente de peajes y alertas automáticas ante desvíos cercanos a los umbrales del 15% (horarios) y 10% (tarifas), generando evidencia audit-ready para reclamos o descargos ante la CNRT.

---
**Backlinks:** [[BelgranoTech_OpenAccess_SaaS]], [[Corredor Bioceanico]], [[Taca Taca]], [[Litio]], [[Cobre]].
