---
type: analysis
tags: [risk-analysis, opportunity, logistics, methodology, regulatory]
sources: [[AndesLogistics_Puna_Logistica]], [[RIGI]], [[Corredor Bioceanico]], [[PreMortem_RIGI_Shield]], [[Salta]], [[Jujuy]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: AndesLogistics Puna — Optimización Física y Mecánica de Flota Pesada Andina

> **Tesis bajo análisis:** [[AndesLogistics_Puna_Logistica]]
> **Análisis escéptico previo:** Pivot de [[PreMortem_RIGI_Shield]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2028. La plataforma AndesLogistics Puna ha sido dada de baja en todos los contratos de flotas pesadas del corredor andino (RN 51, Paso de Sico y Paso de Jama). Ninguna contratista de transporte minero utiliza el software de telemetría pasiva y optimización de tránsito. La startup ha consumido US$ 3.8 millones en capital inicial y ha sido liquidada. Los camiones pesados continúan subiendo insumos críticos de la manera tradicional, con los mismos niveles de fatiga y siniestralidad.

### Horizonte Operativo (90 días desde el lanzamiento)

Durante el despliegue del piloto de 20 camiones Scania R500 y Volvo FH16 operando en la RN 51 (tramo Campo Quijano - Socompa), se descubrió que los sensores telemáticos OBD-II / CAN-bus genéricos de bajo costo no soportaban las condiciones extremas de vibración destructiva ("calamina" o serrucho de ripio) y los choques térmicos diarios (de +25°C a las 14:00 a -15°C a las 04:00 a 4.000 msnm). Las placas soldadas de los routers híbridos se agrietaron por estrés mecánico, provocando cortocircuitos en el sistema eléctrico de 5 camiones en plena subida a la Quebrada del Toro.

A su vez, el motor del software de optimización, diseñado para coordinar el retorno bimodal (camiones cargados de insumos que bajan con concentrado de litio/cobre), fracasó en la práctica. Los tiempos de carga en los yacimientos del Salar de Pocitos y Olaroz y los despachos aduaneros mostraron una variabilidad incontrolable de hasta 14 horas por factores ajenos al software (congelamiento de cañerías en plantas, demoras en el pesaje y caída de sistemas en la aduana fronteriza). El algoritmo no pudo resolver el problema del búfer y continuó reprogramando las ventanas de tránsito en bucle, generando que las tripulaciones de los camiones esperaran en la banquina a temperaturas bajo cero, agotando sus horas de conducción reglamentarias según el CCT 40/89.

### Horizonte Regulatorio (12-18 meses)

El Sindicato de Choferes de Camiones (seccionales Salta y Jujuy) lideró un paro total de transporte minero en la Puna. A pesar de los esfuerzos por anonimizar la telemetría, el sindicato acusó a la plataforma de violar el Convenio Colectivo de Trabajo 40/89 y la Ley de Contrato de Trabajo 20.744, tipificándola como una herramienta de "flexibilización laboral encubierta y hostigamiento digital". Los delegados gremiales argumentaron que las sugerencias del algoritmo para el ajuste de revoluciones óptimas y frenado motor en pendientes extremas eran utilizadas por los supervisores de las contratistas para sancionar o calificar a los conductores.

Paralelamente, la Agencia de Acceso a la Información Pública (AAIP) intervino tras una denuncia gremial, determinando que los metadatos de telemetría (inclinación, velocidad, ubicación, temperatura de frenos) combinados con los horarios de inicio y fin de jornada constituían "datos personales indirectamente identificables" bajo la Ley 25.326. La AAIP impuso una multa de AR$ 150 millones y ordenó la suspensión cautelar de la transmisión de datos en tiempo real hasta que se garantizara una infraestructura de cifrado de grado militar local, inviable para la estructura de costos de la startup.

### Horizonte Estructural (3-5 años)

El colapso estructural del modelo de negocio de AndesLogistics Puna fue gatillado por un cambio tecnológico y de infraestructura masivo: la reactivación e industrialización del **ramal ferroviario C14 (Ferrocarril Belgrano Cargas)**, impulsada por un consorcio de empresas chinas productoras de litio (Ganfeng, Tsingshan) junto con los gobiernos provinciales de Salta y Jujuy. La reactivación de la vía férrea Salta - Antofagasta permitió canalizar el 75% del transporte a granel de concentrados minerales y el 60% de los reactivos químicos pesados (ácido sulfúrico, cal, ceniza de soda) por tren.

El transporte por camión en la RN 51 quedó relegado únicamente a la logística de "última milla" desde las estaciones ferroviarias de la Puna hasta las bocas de mina. La propuesta de valor de AndesLogistics de optimizar flotas de camiones de larga distancia a lo largo de 500 km de montaña perdió el 80% de su mercado objetivo. El Opex ferroviario resultó ser un 45% inferior al costo optimizado por camión de AndesLogistics, haciendo insostenible la viabilidad de la plataforma.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Hugo Varela — Ingeniero de Operaciones de Flotas Mineras en Alta Montaña
* **Rol:** 24 años gestionando la logística de transporte pesado para Minera Alumbrera y proyectos en la Puna (Salar del Hombre Muerto). Ex-Gerente de Mantenimiento de flotas de alta montaña en Transportes La Sevillanita.
* **Justificación:** Conoce las brutales exigencias mecánicas reales a las que se someten los camiones pesados a >4.000 msnm. Sabe cómo la vibración ("serrucho") destruye cualquier hardware que no sea de especificación militar o minera IP69K, y entiende por qué los tiempos de espera físicos en yacimientos no se pueden modelar algebraicamente de manera determinista.

### Agente 2: Dra. Clara Benavídez — Abogada Especialista en Derecho Laboral Colectivo y Protección de Datos
* **Rol:** Ex-asesora legal de la Federación Nacional de Trabajadores Camioneros. Especialista en litigios de protección de datos personales y derecho informático aplicado a las relaciones laborales.
* **Justificación:** Es la experta idónea para anticipar la resistencia gremial y las trampas de la Ley de Datos Personales 25.326. Sabe cómo redactar y certificar procesos de anonimización para resistir auditorías de la AAIP y amparos sindicales en la justicia laboral.

### Agente 3: Lic. Santiago Rossi — Economista de Logística y Corredores Multimodales
* **Rol:** Consultor de infraestructura de transporte del Banco Interamericano de Desarrollo (BID). Autor de los estudios de viabilidad para la rehabilitación del Ramal C14 y el Corredor Bioceánico.
* **Justificación:** Evaluará el riesgo estructural de la reactivación ferroviaria y las tendencias de infraestructura multimodal. Conoce los costos reales por tonelada-kilómetro del transporte ferroviario vs. carretero en la cordillera y puede predecir cuándo el ferrocarril destruirá la ventaja competitiva de los camiones.

### Agente 4: Ing. Walter Krich — Arquitecto de Comunicaciones Críticas e IoT Industrial
* **Rol:** 18 años diseñando infraestructuras de comunicaciones en zonas de nula cobertura celular para petroleras y mineras en Argentina, Chile y Bolivia. Experto en sistemas de conmutación Starlink/Iridium en movimiento.
* **Justificación:** Evaluará la arquitectura tecnológica de la conectividad híbrida. Sabe por qué los routers comerciales fallan en las quebradas andinas y puede cuantificar el costo real de transmitir telemetría pesada continua a través de redes satelitales de banda estrecha de manera confiable.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Varela (Operaciones Físicas y Logística)

**A) El detalle ignorado por optimismo:**
La tesis asumió que el transporte en la Puna es un flujo continuo que se puede optimizar como un almacén de Amazon. Ignoraron que la RN 51 no es una autopista; tiene más de 120 km de ripio suelto, pendientes del 8% y curvas cerradas que someten a la suspensión del camión y a los componentes electrónicos a una aceleración de vibración continua de hasta 4G. El hardware comercial OBD-II conectado directamente al puerto del camión se aflojaba o sufría fatiga por micro-fisuras en las soldaduras de estaño debido a la oscilación térmica brutal del desierto de altura en menos de 30 días.

Además, planificar un "retorno bimodal coordinado" es un ejercicio de física teórica. Los yacimientos operan bajo variables imprevistas permanentes: si una bomba de transferencia de salmuera falla, la carga de un camión cisterna de ácido se suspende por 12 horas. El chofer no puede esperar en la mina porque a 4.000 msnm no hay infraestructura hotelera para 50 choferes parados. El camión debe bajar vacío por regulaciones de seguridad laboral de la misma minera. El algoritmo obligaba a esperar ventanas teóricas que chocaban con la realidad del terreno.

**B) Cadena de eventos hasta el fracaso:**
1. Despliegue de los 20 módulos OBD-II genéricos en el piloto de la RN 51.
2. Tras 25 días, 8 módulos dejan de emitir señal; la inspección revela soldaduras internas rotas por vibración destructiva.
3. Tres camiones sufren fallas en la computadora central (ECU) del motor por picos de tensión generados por cortocircuitos en el módulo de telemetría pasiva. Las contratistas retiran el hardware del resto de sus flotas para proteger la garantía de sus unidades Scania y Volvo.
4. El algoritmo de retorno bimodal programa que 6 camiones esperen en el Salar de Pocitos una ventana de carga de cal que se retrasó 18 horas por tormenta de viento blanco.
5. Los choferes, sin calefacción (prohibido dejar el motor encendido por política ambiental minera), sufren hipotermia leve. El sindicato interviene y denuncia a la empresa contratista y a AndesLogistics ante la Secretaría de Trabajo de Salta.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Destrucción de hardware telemático por vibración extrema y choque térmico | Alta (>60%) | Moderada (15% Capex) | Fulminante (<30 días) |
| Cortocircuitos en ECU de camiones pesados por hardware OBD-II no homologado | Media (30-60%) | Alta (30% Capex) | Fulminante (<30 días) |
| Inviabilidad del retorno bimodal por variabilidad externa de las plantas | Alta (>60%) | Moderada (20% Capex) | Rápida (1-6 meses) |

