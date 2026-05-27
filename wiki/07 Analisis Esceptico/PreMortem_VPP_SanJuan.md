---
type: analysis
tags: [risk-analysis, opportunity, copper, energy, methodology]
sources: [[VPP_Mineria_San_Juan]], [[Distrito Vicuña]], [[Los Azules]], [[RIGI]], [[ENRE]], [[San Juan]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: VPP Minería San Juan — Orquestación de Micro-Redes para Cobre

> **Tesis bajo análisis:** [[VPP_Mineria_San_Juan]]
> **Análisis escéptico previo:** [[Esceptico_VPP_San_Juan]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2028. El proyecto VPP Minería San Juan ha sido abandonado. La "San Juan Energy API" nunca pasó de la etapa de especificación. Ninguna minera del cluster de cobre suscribió un contrato de orquestación energética. Se perdieron US$ 4-7 millones de desarrollo y 24 meses de capital humano especializado.

### Horizonte Operativo (90 días desde el lanzamiento)

La plataforma de Balance de Carga Predictivo fue desplegada en modo piloto conectándose al sistema SCADA de la subestación experimental instalada por [[Los Azules]] en Calingasta. En la primera semana, el sistema generó correctamente las señales de despacho óptimo entre la planta solar piloto (5 MW) y un BESS de 2 MWh. Sin embargo, al intentar conectar el pronóstico meteorológico con el algoritmo de despacho, se descubrió que la estación meteorológica más cercana con datos horarios fiables estaba a 180 km en San José de Jáchal, y que los modelos de predicción solar (GHI/DNI) del SMN tienen un error del ±25% en zonas cordilleranas de alta montaña por la turbulencia convectiva de las quebradas. El algoritmo de despacho oscilaba violentamente entre "full solar" y "full GNL" cada 2 horas, generando ciclos de arranque/parada de los generadores GNL que destruyeron los inyectores en 45 días (vida útil especificada: 18 meses). El costo de reparación fue de US$ 380.000, pagado por la VPP como cláusula de garantía del piloto.

### Horizonte Regulatorio (12-18 meses)

CAMMESA emitió la Resolución 204/2027 que estableció que toda generación distribuida conectada al SADI (Sistema Argentino de Interconexión) debe contar con un "Agente del MEM" (Mercado Eléctrico Mayorista) habilitado que responda a las directivas de despacho centralizadas. La VPP de San Juan operaba en modo "isla virtual" orquestando generación on-site sin coordinación con CAMMESA, lo que constituía una violación del Marco Regulatorio Eléctrico (Ley 24.065). CAMMESA intimó a McEwen Copper y BHP a desconectar la VPP y regularizar su situación como agente del MEM. El proceso de habilitación como Agente del MEM requería: constitución de una sociedad con capital mínimo de US$ 5M, presentación de un Estudio de Acceso Eléctrico ante el ENRE (plazo: 12-18 meses), y cumplimiento de la Resolución SE 281/2017 de seguridad de instalaciones.

### Horizonte Estructural (3-5 años)

La resolución del conflicto eléctrico entre [[Distrito Vicuña]] y [[Los Azules]] no fue tecnológica sino política. La provincia de San Juan, presionada por BHP, negoció con Nación la construcción de una **segunda línea de 500 kV** (Mendoza-San Juan Norte) financiada con regalías anticipadas de cobre, cuyo cronograma de finalización es 2030-2031. La promesa de la nueva línea eliminó la urgencia de las micro-redes off-grid: ambas mineras decidieron diseñar sus operaciones para arrancar con generación diésel transitoria (más cara pero sin riesgo regulatorio) y migrar a la red interconectada cuando la segunda línea se materialice. La VPP se quedó sin propuesta de valor: nadie quiere invertir en una infraestructura transitoria de US$ 200-400M (solar + BESS + GNL distribuido) cuando la solución permanente (línea de 500 kV) ya tiene financiamiento comprometido.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Carlos Marchetti — Ingeniero Eléctrico Senior, Ex-Director de Despacho de CAMMESA
**Rol:** 28 años en el sistema eléctrico argentino. Diseñó los modelos de despacho económico del MEM durante la crisis energética de 2004-2007. Consultor del BID para reformas regulatorias eléctricas en Latinoamérica.
**Justificación:** Es la persona que mejor puede evaluar si una VPP privada que orquesta generación distribuida entre múltiples usuarios puede operar legalmente dentro del marco regulatorio argentino sin constituirse como Agente del MEM. Conoce los puntos de fractura entre la regulación federal (ENRE/CAMMESA) y los entes reguladores provinciales (EPRE San Juan).

### Agente 2: Ing. Alejandra Ponce — Ingeniera Mecánica Especialista en Generación Térmica Distribuida
**Rol:** 15 años diseñando plantas de generación diésel y GNL para operaciones mineras en altura en Chile y Perú (Codelco, Southern Copper). Responsable de la puesta en marcha de la micro-red de la mina Quebrada Blanca (Teck, 4.400 msnm).
**Justificación:** Puede evaluar la viabilidad operativa real de orquestar algorítmicamente generadores GNL a 3.500-4.200 msnm, donde la pérdida de potencia por altitud es del 25-35% y los ciclos de arranque/parada degradan los componentes a una velocidad muy superior al nivel del mar.

### Agente 3: Dr. Facundo Bertrán — Economista Energético y Analista de Project Finance
**Rol:** Director de project finance en una boutique de inversión especializada en energías renovables en Argentina. Estructuró los PPAs (Power Purchase Agreements) de tres parques solares en San Juan.
**Justificación:** Debe validar si el modelo de negocio de la VPP (cobrar una suscripción SaaS por orquestación energética) puede competir en precio con la alternativa que las mineras ya conocen y confían: contratar generación diésel de emergencia a un operador independiente (ej. APR Energy, Aggreko) y esperar la segunda línea de 500 kV.

### Agente 4: Ing. Martín Serrano — Arquitecto de Sistemas SCADA/ICS e Ingeniero de Ciberseguridad Industrial
**Rol:** Consultor senior en ciberseguridad de sistemas de control industrial (ICS/OT) para el sector energético. Certificado ISA/IEC 62443. Asesor de la Dirección Nacional de Ciberseguridad para infraestructura crítica energética.
**Justificación:** La VPP propone una "San Juan Energy API" que conecte los sistemas SCADA de múltiples mineras. Esto crea una superficie de ataque ciber-física donde un compromiso en la API puede provocar el apagón simultáneo de múltiples operaciones mineras de alta criticidad. Serrano puede evaluar si la arquitectura propuesta cumple con ISA/IEC 62443 y si las mineras aceptarían exponer sus SCADA a una API compartida.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Marchetti (Regulación Eléctrica)

**A) El detalle ignorado por optimismo:**
La tesis asume que es posible crear una "isla virtual" de orquestación energética entre mineras vecinas (Josemaría, Los Azules, Filo del Sol) "sin pasar por CAMMESA". Esto es una fantasía regulatoria. En el marco del MEM argentino, TODA generación mayor a 1 MW conectada al SADI o que suministre a un Gran Usuario del MEM (y toda minera de cobre con consumos de 50-200 MW lo es) debe estar despachada por CAMMESA. No existe la figura de un "orquestador privado de despacho" entre agentes del MEM. La Ley 24.065 asigna el monopolio natural de despacho al Organismo Encargado del Despacho (OED), que es CAMMESA.

Si la VPP opera en modo 100% off-grid (isla eléctrica sin conexión al SADI), puede evitar la regulación del MEM, pero entonces pierde la posibilidad de vender excedentes a la red y de usar la red como backup cuando la generación distribuida no alcance. Y operar una mina de cobre de 150 MW en isla eléctrica pura (sin backup de red) es un riesgo que ningún board de BHP o McEwen Mining aceptaría: un apagón de 4 horas en una planta concentradora congela el circuito de molienda y genera un daño de US$ 2-5M.

**B) Cadena de eventos hasta el fracaso:**
1. VPP San Juan se constituye como empresa de servicios energéticos.
2. Firma un PPA con McEwen Copper para suministrar 50 MW de generación solar + GNL orquestada.
3. CAMMESA recibe la notificación de la nueva generación y solicita la habilitación como Agente Generador del MEM.
4. VPP San Juan no cumple los requisitos de capital mínimo ni los estudios de conexión al SADI exigidos por la Resolución SE 61/1992.
5. CAMMESA notifica al ENRE que hay generación no despachada operando en su jurisdicción.
6. El ENRE intima a VPP San Juan a cesar operaciones bajo apercibimiento de multa de AR$ 50M.
7. McEwen Copper, para evitar contingencias regulatorias, rescinde el PPA.
8. Las demás mineras del cluster cancelan las negociaciones preventivamente.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Imposibilidad legal de operar como orquestador privado de despacho sin ser Agente del MEM | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Prohibición regulatoria de "arbitraje energético entre mineras" sin habilitación CAMMESA | Alta (>60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Mineras no aceptan operar en isla eléctrica pura sin backup de red interconectada | Alta (>60%) | Alta (20-50% Capex) | Fulminante (<30 días) |

---

### Agente 2: Ing. Ponce (Generación Térmica en Altura)

**A) El detalle ignorado por optimismo:**
La tesis propone orquestar generación híbrida solar/GNL/BESS a 3.500-4.200 msnm como si el despacho algorítmico resolviera los problemas termodinámicos del hardware. La realidad es que un generador GNL (turbina o motor reciprocante) pierde entre el 25% y el 35% de su potencia nominal a 4.000 msnm por la reducción de densidad del aire (0,64 kg/m³ vs 1,225 kg/m³ a nivel del mar). Un generador especificado en 10 MW produce efectivamente 6,5-7,5 MW en la Puna. Esto significa que el Capex por MW efectivo es un 40-50% mayor al calculado a nivel del mar.

