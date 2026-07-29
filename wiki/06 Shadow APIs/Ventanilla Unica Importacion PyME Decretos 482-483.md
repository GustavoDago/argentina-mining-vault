---
type: shadow-api
tags: [reverse-engineering, regulatory, customs, pyme, rimi, import]
sources: [[RIMI]], [[RIGI]], [[raw/2026-06-27_news_mining_energy.md]], [[raw/2026-07-22_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Importación Agilizada PyME Minera/Energética (Decretos 482-483 / RIMI)

Modelo de ingeniería inversa sobre el régimen preferencial de importación de repuestos, maquinarias y soluciones de almacenamiento (BESS) para contratistas PyME minero-energéticas.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Secretaría de Industria y Comercio, AFIP-DGA y Banco Central de la República Argentina (BCRA).
- **Input Requerido:** 
  - Certificado PyME Minera/Energética homologado.
  - Formulario de solicitud de exención arancelaria bajo los **Decretos 482/2026 y 483/2026**.
  - Adhesión al **RIMI** (Régimen de Incentivo para Medianas Inversiones) para bienes de generación distribuida o almacenamiento en baterías sin exigencia de piso de inversión.
- **Output Esperado:** `200 OK | Licencia Automática de Importación & Acceso Directo a Divisas al Mercado Oficial (MULC)`.
- **Latencia Real:** Reducida de 180 días (esquema tradicional SIRA/SIDI) a **15 a 30 días hábiles** mediante canal verde preferencial.

## Fricciones y Fallas (Error Codes)
- **`ERR_PYME_CERTIFICATE_EXPIRED`:** Caducidad del Certificado PyME o rechazo del encuadre por facturación acumulada superior a los límites del sector industrial.
- **`ERR_TARIFF_CODE_MISMATCH`:** Error en la posición arancelaria (NCM) de componentes específicos de baterías BESS o repuestos pesados de minería de alta montaña.
- **`ERR_BCRA_ACCESS_DELAY`:** Demoras en la validación del acceso al mercado de cambios para transferencias al exterior a proveedores internacionales de equipos (ej. Caterpillar, Komatsu, CATL).

## Oportunidad de Abstracción (SFaaS / Customs Middleware)
**Plataforma de Despacho e Importación Agilizada PyME ("FastImport Minero"):**
- **Arquitectura:** SaaS de pre-clasificación arancelaria y automatización de trámites aduaneros (*Customs Clearing Automation*).
- **Funcionalidad:** Software B2B que conecta a PyMEs de servicios mineros (Tier 2 y Tier 3 en Añelo, San Juan y la Puna) con la aduana. El sistema mapea las posiciones NCM de los repuestos necesarios en tiempo real, verifica el encuadre automático en los Decretos 482/483 y RIMI, e inyecta la solicitud pre-auditada en el portal de la Secretaría de Comercio.
- **Monetización:** Cobro de un porcentaje por tonelada o valor CIF importado con éxito sin fricción de licencias no automáticas.
