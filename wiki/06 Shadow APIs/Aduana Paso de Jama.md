---
type: shadow-api
tags: [reverse-engineering, logistics, customs, afip, jama]
sources: [[Corredor Bioceanico]], [[Sat-Edge_Bioceanico]], [[Paso de Jama]], [[Cauchari-Olaroz]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Paso de Jama y Corredor Bioceánico

Modelo determinístico del circuito de despacho y control transfronterizo en la frontera andina Jujuy-Chile.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Aduana Argentina (AFIP-DGA), Servicio Agrícola y Ganadero de Chile (SAG), Gendarmería Nacional Argentina (GNA) y Carabineros de Chile.
- **Input Requerido:** Manifiesto Internacional de Carga / Declaración Tránsito Aduanero (MIC/DTA), Certificado de Origen Digital (COD VUCE), precintos de seguridad homologados y comprobante de pago de cánones fronterizos.
- **Output Esperado:** `200 OK | Pase Libre Fronterizo` directo hacia los puertos del Pacífico (Angamos, Mejillones, Antofagasta, Iquique).
- **Métrica de Éxito Validada:** Caso Eramine (Cauchari-Olaroz), que logró **reducir en 10 días el tiempo de transporte hacia Asia** despachando carbonato de litio por camión vía Jama directo a Angamos (evitando el canal de Panamá y fletes del Atlántico).
- **Latencia Real:** Altamente asincrónica (8 a 36 horas) debido a colapsos de conectividad en alta montaña y controles analógicos duplicados.

## Fricciones y Fallas (Error Codes)
- **`ERR_OFFLINE_DESERT`:** Apagón digital de **130 km en territorio chileno** posterior al paso de Jama, que interrumpe la sincronización del MIC/DTA electrónico y bloquea el avance del convoy.
- **`ERR_LOCAL_CONTENT_OVERLAP`:** Detención de carga por conflicto entre el 70% de compre local provincial (ej. Catamarca REPEM) y el 20% nacional del RIGI al auditar proveedores de transporte.
- **`ERR_UNION_INTERRUPTION`:** Paros y bloqueos de calzada sobre la RN 51 / RN 52 por reclamos de conductores por falta de servicios e infraestructura básica.

## Oportunidad de Abstracción (SFaaS)
**Plataforma de Digitalización Logística Cross-Border B2B ("Sat-Edge Bioceánico"):**
- **Arquitectura:** Nodos Edge Computing instalados en los cabezales de los camiones mineros con almacenamiento *Store-and-Forward* asíncrono y tokens criptográficos offline eTIR.
- **Funcionalidad:** Permite la pre-validación de manifiestos y la descarga de datos vía Wi-Fi local en paradores de YPF o control de aduana (ej. San Antonio de los Cobres), transmitiendo de forma transparente al SIM de AFIP cuando se recupera la cobertura satelital/celular.
- **Impacto:** Convierte el trámite físico en un peaje digital transparente para los **+7.000 camiones anuales** que transportan litio y suministros industriales por el Corredor de Capricornio.

