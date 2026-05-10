---
type: shadow-api
tags: [reverse-engineering, regulatory, oil-gas, RIGI]
sources: [[RIGI.md]], [[Vaca Muerta.md]]
confidence: high
last_update: 2026-05-10
---

# Shadow API: Aprobación RIGI Upstream (Resolución 484/2026)

Proceso de admisión de proyectos de hidrocarburos no convencionales bajo el esquema de rentabilidad ajustado.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Unidad de Evaluación RIGI (UER) dependiente del Ministerio de Economía, con validación técnica de la Secretaría de Energía.
- **Input Requerido:**
  - Plan de inversión mínimo de **US$ 200 millones**.
  - Modelo financiero auditado que demuestre un **Cociente de Rentabilidad Proyectada (CRP)** que no supere el **35%** en los primeros 3 años (ajuste Res. 484/2026).
  - **Curva de Declino Tipo:** Especificación técnica de la productividad por pozo (EUR - Estimated Ultimate Recovery) que justifique la necesidad de estabilidad fiscal ante el declino acelerado (shale).
- **Output Esperado:** `200 OK | Certificado de Adhesión RIGI`.
- **Latencia Real:** SLA normativo de 45 días hábiles; Latencia real observada de **120 a 180 días** debido a la verificación manual de las planillas de cálculo por la UER.

## Fricciones y Fallas (Error Codes)
- **`ERR_RATIO_EXCESS`:** El proyecto genera retornos rápidos (típico en pozos de alta productividad inicial de Vaca Muerta), superando el umbral del 35% y quedando descalificado.
- **`ERR_DECLINE_DISCREPANCY`:** La Secretaría de Energía rechaza la curva de declino presentada por considerarla artificialmente acelerada para encuadrar en el régimen.
- **`ERR_CAPEX_VALIDATION`:** Imposibilidad de validar la importación de bienes de capital específicos (sets de fractura) a valor de mercado.

## Oportunidades de Abstracción (SFaaS)
**Orquestador de Modelado Financiero RIGI (Algo-Compliance):**
Desarrollar un software propietario que actúe como un "Middleware de Simulación RIGI". 
- **Funcionalidad:** Permite a las operadoras (Vista, Pampa, Tecpetrol) inyectar sus planes de perforación y obtener el CRP exacto que la UER validará.
- **Optimización:** El algoritmo sugiere retrasar la terminación de pozos (*D&C timing*) o acelerar compras de bienes de capital para inflar el CAPEX inicial, garantizando que el CRP caiga al **34.8%**. Esto transforma un proceso administrativo subjetivo en una optimización determinística de variables financieras.
- **Monetización:** Cobrar un % de la desgravación impositiva lograda mediante el "fit" algorítmico al RIGI.