Pero el problema más grave es el régimen de operación. El algoritmo de despacho de la VPP necesita arrancar y parar los generadores GNL según la disponibilidad solar. Cada arranque de una turbina GNL en frío a 4.000 msnm consume 90-120 minutos y un 15% extra de combustible en la fase de calentamiento. Los ciclos de arranque/parada degradan los inyectores, las bujías y los rodamientos principales a una velocidad 3x superior a la operación en régimen continuo. La vida útil del overhaul mayor pasa de 30.000 horas (operación continua) a 12.000-15.000 horas (operación cíclica), triplicando el costo de mantenimiento mayor.

**B) Cadena de eventos hasta el fracaso:**
1. Se instalan 4 generadores GNL de 10 MW nominal (40 MW nominales) para complementar 30 MW de generación solar con tracking.
2. Los 4 generadores producen efectivamente 26-30 MW (no 40 MW) por pérdida de altitud.
3. El déficit de 10-14 MW se compensa con un BESS de 20 MWh que se especificó como "buffer de transición", no como fuente primaria.
4. En los días nublados consecutivos del invierno sanjuanino (junio-agosto, con 40% menos de irradiación), el BESS se agota en 3-4 horas y los generadores deben operar 24/7 en modo base, consumiendo GNL a razón de US$ 8-12/MMBTU (vs. el costo de red interconectada de US$ 3-4/MMBTU equivalente).
5. El Opex de GNL en invierno supera el costo de comprar energía del MEM por un factor de 2-3x, destruyendo la propuesta de valor económico de la VPP.
6. Las mineras descubren que la VPP es más barata que la red solo en verano (octubre-marzo) y más cara en invierno. El ahorro promedio anualizado se reduce al 5-8%, insuficiente para justificar el riesgo operativo.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Pérdida de potencia del 25-35% en generadores GNL por altitud | Alta (>60%) | Alta (20-50% Capex) | Fulminante (<30 días) |
| Degradación acelerada 3x por operación cíclica de turbinas GNL | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |
| Opex de GNL en invierno supera costo de red interconectada en 2-3x | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |

