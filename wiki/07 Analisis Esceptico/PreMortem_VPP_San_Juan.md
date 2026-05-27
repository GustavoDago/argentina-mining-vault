---
type: analysis
tags: [risk-analysis, opportunity, energy, regulatory, mining, methodology]
sources: [[VPP_Mineria_San_Juan]], [[RIGI]], [[San Juan]], [[Distrito Vicuña]], [[Los Azules]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: Orquestación de Micro-Redes y VPP Mineras (San Juan Hub)

> **Tesis bajo análisis:** [[VPP_Mineria_San_Juan]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 Fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: EL ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2027. El proyecto de la **Planta de Energía Virtual (VPP) San Juan Hub** ha colapsado. La red de micro-redes orquestadas nunca llegó a operar en tiempo real. Los gigantes del cobre (McEwen, BHP y Lundin) retiraron su apoyo financiero y técnico del consorcio energético. CAMMESA y la Secretaría de Energía de la Nación aplicaron multas regulatorias millonarias, declarando ilegal el sistema de liquidación y compensación privada de energía. La startup de software encargada del despacho algorítmico se declaró en quiebra tras quemar US$ 3.2 millones en capital de riesgo.

### Horizonte Operativo (90 días desde el lanzamiento)
Durante los primeros 90 días, la integración técnica con los sistemas de control de las minas fue imposible. Los equipos de ciberseguridad industrial y redes de las operadoras mineras (Josemaría y Los Azules) bloquearon terminantemente la instalación de agentes de software externos de AndesLogistics/VPP en sus redes operativas (OT). Argumentaron que conectar un software basado en la nube para controlar el despacho de generadores y almacenamiento BESS violaba las normas de seguridad internacionales IEC 62443 y sus políticas corporativas internas de *Zero Trust*. La VPP tuvo que depender de lecturas manuales en archivos planos diferidos por 24 horas, anulando por completo la capacidad del algoritmo de balancear la carga predictiva en tiempo real.

### Horizonte Regulatorio (12-18 meses)
CAMMESA (Compañía Administradora del Mercado Mayorista Eléctrico) y el ENRE emitieron una resolución conjunta que prohibió el arbitraje bilateral directo ("wheeling") de energía off-grid entre proyectos mineros sin mediación del Mercado Mayorista Eléctrico (MEM). Bajo la Ley 24.065, cualquier transferencia física de electrones entre dos plantas vecinas separadas por el territorio nacional debe considerarse transporte de interés público y está sujeta a peajes de red nacionales y regulaciones de despacho de CAMMESA. El motor de liquidación ("settlement engine") de la VPP fue catalogado como un "mercado eléctrico paralelo ilegal", deteniendo la facturación de los PPAs privados.

### Horizonte Estructural (3-5 años)
Bajo el paraguas de las inversiones del RIGI, el gobierno nacional concretó una licitación de infraestructura para el tendido de la línea de alta tensión de 500kV "San Juan - Rodeo" financiada de manera directa por capitales estatales chinos mediante un acuerdo bilateral de swap de divisas. La obra civil se completó en un tiempo récord de 18 meses, 2 años antes de lo previsto por los modelos de Andes-VPP. Al resolverse la saturación física de la red de 500kV, la energía provista por el SADI (Sistema Argentino de Interconexión) volvió a fluir de forma abundante a una tarifa industrial regulada 3 veces menor que el costo nivelado de generación (LCOE) de las micro-redes de GNL, BESS y solar off-grid del Hub San Juan. La VPP quedó obsoleta antes de recuperar su costo de desarrollo.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Norberto "Tito" Femenía — Especialista en Regulación y Despacho del MEM
*   **Rol:** 30 años en CAMMESA, ex-director del Área de Despacho y Contratos del Mercado Mayorista. Consultor en marcos regulatorios del sector eléctrico argentino.
*   **Justificación:** Conoce todas las trampas legales de la Ley 24.065, las resoluciones de la Secretaría de Energía, y las restricciones de peajes de red en el Mercado a Término de Energías Renovables (MATER).

### Agente 2: Ing. Gabriela Scalise — Experta en Ciberseguridad Industrial OT (IEC 62443)
*   **Rol:** Ex-CISO de YPF Luz y asesora en seguridad cibernética para infraestructura crítica en Sudamérica.
*   **Justificación:** Sabe por qué los directores de IT/OT mineros prefieren dejar una planta sin energía antes que permitir una conexión API externa que controle sus subestaciones eléctricas.

### Agente 3: Dr. Esteban Baldi — Abogado especialista en Project Finance e Infraestructura Compartida
*   **Rol:** Socio de un estudio corporativo de Buenos Aires que estructuró los contratos de financiamiento (PPA y fideicomisos) para parques eólicos y solares del RIGI.
*   **Justificación:** Puede identificar si los contratos de la VPP son "bancables" por la IFC y el BID Invest y evaluar la validez de los contratos bilaterales off-grid.

### Agente 4: Ing. Diego Russo — Ingeniero de Sistemas BESS y Microgrids en Altura
*   **Rol:** Ingeniero de aplicaciones senior de una multinacional de almacenamiento de energía con experiencia en la instalación de bancos de baterías de litio industriales en proyectos a más de 3.500 msnm.
*   **Justificación:** Conoce las limitaciones físicas del BESS en la altura (disipación térmica deficiente en atmósfera enrarecida y degradación de celdas por ciclos de frío extremo).

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Norberto "Tito" Femenía (Regulación)
*   **A) El detalle ignorado por optimismo:**
    Se creyó que por estar "off-grid" o aislados físicamente de la red troncal provincial de San Juan se podía operar sin la injerencia de CAMMESA. En Argentina, la regulación establece que si una micro-red genera y vende energía a un tercero utilizando cualquier porción de infraestructura pública o cruzando servidumbres de paso públicas, ingresa automáticamente a la jurisdicción del MEM. CAMMESA tiene el derecho de confiscar el despacho para garantizar la estabilidad del sistema nacional o exigir que toda la generación sea vendida al fondo de estabilización nacional a precios mínimos de costo, rompiendo el esquema de arbitraje dinámico de la VPP.
*   **B) Cadena de eventos hasta el fracaso:**
    1. Josemaría y Los Azules firman un contrato para intercambiar excedentes solares off-grid a través de una línea privada de 132kV de 15 km de longitud.
    2. La Secretaría de Energía de San Juan inspecciona la línea y declara que cruza una ruta provincial, catalogándola como "infraestructura sujeta a concesión de transporte".
    3. CAMMESA interviene y exige que los flujos sean despachados centralmente, cobrando un peaje punitorio de red retroactivo por "uso indirecto del SADI".
    4. La VPP no puede compensar financieramente las transacciones y las mineras rescinden el contrato para evitar litigios fiscales con la Nación.
