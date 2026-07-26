---
type: framework
tags: [energy, geothermal, circular-economy, transition, lcoe]
sources: [[Full environmental life cycle costing analysis of geothermal power generation.html]]
confidence: high
last_update: 2026-06-28
---

# Energía Geotérmica

La **energía geotérmica** utiliza el calor interno del planeta para producir electricidad o calefacción. A diferencia de la energía solar o eólica, es capaz de proporcionar **energía de base**, funcionando 24/7 sin depender de las condiciones climáticas.

## Modelos de Conversión (Manchester, 2026)
De acuerdo con el estudio de *Full environmental life cycle costing* (FELCC) de Jingyi Li et al. (2026), se evalúan tres configuraciones para la reconversión de pozos de petróleo y gas abandonados (AOGW) utilizando ciclos orgánicos Rankine (ORC), en comparación con una planta convencional (GEO_bau):

1. **R-GEO_double (Doble pozo):** Un pozo productor y uno inyector completamente reentrados.
2. **R-GEO_single (Pozo único):** Uso de un intercambiador coaxial de calor de fondo de pozo (downhole heat exchanger) sin extraer fluidos de la formación.
3. **R-GEO_semi (Pozo semi-abandonado):** Pozos en explotación activa pero con alto corte de agua (high water-cut, ~95%), reconfigurados para aprovechamiento térmico antes de su abandono definitivo.

## Análisis de Costos y Viabilidad (LCOE)
El estudio revela que, aunque la reconversión reduce drásticamente las externalidades ambientales y los costos de perforación iniciales, los sistemas recuperados enfrentan duras limitaciones económicas debido a su **bajo rendimiento anual (125.120 kWh/año)** y una **vida útil corta (15 años)** en comparación con los 30 años de una planta convencional:

| Sistema | Tipo de Configuración | LCOE (Centavos €_2022 / kWh) |
| :--- | :--- | :--- |
| **GEO_bau** | Convencional (Alsacia, 4.1 MWe) | **12.6** |
| **R-GEO_semi** | Semi-abandonado (Chaunoy, 20 kWe) | **173.3** |
| **R-GEO_single** | Monopozo Coaxial (Chaunoy, 20 kWe) | **461.7** |
| **R-GEO_double** | Doblete reentrado (Chaunoy, 20 kWe) | **818.8** |

### Viabilidad de Punto de Equilibrio (Break-even)
* Para que el sistema **R-GEO_semi** (el más competitivo) logre igualar el LCOE de **GEO_bau** (12.6 centavos), necesitaría alcanzar una **eficiencia de sistema del 68%** operando a 15 años, lo cual excede el límite térmico actual del ciclo ORC de baja entalpía (~4.2%).
* Las externalidades de salud y ambientales (huella de carbono e impacto toxicológico) de la geotermia son insignificantes comparadas con los combustibles fósiles, pero el Capex por kW instalado de los sistemas reconvertidos sigue siendo la barrera crítica.
