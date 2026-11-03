---
type: tech-lead-opp
tags: [opportunity, technology, energy, oil-gas, logistics, supply-chain, saas]
sources: [[raw/2026-08-09_news_mining_energy.md]], [[raw/2026-08-11_news_mining_energy.md]], [[raw/2026-11-03_news_mining_energy.md]], [[Vaca Muerta]]
confidence: high
last_update: 2026-11-03
---

# Opp: SandLogistics - Control de Trazabilidad y Despacho Multi-Modal de Arenas de Fractura

## 1. Oportunidad de Negocio (High-Leverage)
La actividad en [[Vaca Muerta]] cierra 2026 superando las **28.000 etapas de fractura** y proyecta alcanzar **39.000 etapas en 2027 (+39%)**. Este salto operativo empuja la demanda de arena de fractura por encima de los **8 millones de toneladas anuales**. 

El transporte terrestre representa entre el **70% y el 80% del costo puesto en locación**. La saturación de las rutas provinciales de Neuquén y Río Negro (Ruta 7, Ruta 151, Ruta 6) y las colas de espera en los pads generan sobrecostos millonarios por paradas no programadas (*stand-by*) de los sets de fractura, valuados en más de US$ 50.000 a US$ 80.000 diarios por cuadrilla.

Existe una oportunidad crítica para un **middleware SaaS de agendamiento dinámico y despacho *Just-In-Time* (JIT)** que sincronice la logística de camiones tolva/bateas con la tasa de consumo de proppant en tiempo real de los pozos.

## 2. El Play Tecnológico

- **Algoritmo de Slot Allocation en Pozo:** Despacho sincronizado directamente con la telemetría del manifold de fractura (consumo de libras/minuto de arena). Si una etapa se demora por presión o pesca de tapón, el sistema frena o desvía automáticamente las bateas en tránsito hacia hubs intermedios, eliminando colas en locación.
- **Trazabilidad y Geofencing de Hubs Intermedios:** Monitoreo telemático de flotas que valida pesos en balanza de origen, precintos electrónicos y tiempos de tránsito desde canteras en Entre Ríos y canteras de cercanía en Río Negro.
- **QA/QC Digital y Registro Inmutable:** Certificación de especificaciones de granulometría (mallas 40/70 y 100) y conductividad para evitar que partidas fuera de especificación ingresen al pozo, mitigando fallas de estimulación.

## 3. Apalancamiento RIGI & Reducción de OPEX
- **Ahorro Directo de OPEX:** Reducción de hasta un 15-20% en costos de stand-by y demoras logísticas para operadoras RIGI ([[YPF]], [[Vista Energy]], [[Pan American Energy]], [[Tecpetrol]], [[Pampa Energía]], [[Continental Resources]]).
- **Cumplimiento y Compre Local:** Habilitación de transportistas locales en el sistema para cumplir con los estándares de compre provincial de Neuquén y Río Negro.

## 4. Análisis Escéptico y Riesgos Críticos
- **Trade-off:** La resistencia de los choferes y empresas de transporte tradicionales a instalar dispositivos telemáticos o adherirse a turnos estrictos de descarga sin cobrar horas de espera.
- **Riesgo Crítico:** Fragmentación del mercado: las grandes operadoras (YPF con AESA, Halliburton, SLB) operan con sistemas internos cerrados. La estrategia debe orientarse a operadoras independientes de escala media/alta (Vista, Pluspetrol, Phoenix, Continental) o a los propios consorcios logísticos de transporte de arena.
- **Próximo Movimiento:** Desarrollar un conector API ligero con los SCADA de pozos para capturar el feed de bombeo de arena y simular el ahorro de stand-by en un cluster de 3 pads simultáneos.

---
**Backlinks:** [[Vaca Muerta]], [[RIGI]], [[VMOS]], [[Oportunidades y Conexiones]].
