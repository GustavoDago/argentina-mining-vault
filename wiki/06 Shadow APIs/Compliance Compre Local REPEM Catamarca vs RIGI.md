---
type: shadow-api
tags: [reverse-engineering, regulatory, compliance, catamarca, RIGI, mining]
sources: [[Catamarca]], [[RIGI]], [[Tres Quebradas]], [[raw/2026-07-17_news_mining_energy.md]], [[raw/2026-07-23_news_mining_energy.md]], [[raw/2026-11-24_news_mining_energy.md]]
confidence: high
last_update: 2026-11-24
---

# Shadow API: Compliance Compre Local (REPEM Catamarca vs RIGI)

Ingeniería inversa de la superposición de marcos regulatorios de contratación local entre leyes provinciales subnacionales y el régimen nacional RIGI (actualizado tras el **Decreto 1366/2026**).

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Secretaría de Desarrollo Minero de Catamarca (Registro de Proveedores de Empresas Mineras - REPEM) vs. Comité Evaluador RIGI (Ministerio de Economía Nacional).
- **Input Requerido:** 
  - Declaración Jurada de Compras e Insumos Mineros.
  - Padrón de contratistas locales inscriptos en el **REPEM** (exigencia del **70%** de mano de obra y servicios locales en Catamarca).
  - Padrón de proveedores nacionales RIGI (**20%** mínimo bajo el régimen del RIGI; tras el **Decreto 1366/2026** del 16/11/2026, basta constitución y domicilio en Argentina sin exigencia del 51% de capital/votos nacionales, pero manteniendo reglas de origen nacional MERCOSUR **ACE N° 18** para bienes).
- **Output Esperado:** `200 OK | Certificado de Cumplimiento Dual (REPEM Provincial + Cupo RIGI/ACE 18)`.
- **Fricción Crítica Registrada:** Operadores de megaproyectos de litio (ej. **Tres Quebradas** por US$ 709M, **Fénix expansión**, **Hombre Muerto Oeste**, **[[Kachi]]** por US$ 1.160M) enfrentan ahora una divergencia estructural: filiales extranjeras domiciliadas en el país pasan el filtro federal RIGI gracias al Decreto 1366/2026, pero disparan bloqueos locales y rechazo de la FAPM/CAPPROMIN por no cumplir el estándar provincial REPEM.
- **Latencia Real:** Auditorías trimestrales con demoras de **60 a 120 días** e inspecciones cruzadas provinciales-nacionales.

## Fricciones y Fallas (Error Codes)
- **`ERR_REPEM_UNDERQUOTA`:** Incumplimiento del piso del 70% de proveedores catamarqueños por inexistencia de oferta técnica especializada (ej. campamentos de alta montaña, química pesada).
- **`ERR_MULTINATIONAL_SUBSIDIARY_PROVINCIAL_REJECT`:** Proveedor calificado como "local" en RIGI federal bajo el Decreto 1366/2026 (filial argentina de capital extranjero), pero rechazado/bloqueado por cámaras y auditoría REPEM provincial al carecer de capital y radicación genuina local.
- **`ERR_ACE18_ORIGIN_MISMATCH`:** Bien provisto por empresa domiciliada en Argentina que falla el certificado de origen nacional del Acuerdo de Complementación Económica N° 18 (ACE 18) del MERCOSUR exigido para el cómputo de bienes RIGI.
- **`ERR_SUPPLY_CHAIN_BOTTLENECK`:** Paralización de obras civiles por multas o suspensiones de permisos provinciales dictados por la autoridad local minera.

## Oportunidad de Abstracción (SFaaS / Compliance Arbitrage)
**Middleware de Arbitraje de Compre Local ("Dual Local Content Compliance Engine"):**
- **Arquitectura:** Plataforma SaaS de gestión de compras B2B, validación de origen ACE 18 y scoring de proveedores (*Local Supplier Incubator & Matcher*).
- **Funcionalidad:** Software que audita la matriz de proveedores de las mineras (Zijin, Rio Tinto, Galan, Lake Resources) en tiempo real. El algoritmo valida certificados ACE 18 para bienes y sugiere esquemas de Joint Ventures (UTE) entre filiales especializadas habilitadas por el Decreto 1366/2026 (que pasan RIGI federal) y proveedores locales catamarqueños del REPEM (que blindan el 70% provincial), garantizando que una sola estructura contractual supere simultáneamente ambos filtros.
- **Monetización:** Cobrar un % de ahorro sobre las penalizaciones o multas evitadas + fee de suscripción SaaS por orden de compra procesada.
