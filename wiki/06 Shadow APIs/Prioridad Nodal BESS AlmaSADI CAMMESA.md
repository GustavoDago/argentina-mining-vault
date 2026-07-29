---
type: shadow-api
tags: [reverse-engineering, energy, bess, cammesa, mater, grid]
sources: [[Renovables_y_BESS]], [[ENRGE]], [[raw/2026-07-22_news_mining_energy.md]], [[raw/2026-07-23_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Prioridad Nodal BESS AlmaSADI (CAMMESA / MATER)

Modelo de ingeniería inversa sobre el algoritmo de adjudicación de capacidad y remuneración por potencia almacenada en sistemas BESS (Baterías) en nodos críticos del SADI sin offtaker estatal.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Compañía Administradora del Mercado Mayorista Eléctrico S.A. (**CAMMESA**), Secretaría de Energía (Res. SE 400/2025 y convocatorias AlmaGBA / AlmaSADI).
- **Input Requerido:** 
  - Oferta de potencia firme de almacenamiento en BESS (rango 10 MW a 100 MW por nodo crítico).
  - Certificación de tecnología de baterías de ion de litio con costo objetivo ≤ **US$ 108/kWh**.
  - Contrato bilateral PPA privado registrado en el MATER o esquema de remuneración por disponibilidad nodal (contrato a 15 años en US$/MW-mes).
- **Output Esperado:** `200 OK | Adjudicación de Capacidad Nodal BESS & Prioridad de Inyección MATER` (ej. 713 MW adjudicados en AlmaGBA y 700-770 MW en AlmaSADI a ~US$ 11.337/MW-mes).
- **Latencia Real:** 60 a 90 días por ronda de licitación y 18 meses para la puesta en marcha técnica comercial.

## Fricciones y Fallas (Error Codes)
- **`ERR_NODE_CONGESTION`:** El nodo SADI seleccionado (ej. Ezeiza, Abasto, Cuyo o Puna) supera el límite de cortocircuito o capacidad de transformación disponible.
- **`ERR_OFFTAKER_CREDIT_RISK`:** Al eliminarse la garantía de compra de CAMMESA (Res. SE 400/2025), la oferta es descalificada si el offtaker privado del MATER no acredita calificación crediticia Investment Grade.
- **`ERR_DEGRADATION_PENALTY`:** Penalizaciones por degradación de la capacidad de almacenamiento BESS por debajo del 80% del valor nominal contratado antes del año 5 de operación.

## Oportunidad de Abstracción (SFaaS / Storage Management System)
**SaaS de Orquestación y Bidding Nodal BESS ("BESS Node Optimizer"):**
- **Arquitectura:** Software de Gestión de Energía (EMS) impulsado por modelos predictivos de despacho y tarifas marginales locales de CAMMESA.
- **Funcionalidad:** Permite a generadores e inversores (ej. YPF Luz, Central Puerto, Genneia) simular ofertas de potencia en las licitaciones AlmaSADI. El algoritmo calcula la tasa de descarga óptima en horas pico (*arbitraje de precios marginales locacionales*) y automatiza la inyección para evitar el `ERR_DEGRADATION_PENALTY`.
- **Integración con Litio:** Conecta directamente los proyectos de litio en la Puna que despliegan microredes BESS off-grid con los beneficios impositivos sin piso de inversión del régimen [[RIMI]].
- **Monetización:** Cobrar una tarifa mensual SaaS por MW orquestado + % de ganancia por arbitraje tarifario en el MATER.