---

### Agente 2: Dra. Benavídez (Legal y Gremial)

**A) El detalle ignorado por optimismo:**
Pensar que en Argentina se puede implementar un software de optimización que le sugiera a un camionero cómo conducir mediante un algoritmo sin activar el radar del Sindicato de Camioneros es de una ingenuidad regulatoria terminal. Hugo Moyano y los delegados provinciales no ven "eficiencia y cuidado ambiental"; ven control patronal totalitario a través de algoritmos de Inteligencia Artificial.

Aunque los datos personales del chofer se eliminen en la base de datos externa de la startup, la contratista tiene la lista de qué conductor maneja qué camión cada día. Correlacionar la patente con el legajo es trivial. El algoritmo genera un perfil del chofer (velocidad de paso, uso del freno de motor, tiempo de ralentí). Si la contratista usa esta información para evaluar la productividad o rescindir un contrato de transporte, el sindicato reacciona bloqueando las rutas de acceso.

**B) Cadena de eventos hasta el fracaso:**
1. El software de AndesLogistics genera un reporte semanal de "Eficiencia de Conducción" para la contratista minera.
2. La contratista suspende a un conductor por "conducción ineficiente" (exceso de revoluciones en subida).
3. El sindicato de Camioneros bloquea la RN 51 en Campo Quijano, paralizando todo el transporte de litio hacia Salta.
4. El sindicato exige la prohibición del software de AndesLogistics en todas las flotas mineras operando en la provincia.
5. La AAIP inicia una investigación de oficio y descubre que el software carece de una Evaluación de Impacto en la Protección de Datos (DPIA) y que las direcciones IP y parámetros de telemetría de los routers Starlink instalados en las cabinas permiten identificar el comportamiento de conductores específicos.
6. La justicia laboral dicta una medida cautelar ordenando desconectar el sistema de telemetría por violar el derecho a la intimidad laboral.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Conflicto gremial y bloqueos por percepción de control laboral algorítmico | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Clausura cautelar por parte de la AAIP por violación de la Ley 25.326 | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