*   **C) Cuantificación:**
    *   *Intervención regulatoria de CAMMESA por peajes y despacho centralizado:* Probabilidad: **Alta (>60%)** | Severidad: **Crítica (>50% Capex)** | Velocidad: **Rápida (1-6 meses)**.
    *   *Multas de la Secretaría de Energía por generación no registrada:* Probabilidad: **Media (30-60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Gradual (6-18 meses)**.

---

### Agente 2: Ing. Gabriela Scalise (Ciberseguridad)
*   **A) El detalle ignorado por optimismo:**
    Se asumió que las mineras aceptarían un SaaS en la nube para optimizar en tiempo real el setpoint de sus baterías y generadores de GNL. Para una mina que produce US$ 3 millones de cobre al día, el control energético es la arteria de vida. Un hackeo de la plataforma SaaS de la VPP podría apagar los sistemas de ventilación profunda o las bombas de drenaje, causando catástrofes humanitarias e inundaciones millonarias. Ningún director de operaciones OT firmará un permiso para que una API en la nube envíe comandos de escritura a un PLC de subestación.
*   **B) Cadena de eventos hasta el fracaso:**
    1. Se firma el piloto de software y se inicia la fase de integración con los sistemas SCADA de la mina.
    2. El comité de ciberseguridad minero audita la API de Andes-VPP y encuentra vulnerabilidades estándar de OWASP Top 10 en el dashboard de visualización.
    3. El CISO corporativo de la casa matriz en Vancouver veta el acceso OT a la red externa de forma permanente.
    4. La VPP queda reducida a un software de "visualización pasiva de datos viejos" en un dashboard secundario, incapaz de controlar activamente el despacho de energía. El ahorro proyectado cae del 18% al 0%.
