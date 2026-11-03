---
type: shadow-api
tags: [rigi, logistics, aduana, supply-chain, imports]
sources: [[raw/2026-10-25_news_mining_energy.md]]
confidence: high
last_update: 2026-10-25
---

# Aduana Green Channel (Canal Verde RIGI)

**Tipo:** Interfaz Logística / Burocrática (Shadow API)
**Ámbito:** Nacional (Dirección General de Aduanas)
**Impacto Principal:** Reducción drástica de tiempos de importación para bienes de capital bajo el régimen [[RIGI]].

## 1. Definición y Alcance
El **Aduana Green Channel** es un mecanismo operativo acelerado (vía rápida) implementado por la Dirección General de Aduanas de Argentina, diseñado específicamente para dar curso a las importaciones de bienes de capital e insumos críticos destinados a proyectos aprobados dentro del Régimen de Incentivo para Grandes Inversiones ([[RIGI]]).

## 2. Mecánica Operativa (Reverse Engineering)
A diferencia de los canales de importación tradicionales (que a menudo involucran canales rojos o naranjas con inspecciones físicas y documentales exhaustivas y demoradas), el Green Channel funciona bajo una lógica de:
- **Pre-aprobación sistémica:** Si el CUIT del importador y la posición arancelaria coinciden con el listado de bienes aprobados en el VPU (Vehículo de Proyecto Único) del RIGI, el sistema SIM (Sistema Informático Malvina) asigna automáticamente el canal verde.
- **Liberación Inmediata:** Permite el despacho a plaza de la mercadería casi en tiempo real tras su arribo a puerto o frontera.
- **Auditoría Ex-post:** La verificación técnica se traslada a controles posteriores o auditorías documentales, evitando el cuello de botella físico en las terminales portuarias.

## 3. Impacto en los Megaproyectos (Octubre 2026)
La implementación oficial de este mecanismo en octubre de 2026 ha sido un catalizador crítico para evitar retrasos en los CAPEX. Proyectos como **[[Taca Taca]]** (movimientos de suelo), **[[Continental Resources]]** (equipos de perforación) y expansiones de litio en el NOA se han beneficiado de una logística sin fricciones.

## 4. Oportunidades de Apalancamiento Tecnológico
- **Integración B2B Logística:** Desarrollar middleware que conecte los sistemas de gestión de las operadoras (ERP) con las actualizaciones de estado de la Aduana para prever con exactitud la llegada de componentes críticos al *site prep*.
- **Trazabilidad Inmutable:** Proveer plataformas de registro (ej. DLT/Blockchain) para mantener un historial auditable de las importaciones por el Green Channel, facilitando las auditorías ex-post de la AFIP/Aduana y minimizando el riesgo de penalidades por incumplimientos percibidos del RIGI.

## Conexiones
- [[RIGI]]
- [[Taca Taca]]
- [[Continental Resources]]
- [[Ventanilla Unica Importacion PyME Decretos 482-483]]