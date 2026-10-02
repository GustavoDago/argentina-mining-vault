---
type: tech-lead-opp
tags: [energy, ai, data-centers, patagonia, gas, ppa, stargate, infrastructure]
sources:
  - [[raw/2026-07-11_news_mining_energy.md]]
  - [[raw/2026-08-16_news_mining_energy.md]]
  - [[wiki/01 Projects/Stargate Argentina.md]]
  - [[wiki/03 Analysis/Demanda Energetica de Data Centers e IA.md]]
confidence: medium
last_update: 2026-10-02
---

# Stargate-Infra — Stack de Infraestructura Tech para Data Centers de IA en Patagonia

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🟠 ALTA (pero con riesgo de materialización de Stargate).

## El Gatillo Factual

**Stargate Argentina** (OpenAI + Sur Energy) anunció un proyecto de US$ 25.000 millones para un data center de IA en la Patagonia, presentado bajo RIGI como Proyecto de Exportación Estratégica de Largo Plazo (PEELP). Demanda de **500 MW** de energía.

El **Midstream & Gas Day 2026** validó el cruce de agendas: los data centers son el nuevo vector de demanda de gas natural de [[Vaca Muerta]], dado que requieren energía **firme 24/7/365** — exactamente lo que no pueden dar solar y eólico, pero sí puede el gas de la cuenca neuquina.

**Señal adicional (agosto 2026):** La presión de EEUU sobre CALF por su contrato con Huawei indica que los data centers de IA en Argentina deberán usar **hardware de networking no-Huawei** → oportunidad de integración con proveedores americanos (Cisco, Juniper, NVIDIA).

## Diferencial del Play

No competir con Stargate ni con los grandes integradores globales (Equinix, Digital Bridge). El play es ser el **Tier-1 supplier stack local** especializado en tres brechas estructurales que ningún actor global puede llenar sin conocimiento del mercado argentino:

## El Play Tech

### Módulo A — Energy PPA Brokering Platform
Los data centers necesitan contratos PPA (Power Purchase Agreements) de **10-15 años a precio fijo en USD**. El mercado eléctrico argentino nunca ha estructurado este tipo de contratos para este sector.

Plataforma de matching y estructuración contractual entre:
- **Compradores:** Operadores de data centers (Stargate, futuros actores)
- **Vendedores:** Generadores de gas de [[Vaca Muerta]] (YPF, Tecpetrol, Central Puerto) y renovables patagónicas

Diferencial: manejo del riesgo regulatorio argentino (precio de gas, tipo de cambio, prioridad de despacho) en contratos de largo plazo denominados en USD.

### Módulo B — Patagonia Free-Cooling SaaS
El clima naturalmente frío de la Patagonia reduce los costos de enfriamiento de data centers hasta un **35% vs. regiones tropicales**. Software de gestión de **free-cooling natural** para maximizar esta ventaja climática:
- Modelos meteorológicos locales (temperatura, humedad, viento patagónico)
- Optimización de la fracción de cooling natural vs. mecánico
- Ahorro proyectado: 15-25% del OPEX total del data center

### Módulo C — Grid Resiliency Layer
Con 500 MW exigidos y conectividad de alta confiabilidad al SADI como requisito, surge un software de **"network resiliency layer"**:
- Monitoreo en tiempo real de la estabilidad del nodo de conexión 500kV (lecciones del [[Cuello de Botella Electrico San Juan]])
- Activación automática de contingencias (switching a generación de respaldo)
- SLA de uptime de energía ≥ 99,99% como producto contractual garantizado

## Tech Stack
- API CAMMESA para monitoreo de despacho en tiempo real
- Modelos meteorológicos (ERA5 + WRF para Patagonia)
- Algoritmo de optimización de PPA (programación lineal estocástica)
- Smart Contracts para liquidación de PPAs (Ethereum/Polygon L2)
- Network monitoring (SNMP/Prometheus para la capa eléctrica)

## Riesgo Crítico
Stargate Argentina es aún un proyecto en evaluación bajo RIGI. El riesgo de postergación o cancelación es real. La estrategia de mitigación es diseñar los módulos de forma modular para que sean útiles incluso sin Stargate: los data centers medianos y los hubs de IA regionales tienen exactamente los mismos problemas de PPA y cooling.

## Próximo Movimiento
1. Analizar el pliego RIGI de Stargate Argentina cuando esté disponible públicamente.
2. Contactar a Sur Energy como cliente ancla del Módulo A (PPA Brokering).
3. Presentar el Módulo B a los data centers existentes en CABA/GBA como validación de mercado temprana.

---
**Backlinks:** [[Stargate Argentina]], [[Vaca Muerta]], [[Energía]], [[Cuello de Botella Electrico San Juan]], [[RIGI]], [[Demanda Energetica de Data Centers e IA]].