---

### Agente 3: Dr. Bertrán (Economía Energética / Project Finance)

**A) El detalle ignorado por optimismo:**
El modelo de negocio asume que las mineras pagarán una suscripción SaaS por el "Balance de Carga Predictivo". Pero las mineras de cobre de clase mundial (BHP, McEwen, Lundin) no compran software de orquestación energética: contratan una solución EPC (Engineering, Procurement, Construction) turnkey de generación. El decision-maker no es el CTO sino el VP de Operaciones, que quiere un contrato PPA a precio fijo en US$/MWh con un operador que asuma el riesgo de disponibilidad. Si el generador no produce, el operador paga la penalidad. La VPP propone exactamente lo contrario: vender software y que la minera asuma el riesgo de los activos.

El competidor real no es la red interconectada sino **Aggreko/APR Energy/Atlas Copco Power**, que ya operan generación temporal diésel en sitios mineros en Argentina y tienen contratos con BHP y Glencore globalmente. Estas empresas pueden instalar 50-100 MW de generación diésel modular en 60-90 días, a un costo de US$ 0.18-0.22/kWh, con disponibilidad garantizada del 98%. La VPP necesita demostrar un costo inferior a US$ 0.15/kWh para ser competitiva, y con la pérdida de potencia por altitud y el Opex de GNL invernal, es muy difícil bajar de US$ 0.20/kWh.

