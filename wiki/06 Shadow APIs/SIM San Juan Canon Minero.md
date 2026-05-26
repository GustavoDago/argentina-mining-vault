---
type: shadow-api
tags: [reverse-engineering, regulatory, compliance, san-juan]
sources: [[Oportunidades y Conexiones]]
confidence: high
last_update: 2026-04-26
---

# Shadow API: SIM San Juan (Canon Minero)

Proceso provincial en transición digital que ofrece oportunidad de integración B2B.

## Especificación del Proceso (Endpoint)
- **Input Requerido:** Presentación de comprobantes y datos de compliance para el pago del canon minero en San Juan.
- **Output Esperado:** Aprobación del pago y mantenimiento de la titularidad de la concesión minera.
- **Latencia Real:** Previamente manual; transicionando a tiempo real mediante el SIM (Sistema Integral Minero).

## Fricciones y Fallas (Error Codes)
- **Fricción Administrativa Legacy:** Históricamente, las concesiones se perdían por demoras en la actualización física de expedientes.
- **Adaptación al Sistema:** La fricción actual es la carga y actualización continua de datos por parte de las mineras en el nuevo portal.

## Oportunidad de Abstracción (SFaaS)
**Software de Compliance Minero Automatizado:**
Construir un conector privado que automatice la interacción con el SIM. La oportunidad reside en vender a las empresas un backend que gestione el compliance, programe pagos y genere alertas de vencimiento, abstrayendo la interacción manual con el portal provincial.
