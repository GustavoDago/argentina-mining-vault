---
type: shadow-api
tags: [reverse-engineering, regulatory, oil-gas, RIGI]
sources: [[RIGI.md]], [[Vaca Muerta.md]]
confidence: high
last_update: 2026-04-27
---

# Shadow API: Aprobación RIGI Upstream (Resolución 484/2026)

Proceso de admisión de proyectos de hidrocarburos no convencionales bajo el esquema de rentabilidad ajustado.

## Especificación del Proceso (Endpoint)
- **Input Requerido:**
  - Plan de inversión mínimo de **US$ 200 millones**.
  - Modelo financiero que demuestre un ratio de rentabilidad ajustado (flujo de caja libre sobre inversión) que no supere el **35%** en los primeros 3 años.
  - Curva de declino técnico del yacimiento (tipo de pozo).
- **Output Esperado:** Resolución conjunta de la Secretaría de Energía y el Ministerio de Economía otorgando los beneficios del [[RIGI]] (estabilidad fiscal, arancel 0%, libre disponibilidad de divisas).
- **Latencia Real:** SLA normativo de 45 días hábiles; Latencia real observada de **120 a 180 días** debido a auditorías cruzadas de modelos financieros.

## Fricciones y Fallas (Error Codes)
- **`ERR_RATIO_EXCESS`:** El proyecto genera retornos rápidos (típico en pozos de alta productividad inicial de Vaca Muerta), superando el umbral del 35% y quedando descalificado.
- **`ERR_DECLINE_DISCREPANCY`:** La Secretaría de Energía rechaza la curva de declino presentada por considerarla artificialmente acelerada para encuadrar en el régimen.
- **`ERR_CAPEX_VALIDATION`:** Imposibilidad de validar la importación de bienes de capital específicos (sets de fractura) a valor de mercado.

## Oportunidades de Abstracción (SFaaS)
**Orquestador de Modelado Financiero RIGI (Algo-Compliance):**
Desarrollar un software propietario que simule los algoritmos de revisión de la Secretaría de Energía. El sistema permite a las operadoras (Vista, Pampa, Tecpetrol) "stress-testear" sus presentaciones, ajustando dinámicamente el ritmo de inversión (CAPEX) y la activación de pozos para garantizar que el ratio se mantenga en el umbral del 34.9%, optimizando la aprobación sin intervención humana discrecional.
