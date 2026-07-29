---
type: analysis
tags: [reverse-engineering, regulatory]
confidence: high
last_update: 2026-07-23
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

## Shadow APIs Documentadas (9 Endpoints)
1. **[[Aprobacion RIGI Upstream Res 484-2026]]**: Ingeniería del Cociente de Rentabilidad Proyectada (CRP).
2. **[[Evaluacion RIGI Filtro Inversion Nueva]]**: Criterios de admisiibilidad y descalificación de activos preexistentes (Caso Mariana).
3. **[[Prioridad Nodal BESS AlmaSADI CAMMESA]]**: Algoritmo de adjudicación de almacenamiento en baterías BESS sin offtaker estatal.
4. **[[Compliance Compre Local REPEM Catamarca vs RIGI]]**: Arbitraje de compliance entre el 70% provincial (REPEM) y el 20% RIGI.
5. **[[Ventanilla Unica Importacion PyME Decretos 482-483]]**: Desgravación e importación agilizada de repuestos y equipos bajo RIMI.
6. **[[Aduana Paso de Jama]]**: Procesamiento de despachos en frontera andina e integración Sat-Edge.
7. **[[Convencion TIR Logistica Bioceanica]]**: Interoperabilidad aduanera internacional y pre-clearance eTIR.
8. **[[ENRE Prioridad de Despacho]]**: Arbitraje de acceso a capacidad eléctrica (ENRGE / SADI 500kV).
9. **[[SIM San Juan Canon Minero]]**: Automatización de cumplimiento de concesiones y cánones mineros provinciales.

