---
type: analysis
tags: [reverse-engineering, regulatory]
confidence: high
last_update: 2026-04-26
---

# Vector 06: Shadow APIs e Ingeniería Inversa de Procesos

Este vector de documentación está dedicado a mapear los procesos burocráticos y las deficiencias tecnológicas del Estado para convertirlos en especificaciones de interoperabilidad.

## Objetivo
Tratar la ineficiencia del Estado como una API rota. El propósito es documentar los inputs, outputs, puntos de falla humana, latencias asincrónicas y dependencias circulares de los trámites y regulaciones (ej. aprobaciones ambientales, aduanas, permisos provinciales).

## Criterios de Ingesta
Cada documento en este directorio debe seguir la lógica de un endpoint de software:
- **Input Requerido:** Qué documentos/datos pide el Estado.
- **Output Esperado:** Qué certificado/resolución entrega.
- **Latencia Real:** Tiempo SLA normativo vs. Tiempo de latencia en el mundo real.
- **Fallas (Error Codes):** Puntos donde el trámite se traba (fricciones, arbitrio humano).
- **Oportunidad de Abstracción:** Cómo automatizar o puentear esta deficiencia mediante software privado.

## Shadow APIs Documentadas
- [[Aprobacion RIGI Upstream Res 484-2026]]: Ingeniería del Cociente de Rentabilidad.
- [[Aduana Paso de Jama]]: Procesamiento de despachos en frontera.
- [[Convencion TIR Logistica Bioceanica]]: Interoperabilidad aduanera internacional.
- [[ENRE Prioridad de Despacho]]: Arbitraje de acceso a capacidad eléctrica.
- [[SIM San Juan Canon Minero]]: Automatización de cumplimiento provincial.
