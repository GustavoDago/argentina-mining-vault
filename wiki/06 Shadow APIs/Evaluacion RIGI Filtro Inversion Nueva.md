---
type: shadow-api
tags: [reverse-engineering, regulatory, RIGI, lithium, mining]
sources: [[RIGI]], [[Litio]], [[raw/2026-07-13_news_mining_energy.md]], [[raw/2026-07-23_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Evaluación RIGI y Filtro de "Inversión Nueva" (Caso Mariana)

Modelo de ingeniería inversa sobre los criterios de la Unidad de Evaluación RIGI (UER) para la descalificación de activos preexistentes e inversiones hundidas.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Comité Evaluador del RIGI, Secretaría de Minería / Secretaría de Energía y Ministerio de Economía.
- **Input Requerido:** 
  - Solicitud de adhesión al RIGI con monto de inversión proyectado (mínimo US$ 200M).
  - Auditoría patrimonial y contable de activos preexistentes (*Audited Asset Baseline*).
  - Plan de ejecución físico-financiero que demuestre que el 100% de la inversión postulada corresponde a Capex "fresco" no ejecutado ni construido con anterioridad a la promulgación del RIGI.
- **Output Esperado:** `200 OK | Aprobación de Proyecto RIGI` (otorgado a 22 proyectos por US$ 51.221M).
- **Casos de Rechazo Notorio:** Proyecto de litio **Mariana (Ganfeng Lithium)** en Salta por US$ 273M, rechazado por el Comité Evaluador al detectarse que correspondía a una planta de cloruro de litio ya construida e inaugurada.
- **Latencia Real:** 90 a 150 días de escrutinio técnico contable antes del dictamen del Comité Evaluador.

## Fricciones y Fallas (Error Codes)
- **`ERR_SUNK_COST_DETECTED`:** El Comité Evaluador detecta que parte del Capex declarado corresponde a obras civiles ejecutadas previamente o infraestructura ya operativa.
- **`ERR_BROWNFIELD_AMBIGUITY`:** Imposibilidad de separar contablemente la inversión de expansión marginal (Brownfield) del activo base preexistente.
- **`ERR_VPU_INCORPORATION`:** Fallas en la estructuración de la Vehículo de Proyecto Único (VPU) al intentar transferir derechos mineros o concesiones anteriores sin neutralizar los pasivos contables.

## Oportunidad de Abstracción (SFaaS / RIGI Compliance)
**Software de Estructuración de VPU y Separación de Capex ("RIGI Greenfield Separator"):**
- **Arquitectura:** Middleware de modelado contable-financiero y auditoría de activos (*Smart VPU Architect*).
- **Funcionalidad:** Permite a empresas mineras y petroleras con proyectos Brownfield o expansiones (ej. Ganfeng, Arcadium, Posco) auditar su inventario físico preexistente antes de la presentación formal. El algoritmo re-estructura la presentación del VPU aislando la infraestructura heredada en un SPV operativo secundario e inyectando un plan de obras 100% Greenfield modular (ej. nuevas celdas de evaporación o plantas DLE independientes), garantizando que el `ERR_SUNK_COST_DETECTED` no se active.
- **Monetización:** Arancel de consultoría algorítmica previa + % del beneficio fiscal asegurado tras la aprobación.
