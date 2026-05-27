---
type: analysis
tags: [risk-analysis, opportunity, logistics, regulatory, methodology]
sources: [[AndesLogistics_Puna_Logistica]], [[RIGI]], [[Corredor Bioceanico]], [[Taca Taca]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: AndesLogistics Puna - SaaS de Logística Pesada Andina

> **Tesis bajo análisis:** [[AndesLogistics_Puna_Logistica]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 Fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: EL ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2027. El proyecto **AndesLogistics Puna** ha fracasado de manera absoluta. El piloto comercial en la Ruta Nacional 51 (Salta) y el Paso de Jama (Jujuy) fue suspendido de manera permanente. El Sindicato de Camioneros bloqueó indefinidamente las bases logísticas de los proyectos de litio y cobre que adoptaron el software, catalogándolo como "herramienta de persecución y espionaje laboral". Las terminales de hardware IoT sufrieron una tasa de fallo mecánico del 65% en alta montaña y la startup quemó US$ 1.8 millones en Capex tecnológico sin lograr un solo contrato anual recurrente (ARR) viable.

### Horizonte Operativo (90 días desde el lanzamiento)
Durante los primeros 90 días del piloto, la electrónica de los dongles OBD-II industriales no resistió las vibraciones continuas de los caminos no pavimentados de la RN 51 y la RN 52. Las vibraciones de alta frecuencia rompieron las soldaduras internas del chip transceptor del CAN-bus en el 40% de la flota. Asimismo, las antenas autoguiadas de Starlink instaladas en los techos de las cabinas de los camiones sufrieron desajustes mecánicos por el azote del viento blanco andino a 4.200 msnm. Al perder alineación, los routers conmutaban a la red de banda estrecha de Iridium, pero debido a la saturación de paquetes y el tamaño de la telemetría mecánica, el buffer local del Edge se desbordaba, provocando pérdida crítica de registros de desgaste de frenos y consumos.

### Horizonte Regulatorio (12-18 meses)
El Sindicato de Choferes de Camiones (seccional Salta/Jujuy) presentó una denuncia ante la Dirección Provincial del Trabajo y obtuvo una medida cautelar dictada por un juez laboral de Salta que suspendió el uso del software. A pesar de que AndesLogistics implementó la anonimización de identidad, el gremio demostró que la telemetría del CAN-bus (presión de frenado, aceleraciones, tiempos de ralentí) permitía a las empresas transportistas correlacionar indirectamente el comportamiento de conductores específicos con sus cronogramas de descanso. El sindicato declaró que el sistema violaba la Ley de Protección de Datos Personales 25.326 y los convenios colectivos de trabajo (CCT 40/89), forzando el retiro de la aplicación bajo amenaza de paros generales en todo el corredor minero.

### Horizonte Estructural (3-5 años)
El RIGI aceleró el financiamiento de infraestructura de gran escala. Dos de las mineras de cobre líderes en San Juan y Salta decidieron financiar de manera conjunta el ramal ferroviario del Tren Belgrano Cargas utilizando las ventajas del RIGI para transporte bimodal masivo, reduciendo en un 70% la dependencia de camiones pesados por carretera para el traslado de concentrado. Paralelamente, los megaproyectos de litio del Salar de Rincón y Hombre Muerto completaron sus plantas de carbonato de litio grado batería in-situ, reduciendo el volumen físico de carga de salmueras líquidas por camión a una décima parte del volumen original. El mercado total direccionable (TAM) de camiones pesados andinos colapsó y AndesLogistics se quedó sin masa crítica operativa.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Héctor "El Mono" Quiroga — Operador de Flota de Alta Montaña
*   **Rol:** Ex-Gerente de Logística en Minera Alumbrera y actual consultor de transporte pesado para el NOA. 25 años operando camiones Scania y Volvo de más de 45 toneladas en pasos fronterizos andinos.
*   **Justificación:** Comprende la física destructiva de la Puna sobre las transmisiones, la realidad del desgaste de frenos en pendientes del 12%, y la cultura del chofer andino.

### Agente 2: Dra. Cecilia Pautasso — Abogada Laborista y Especialista en CCT 40/89
*   **Rol:** Asesora legal externa de cámaras de transporte y experta en litigios gremiales en el norte argentino.
*   **Justificación:** Identifica con precisión quirúrgica qué métricas del CAN-bus son consideradas por el Sindicato de Camioneros como "herramientas de productividad encubierta" y cómo blindar el software ante la Ley 25.326.

### Agente 3: Lic. Gabriel Goldstein — Economista de Infraestructura y Transporte Andino
*   **Rol:** Ex-analista del Banco Interamericano de Desarrollo (BID) especializado en corredores bioceánicos de Sudamérica.
*   **Justificación:** Evalúa la competencia estructural de medios de transporte (tren vs. camión) y modela el impacto real del bimodalismo y los oleoductos/mineraloductos en la Puna.

### Agente 4: Ing. Lucas Varela — Arquitecto de IoT y Sistemas Embebidos para Climas Extremos
*   **Rol:** Investigador del CONICET y diseñador de electrónica embebida para estaciones meteorológicas de altura en los Andes centrales.
*   **Justificación:** Capaz de rediseñar la arquitectura física de adquisición de datos para que resista amplitud térmica de 50°C, radiación UV extrema e interferencia electromagnética.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Héctor "El Mono" Quiroga (Operaciones)
*   **A) El detalle ignorado por optimismo:**
    Se asumió que el motor de despacho bimodal (subida de insumos, bajada de mineral) se puede optimizar puramente mediante algoritmos. En la práctica, la bimodalidad andina choca con los tiempos impredecibles de la Aduana argentina y chilena en Sico y Jama. Un camión puede ser retenido 14 horas por una inspección de Gendarmería o SENASA por discrepancias menores en los MIC/DTA en papel. Toda la planificación algorítmica del viaje de retorno se cae a pedazos y el camión termina regresando vacío ("deadhead") para no perder la ventana operativa del yacimiento. La ineficiencia no es matemática; es burocrática e inmanejable por el SaaS.
*   **B) Cadena de eventos hasta el fracaso:**
    1. El optimizador de AndesLogistics asigna un retorno bimodal a 15 camiones en Paso de Sico.
    2. Aduana de Chile suspende el paso temporalmente por viento blanco de 110 km/h.
    3. Los camiones quedan varados en el llano sin conectividad. El software asume que están en tránsito y reprograma los turnos en la mina.
    4. Al reabrir el paso, se genera un cuello de botella de 80 camiones acumulados. Las mineras pierden la paciencia por la falta de insumos críticos y rompen el contrato dinámico para volver al esquema tradicional de despacho fijo manual.