**B) Cadena de eventos hasta el fracaso:**
1. VPP San Juan modela un costo nivelado de energía (LCOE) de US$ 0.12/kWh (solar + BESS + GNL complementario).
2. El LCOE real, ajustado por altitud, estacionalidad y costos de O&M, resulta ser US$ 0.19-0.23/kWh.
3. BHP solicita una cotización paralela a Aggreko para 80 MW de generación diésel modular en Josemaría.
4. Aggreko cotiza US$ 0.20/kWh con 98% de disponibilidad garantizada, entrega en 75 días, y sin riesgo de integración SCADA.
5. BHP elige Aggreko porque: (a) el costo es similar, (b) no requiere integrar sistemas SCADA entre mineras competidoras, (c) Aggreko asume 100% del riesgo de disponibilidad, y (d) la solución es temporal hasta que se construya la segunda línea de 500 kV.
6. Sin BHP como cliente anchor (Josemaría = 50% de la demanda del cluster), la VPP pierde masa crítica.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| LCOE real 60-90% mayor al modelado por ajustes de altitud y estacionalidad | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Competencia directa con operadores diésel temporales (Aggreko/APR) que asumen riesgo de disponibilidad | Alta (>60%) | Alta (20-50% Capex) | Fulminante (<30 días) |
| Solución transitoria innecesaria si se confirma financiamiento de segunda línea 500 kV | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |

---

### Agente 4: Ing. Serrano (Ciberseguridad Industrial)

**A) El detalle ignorado por optimismo:**
La "San Juan Energy API" propone interconectar los sistemas SCADA de Josemaría (BHP/Lundin), Los Azules (McEwen Copper) y Filo del Sol para coordinar despacho energético. Esto requiere que tres empresas mineras competidoras abran sus redes OT (Operational Technology) a un software de terceros, creando un único punto de falla ciber-físico que podría apagar simultáneamente tres minas de cobre con un valor combinado de US$ 25.000M.

En el mundo de la ciberseguridad industrial, las redes SCADA de las minas son "air-gapped" (aisladas de internet) precisamente para evitar este escenario. La norma ISA/IEC 62443 Level 3 (requerida por BHP globalmente) exige que no exista ninguna conexión directa entre la red OT de la mina y redes externas. Una API que envía señales de despacho a los sistemas de control de generación eléctrica de una mina es, por definición, una "conduit" que viola el air gap.

BHP tiene un estándar global llamado "OT Cybersecurity Minimum Requirements" que prohíbe explícitamente que cualquier software externo envíe comandos de control a sistemas de generación eléctrica de mina. McEwen, como empresa canadiense, está sujeta a los "CSA Z246.1 Security Management for Critical Infrastructure" que imponen restricciones similares.