### Agente 3: Lic. Rossi (Macroestructura y Competencia Multimodal)

**A) El detalle ignorado por optimismo:**
El plan de negocios se basó en el supuesto estático de que la logística andina dependerá para siempre de camiones pesados circulando por sinuosas carreteras de montaña. Se ignoró por completo el "Plan Ferroviario del Norte Grande" y la fuerte presión de las mineras chinas sobre el Ministerio de Transporte de la Nación para habilitar el tráfico multimodal en el Ramal C14 del Belgrano Cargas. El ferrocarril es la respuesta estructural definitiva al transporte de insumos masivos (como la ceniza de soda que requiere la producción de carbonato de litio) y concentrado de cobre (de proyectos gigantescos como [[Taca Taca]]).

El software de optimización de camiones de AndesLogistics asume que el costo por tonelada transportada por camión es la base del mercado. El ferrocarril reactivado reduce ese costo a menos de la mitad. Cuando el tren comenzó a operar de forma regular entre Salta y Socompa, las mineras cancelaron de inmediato los contratos de larga distancia con flotas de camiones, limitando el transporte automotor a trayectos cortos de menos de 40 km desde los nodos ferroviarios hasta los yacimientos.

**B) Cadena de eventos hasta el fracaso:**
1. Reactivación y prueba de carga exitosa del ramal ferroviario C14 de ancho de vía métrico por parte de Belgrano Cargas.
2. Firma de convenios plurianuales entre los 3 productores clave de litio de la Puna y el operador ferroviario para el transporte de cal y ceniza de soda.
3. Desplome en la demanda de flotas de camiones de larga distancia en la RN 51 en un 60% en menos de 12 meses.
4. Las contratistas de camiones entran en crisis de sobrecapacidad; el uso de software de eficiencia de flota pasa a ser una prioridad de supervivencia secundaria frente a la falta de contratos de carga general.
5. AndesLogistics pierde el 70% de su base de clientes proyectada en su modelo financiero y no logra alcanzar el punto de equilibrio.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Sustitución modal del transporte carretero por reactivación del Ferrocarril Ramal C14 | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Contracción del TAM por desvío de insumos pesados y minerales al ferrocarril | Media (30-60%) | Alta (40% Capex) | Lenta (>18 meses) |

