---
type: shadow-api
tags: [reverse-engineering, logistics, regulatory, bioceanico]
sources: [[Corredor Bioceanico]], [[raw/2026-04-25_news_mining_energy.md]], [[raw/2026-06-29_news_mining_energy.md]], [[raw/2026-07-23_news_mining_energy.md]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: Convención TIR - Corredor Bioceánico

**Propietario del Proceso:** Aduanas coordinadas de Brasil (RFB), Paraguay (DNA), Argentina (AFIP-DGA) y Chile (SNA).
**Vector de Fricción:** Tránsito Aduanero Internacional por Carretera y Asimetría de Protocolos eTIR.

## 1. Naturaleza de la Fricción
La habilitación operativa del Puente de la Bioceánica (85% de avance físico) y la **ratificación formal de la Convención TIR por parte de Brasil** desbloquean la libre circulación del tránsito pesado desde el Océano Atlántico hasta el Pacífico. El Convenio TIR exime a los camiones con precintos de inspecciones físicas y de garantías aduaneras adicionales en fronteras intermedias (Argentina/Paraguay). Sin embargo, la brecha de digitalización entre el sistema global eTIR (gestionado por IRU en Ginebra) y las plataformas aduaneras locales genera un "Downtime Regulatorio".

## 2. Parámetros Técnicos (Endpoints de Burocracia)
- **Input:** Manifiesto electrónico eTIR, Certificado de Precintado Homologado en Origen (Santos, Paranaguá o Güemes), Garantía Internacional emitida por la cámara nacional garante (FADEEAC en Argentina).
- **Output:** `200 OK | Pase Libre de Frontera Intermedia` directo hacia los puertos de exportación en el Pacífico (Antofagasta, Angamos, Iquique).
- **Rate Limit / Latencia:** Aunque la norma prevé cruce directo, la falta de APIs de sincronización entre el sistema SIM (Argentina) y el SOFIA (Paraguay) introduce demoras de **48 a 72 horas** por re-verificación manual en cabeceras de puente.
- **Inversión de Red:** El financiamiento del BID para el tramo paraguayo PY15 (US$ 200M) y la pavimentación de la RN 51 en Salta (US$ 100M) aceleran la velocidad de circulación física, trasladando el 100% de la latencia a la capa informática.

## 3. Vulnerabilidades y Fallos del Estado (Oportunidad)
1. **Incompatibilidad de Schemas XML/JSON:** La DGA de AFIP no cuenta con una API pública para inyectar manifiestos eTIR en tiempo real desde plataformas externas.
2. **Inspecciones Físicas Duplicadas:** Ante caídas de red en el Paso de Jama o Sico, las autoridades fronterizas degradan el protocolo eTIR a inspección física manual de la carga minera.

## 4. Diseño del Exploit (Middleware eTIR B2B / "AndesTrack")
**Data-as-a-Service (DaaS) de Trazabilidad eTIR & Compliance:**
- **Sistema de Orquestación:** Middleware que convierte los Manifiestos de Carga (MIC/DTA) de las operadoras (Taca Taca, Minera Exar, Rio Tinto) al formato estándar eTIR de IRU y efectúa una pre-validación criptográfica (*pre-clearance*).
- **Integración con FADEEAC:** Asignación del rol de partner tecnológico B2B con las cámaras de transporte para homologar los datos de telemetría sin violar el CCT 40/89.
- **Valor Agregado:** Garantiza la eliminación del tiempo de espera de 72 horas en fronteras intermedias, asegurando entregas *Just-In-Time* para los fletes de concentrados de cobre y litio hacia el mercado asiático.

