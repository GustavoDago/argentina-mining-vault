---
type: shadow-api
tags: [reverse-engineering, regulatory, compliance, catamarca, RIGI, mining]
sources: [[Catamarca]], [[RIGI]], [[Tres Quebradas]], [[raw/2026-07-17_news_mining_energy.md]], [[raw/2026-07-23_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Compliance Compre Local (REPEM Catamarca vs RIGI)

Ingeniería inversa de la superposición de marcos regulatorios de contratación local entre leyes provinciales subnacionales y el régimen nacional RIGI.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Secretaría de Desarrollo Minero de Catamarca (Registro de Proveedores de Empresas Mineras - REPEM) vs. Comité Evaluador RIGI (Ministerio de Economía Nacional).
- **Input Requerido:** 
  - Declaración Jurada de Compras e Insumos Mineros.
  - Padrón de contratistas locales inscriptos en el **REPEM** (exigencia del **70%** de mano de obra y servicios locales en Catamarca).
  - Padrón de proveedores nacionales RIGI (exigencia del **20%** mínimo de origen nacional bajo el régimen del RIGI).
- **Output Esperado:** `200 OK | Certificado de Cumplimiento de Compre Local & Aprobación Auditada RIGI`.
- **Fricción Crítica Registrada:** Operadores de megaproyectos de litio (ej. **Tres Quebradas** por US$ 709M, **Fénix expansión**, **Hombre Muerto Oeste**) alertan sobre la imposibilidad física de cumplir simultáneamente ambos cupos sin colapsar la cadena de suministro por falta de proveedores capacitados en alta montaña en la provincia.
- **Latencia Real:** Auditorías trimestrales con demoras de **60 a 120 días** e inspecciones cruzadas provinciales-nacionales.

## Fricciones y Fallas (Error Codes)
- **`ERR_REPEM_UNDERQUOTA`:** Incumplimiento del piso del 70% de proveedores catamarqueños por inexistencia de oferta técnica especializada (ej. campamentos de alta montaña, química pesada).
- **`ERR_RIGI_LOCAL_CONFLICT`:** El gasto realizado en contratistas locales catamarqueños no califica dentro del 20% nacional exigido por RIGI al no estar inscriptos como VPU o PyME homologada nacional.
- **`ERR_SUPPLY_CHAIN_BOTTLENECK`:** Paralización de obras civiles por multas o suspensiones de permisos provinciales dictados por la autoridad local minera.

## Oportunidad de Abstracción (SFaaS / Compliance Arbitrage)
**Middleware de Arbitraje de Compre Local ("Local Content Compliance Engine"):**
- **Arquitectura:** Plataforma SaaS de gestión de compras B2B y scoring de proveedores (*Local Supplier Incubator & Matcher*).
- **Funcionalidad:** Software que audita la matriz de proveedores de las mineras (Zijin, Rio Tinto, Galan) en tiempo real. El algoritmo clasifica las órdenes de compra y sugiere esquemas de Joint Ventures (UTE) entre proveedores locales de Catamarca (Tier 3) y contratistas nacionales homologados RIGI (Tier 1), garantizando que una sola factura satisfaga simultáneamente el 70% del REPEM y el 20% del RIGI.
- **Monetización:** Cobrar un % de ahorro sobre las penalizaciones o multas evitadas + fee de suscripción SaaS por orden de compra procesada.