*   **C) Cuantificación:**
    *   *Veto de IT/OT corporativo internacional a conexiones bidireccionales:* Probabilidad: **Alta (>60%)** | Severidad: **Crítica (>50% Capex)** | Velocidad: **Fulminante (<30 días)**.
    *   *Incidentes de ciberseguridad en APIs expuestas:* Probabilidad: **Media (30-60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Rápida (1-6 meses)**.

---

### Agente 3: Dr. Esteban Baldi (Finanzas/Project Finance)
*   **A) El detalle ignorado por optimismo:**
    La "bancabilidad" de la infraestructura compartida. Para financiar la construcción de los parques de generación híbridos (solar + GNL + BESS) de US$ 150M mediante Project Finance tradicional, los bancos multilaterales (IFC, BID Invest) exigen contratos PPA del tipo "Take-or-Pay" estables a 15-20 años con una contraparte calificada (Investment Grade). El modelo de VPP dinámico con tarifas marginales spot "inteligentes" no califica como flujo de caja predecible ante los comités de riesgo bancario. Los bancos no financian algoritmos de optimización spot en mercados eléctricos altamente intervenidos.
*   **B) Cadena de eventos hasta el fracaso:**
    1. La startup Andes-VPP busca US$ 80M en deuda corporativa para financiar las baterías del Hub.
    2. El BID Invest audita los contratos PPA dinámicos basados en arbitraje algorítmico y determina que la volatilidad regulatoria argentina y la variabilidad de las tarifas spot invalidan la garantía del flujo de servicio de deuda.
    3. El financiamiento es denegado. La startup debe recurrir a capital propio (Equity), encareciendo el costo de capital (WACC) al 18% anual.
    4. El proyecto se vuelve financieramente inviable comparado con las alternativas de autogeneración fija y simple.
*   **C) Cuantificación:**
    *   *Falta de bancabilidad de PPAs marginales spot para Project Finance:* Probabilidad: **Alta (>60%)** | Severidad: **Crítica (>50% Capex)** | Velocidad: **Lenta (>18 meses)**.
    *   *Encarecimiento del WACC por financiamiento en Equity:* Probabilidad: **Alta (>60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Rápida (1-6 meses)**.

---

### Agente 4: Ing. Diego Russo (Física del BESS en Altura)
*   **A) El detalle ignorado por optimismo:**
    La degradación térmica no modelada a 3.800 metros de altitud. A esa presión atmosférica, el aire tiene un 35% menos de densidad, lo que reduce la capacidad de enfriamiento por aire forzado de los contenedores BESS en más de un 40%. Las celdas de litio operan a temperaturas internas un 15°C superiores a lo normal, acelerando su degradación por "lithium plating" y acortando la vida útil del banco de baterías de 10 años a apenas 3.8 años. El costo de reposición de las celdas destruye la rentabilidad del arbitraje de energía.
*   **B) Cadena de eventos hasta el fracaso:**
    1. Se instalan contenedores de baterías estándar con refrigeración por aire en las inmediaciones del yacimiento.
    2. En el primer verano, los sistemas de refrigeración operan al 100% de su capacidad las 24 horas del día. El autoconsumo de energía de los aires acondicionados consume el 18% de la capacidad de la batería ("parasitic load").
    3. La temperatura interna de las celdas supera los 45°C durante ciclos de carga rápida solar.
    4. El sistema BMS (Battery Management System) de la batería reduce preventivamente la potencia de carga a la mitad para evitar eventos de fuga térmica (thermal runaway), impidiendo que la VPP capte los picos de generación solar excedente.