*   **C) Cuantificación:**
    *   *Riesgo de retraso aduanero y meteorológico inmanejable por software:* Probabilidad: **Alta (>60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Rápida (1-6 meses)**.
    *   *Desgaste físico no lineal en descenso con sobrecarga:* Probabilidad: **Media (30-60%)** | Severidad: **Moderada (5-20% Capex)** | Velocidad: **Gradual (6-18 meses)**.

---

### Agente 2: Dra. Cecilia Pautasso (Gremial/Legal)
*   **A) El detalle ignorado por optimismo:**
    Creer que el consentimiento informado y la anonimización bastaban para detener la reacción del sindicato. En el transporte argentino, el CCT 40/89 otorga al sindicato un poder de policía de hecho en ruta. Si el gremio sospecha que una transportista usa el OBD-II para medir cuántas veces frena un chofer o a qué velocidad toma una curva para evaluar su rendimiento individual y condicionar su continuidad o premios, el gremio paralizará la flota de inmediato. El "control mecánico" es percibido directamente como "persecución laboral".
*   **B) Cadena de eventos hasta el fracaso:**
    1. Una transportista utiliza los datos del software AndesLogistics para suspender a un chofer que excedió las revoluciones del motor en un descenso en la cuesta del Lipán.
    2. El chofer acude al sindicato denunciando hostigamiento digital.
    3. El gremio activa piquetes en el acceso a la RN 52 en Purmamarca, impidiendo el paso de todos los camiones de la mina.
    4. La minera intima a la transportista a remover inmediatamente los dispositivos telemáticos de la flota para reanudar operaciones.
    5. AndesLogistics pierde el 100% de sus camiones instalados en Jujuy en 72 horas.