**B) Cadena de eventos hasta el fracaso:**
1. VPP San Juan diseña la "San Juan Energy API" como una REST API que envía señales de setpoint a los PLCs de generadores y BESS de cada minera.
2. BHP somete la API a una auditoría de ciberseguridad IEC 62443 pre-conexión (procedimiento estándar global de BHP para cualquier integración OT).
3. La auditoría detecta que la API viola el requisito de air gap (Zone & Conduit Level 3) y que no implementa autenticación de dispositivos de campo conforme al estándar NERC CIP-007.
4. El CISO global de BHP emite una directiva de "No Connect" para Josemaría.
5. Sin BHP, la API no tiene masa crítica (Josemaría = 50% de la demanda del cluster).
6. McEwen Copper, al enterarse del rechazo de BHP, cancela preventivamente su piloto para no asumir sola el riesgo reputacional de un ciberincidente.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Rechazo por violación del air gap SCADA (IEC 62443 Level 3) | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Estándares globales de BHP y McEwen prohíben APIs externas enviando comandos a OT de mina | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Superficie de ataque unificada: compromiso de la API apaga 3 minas simultáneamente | Media (30-60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Imposibilidad legal de operar como orquestador sin ser Agente MEM | Marchetti | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 2 | Rechazo por violación del air gap SCADA (IEC 62443) | Serrano | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 3 | Estándares globales BHP/McEwen prohíben APIs externas en OT | Serrano | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 4 | LCOE real 60-90% mayor al modelado | Bertrán | Operativo | Alta | Crítica | Rápida | **A×C** |
| 5 | Prohibición de arbitraje energético sin habilitación CAMMESA | Marchetti | Regulatorio | Alta | Crítica | Gradual | **A×C** |
| 6 | Pérdida de potencia 25-35% en GNL por altitud | Ponce | Operativo | Alta | Alta | Fulminante | **A×A** |
| 7 | Competencia directa con Aggreko/APR (riesgo de disponibilidad asumido por ellos) | Bertrán | Estructural | Alta | Alta | Fulminante | **A×A** |
| 8 | Mineras no aceptan isla eléctrica sin backup de red | Marchetti | Operativo | Alta | Alta | Fulminante | **A×A** |
| 9 | Degradación acelerada 3x de turbinas por operación cíclica | Ponce | Operativo | Alta | Alta | Rápida | **A×A** |
| 10 | Superficie de ataque unificada apaga 3 minas simultáneamente | Serrano | Operativo | Media | Crítica | Rápida | **M×C** |
| 11 | Solución innecesaria si se confirma segunda línea 500 kV | Bertrán | Estructural | Media | Crítica | Gradual | **M×C** |
| 12 | Opex GNL invernal supera costo de red en 2-3x | Ponce | Operativo | Media | Crítica | Gradual | **M×C** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **BARRERA REGULATORIA INFRANQUEABLE (Vectores #1, #5, #8):** El marco regulatorio eléctrico argentino (Ley 24.065, CAMMESA, MEM) no contempla la figura de un "orquestador privado de despacho" entre grandes usuarios mineros. Toda generación >1 MW que suministre a un Gran Usuario debe ser despachada por CAMMESA. La VPP necesita o bien constituirse como Agente Generador del MEM (costo: US$ 5M, plazo: 18 meses, requisitos técnicos de interconexión complejos) o bien operar en isla eléctrica pura (riesgo operativo inaceptable para mineras de clase mundial que no toleran apagones).

2. **FORTALEZA DIGITAL IMPENETRABLE (Vectores #2, #3, #10):** Las mineras de cobre de clase mundial (BHP, McEwen) operan bajo estándares de ciberseguridad industrial (IEC 62443, NERC CIP, CSA Z246.1) que prohíben categóricamente la conexión de APIs externas a sus redes SCADA de generación. La "San Juan Energy API" es invendible como producto porque su premisa fundamental (enviar señales de despacho a los PLCs de generadores dentro de minas competidoras) viola el principio de air gap que estas empresas consideran innegociable. El CISO de BHP tiene poder de veto absoluto.

3. **PROPUESTA DE VALOR TRANSITORIA EN UN MERCADO QUE SE RESUELVE SOLO (Vectores #4, #7, #11):** La VPP es una solución de puente para un problema (falta de capacidad eléctrica) que se está resolviendo por la vía convencional (segunda línea de 500 kV) y por la competencia directa (generación diésel modular de Aggreko/APR). El LCOE real de la VPP, ajustado por altitud y estacionalidad, no es competitivo frente a la alternativa diésel temporal. Las mineras no invertirán en infraestructura permanente solar + BESS + GNL para un problema cuya solución definitiva (la línea de 500 kV) ya tiene financiamiento.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Rediseñar como "Energy Advisor SaaS" — Sin Despacho, Sin SCADA

- **Acción específica:** Abandonar completamente la capa de despacho (no enviar señales a SCADA). Pivotar a una plataforma de **advisory analítico**: modelado predictivo del costo de energía por hora (MEM vs. on-site), optimización de contratos PPA, y simulación de escenarios de generación propia para los equipos de planificación energética de las mineras. La plataforma NO controla nada: genera reportes y recomendaciones que el operador eléctrico de la mina ejecuta manualmente.
- **Responsable sugerido:** CTO de VPP San Juan.
- **Plazo de implementación:** Prototipo en 3 meses. Piloto con McEwen Copper (Los Azules, que es el más necesitado por el bloqueo de la línea de 500 kV) en 6 meses.
- **Costo estimado:** US$ 300.000-500.000 (vs. US$ 4-7M del modelo original con hardware y API SCADA).
- **Métrica de éxito:** Demostrar un ahorro modelado de ≥10% en el costo energético anual proyectado de Los Azules vs. el escenario baseline (diésel temporal de Aggreko).
- **Dependencias:** Acceso a las tarifas horarias del MEM (datos públicos de CAMMESA) y a las curvas de irradiación solar de San Juan (datos del INTI).

### Antídoto #2: Constituirse como Agente Generador del MEM desde el Día 1

- **Acción específica:** Si se insiste en la capa de generación y despacho, constituir la empresa como Agente Generador del MEM antes de instalar un solo panel solar. Esto requiere: sociedad con capital mínimo de US$ 5M, Estudio de Acceso Eléctrico aprobado por ENRE, y contratos de abastecimiento (PPA) registrados ante CAMMESA. Esto permite vender excedentes a la red, usar la red como backup, y operar dentro del marco legal.
- **Responsable sugerido:** Director legal de VPP San Juan + consultora regulatoria eléctrica especializada (ej. Bridas Energy Advisors, ESUCO).
- **Plazo de implementación:** 12-18 meses para completar la habilitación como Agente del MEM.
- **Costo estimado:** US$ 5M-8M en capital constitutivo + honorarios regulatorios + Estudio de Acceso.
- **Métrica de éxito:** Habilitación formal como Agente Generador del MEM emitida por CAMMESA/ENRE.
- **Dependencias:** Capacidad de la línea de 500 kV existente para admitir la inyección de generación distribuida (actualmente saturada al 90% por Distrito Vicuña).

### Antídoto #3: Alianza con un IPP Establecido — No Reinventar la Rueda

- **Acción específica:** En lugar de construir una VPP desde cero, aliarse con un Productor Independiente de Energía (IPP) que ya sea Agente del MEM y que ya opere generación renovable en San Juan (ej. 360 Energy, YPF Luz, JEMSE). El IPP aporta la habilitación regulatoria, el capital y la experiencia operativa. VPP San Juan aporta el algoritmo de optimización y los contratos con las mineras. Modelo de revenue share 70/30 (IPP/VPP).
- **Responsable sugerido:** CEO de VPP San Juan.
- **Plazo de implementación:** Negociación de JV en 4-6 meses. Primer proyecto conjunto en 12-15 meses.
- **Costo estimado:** US$ 500.000-1M en negociación de JV + desarrollo de software adaptado a los sistemas del IPP.
- **Métrica de éxito:** JV firmado con IPP establecido y primer PPA minero firmado conjuntamente.
- **Dependencias:** Interés del IPP en el segmento minero (actualmente operan parques solares para el MEM, no para clientes industriales aislados).

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Marchetti evalúa los antídotos:
- **Antídoto #1 (Advisory SaaS):** Resuelve completamente el riesgo regulatorio. Un software de modelado y advisory no necesita habilitación del MEM porque no genera, despacha ni comercializa energía. Es un servicio de consultoría digital. **Veredicto: regulatoriamente viable.**
- **Antídoto #2 (Agente del MEM):** Técnicamente correcto pero destruye el timeline y el Capex del proyecto. La habilitación tarda 12-18 meses y la línea de 500 kV está saturada, por lo que el Estudio de Acceso podría ser rechazado. **Riesgo de segundo orden: invertir US$ 5-8M en la habilitación y que el ENRE rechace la conexión por falta de capacidad en la línea existente.**
- **Antídoto #3 (JV con IPP):** El más pragmático. Pero los IPPs establecidos en San Juan (360 Energy, YPF Luz) ya tienen contratos PPA a largo plazo con CAMMESA a precios fijos. Aceptar un cliente minero industrial con demanda variable y picos de consumo altísimos puede no ser atractivo para su portafolio, especialmente si distorsiona su factor de planta.

### Ing. Ponce evalúa los antídotos:
- **Antídoto #1 (Advisory):** No resuelve el problema de hardware de las mineras (seguirán necesitando generación, solo que el advisory les dice cuándo encender cada fuente). Pero al eliminar la responsabilidad sobre los activos de generación, elimina el riesgo de degradación de turbinas y el Opex de GNL. **Sin riesgo de segundo orden.**
- **Antídoto #3 (JV con IPP):** Si el IPP aporta la generación solar y el BESS, el IPP asume el riesgo de disponibilidad, no VPP San Juan. Esto transforma la VPP de un operador de activos de generación a un "brain" de optimización. **Veredicto: correcto, si el IPP acepta asumir el riesgo de disponibilidad en altura (que es considerable).**

### Dr. Bertrán evalúa los antídotos:
- **Antídoto #1 (Advisory SaaS):** El TAM es pequeño. ¿Cuántas minas en San Juan necesitan un advisory energético SaaS? 3-5 minas grandes, con un fee de US$ 100-200K/año cada una. El negocio genera US$ 300-1.000K/año. No es venture-scalable. Pero es un negocio legítimo de consulting/SaaS de nicho con márgenes del 80% y riesgo de ejecución mínimo. **Veredicto: viable como lifestyle business, no como unicornio.**
- **Antídoto #3 (JV con IPP):** El modelo de revenue share funciona si el IPP es el que pone los US$ 200-400M de Capex en generación solar + BESS. En ese caso, VPP San Juan captura un 30% de los ingresos con un Capex de US$ 1M (el software). Los unit economics son excelentes. **Veredicto: el único modelo con potencial de escala.**

### Ing. Serrano evalúa los antídotos:
- **Antídoto #1 (Advisory SaaS):** Resuelve completamente el riesgo de ciberseguridad. Un software que genera reportes no necesita acceso a la red OT de la mina. Se conecta a datos públicos (CAMMESA, pronóstico meteorológico) y a datos que la mina exporta voluntariamente a una zona DMZ. No viola el air gap. **Veredicto: ciber-seguro.**
- **Antídoto #3 (JV con IPP):** Si el IPP opera sus propios activos de generación con su propio SCADA, y la "San Juan Energy API" se limita a una interfaz entre el SCADA del IPP (un solo sistema bajo su control) y los datos de demanda de la mina (exportados a una DMZ), el riesgo de ciberseguridad se reduce drásticamente. Ya no hay conexión directa entre los SCADA de mineras competidoras. **Parche correctivo: la API debe conectar el SCADA del IPP con las curvas de demanda de las mineras, no los SCADA de las mineras entre sí.**

---

## VEREDICTO FINAL DEL FACILITADOR

### 🔴 REDISEÑAR PLAN

El modelo original de VPP Minería San Juan (orquestación directa de micro-redes mineras vía API SCADA, operando fuera del MEM) es **inviable en su forma actual** por tres razones simultáneas e independientes: (1) la regulación eléctrica argentina prohíbe el despacho privado entre grandes usuarios, (2) los estándares de ciberseguridad de las mineras globales prohíben APIs externas en sus redes SCADA, y (3) el LCOE real no es competitivo frente a la alternativa diésel temporal.

**Recomendación:** Adoptar una **estrategia en dos fases**:

1. **Fase inmediata (0-12 meses):** Lanzar el **Antídoto #1 — Energy Advisor SaaS**. Producto de bajo riesgo, bajo Capex (US$ 300-500K), ciber-seguro y regulatoriamente limpio. Genera credibilidad en el cluster minero de San Juan y demuestra el valor del algoritmo de optimización sin tocar un solo SCADA. Clientes target: Los Azules (McEwen), Gualcamayo, Veladero.

2. **Fase estratégica (12-36 meses):** Negociar el **Antídoto #3 — JV con un IPP establecido** (YPF Luz, 360 Energy, JEMSE) que aporte la habilitación como Agente del MEM, el Capex de generación y el riesgo de disponibilidad. VPP San Juan aporta el "brain" de optimización, los contratos con las mineras y la arquitectura de la API (diseñada para conectar el SCADA del IPP con datos de demanda minera en una DMZ segura, NO para interconectar SCADAs de mineras competidoras).

**El verdadero IP de VPP San Juan no es la micro-red ni la API; es el modelo predictivo que sabe cuánto le cuesta a cada mina cada MWh en cada hora del año y le dice cuándo comprar del MEM, cuándo generar on-site y cuándo almacenar en BESS.** Monetizar la inteligencia, no la infraestructura.

---

**Backlinks:** [[VPP_Mineria_San_Juan]], [[Distrito Vicuña]], [[Los Azules]], [[Josemaría]], [[RIGI]], [[ENRE]], [[San Juan]], [[Cobre]], [[Pre-Mortem Framework]].
