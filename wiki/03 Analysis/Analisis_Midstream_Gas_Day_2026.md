---
type: analysis
tags: [energy, oil-gas, regulatory, infrastructure]
sources: [raw/Midstream & Gas Day.html, raw/Midstream.pdf]
confidence: high
last_update: 2026-06-06
---

# Tesis de Posicionamiento: Midstream & Gas Day 2026

## Contexto Estratégico

La quinta edición del **Midstream & Gas Day** (10 de junio de 2026) se celebra en un punto de inflexión estructural para el sector energético argentino:
1. **Fusión Regulatoria (ENRGE):** La unificación del ENRE y el ENARGAS (01/06/2026) altera la dinámica de tarifas, prioridades de despacho y el control institucional sobre el transporte de gas y electricidad.
2. **Saturación del CAPEX Físico:** Vaca Muerta registra récords históricos de actividad (2.484 etapas de fractura en mayo de 2026) impulsados por las aprobaciones del [[RIGI]] (ej. [[Proyecto LLL Oil]] de YPF por US$ 25.000M, Pluspetrol por US$ 12.000M y Vista). La capacidad instalada de transporte de crudo y gas (Oldelval, TGS, VMOS) está al límite.
3. **El Play de la Demanda Tecnológica:** La irrupción de la demanda energética para Data Centers e IA en el Cono Sur dinamiza el mercado spot del gas no convencional y redefine los requerimientos de generación termoeléctrica distribuida.

---

## Mapeo de Actores Clave y Puntos de Contacto

### 1. El Regulador y el Marco Regulatorio
*   **María Tettamanti** (Secretaria de Energía de la Nación) y **Mauricio Roitman** (Energeia): Foco en la reglamentación del **Súper RIGI** y la transición del ENRGE.
*   *Punto de Interés:* Certificación y debida diligencia actuarial para el cumplimiento del 20% obligatorio de contenido local (Decreto 105/2026).

### 2. Los Dueños de la Infraestructura Física (Midstream)
*   **Gustavo Chaab** (CEO de VMOS / Vaca Muerta Oil Sur): VMOS está al 60% de avance físico del oleoducto de exportación a Punta Colorada, habiendo iniciado el tendido submarino. Representa la mayor ruta de evacuación de crudo.
*   **Oscar Sardi** (CEO de [[TGS]]) y **Horacio Pizarro** (CEO de TGN): Foco en la expansión de gasoductos troncales bajo el RIGI y el flujo revertido del Gasoducto Norte para exportar a Bolivia/Brasil.
*   **Ricardo Hösel** (CEO de [[Oldelval]]): Expansión del sistema Duplicar Plus y evacuación de crudo hacia el Atlántico.
*   **Tomás Córdoba** (CEO de [[Compañía MEGA]]): Procesamiento de líquidos de gas natural (NGLs) en origen para petroquímica aguas abajo.

### 3. Las Operadoras (Upstream & Demanda)
*   **Santiago Martínez Tanoira** (VP de LNG y Gas Integrado de [[YPF]]): Impulsa el megaproyecto de GNL (Southern Energy LNG, US$ 6.900M) en Río Negro y el play de Loma La Lata.
*   **Leopoldo Macchia** (CCO de [[Tecpetrol]]) y **Victoria Sabbioni** (VP Comercial de CGC): Operadoras ágiles del no convencional que sufren los cuellos de botella de servicios Tier 2 (fractura y perforación) y costos de parada por repuestos.
*   **Dolores Brizuela** (Presidenta de Dow Argentina): Consumidora petroquímica líder de NGLs y gas industrial en Bahía Blanca.

### 4. Proveedores Tecnológicos y de Servicios
*   **Emilio Weber** (Director Comercial de Galileo Technologies): Líderes en tecnología criogénica de gasoducto virtual a pequeña escala (Cryobox) y licuación en boca de pozo.
*   **Paulo Castro** (Business Development de Wärtsilä): Especializados en microrredes industriales de alta capacidad, almacenamiento BESS y generación dual-fuel.

---

## Tesis y Propuestas de Valor Tecnológicas (Plays High-Leverage)

A partir de la inteligencia consolidada en la Wiki, existen cuatro plays tecnológicos listos para ser presentados o validados durante el networking del evento:

### Tesis A: ShaleFlow Añelo (Mantenimiento Predictivo & Ruteo OEM)
*   **Destinatarios:** Operadoras (YPF, Tecpetrol, CGC, Pampa) y OEMs regionales (SLB, Halliburton, Weir, NOV).
*   **El Problema:** La fatiga mecánica por el récord de fracturas provoca paradas en los trailers de bombeo. Las demoras de repuestos importados cuestan US$ 80.000 diarios en standby.
*   **La Solución:** Software Edge AI para predecir fallas hidráulicas 72 horas antes + integración vía API segura (Shadow API) con almacenes locales de OEMs para automatizar el ruteo directo del repuesto al pozo.
*   **Detalle:** [[ShaleFlow_Anelo_Supply]] y análisis pre-mortem [[PreMortem_ShaleFlow]].

### Tesis B: Logística Andina y Sinergias con Gas Virtual
*   **Destinatarios:** Galileo Technologies (Emilio Weber), Wärtsilä (Paulo Castro) y operadoras de litio/cobre en el NOA y Cuyo (CGC, Pampa, Ganfeng).
*   **El Problema:** El colapso del transporte de red eléctrica en San Juan (disputa del ENRGE bajo Res. 219/2026 entre [[Los Azules]] y [[Josemaría]]) y las barreras geográficas de la Puna exigen generación off-grid de escala industrial.
*   **La Solución:** Conectar la abundancia de gas en boca de pozo en Vaca Muerta con el bypass energético minero a través de micro-GNL modular (Galileo) alimentando microrredes mineras (Wärtsilä). Esto se optimiza con el SaaS de logística andina bimodal.
*   **Detalle:** [[AndesLogistics_Puna_Logistica]] y análisis pre-mortem [[PreMortem_AndesLogistics]].

### Tesis C: Marketplace Tier 2 (Fracking/Drilling Share)
*   **Destinatarios:** Operadoras medianas/grandes y contratistas de servicios.
*   **El Problema:** La saturación de la capacidad instalada física de sets de fractura y equipos hacia 2027 debido a las barreras arancelarias de importación.
*   **La Solución:** Un motor SaaS B2B de despacho y optimización de capacidad ociosa (stand-by) compartido dinámicamente entre operadoras, reduciendo los tiempos muertos del hardware.
*   **Detalle:** [[Marketplace_Tier2_VacaMuerta]] y análisis pre-mortem [[PreMortem_Marketplace_Tier2]].

### Tesis D: Compliance Ledger RIGI
*   **Destinatarios:** Consultores regulatorios (Energeia), directores de legales de YPF y grandes operadoras.
*   **El Problema:** Auditoría y cumplimiento normativo del 20% obligatorio de compras locales exigido por el RIGI, bajo riesgo de sanciones ante la nueva fiscalización del ENRGE.
*   **La Solución:** Suite de debida diligencia de contratación de pymes proveedoras con trazabilidad cifrada.
*   **Detalle:** [[Super RIGI e Industrializacion]] y análisis pre-mortem [[PreMortem_Tokenizacion_Contenido_Local]].

---

**Backlinks:** [[RIGI]], [[Vaca Muerta]], [[TGS]], [[Compañía MEGA]], [[Oldelval]], [[ShaleFlow_Anelo_Supply]], [[AndesLogistics_Puna_Logistica]], [[Marketplace_Tier2_VacaMuerta]], [[Cuello de Botella Electrico San Juan]].