*   **C) Cuantificación:**
    *   *Boicot gremial por control de rendimiento encubierto:* Probabilidad: **Alta (>60%)** | Severidad: **Crítica (>50% Capex)** | Velocidad: **Fulminante (<30 días)**.
    *   *Acción judicial de la AAIP por violación de la Ley 25.326:* Probabilidad: **Media (30-60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Gradual (6-18 meses)**.

---

### Agente 3: Lic. Gabriel Goldstein (Infraestructura/Finanzas)
*   **A) El detalle ignorado por optimismo:**
    Se asumió que las transportistas Tier 2/3 tienen los márgenes y la cultura financiera para pagar una suscripción SaaS B2B en dólares. Estas pymes operan en pesos, con flujo de caja asfixiado por las tasas de interés y los plazos de pago de las mineras (a 90 o 120 días). Cobrarles un fee mensual por camión para ahorrarles un "5% teórico de combustible" no funciona porque el combustible en Argentina suele estar sujeto a subsidios locales, cupos de gasoil minero, o es provisto directamente en boca de mina por la operadora principal. El ahorro de OPEX no fluye al bolsillo de quien paga la suscripción.
*   **B) Cadena de eventos hasta el fracaso:**
    1. AndesLogistics establece una tarifa mensual de US$ 120 por camión.
    2. Las transportistas locales se demoran en los pagos del SaaS alegando que la minera no les liquida sus certificados a tiempo.
    3. Al no ver el ahorro inmediato reflejado en sus cuentas de combustible (porque la minera les descuenta el gasoil provisto directamente de la facturación consolidada), las pymes cancelan la suscripción masivamente.
    4. La startup no logra cubrir el costo del ancho de banda de Starlink Business (US$ 250/mes por terminal) y entra en cesación de pagos.
*   **C) Cuantificación:**
    *   *Desconexión del beneficio económico del ahorro de gasoil:* Probabilidad: **Alta (>60%)** | Severidad: **Crítica (>50% Capex)** | Velocidad: **Rápida (1-6 meses)**.
    *   *Sustitución por infraestructura ferroviaria (Belgrano Cargas):* Probabilidad: **Baja (<30%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Lenta (>18 meses)**.

---

### Agente 4: Ing. Lucas Varela (IoT/Hardware)
*   **A) El detalle ignorado por optimismo:**
    Se confió en terminales Starlink estándar montadas sobre vehículos en movimiento continuo en zonas de calor y vibración extrema. La vibración rompe los engranajes de los modelos articulados y las variaciones extremas de voltaje de los alternadores de los camiones viejos queman los transformadores DC-AC no rugerizados de las terminales satelitales.
*   **B) Cadena de eventos hasta el fracaso:**
    1. Se instalan routers y antenas Starlink sin filtros de línea eléctrica ni soportes antivibración industriales.
    2. Las sobretensiones del sistema eléctrico del camión queman la fuente de la antena.
    3. Los camiones quedan sin telemetría satelital en el tramo crítico de alta montaña.
    4. La pérdida de datos destruye los modelos de predicción de desgaste de frenos y la alerta temprana de fallas mecánicas.
*   **C) Cuantificación:**
    *   *Falla física de hardware satelital no certificado vehicular:* Probabilidad: **Alta (>60%)** | Severidad: **Alta (20-50% Capex)** | Velocidad: **Rápida (1-6 meses)**.
    *   *Corrosión salina en contactos de sensores OBD-II:* Probabilidad: **Alta (>60%)** | Severidad: **Moderada (5-20% Capex)** | Velocidad: **Lenta (>18 meses)**.

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Probabilidad | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Boicot gremial por control de rendimiento encubierto | Pautasso | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Desconexión del beneficio económico del gasoil | Goldstein | Estructural | Alta | Crítica | Rápida | **A×C** |
| 3 | Retraso aduanero y meteorológico incontrolable | Quiroga | Operativo | Alta | Alta | Rápida | **A×A** |
| 4 | Falla física de hardware satelital por vibración | Varela | Operativo | Alta | Alta | Rápida | **A×A** |
| 5 | Corrosión salina e intemperie en Puna y Salares | Varela | Operativo | Alta | Moderada | Lenta | **A×M** |
| 6 | Sustitución de flete por Belgrano Cargas RIGI | Goldstein | Estructural | Baja | Alta | Lenta | **B×A** |

