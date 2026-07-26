---
type: shadow-api
tags: [reverse-engineering, energy, enre, grid]
sources: [[2026-04-10_Arbitraje_OffGrid_y_Servicios_Mendoza]], [[Oportunidades y Conexiones]]
confidence: high
last_update: 2026-04-26
---

# Shadow API: ENRE y Prioridad de Despacho (500kV)

El sistema interconectado nacional opera como un recurso compartido con asignación discrecional.

## Especificación del Proceso (Endpoint)
- **Input Requerido:** Solicitud de prioridad de despacho y capacidad de transporte eléctrico al ENRE.
- **Output Esperado:** Asignación de cuota de capacidad en la red de Extra Alta Tensión (ej. Resolución 079/2026).
- **Latencia Real:** Impredecible, sujeta a lobby político y plazos judiciales si hay disputas entre competidores (ej. Los Azules vs Distrito Vicuña).

## Fricciones y Fallas (Error Codes)
- **Discrecionalidad Regulatoria:** El sistema interconectado es un activo regido por decisiones políticas y cuellos de botella burocráticos.
- **Saturación Física:** La infraestructura de 500kV no soporta la demanda sumada de los megaproyectos en Cuyo/NOA.

## Oportunidad de Abstracción (SFaaS)
**Bypass al ENRE (Orquestación de Microgrids):**
Desarrollo de un backend de orquestación para micro-redes híbridas (Solar + Baterías + LNG-to-Power). El objetivo es operar con independencia total del ENRE, vendiendo "Seguridad de Despacho" en lugar de "energía".

**Próximo Paso de Ejecución:**
La capa de software debe gestionar el mix energético local y predecir fallos o bloqueos regulatorios en la red interconectada para activar el modo off-grid de forma automática, garantizando el cumplimiento de cuotas de exportación.
