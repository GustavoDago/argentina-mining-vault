---
type: analysis
tags: [energy, geothermal, red-team, skeptic, lcoe]
sources: [[Full environmental life cycle costing analysis of geothermal power generation.html]], [[Reconversión Pozos Petroleros a Geotermia]]
confidence: high
last_update: 2026-06-28
---

# Análisis Escéptico: Geotermia en Pozos Petroleros Argentinos

Si bien la reconversión de pozos petroleros en centrales de [[Energía Geotérmica]] es excelente en la teoría, la modelización de costos ambientales y financieros (FELCC) de Jingyi Li et al. (2026) presenta desafíos demoledores para la tesis original en Argentina:

## 1. El Desafío de la Escala y el LCOE
El estudio demuestra que los sistemas reconvertidos tienen un costo de generación (LCOE) prohibitivo:
* **R-GEO_double:** **818.8 c€/kWh** (8.18 USD/kWh, un absurdo comercial).
* **R-GEO_single:** **461.7 c€/kWh** (4.61 USD/kWh).
* **R-GEO_semi:** **173.3 c€/kWh** (1.73 USD/kWh, el único caso con sentido técnico pero aún 14 veces más costoso que la geotermia convencional de 12.6 c€/kWh).

La causa raíz es la **baja potencia anual (125.120 kWh/año)** y una **vida útil estimada de solo 15 años** debido al desgaste térmico y mecánico de pozos no diseñados originalmente para este fin.

## 2. La Ilusión del "Break-Even"
Para que un proyecto de pozo semi-abandonado (**R-GEO_semi**) en cuencas como Neuquén o Golfo San Jorge sea competitivo con el sistema convencional (GEO_bau):
* Debería alcanzar una **eficiencia de sistema del 68%** operando a 15 años. 
* Los ciclos ORC de baja entalpia típicos para estas temperaturas operan a una eficiencia real de entre **4.2% y 12%**. Físicamente, es imposible alcanzar el punto de equilibrio sin subsidios masivos.

## 3. Barrera de Regulación y Propiedad en Argentina
En la legislación argentina (Ley de Hidrocarburos 17.319 y normativas provinciales), el abandono de pozos es responsabilidad indelegable del titular de la concesión (ej. YPF, PAE, Vista). 
* Si se traspasa el pozo para geotermia, el operador petrolero querrá transferir el **pasivo ambiental** completo (riesgo de contaminación de acuíferos, cementaciones deficientes).
* Ninguna aseguradora ni PYME tecnológica de energía renovable tiene el balance suficiente para absorber la contingencia legal y ambiental de un pozo hidrocarburífero heredado de décadas de operación.

## Conclusión Red Team
La tesis de reconversión de pozos secos o cerrados (R-GEO_double/single) está **muerta** comercialmente debido a un LCOE inviable.

La única ventana de oportunidad real es la **micro-generación distribuida a partir de salmueras coproducidas en pozos activos (R-GEO_semi)** en yacimientos remotos sin conexión a la red. El gas de venteo (flaring) o el diésel transportado en camiones a zonas aisladas de la Patagonia tiene un costo equivalente muy alto, lo que podría justificar instalar un ciclo ORC de baja entalpía para alimentar las propias bombas del yacimiento, operando como un sistema de eficiencia energética del operador petrolero y no como un negocio de venta de energía a la red.
