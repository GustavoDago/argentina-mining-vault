---
type: shadow-api
tags: [reverse-engineering, regulatory, oil-gas, RIGI]
sources: [[RIGI]], [[Vaca Muerta]], [[Pampa Energía]], [[Vista Energy]], [[raw/2026-07-23_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Aprobación RIGI Upstream (Resolución 484/2026)

Proceso de admisión de proyectos de hidrocarburos no convencionales bajo el esquema de rentabilidad ajustado y evaluación de la Unidad de Evaluación RIGI (UER).

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Unidad de Evaluación RIGI (UER) dependiente del Ministerio de Economía, con validación técnica de la Secretaría de Energía y el Comité Evaluador RIGI.
- **Input Requerido:**
  - Plan de inversión mínimo de **US$ 200 millones** (o **US$ 600 millones** según Decreto 105/2026 para esquemas upstream no convencionales).
  - Modelo financiero auditado que demuestre un **Cociente de Rentabilidad Proyectada (CRP)** que no supere el **35%** en los primeros 3 años (elevado desde 30% por Res. 484/2026).
  - **Curva de Declino Tipo:** Especificación técnica de la productividad por pozo (EUR - Estimated Ultimate Recovery) que justifique la necesidad de estabilidad fiscal ante el declino acelerado del shale.
- **Output Esperado:** `200 OK | Certificado de Adhesión RIGI` (otorgado a Proyectos clave como **Rincón de Aranda** de Pampa Energía por **US$ 4.521M** - Proyecto #22).
- **Latencia Real:** SLA normativo de 45 días hábiles; Latencia real observada de **120 a 180 días** debido a la verificación manual de las planillas de cálculo y auditorías de desembolsos iniciales por la UER.

## Fricciones y Fallas (Error Codes)
- **`ERR_RATIO_EXCESS`:** El proyecto genera retornos rápidos (típico en pozos de alta productividad inicial en Bajada del Palo o Añelo), superando el umbral del 35% y quedando descalificado.
- **`ERR_DECLINE_DISCREPANCY`:** La Secretaría de Energía rechaza la curva de declino presentada por considerarla artificialmente acelerada para encuadrar en el régimen.
- **`ERR_CAPEX_VALIDATION`:** Imposibilidad de validar la importación de bienes de capital específicos (sets de fractura o baterías de separación de 40.000 bpd como las solicitadas por Vista para Bandurria Norte por US$ 5.800M) a valor de mercado.

## Oportunidades de Abstracción (SFaaS)
**Orquestador de Modelado Financiero RIGI ("RIGI Fiscal Ledger"):**
Desarrollar un software propietario que actúe como un "Middleware de Simulación RIGI":
- **Funcionalidad:** Permite a las operadoras (Vista, Pampa, Tecpetrol, Pluspetrol) inyectar sus planes de perforación y obtener el CRP exacto que la UER validará mediante criptografía de prueba de cero conocimiento (ZKP).
- **Optimización:** El algoritmo sugiere retrasar la terminación de pozos (*D&C timing*) o acelerar compras de bienes de capital para inflar el CAPEX inicial, garantizando que el CRP caiga al **34.8%**. Esto transforma un proceso administrativo subjetivo en una optimización determinística de variables financieras.
- **Monetización:** Cobrar un % de la desgravación impositiva lograda mediante el "fit" algorítmico al RIGI.

