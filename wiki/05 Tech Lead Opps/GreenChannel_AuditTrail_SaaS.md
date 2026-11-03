---
type: tech-lead-opp
tags: [mining, energy, software, compliance, aduana, rigi, saas, regtech, supply-chain]
sources: [[raw/2026-10-21_news_mining_energy.md]], [[raw/2026-10-25_news_mining_energy.md]], [[raw/2026-10-26_news_mining_energy.md]], [[raw/2026-10-27_news_mining_energy.md]], [[raw/2026-11-01_news_mining_energy.md]], [[raw/2026-11-02_news_mining_energy.md]]
confidence: high
last_update: 2026-11-02
---

# SaaS de Trazabilidad y Compliance para el Aduana Green Channel RIGI

**Sector:** RegTech Aduanero / Supply Chain Industrial / Minería y Oil & Gas.  
**Ubicación Clave:** Puertos Atlánticos (Buenos Aires, Bahía Blanca, San Antonio Este), Pasos Andinos ([[Paso de Jama]], Sico) y Yacimientos ([[Vaca Muerta]], San Juan, Puna).

---

## 1. La Tesis en Una Línea

> La activación del [[Aduana Green Channel]] para proyectos [[RIGI]] reduce los plazos de nacionalización de bienes de capital a menos de 48 horas pero traslada todo el riesgo a fiscalizaciones ex-post de la AFIP/DGA, creando una oportunidad ineludible para una plataforma SaaS B2B que conecte los sistemas ERP corporativos con el SIM aduanero y telemetría IoT de activos para generar un registro inmutable de afectación exclusiva al proyecto.

---

## 2. Señal de Mercado y Diagnóstico del Cuello de Botella

- **El Despliegue Operativo del Canal Verde (Octubre - Noviembre 2026):** La AFIP y la Dirección General de Aduanas pusieron en marcha el carril prioritario exclusivo para megaproyectos RIGI, permitiendo el ingreso inmediato de más de 50 contenedores críticos para operadoras como [[Continental Resources]], [[Taca Taca]], [[Posco]] y [[VMOS]].
- **La Trampa de la Auditoría Ex-Post:** El beneficio arancelario del RIGI exige que cada bien de capital importado permanezca afectado exclusivamente al Vehículo de Proyecto Único (VPU) durante toda la vida útil o período fiscal. En la industria, contratistas y subcontratistas rotan equipos habitualmente entre áreas concesionadas bajo distintos regímenes tributarios.
- **Riesgo Económico y Penal:** Una inconsistencia detectada en fiscalizaciones posteriores puede anular las exenciones arancelarias, detonar penalidades de hasta el 300% del valor CIF y amenazar la estabilidad jurídica del RIGI para toda la compañía.

---

## 3. La Solución Tecnológica: RIGI Asset & Customs Tracking Engine

Una suite SaaS B2B multi-tenant con arquitectura híbrida (Cloud + Edge):

1. **Conector Middleware Aduanero (Shadow API):**
   - Interoperabilidad directa con el Sistema Informático Malvina (SIM) y ventanillas electrónicas aduaneras para captura automática de despachos, CUITs, posiciones arancelarias y declaraciones juradas de VPU.
2. **Matching Automatizado ERP vs. VPU:**
   - Conciliación algorítmica entre las órdenes de compra / inventarios de SAP/Oracle y el listado taxativo de bienes de capital aprobados por el Ministerio de Economía bajo el RIGI.
3. **Geocercas IoT y Certificación de Afectación Física en Yacimiento:**
   - Integración con dispositivos telemáticos / sensores IoT instalados en los equipos pesados (rigs, bateas, generadores, turbinas, módulos DLE) para certificar en tiempo real que el activo opera dentro de los polígonos geoespaciales del VPU autorizado.
4. **Bóveda Criptográfica Audit-Ready:**
   - Generación de expedientes de compliance sellados en blockchain o registros inmutables, listos para ser presentados con un solo clic ante cualquier requerimiento de auditoría de la AFIP, Aduana o Secretarías de Minería provinciales.

---

## 4. Métricas de Impacto y Modelo de Negocio

| Indicador | Gestión Tradicional / Manual | Con Plataforma SaaS Green Channel |
| :--- | :--- | :--- |
| **Tiempo de Preparación Auditoría Ex-Post** | 3 a 6 meses de búsqueda documental | Instantáneo (< 5 minutos) |
| **Riesgo de Multas por Desvío de Activos** | Alto (rotación no documentada) | Cero (geocercas y alertas preventivas) |
| **Costos Administrativos de Compliance** | US$ 150.000 - US$ 400.000 / año por proyecto | Suscripción SaaS: US$ 3.000 - US$ 8.000 / mes |
| **Monetización** | N/A | SaaS recurrente + fee por activo telemático monitoreado |

---

## 5. Riesgos Críticos y Factores de Falla

- **Resistencia de Subcontratistas EPC a la Telemática:** Los contratistas independientes suelen resistirse al monitoreo en tiempo real de su maquinaria por temores comerciales. *Mitigación:* Cláusula de exigencia contractual obligatoria por parte del operador principal (mandato RIGI).
- **Zonas Sombra de Telecomunicaciones en Cordillera:** Falta de señal 4G/5G en salares y alta montaña. *Mitigación:* Almacenamiento local en el dispositivo (Edge buffering) y sincronización automática vía satélite LEO (Starlink/Satellogic).

---

## 6. Próximo Movimiento

1. Presentar el caso de uso a los directores de Supply Chain y Asuntos Regulatorios de las 5 operadoras líderes con aprobaciones RIGI activas ([[Continental Resources]], [[Posco]], First Quantum / [[Taca Taca]], [[YPF]]).
2. Desarrollar un prototipo del conector SIM con validación de geofencing sobre un set de 20 activos pesados en la Cuenca Neuquina y la Puna.

---

## Conexiones
- [[RIGI]]
- [[Aduana Green Channel]]
- [[Esceptico_Aduana_Green_Channel_RIGI]]
- [[Compliance_Compre_Local_8020_SaaS]]
- [[Continental Resources]]
- [[Taca Taca]]
- [[Posco]]
- [[Vaca Muerta]]
- [[Litio]]
- [[Cobre]]
