---
type: tech-lead-opp
tags: [oil-gas, water, flowback, circular-economy, vaca-muerta, iot, digital-twin]
sources:
  - [[raw/Supplier_day_2026_Econojournal.md]]
  - [[raw/2026-08-16_news_mining_energy.md]]
  - [[wiki/03 Analysis/Mapa_de_Puntos_de_Dolor_2026.md]]
confidence: high
last_update: 2026-10-02
---

# WaterLoop_VacaMuerta — SaaS de Trazabilidad y Reuso de Agua de Flowback

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🟠 ALTA.

## El Gatillo Factual

Tres señales convergentes del **Supplier Day 2026** (agosto 2026, Neuquén):

1. **SIAM (Martín Gessler):** Detectó como cuello de botella el tratamiento de agua de flowback para reutilización en fractura → ya desarrolla soluciones pero sin plataforma digital integrada.

2. **PAE (Marcelo Gioffré):** Cuatro meses de retraso en 15 km de caño para el proyecto GNL por falta de proveedores locales especializados → los proyectos de infraestructura de agua tienen gaps críticos en capacidad local.

3. **Récord de producción (agosto 2026):** Argentina alcanzó **929.363 bpd** históricos en agosto 2026. A mayor producción de shale, mayor volumen de agua de producción (cut de agua típico: **70-90%** del fluido total producido). Con 929K bpd, el volumen de agua de producción supera los 3-5 millones de m³ diarios.

**Señal adicional (Mapa de Puntos de Dolor):** La judicialización de permisos hídricos en Catamarca y la sensibilidad social sobre el uso del agua son riesgos sistémicos amplificados por la fragmentación de datos ambientales.

## Diferenciación vs. Marketplace_y_Trazabilidad_de_Pasivos_Circulares

[[Marketplace_y_Trazabilidad_de_Pasivos_Circulares]] abarca salmueras de litio, relaves, efluentes mineros y pasivos generales → regulación, física y clientes son de minería. Este play es **ultra-específico** para el **agua de producción en O&G** (flowback y produced water), con regulación específica (Ley 25.688, AIC), física distinta (hidrocarburos disueltos, NORM) y clientes completamente distintos (operadoras de Vaca Muerta). Son mercados separados y no competidores.

## El Play Tech

**SaaS B2B de gestión integral del ciclo del agua de producción** en Vaca Muerta:

### Módulo 1 — Digital Water Twin
Gemelo digital de la infraestructura de aguas del yacimiento:
- Pozos fuente de agua + piletas de almacenamiento + ductos de reinyección + plantas de tratamiento
- Balance hídrico en tiempo real: ¿cuánta agua ingresa? ¿cuánta se reutiliza? ¿cuánta se reinyecta? ¿cuánta se pierde?
- Detección automática de fugas o desequilibrios en el balance hídrico

### Módulo 2 — Quality Trazability (IoT)
Monitoreo IoT en tiempo real de los parámetros fisicoquímicos del agua de flowback:
- **TDS** (sólidos disueltos totales), **temperatura**, **pH**, **conductividad**, **contenido de hidrocarburos** (TPH)
- Certificación automática de que el agua cumple con los estándares de reutilización en fractura o de reinyección
- Sensores ATEX-certificados (zona 1, gas/explosión) para instalación en boca de pozo
- Alertas en tiempo real ante desvíos de parámetros que impliquen riesgo de contaminación acuífera

### Módulo 3 — Water Rights & Compliance
Gestión automatizada del marco regulatorio hídrico:
- Permisos de extracción de agua subterránea (Ley 25.688)
- Reportes a la Autoridad Interjurisdiccional de Cuencas (AIC) y Subsecretaría de RRHH Hídricos
- Dashboard de riesgo regulatorio hídrico: semáforo de cumplimiento normativo en tiempo real
- **Nota crítica:** Integrar monitoreo sísmico básico (acelerómetros) dado el reporte de microsismos en zona Chevron (El Trapial, agosto 2026) asociados a reinyección.

### Modelo de Negocio
- SaaS B2B con contrato anual por pozo activo monitorizado
- Fee adicional por **certificado de calidad de agua reutilizada** (para reporte ESG de las operadoras)
- Las operadoras acreditan la reutilización de agua en sus reportes ASG/ESG y reducen el costo de extracción de agua nueva

## Tech Stack
- Sensores IoT ATEX (LoRaWAN o 4G industrial en zonas con cobertura)
- SCADA hídrico con protocolo Modbus/OPC-UA
- Digital Twin (modelado físico con MODFLOW para acuíferos, Ansys Fluent para ductos)
- API AIC / Subsecretaría de RRHH Hídricos (scraping regulatorio)
- ML para predicción de parámetros de calidad (LSTM para series temporales)
- Dashboard ESG con trazabilidad de cadena de custodia del agua reutilizada

## Riesgo Crítico
La reinyección subterránea en Vaca Muerta tiene asociación documentada con **microsismos inducidos** (reportados en El Trapial/Chevron, agosto 2026). El software debe incorporar un módulo básico de monitoreo sísmico para no convertirse en herramienta de evidencia contra el operador. Este riesgo debe gestionarse desde el diseño del producto.

## Próximo Movimiento
1. Contactar al equipo de **SIAM** (Martín Gessler) para un posible desarrollo conjunto del Módulo 1 y 2.
2. Presentar prototipo de Digital Water Twin a **YPF** (Walter Actis, VP Supply Chain) como cliente ancla.
3. Validar marco regulatorio con la **AIC** (Autoridad Interjurisdiccional de Cuencas) de Neuquén.

---
**Backlinks:** [[Marketplace_y_Trazabilidad_de_Pasivos_Circulares]], [[Vaca Muerta]], [[ShaleFlow_Anelo_Supply]], [[SupplierDay_2026_VacaMuerta_Cadena_de_Valor]], [[Mapa_de_Puntos_de_Dolor_2026]].