*   **C) Cuantificación:**
    *   *Degradación acelerada de BESS por refrigeración ineficiente a gran altitud:* Probabilidad: **Alta (>60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Lenta (>18 meses)**.
    *   *Elevada carga parásita (autoconsumo de enfriamiento):* Probabilidad: **Alta (>60%)** | Severidad: **Moderada (5-20% Capex)** | Velocidad: **Rápida (1-6 meses)**.

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Probabilidad | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Veto de IT/OT minera a conexiones API bidireccionales | Scalise | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Intervención y peajes regulatorios de CAMMESA | Femenía | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 3 | Falta de bancabilidad de PPAs marginales spot | Baldi | Estructural | Alta | Crítica | Lenta | **A×C** |
| 4 | Degradación acelerada de celdas BESS en altura | Russo | Operativo | Alta | Alta | Lenta | **A×A** |
| 5 | Elevada carga parásita del cooling de baterías | Russo | Operativo | Alta | Moderada | Rápida | **A×M** |
| 6 | Completamiento acelerado de línea 500kV de red | Baldi | Estructural | Media | Alta | Lenta | **M×A** |

### 🔴 Top 3 Vectores de Riesgo Sistémico
1.  **VETO DE SEGURIDAD INDUSTRIAL OT (Vector #1):** Sin control físico real sobre el hardware de generación y almacenamiento (imposibilitado por ciberseguridad industrial), la VPP no pasa de ser un sistema pasivo de contabilidad diferida. El valor del algoritmo en tiempo real cae a cero.
2.  **ASFIXIA REGULATORIA DEL DESPACHO MONOPÓLICO (Vector #2):** En Argentina, las transferencias off-grid comerciales privadas están sujetas a penalizaciones y peajes masivos por parte de CAMMESA. Operar al margen del MEM es inviable legalmente.
3.  **NO BANCABILIDAD FINANCIERA (Vector #3):** Sin la capacidad de estructurar PPAs fijos estables con grado de inversión, los bancos no otorgarán Project Finance para la sensórica y el software, limitando el crecimiento del hub.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Estructura del "Autoproductor Asociado MATER" de CAMMESA
*   **Acción específica:** Abandonar el modelo de arbitraje bilateral off-grid "gris". En su lugar, registrar formalmente al consorcio San Juan Hub como un **Autoproductor Asociado bajo la Res. 281-E/2017** del Mercado a Término de Energías Renovables (MATER). La línea privada de interconexión debe registrarse formalmente como una ampliación de transporte dedicada autorizada por el ENRE. Así, las transacciones de energía e intercambio se compensan y liquidan de manera 100% legal utilizando la infraestructura del MATER, pagando los peajes mínimos correspondientes pero operando con total estabilidad legal y estabilidad fiscal RIGI por 30 años.
*   **Responsable sugerido:** Director de Regulación Energética + Estudio Legal Regulatorio especializado.
*   **Plazo de implementación:** Tramitación en Secretaría de Energía y CAMMESA: 9-12 meses.
*   **Costo estimado:** US$ 150.000 en lobby, presentación técnica y tasas de tramitación.
*   **Métrica de éxito:** Aprobación por boletín oficial de la Secretaría de Energía del carácter de Autoproductor Asociado MATER para el Hub.
*   **Dependencias:** Voluntad de las mineras de firmar la documentación regulatoria integrada ante el ENRE.

### Antídoto #2: Arquitectura OT "Local Edge Air-Gapped" y Pasarela OPC-UA / Modbus
*   **Acción específica:** Modificar drásticamente la arquitectura del software. El algoritmo de balance predictivo y despacho no debe correr en la nube pública de Andes-VPP. En su lugar, el software debe empaquetarse en un **servidor industrial físico local de grado OT (Edge Appliance)** instalado de manera dedicada e independiente en la subestación de cada mina, conectado físicamente mediante una red local "Air-Gapped" aislada de internet. Este servidor local interactúa de forma directa mediante protocolos industriales robustos (OPC-UA o Modbus TCP) con los PLCs del SCADA de la mina. El servidor Edge procesa localmente el balance predictivo de carga y solo transmite metadatos estadísticos agregados no sensibles a la nube a través de una conexión VPN unidireccional por diodos de datos (Data Diode).
*   **Responsable sugerido:** Lead Architect OT de VPP + Ingeniero de Ciberseguridad Industrial.
*   **Plazo de implementación:** Diseño y certificación del Edge Appliance certificado en IEC 62443: 6 meses.
*   **Costo estimado:** US$ 180.000 en I+D de hardware y certificación de seguridad.
*   **Métrica de éxito:** Aprobación del diseño de integración OT por parte de los comités de ciberseguridad de las mineras (BHP, McEwen).
*   **Dependencias:** Disponibilidad de servidores de seguridad perimetral de tipo diodo de datos industriales.

### Antídoto #3: BESS con Refrigeración Líquida Activa y Sobredimensionamiento del 20%
*   **Acción específica:** Reemplazar por completo los contenedores BESS de refrigeración por aire por **sistemas de refrigeración líquida de lazo cerrado con base en glicol de alta resistencia térmica**. El glicol permite transferir calor de manera eficiente aun con baja densidad del aire a 3.800 msnm. Adicionalmente, sobredimensionar la capacidad nominal de celdas de litio en un 20% y programar el software BMS para que opere estrictamente en una ventana de carga/descarga conservadora del 15% al 85% del SOC (State of Charge), mitigando el calentamiento y garantizando la duración de las baterías de litio por 10 años.
*   **Responsable sugerido:** Ingeniero de Aplicaciones BESS + Proveedor OEM de BESS líquido (ej. CATL o Tesla Powerpack Industrial).
*   **Plazo de implementación:** Especificación de compra de equipos: 60 días.
*   **Costo estimado:** Aumento del 25% en el Capex del hardware de baterías (compensado por Opex de reemplazo a 10 años).
*   **Métrica de éxito:** Mantenimiento de la temperatura interna de las celdas por debajo de 35°C durante ciclos de carga pico.
*   **Dependencias:** Logística de importación de equipos de almacenamiento líquido bajo beneficios arancelarios RIGI.

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Norberto "Tito" Femenía evalúa los antídotos:
*   **Sobre Antídoto #1 (MATER):** Es la única forma real de operar. La resolución 281-E/2017 es la columna vertebral del mercado de renovables y RIGI. Si el proyecto se encuadra como MATER, CAMMESA no puede intervenirlo arbitrariamente y las transacciones son perfectamente legales y auditables.
*   **Riesgo de segundo orden:** El proceso de asignación de prioridad de despacho del MATER en CAMMESA es altamente competitivo y se realiza trimestralmente. Si otros proyectos mineros en el país saturan el sistema de asignación de capacidad antes que el Hub San Juan, el proyecto quedará congelado. **Parche correctivo:** Tramitar la prioridad de despacho bajo el paraguas directo del RIGI que otorga prioridad legal superior frente a otros proyectos generales del MATER.

### Ing. Gabriela Scalise evalúa los antídotos:
*   **Sobre Antídoto #2 (Edge Appliance):** Excelente respuesta arquitectónica. Al correr el algoritmo in-situ y aislar la red OT mediante diodos de datos unidireccionales, el 95% de las objeciones de ciberseguridad industrial se disuelven. Permite un despliegue rápido y seguro respetando la IEC 62443.

### Dr. Esteban Baldi evalúa los antídotos:
*   **Sobre Antídoto #1 (MATER):** Convierte el proyecto en "bancable". Un contrato PPA bajo el régimen MATER con prioridad legal y estabilidad fiscal RIGI es una garantía que cualquier banco internacional de desarrollo aceptará para estructurar la deuda.

### Ing. Diego Russo evalúa los antídotos:
*   **Sobre Antídoto #3 (BESS Líquido):** Indispensable a más de 3.500 msnm. Sin la refrigeración líquida, la degradación física haría imposible recuperar el Capex. El sobredimensionamiento y la limitación del SOC resuelven la vida útil y garantizan un rendimiento del 90% a largo plazo.

---

## VEREDICTO FINAL DEL FACILITADOR

### 🟡 REDISEÑAR PLAN

El proyecto de orquestación VPP debe continuar, pero **rediseñado desde sus cimientos** para evitar la interferencia de CAMMESA, el rechazo de IT/OT minero y la degradación física en altura:
1.  **Encuadre Legal MATER RIGI:** Operar estrictamente bajo la regulación del MATER (Res. 281-E) para legalizar las transacciones.
2.  **Arquitectura OT Local Aislada (Edge Appliance):** No vender software SaaS Cloud a las mineras. Desplegar hardware de computación en el Edge con diodos de datos perimetrales locales en subestaciones OT.
3.  **Sensórica y BESS Líquido de Altura:** Utilizar únicamente sistemas de baterías refrigerados por glicol líquido sobredimensionados para resistir las condiciones termodinámicas andinas.

---

**Backlinks:** [[VPP_Mineria_San_Juan]], [[San Juan]], [[Distrito Vicuña]], [[Los Azules]], [[RIGI]], [[Cobre]].