### 🔴 Top 3 Vectores de Riesgo Sistémico
1.  **VETO SINDICAL LABORAL (Vector #1):** El Sindicato de Camioneros tiene la capacidad física e institucional de matar la startup en 72 horas si percibe el sistema como control disciplinario encubierto. Ningún software sobrevive a un bloqueo en la base minera.
2.  **DESALINEACIÓN DE INCENTIVOS ECONÓMICOS (Vector #2):** El pagador del SaaS (transportista pyme) no ve el beneficio directo del ahorro de combustible porque el gasoil es un costo asumido o provisto en especie por la minera principal. El pagador tiene un costo real y un ahorro teórico invisible.
3.  **FRAGILIDAD DEL HARDWARE EN ALTURA (Vector #4):** Depender de Starlink estándar en movimiento sin amortiguación andina ni protección contra oscilaciones de tensión eléctrica garantiza el apagón de datos en el 50% del trayecto de montaña.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: El "Dashboard de Seguridad del Chofer" y Cogestión de Beneficios
*   **Acción específica:** Rediseñar la interfaz de usuario. Eliminar cualquier ranking de choferes visible para la gerencia de la transportista. En su lugar, el software debe enviar las alertas de conducción (ej. exceso de velocidad o temperatura de frenos) **únicamente a una pantalla en la cabina del camión**, funcionando como un asistente de seguridad y copiloto para el propio chofer. Además, estructurar un acuerdo por convenio donde la transportista destina el **20% de los ahorros reales de combustible medidos a un bono en efectivo mensual para el chofer**. El sindicato pasa a defender la plataforma porque reduce los accidentes de sus afiliados y aumenta sus salarios reales.
*   **Responsable sugerido:** Director de Producto SaaS + Delegado regional de Camioneros.
*   **Plazo de implementación:** Rediseño de UI en 60 días. Negociación gremial en 90 días.
*   **Costo estimado:** US$ 40.000 en software + US$ 10.000 en asesoría legal laboral.
*   **Métrica de éxito:** Homologación del uso del copiloto de seguridad por acta del Sindicato de Camioneros de Salta.
*   **Dependencias:** Aceptación de las transportistas de compartir parte de los ahorros de combustible con el personal de conducción.

### Antídoto #2: Integración de Aduana y Ventanilla Única de Despacho ("Customs Gateway")
*   **Acción específica:** Pivotar la propuesta de valor. El software no debe venderse como "ahorro de combustible" sino como **reducción del tiempo de espera aduanera y puerto seco**. Integrar la "Shadow API" del Sistema Informático MALVINA/MIDA de Aduanas y el despacho digital de cartas de porte internacionales (MIC/DTA). Al pre-cargar los manifiestos de manera digital y geolocalizar la llegada exacta del camión a la frontera, se reducen las esperas en Sico y Sapa de 14 horas a menos de 2 horas. Las mineras pagan con gusto el SaaS porque reducir el "tiempo de camión parado" ahorra US$ 1.500 diarios por unidad.
*   **Responsable sugerido:** Lead Architect de Integraciones + Despachante de Aduanas consultor.
*   **Plazo de implementación:** Desarrollo del módulo de integraciones aduaneras en 6 meses.
*   **Costo estimado:** US$ 120.000 en desarrollo de integraciones complejas.
*   **Métrica de éxito:** Reducción verificada del tiempo de cruce de frontera en un 60% en los camiones piloto.
*   **Dependencias:** Estabilidad de la conectividad en el paso fronterizo y accesos a APIs aduaneras.

### Antídoto #3: Hardware Vehicular Rugerizado Certificado MIL-STD e Inversor de Grado Médico
*   **Acción específica:** Descartar terminales de consumo. Comprar antenas Starlink Flat High Performance (especificadas para uso móvil marino/terrestre de alta resistencia) y montarlas sobre racks amortiguados de aleación aeronáutica. Alimentar el sistema exclusivamente a través de inversores de energía inteligentes con aislamiento galvánico de grado médico para anular cualquier pico de tensión del camión.
*   **Responsable sugerido:** Ingeniero de Hardware IoT de AndesLogistics.
*   **Plazo de implementación:** 90 días para el ensamblaje y prueba del rack de energía de alta montaña.
*   **Costo estimado:** US$ 3.500 adicionales por camión (Capex de hardware y protección).
*   **Métrica de éxito:** Cero fallas eléctricas ni desalineación de antenas en 180 días de operación continua en ripio andino.
*   **Dependencias:** Importación fluida de componentes de alta gama bajo RIGI arancel 0%.

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Héctor "El Mono" Quiroga evalúa los antídotos:
*   **Sobre Antídoto #2 (Aduana):** Brutal. El tiempo muerto en aduana es la pesadilla del transportista. Si el software agiliza los trámites MIC/DTA y reduce el papeleo físico, el contratista pagará lo que sea. Resuelve el problema financiero de raíz.
*   **Sobre Antídoto #1 (Bonos a choferes):** En teoría excelente, pero las pymes de transporte del NOA suelen ser muy informales. Monitorear los ahorros para pagar el bono puede generar disputas si el chofer argumenta que el camión fallaba mecánicamente y por eso gastó más. **Parche correctivo:** El cálculo del bono debe basarse en un algoritmo transparente auditado por el gremio, y el bono debe pagarse sobre metas grupales por tramo y no individuales por chofer para evitar competencia desleal.

### Dra. Cecilia Pautasso evalúa los antídotos:
*   **Sobre Antídoto #1 (Gremio):** El cambio a "asistente de cabina" y no "policía de flota" es la única forma legal y política de salvar el software. Si el dato de ralentí o revoluciones no va a la gerencia de RRHH directamente para sanciones, la Ley 25.326 se cumple perfectamente porque el fin es la asistencia en viaje y seguridad vial del trabajador.

### Lic. Gabriel Goldstein evalúa los antídotos:
*   **Sobre Antídoto #2 (Aduana):** Reorientar el cobro de la licencia SaaS a las grandes mineras mineras (BHP, Arcadium, Taca Taca) en vez de a las pymes transportistas. La minera tiene el músculo financiero, paga en dólares, y es la que más sufre las demoras aduaneras de sus insumos clave. Esto elimina el riesgo de morosidad y desalineación de incentivos.

### Ing. Lucas Varela evalúa los antídotos:
*   **Sobre Antídoto #3 (Hardware Flat):** La antena Flat High Performance resuelve el desgaste de engranajes porque es 100% estática. Sin embargo, el costo se eleva significativamente. **Riesgo de segundo orden:** El robo de antenas de US$ 2.500 en paradores de ruta. **Parche correctivo:** Diseñar una jaula antirrobo de acero soldada directamente al chasis superior de la cabina, que proteja físicamente la antena sin interferir con la línea de visión satelital.

---

## VEREDICTO FINAL DEL FACILITADOR

### 🟡 REDISEÑAR PLAN

El plan de AndesLogistics debe ser reestructurado de inmediato bajo estas tres directrices innegociables:
1.  **Pivotar el Cliente y Propuesta de Valor:** Vender el software a las **Empresas Mineras Principales** (no a los fleteros) y enfocarlo en la **Ventanilla Aduanera / Reducción de Tiempos Muertos en Frontera**, no en el ahorro de combustible básico.
2.  **Copiloto de Seguridad (Sindicato Safe):** Desplegar la app como un software de asistencia para el conductor en cabina. Compartir los beneficios económicos del ahorro vía bonos homologados con el Sindicato de Camioneros.
3.  **Hardware de Grado de Infraestructura:** No escatimar en hardware. Jaulas de protección de acero y antenas Starlink Flat de alta gama para evitar fallas catastróficas en el ripio andino.

---

**Backlinks:** [[AndesLogistics_Puna_Logistica]], [[RIGI]], [[Taca Taca]], [[Salta]], [[Jujuy]], [[Corredor Bioceanico]].