---

### Agente 4: Ing. Krich (Comunicaciones e IoT Edge)

**A) El detalle ignorado por optimismo:**
La tesis de AndesLogistics asume que la conmutación Starlink/Iridium en movimiento es un problema de software resuelto. En la Puna andina, las quebradas son profundas y estrechas (como la Quebrada del Toro). Las antenas satelitales instaladas en los techos de las cabinas de los camiones sufren un bloqueo continuo del horizonte de visibilidad satelital (campo de visión obstruido por paredes de piedra de hasta 80 grados). Starlink en movimiento requiere un arco de visión libre constante; en curvas pronunciadas y desfiladeros, la conexión LEO se corta por períodos de 15 a 35 minutos.

El router de comunicación híbrida alternativo debía conmutar a la red de banda estrecha de Iridium (mensajería satelital pura). Pero la latencia de conmutación de Iridium y el bajísimo ancho de banda (2.4 kbps) hacían imposible transmitir paquetes de telemetría CAN-bus densos. Al intentar enviar ráfagas de datos acumulados en el buffer del gateway de borde, los costos de transmisión satelital por kilobyte de Iridium explotaron de los US$ 15/mes proyectados a más de US$ 450/mes por camión, superando el fee mensual completo que cobraba AndesLogistics por el software.

**B) Cadena de eventos hasta el fracaso:**
1. Despliegue de antenas satelitales en camiones de prueba.
2. Cortes continuos de conectividad en tramos críticos de la RN 51 por obstrucción orográfica.
3. El router híbrido conmuta a Iridium de manera persistente en las quebradas.
4. Se envían reportes densos de telemetría mecánica a través del canal Iridium satelital de emergencia.
5. La startup recibe una factura de conectividad de los proveedores satelitales de US$ 9.000 por el primer mes de operación de solo 10 camiones piloto.
6. Para evitar el descalabro financiero, se desactiva la transmisión en tiempo real de telemetría de Iridium, dejando al camión incomunicado en las zonas ciegas.
7. Sin datos en tiempo real, el motor de optimización de tránsitos bimodales no puede predecir el arribo de los camiones y pierde su precisión operativa, volviendo inútil el software.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Costos explosivos de transmisión satelital a través de redes redundantes de banda estrecha | Alta (>60%) | Alta (45% Capex) | Rápida (1-6 meses) |
| Pérdida de tracking en tiempo real por obstrucción física del horizonte LEO en quebradas | Alta (>60%) | Moderada (25% Capex) | Fulminante (<30 días) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Conflicto gremial y bloqueos por percepción de control laboral | Benavídez | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Costos de conectividad satelital redundante exceden el fee del SaaS | Krich | Operativo | Alta | Alta | Rápida | **A×A** |
| 3 | Clausura cautelar por parte de la AAIP (Ley 25.326) | Benavídez | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 4 | Destrucción de hardware OBD-II por fatiga térmica y mecánica extrema | Varela | Operativo | Alta | Moderada | Fulminante | **A×M** |
| 5 | Sustitución de transporte carretero por tren Ramal C14 | Rossi | Estructural | Media | Crítica | Gradual | **M×C** |
| 6 | Inviabilidad del retorno bimodal por variabilidad de plantas mineras | Varela | Operativo | Alta | Moderada | Rápida | **A×M** |
| 7 | Pérdida de tracking por obstrucción orográfica de señal LEO | Krich | Operativo | Alta | Moderada | Fulminante | **A×M** |
| 8 | Contracción del TAM de camiones pesados por tren multimodal | Rossi | Estructural | Media | Alta | Lenta | **M×A** |
| 9 | Cortocircuitos en ECUs por hardware OBD-II no homologado | Varela | Operativo | Media | Alta | Fulminante | **M×A** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **EL MURO GREMIAL Y LA LEY DE DATOS PERSONALES (Vectores #1, #3):** El Sindicato de Camioneros y la AAIP representan una barrera de entrada letal. Cualquier sistema que rastree parámetros vehiculares continuos de conductores asalariados en Argentina es catalogado como control de productividad algorítmico abusivo y violación a la privacidad bajo la Ley 25.326. La falta de un marco de consentimiento explícito e inalterable y el diseño de la API sin protección nativa desde el diseño (Privacy by Design) condena al software a la suspensión legal y al conflicto físico (piquetes y bloqueos en RN 51).

2. **DRENAJE DE CAJA POR CONECTIVIDAD SATELITAL EN ZONAS CIEGAS (Vector #2):** El "Apagón digital" andino no se soluciona simplemente instalando Starlink en movimiento. Las quebradas bloquean físicamente la órbita LEO. Forzar la transmisión de telemetría masiva a través de Iridium (banda estrecha) genera facturas de comunicaciones que destruyen los márgenes financieros del SaaS. Sin tiempo real, el software pierde precisión, pero con tiempo real, los costos satelitales consumen toda la caja operativa de la empresa.

3. **AMENAZA DE DISRUPCIÓN DE INFRAESTRUCTURA MULTIMODAL - RAMAL C14 (Vector #5):** La reactivación del Ferrocarril Belgrano Cargas (Ramal C14) es una fuerza estructural imparable. Al operar bajo el paraguas de inversiones de capitales chinos enfocados en la extracción masiva de carbonato de litio, el transporte por camión de larga distancia andino está destinado a encogerse dramáticamente. Optimizar flotas de camiones pesados de larga distancia es una propuesta de valor con fecha de vencimiento.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Certificación "Privacy-First" y Homologación Gremial del Software

* **Acción específica:** Rediseñar la arquitectura de adquisición de datos para que los datos de telemetría (CAN-bus y mecánicos) se procesen localmente en el dispositivo de borde (Edge Computing) y solo se transmitan métricas agregadas agregando ruido diferencial (Differential Privacy). El software no registrará velocidades instantáneas por tramo vinculadas a vehículos, sino índices de fatiga mecánica del material por tipo de chasis. Se debe constituir un "Comité de Eficiencia y Seguridad Vial de Altura" conjunto con el Sindicato de Camioneros, homologando la plataforma como una herramienta exclusiva para la prevención de accidentes y reducción de esfuerzo físico del chofer, eliminando reportes de productividad individual.
* **Responsable sugerido:** DPO (Data Protection Officer) + Asesor de Asuntos Gremiales.
* **Plazo de implementación:** Antes de firmar el primer piloto comercial.
* **Costo estimado:** US$ 80.000 en asesoría legal de protección de datos, DPIA formal ante la AAIP y convenios gremiales.
* **Métrica de éxito:** Obtención del dictamen de conformidad de la AAIP y acuerdo homologado firmado por las seccionales de Camioneros de Salta y Jujuy.
* **Dependencias:** Rediseño de la base de datos para anonimizar datos desde el firmware del OBD-II.

### Antídoto #2: Arquitectura de Almacenamiento Asíncrono "Store-and-Forward" Inteligente

* **Acción específica:** Eliminar la transmisión en tiempo real de telemetría CAN-bus densa a través de redes de banda estrecha de alto costo (Iridium). Rediseñar el gateway de borde para operar bajo un modelo asíncrono estricto: la telemetría mecánica completa se procesa y almacena localmente en la memoria flash de grado automotriz del camión. Solo se transmite mediante Iridium una "Alerta de Estado Mecánico Crítico" (paquetes binarios ultracompactos de <100 bytes) en caso de anomalías severas (temperatura de transmisión peligrosa, falla de frenos). Toda la telemetría de optimización se descarga automáticamente a la nube vía Wi-Fi local cuando el camión llega a nodos con conectividad de alta capacidad (nodos Starlink fijos en yacimientos o centros logísticos en Campo Quijano y San Antonio de los Cobres).
* **Responsable sugerido:** Ingeniero Principal de Sistemas IoT.
* **Plazo de implementación:** Durante la fase de prototipado del hardware de borde.
* **Costo estimado:** US$ 50.000 en desarrollo de software de compresión binaria y hubs de descarga Wi-Fi locales en puntos de parada obligatoria.
* **Métrica de éxito:** Reducción del costo de conectividad satelital móvil a menos de US$ 25/mes por camión, manteniendo la precisión de los modelos mecánicos predictivos post-viaje.
* **Dependencias:** Instalación de antenas de descarga rápida Wi-Fi seguras en las bases operativas de las mineras.

### Antídoto #3: Pivot al Segmento "Última Milla y Maquinaria Pesada en Yacimiento" (Bypass al Tren)

* **Acción específica:** Ante el avance del Tren de Carga (Ramal C14), retirar el enfoque de camiones de larga distancia (ruta completa Salta-Mina) y enfocar el software en dos nichos no ferroviarios inmunes a la sustitución modal: (a) la logística de distribución de última milla (distancias cortas de <40 km entre las estaciones ferroviarias de transferencia andinas como Olacapato o Tolar Grande y los campamentos mineros), y (b) la flota interna de movimiento de tierras y maquinaria amarilla pesada de los yacimientos (palas mecánicas, retroexcavadoras, camiones fuera de ruta Caterpillar/Komatsu). Estas flotas operan en circuitos cerrados, consumen un volumen crítico de diésel y componentes mecánicos a gran altura, y son 100% inmunes al transporte ferroviario.
* **Responsable sugerido:** Director de Desarrollo de Negocios (SaaS B2B).
* **Plazo de implementación:** Inmediata, adaptando los modelos matemáticos a la maquinaria vial y de minería de tajo abierto / subterránea.
* **Costo estimado:** US$ 120.000 en entrenamiento de algoritmos para patrones de consumo de motores industriales estacionarios y vehículos pesados fuera de ruta.
* **Métrica de éxito:** Firma de contratos piloto con contratistas de movimiento de suelos en la Puna (ej. Milicic, Cartellone).
* **Dependencias:** Acceso a los protocolos CAN-bus específicos de fabricantes de maquinaria amarilla (J1939 en lugar de OBD-II estándar).

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Varela evalúa los antídotos:
* **Antídoto #2 (Almacenamiento Asíncrono):** Es la única forma realista de operar en la RN 51. Querer transmitir telemetría densa continua a través de desfiladeros es una utopía técnica. Descargar vía Wi-Fi en puntos fijos es viable porque los camiones paran obligatoriamente para control de aduana y descanso en San Antonio de los Cobres.
* **Antídoto #3 (Pivot a Maquinaria Amarilla):** Excelente movimiento táctico. La maquinaria pesada de tajo abierto consume más combustible por hora que una flota completa de camiones en ruta. Además, al operar en circuito cerrado dentro del yacimiento, las variables operativas (pendientes, tiempos de ciclo de carga) son predecibles en un 95%, lo que hace que los algoritmos de optimización de AndesLogistics funcionen con una precisión quirúrgica.

### Dra. Benavídez evalúa los antídotos:
* **Antídoto #1 (Privacy-First y Homologación Gremial):** Funciona jurídicamente si se certifica ante la AAIP. Pero con Camioneros no basta con firmar un papel. Para que el sindicato no bloquee la RN 51, se debe incluir en la interfaz de la plataforma una vista de control para el propio conductor en su cabina (ej. una pantalla LED en el tablero que le muestre sugerencias mecánicas de conducción eficiente enfocadas exclusivamente en su seguridad vial y reducción de fatiga física, no un ranking de penalidades). Debe presentarse como un "asistente de seguridad vial" para el chofer.

### Lic. Rossi evalúa los antídotos:
* **Antídoto #3 (Pivot a Maquinaria):** Neutraliza completamente el riesgo estructural del Ramal C14. El tren nunca entrará a la cantera de litio ni al rajo abierto de la mina de cobre. La maquinaria pesada off-road seguirá operando por combustión interna o sistemas híbridos durante las próximas tres décadas. El TAM en este nicho es menor en cantidad de unidades, pero el valor capturado por unidad optimizada (reducción de consumo de motores diésel de 1.500 HP) es 10 veces mayor.

### Ing. Krich evalúa los antídotos:
* **Antídoto #2 (Almacenamiento Asíncrono):** Resuelve el problema del descalabro de costos de Iridium. **Riesgo de segundo orden:** Si el camión sufre un accidente grave o vuelco en una quebrada sin cobertura Starlink y la telemetría histórica está guardada localmente en una memoria física rota, se pierde el análisis forense inmediato del siniestro. **Parche correctivo:** Integrar un sistema de transmisión de emergencia por canal satelital mínimo de solo la última posición GPS grabada y el vector de aceleración de choque (tipo caja negra de aviación), limitado a activarse estrictamente ante eventos de despliegue de airbag o desaceleraciones bruscas (>3G).

---

## VEREDICTO FINAL DEL FACILITADOR

### 🟡 REDISEÑAR PLAN

El plan original de AndesLogistics Puna enfocado en la telemetría continua en tiempo real para optimización bimodal de flotas de camiones de larga distancia andinas es **inviable físicamente por limitaciones orográficas satelitales, insostenible financieramente por el costo de conectividad de banda estrecha, y políticamente de alto riesgo por la fricción sindical y regulatoria en Argentina.**

**Recomendación:** Rediseñar la empresa bajo la tesis de **"AndesLogistics Edge & Off-Road"**:
1. **Fase Inmediata (0-6 meses):** Pivotar el motor de software y adquisición de datos hacia la **maquinaria pesada off-road y viales de yacimiento (Antídoto #3)**. Es un mercado cerrado, de alto consumo de combustible, inmune a la sustitución por ferrocarriles y con redes de comunicaciones Wi-Fi locales administradas dentro del yacimiento minero que anulan la necesidad de transmisión satelital móvil cara.
2. **Re-arquitectura IoT (0-12 meses):** Implementar la solución asíncrona "Store-and-Forward" (Antídoto #2) con el parche correctivo de "caja negra" en caso de accidentes catastróficos.
3. **Validación Social-Gremial (0-3 meses):** Implementar el enfoque "Privacy-First" (Antídoto #1) y empaquetar la aplicación como un software de "Asistencia de Seguridad y Confort en Ruta" para el camionero, eliminando cualquier ranking punitivo de productividad.

---

**Backlinks:** [[AndesLogistics_Puna_Logistica]], [[PreMortem_RIGI_Shield]], [[Corredor Bioceanico]], [[Salta]], [[Jujuy]], [[Taca Taca]], [[RIGI]], [[Pre-Mortem Framework]].
