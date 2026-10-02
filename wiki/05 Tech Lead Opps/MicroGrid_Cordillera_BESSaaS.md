---
type: tech-lead-opp
tags: [energy, bess, microgrid, mining, lithium, copper, off-grid, puna, cordillera]
sources:
  - [[raw/2026-07-16_news_mining_energy.md]]
  - [[raw/2026-08-29_news_mining_energy.md]]
  - [[raw/2026-07-15_news_mining_energy.md]]
confidence: high
last_update: 2026-10-02
---

# MicroGrid-Cordillera — BESS-as-a-Service para Alta Montaña

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🔴 MUY ALTA.

## Los Gatillos Factuales (Convergencia de 5 Señales)

1. **Informe Aggreko (julio 2026):** Los megaproyectos andinos de cobre y litio migran masivamente a **microredes híbridas descentralizadas** (solar + BESS + GNL backup) ante la imposibilidad física de conectarse al SADI. Ahorro potencial documentado: **40% de OPEX en diésel**.

2. **RIMI** (Régimen de Incentivo para Medianas Inversiones): Exime al equipamiento BESS de los montos mínimos del RIGI, habilitando un mercado de proveedores off-grid en escala media sin necesidad de comprometer US$ 200M mínimos.

3. **Resolución 155/2026 (BESS Alma SADI):** El gobierno adjudicó **700,5 MW en proyectos BESS** (Genneia, DQD, 360 Energy, Aluar, Intermepro) → hay un ecosistema técnico local validado y listo para exportar know-how a la minería.

4. **Demanda eléctrica minera (OLACDE):** Proyección de crecimiento del **+428% hacia 2034** impulsada por cobre en San Juan y litio en el NOA.

5. **Distrito Vicuña (septiembre 2026):** BHP/Lundin recibieron autorización para construir su propia línea de **500kV** bajo el modelo "el beneficiario paga" → el paradigma de auto-abastecimiento eléctrico es la nueva norma en minería de gran escala.

## Diferenciación vs. VPP_Mineria_San_Juan

[[VPP_Mineria_San_Juan]] se enfoca en proyectos **conectados o semi-conectados** a la red de 500kV de San Juan (arbitraje de despacho con el SADI). Este play apunta exclusivamente a la **Puna y la cordillera de Salta/Catamarca** donde no hay red y los proyectos son **100% off-grid**. Son mercados distintos y complementarios, no competidores.

## El Play Tech

**Plataforma de Gestión Energética + BESS-as-a-Service** para proyectos mineros en alta cordillera:

### Capa de Hardware (diseño rugerizado)
- Integración con proveedores BESS con experiencia local (Genneia, DQD) y paneles solares (importados a arancel 0% bajo RIGI).
- Diseño rugerizado estándar **MIL-STD-810H** para operación en alturas > 3.000 m sobre el nivel del mar, temperaturas de -20°C a +45°C y vibración por caminos de montaña.

### Capa de Software (EMS/SCADA)
- **Algoritmo de despacho óptimo** en tiempo real que maximiza el uso solar, minimiza el arranque de generadores diésel/GNL y predice la demanda en función del schedule de turnos de maquinaria pesada.
- **Predicción meteorológica ML** entrenada con datos de irradiación solar en la Puna (SENAMHI / ERA5) para anticipar días nublados con 24h de antelación y precargar el BESS.
- Dashboard de **KPIs de huella de carbono** en tiempo real para reportes ASG.

### Modelo de Negocio: Energy-as-a-Service (EaaS)
Las mineras **no compran el activo** → pagan por MWh entregado a precio fijo en USD (8-10 años). El proveedor financia el CAPEX mediante deuda de largo plazo con el BID o CAF (garantías de deuda verde). Las mineras eliminan el BESS de balance y aseguran costos de energía previsibles para su modelo financiero RIGI.

### Certificados de Energía Limpia
Generación de **atributos de energía renovable (RECs)** verificados por CAMMESA o auditor multilateral → alimentan el reporte ASG/ESG exigido por BID/IFC para el des-riesgo financiero de proyectos de litio de gran escala.

## Tech Stack
- EMS con ML de predicción solar en alta montaña
- API SCADA industrial (Modbus TCP/IP, DNP3, IEC 61850)
- Algoritmo de Unit Commitment (optimización estocástica)
- Integración con BMS (Battery Management System) de proveedores BESS
- Dashboard ESG (generación de certificados RECs)

## Riesgo Crítico
El CAPEX inicial del stock de BESS es alto (~US$ 108/kWh × escala de MW). El modelo EaaS requiere financiamiento de largo plazo para el proveedor del servicio. La clave es estructurar el primer contrato con respaldo de un banco multilateral de desarrollo (BID/CAF) o una garantía de un estado provincial.

## Próximo Movimiento
1. Presentar modelo EaaS a Aggreko (ya activo en el mercado) y a CAF/BID como posibles garantes.
2. Contactar a los **7 proyectos de salmueras operativos** en Catamarca/Salta que ya operan con diésel y son el cliente natural del modelo.
3. Evaluar sinergias con [[HydroTrust_Puna_Hidrico]] para ofrecer un bundle de auditoría hídrica + gestión energética.

---
**Backlinks:** [[VPP_Mineria_San_Juan]], [[HydroTrust_Puna_Hidrico]], [[Litio]], [[Cobre]], [[Taca Taca]], [[Rincón]], [[RIGI]], [[Distrito Vicuña]], [[Energía]].
