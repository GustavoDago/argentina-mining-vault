---
type: tech-lead-opp
tags: [mining, copper, exploration, due-diligence, saas, geology, ma, lunahuasi, san-juan]
sources:
  - [[raw/2026-07-16_news_mining_energy.md]]
  - [[raw/2026-07-15_news_mining_energy.md]]
  - [[raw/2026-07-23_news_mining_energy.md]]
confidence: medium
last_update: 2026-10-02
---

# GeoIntel_Andino — Plataforma de Due Diligence Geológico y Alertas M&A

> ⭐ NUEVO — Identificado Oct 2026. Urgencia: 🟡 MEDIA (mercado early stage pero con alta velocidad de M&A).

## El Gatillo Factual

**NGEx Minerals / Lunahuasi (San Juan, julio 2026):** La campaña de perforación Fase 4 concluyó con resultados de clase mundial: el pozo DPDH077 en la zona *Jupiter* interceptó **57,75 metros con 9,41% CuEq**, incluyendo un tramo espectacular de **8 metros con 37,38% CuEq** desde los 310 metros. Esto posiciona a Lunahuasi como el potencial megaproyecto de cobre de siguiente generación en el [[Distrito Vicuña]].

**Rio Tinto + Mogotes Metals / Filo Sur (julio 2026):** Rio Tinto firmó una inversión estratégica de US$ 15 millones para adquirir ~5% de Mogotes Metals con exclusividad sobre el proyecto **Filo Sur** (100 km² al sur de Filo del Sol). Período de exclusividad de 15 meses para análisis geotécnico con herramientas propias de Rio Tinto.

**Taca Taca / First Quantum (julio 2026):** First Quantum negocia la venta de participaciones minoritarias a Rio Tinto, Mitsubishi y Mitsui → los grandes compradores estratégicos se posicionan en etapa de exploración avanzada.

**Métricas de contexto:** Al julio de 2026, el sector minero proyecta exportaciones récord de **US$ 9.000 millones** (+49% interanual). La velocidad de entrada de capital extranjero genera una necesidad masiva de due diligence técnico rápido.

## El Gap de Mercado

Los inversores institucionales (fondos junior, strategic buyers, royalty companies) que quieren posicionarse en el corredor andino argentino enfrentan tres problemas:
1. **Datos fragmentados:** Los resultados de perforación están dispersos en SEDAR+, ASX, Boletín Oficial y páginas de IR de las empresas, en formatos incompatibles.
2. **Latencia informacional:** Las señales de M&A (alianzas estratégicas, opciones de compra, derechos de tanteo) aparecen cuando ya es tarde para negociar un buen precio de entrada.
3. **Falta de benchmarks:** No existe una plataforma que compare las leyes de distintos proyectos en el mismo corredor geológico usando estándares homogéneos (CIM, JORC).

## El Play Tech

**Plataforma SaaS de inteligencia geológica y due diligence minero** para el corredor andino argentino (San Juan, Salta, Catamarca):

### Módulo 1 — Drill Data Aggregator
Repositorio estandarizado de datos de perforación pública:
- Ingesta automática de comunicados de prensa (NI 43-101, ASX) con NLP
- Normalización de formatos QAQC (conversión a CuEq estándar, corrección por densidad, dilución)
- Indexación por proyecto, zona, método de análisis y laboratorio
- Visualización 3D básica de los datos de collar/assay

### Módulo 2 — Resource Estimation Assistant (IA)
Herramienta de estimación preliminar de recursos usando datos públicos:
- **Kriging + ML** sobre datos de campañas parciales para estimar recursos inferred/indicated
- Benchmark automático vs. proyectos comparables en el mismo corredor geológico
- Generación de rangos de recursos con intervalos de confianza (para due diligence no vinculante)
- **No reemplaza al QP** — es una herramienta de screening previo al due diligence técnico formal

### Módulo 3 — M&A Signal Alerts
Monitor de alertas tempranas sobre movimientos estratégicos:
- Agregación de EDGAR, SEDAR+, ASX y Boletín Oficial argentino
- Detección de señales: nuevas participaciones minoritarias, acuerdos de exclusividad, derechos de tanteo, opciones de compra, cambios en el share register
- Alertas tempranas: cuando una major (BHP, Rio Tinto, Glencore) ingresa a un proyecto junior → señal de validación técnica implícita
- Ejemplo concreto: la inversión de Rio Tinto en Mogotes Metals/Filo Sur fue detectable 2 semanas antes del anuncio en los cambios de registro accionarial en SEDAR

## Tech Stack
- **NLP:** spaCy + LLM fine-tuned para NI 43-101 / ASX announcements
- **Geoestadística:** PyGS / SGeMS (Kriging, Gaussian Simulation), variogram fitting
- **3D Viz:** Three.js o Leapfrog API (web-based drill visualization)
- **Data Feeds:** SEDAR+ API, ASX Announcements API, SEGEMAR web scraper, Boletín Oficial RIGI scraper
- **Alertas:** Websockets + Email + Slack integration para notificaciones en tiempo real

## Riesgo Crítico
Los datos de perforación son el activo más confidencial de una exploradora junior. La propuesta de valor debe construirse sobre **datos públicos + anonimizados** con una capa premium para datos propietarios. El riesgo legal de interpretaciones erróneas de recursos (que luego se usen para decisiones de inversión) requiere disclaimers fuertes y posiblemente una regulación de actividad de consultoría.

## Usuarios Target
1. **Royalty companies** (Franco-Nevada, Wheaton, Osisko) buscando corredor andino
2. **Fondos junior mineros** (Sprott, Red Cloud) con exposición a San Juan/Salta
3. **Strategic buyers** (BHP, Rio Tinto Ventures, Mitsubishi Materials) evaluando optionalidad
4. **M&A boutiques** especializadas en minería latinoamericana

## Próximo Movimiento
1. Construir MVP del Módulo 3 (M&A Signal Alerts) con datos públicos de SEDAR+ → menor barrera de entrada y mayor velocidad de validación con inversores.
2. Validar el modelo de datos con SEGEMAR y la Cámara Minera de San Juan (CMSJ).
3. Presentar piloto a un fondo de royalties (Franco-Nevada o Wheaton Precious Metals) que ya tiene exposición al corredor Vicuña.

---
**Backlinks:** [[Lunahuasi]], [[Distrito Vicuña]], [[Los Azules]], [[Taca Taca]], [[Filo del Sol]], [[Cobre]], [[San Juan]], [[RIGI]].
