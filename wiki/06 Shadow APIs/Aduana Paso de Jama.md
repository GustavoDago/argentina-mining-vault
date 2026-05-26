---
type: shadow-api
tags: [reverse-engineering, logistics, customs, afip]
sources: [[2026-04-05_Evaluacion_Oportunidades_Tech]]
confidence: high
last_update: 2026-04-26
---

# Shadow API: Paso de Jama y Corredor Bioceánico

Este documento modela el cuello de botella logístico binacional como una interfaz a ser optimizada.

## Especificación del Proceso (Endpoint)
- **Input Requerido:** Trámites aduaneros (AFIP/Aduana de Chile), manifiestos de carga, pago de peajes.
- **Output Esperado:** Autorización de tránsito fronterizo para camiones pesados (litio, insumos).
- **Latencia Real:** Altamente asincrónica y bloqueante debido a infraestructura burocrática arcaica y falta de digitalización.

## Fricciones y Fallas (Error Codes)
- **Bloqueos Estatales:** Dependencia de decisiones gubernamentales binacionales (Argentina/Chile).
- **Arbitrio Sindical:** Fricciones insalvables con actores estatales y sindicatos de transporte que se benefician de la opacidad.
- **Cambio Normativo:** Un cambio de política en la AFIP o en la aduana chilena puede invalidar la arquitectura operativa.

## Oportunidad de Abstracción (SFaaS)
**Plataforma de Digitalización Logística Cross-Border B2B:**
Un backend que unifique trámites aduaneros, peajes y trazabilidad. Si se supera la fricción institucional, la plataforma se convierte en el peaje digital por defecto de las exportaciones mineras del NOA, procesando datos de tránsito para más de 7000 camiones anuales.

**Próximo Paso de Ejecución:**
Construir un MVP de monitoreo (solo lectura) usando hardware IoT para medir latencias reales, antes de intentar integración bidireccional, utilizando a una minera Tier 1 como cliente ancla.
