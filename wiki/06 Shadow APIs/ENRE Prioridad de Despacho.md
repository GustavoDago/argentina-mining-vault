---
type: shadow-api
tags: [reverse-engineering, energy, enre, enrge, grid, bess]
sources: [[ENRGE]], [[Cuello de Botella Electrico San Juan]], [[Renovables_y_BESS]], [[Oportunidades y Conexiones]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: ENRGE y Prioridad de Despacho (500kV)

El sistema de transmisión interconectado nacional (SADI) opera como un recurso saturado de asignación discrecional administrado por el nuevo organismo unificado.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Ente Nacional Regulador del Gas y la Electricidad (**ENRGE**, fusión formal de ENRE y ENARGAS), Secretaría de Energía (DNU 585/2026 de Prórroga de Emergencia Eléctrica) y CAMMESA.
- **Input Requerido:** Solicitud de prioridad de despacho y cupo de capacidad de transporte en nodos de 500kV (ej. Audiencia Pública Res. 219/2026 para la línea de 500kV San Juan - Rodeo).
- **Output Esperado:** `200 OK | Asignación de Prioridad de Despacho MATER` o resolución de acceso a capacidad firme.
- **Latencia Real:** Altamente volátil e impredecible (12 a 24 meses) debido a la parálisis burocrática por fusión de entes y disputas por cuotas de capacidad entre minas de cobre (ej. Los Azules vs. Josemaría / Distrito Vicuña en San Juan).

## Fricciones y Fallas (Error Codes)
- **`ERR_GRID_SATURATION`:** La capacidad física transformadora y de líneas de 500kV en Cuyo y NOA está al 100% de uso.
- **`ERR_MERGER_PARALYSIS`:** Demoras en la firma de resoluciones definitivas por vacantes y paritarias de personal tras la unificación en el ENRGE.
- **`ERR_LEGAL_INJUNCTION`:** Medidas cautelares ambientales o recursos de amparo judiciales presentados por competidores desplazados de la cola de despacho.

## Oportunidad de Abstracción (SFaaS / Virtual Power Plant)
**Bypass Regulatorio al SADI ("Virtual Power Plant & Energy Advisor"):**
- **Arquitectura:** Desarrollo de un software SaaS de orquestación de micro-redes híbridas descentralizadas (Solar Fotovoltaica + BESS a US$ 108/kWh + Generación a GNL/Diésel).
- **Funcionalidad:** En lugar de competir por prioridad de despacho ante el ENRGE, la plataforma vende "Garantía de Despacho Off-Grid" a las operadoras mineras.
- **Autonomía:** El motor predictivo monitorea las variables de frecuencia del SADI en tiempo real y conmuta automáticamente los salares o minas a modo *Island Mode* (autogeneración local) ante picos de demanda o caídas de tensión, blindando el cumplimiento de contratos de exportación sin depender del Ente Regulador.
