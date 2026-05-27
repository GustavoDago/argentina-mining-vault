---
type: analysis
tags: [risk-analysis, opportunity, oil-gas, marketplace, methodology]
sources: [[Marketplace_Tier2_VacaMuerta]], [[Vaca Muerta]], [[RIGI]], [[Proyecto LLL Oil]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: Marketplace Tier 2 Vaca Muerta — "Uber Freight" de Equipos de Fractura

> **Tesis bajo análisis:** [[Marketplace_Tier2_VacaMuerta]]
> **Análisis escéptico previo:** [[Esceptico_Marketplace_Tier2_VacaMuerta]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2028. El Marketplace Tier 2 ha sido cerrado. La plataforma nunca logró transaccionar un solo "slot" de tiempo de equipo de fractura entre operadoras. Se perdieron US$ 5-8 millones de capital semilla y 20 meses de desarrollo.

### Horizonte Operativo (90 días desde el lanzamiento)

La plataforma se lanzó con un MVP que permitía a las operadoras publicar "slots disponibles" de sus equipos de fractura y perforación. En la primera semana, el equipo comercial descubrió un problema fundamental: ninguna operadora quería publicar sus slots vacíos. YPF, Vista Energy y Tecpetrol consideraron que revelar los tiempos ociosos de sus equipos equivalía a confesar ineficiencias operativas ante sus accionistas y directivos. El VP de Operaciones de Vista comentó en privado: "Si publico que tengo un set de fractura parado 3 días, lo primero que me va a preguntar mi CEO es por qué tenemos un set parado, no cómo monetizarlo". La asimetría informacional que el marketplace pretendía resolver era, en realidad, la herramienta de negociación más poderosa de las operadoras: el monopolio de información sobre su propia capacidad instalada.

### Horizonte Regulatorio (12-18 meses)

La Comisión Nacional de Defensa de la Competencia (CNDC) inició una investigación preliminar sobre el Marketplace Tier 2 tras recibir una denuncia anónima de una operadora mediana. El argumento: la plataforma facilitaba el intercambio de "información competitivamente sensible" (cronogramas de perforación, ubicaciones de pozos activos, precios de contratación de servicios) entre operadoras que compiten directamente por áreas concesionadas. La CNDC determinó que el marketplace constituía un "hub de información" que potencialmente violaba el Art. 1° de la Ley 27.442 de Defensa de la Competencia (acuerdos entre competidores que restrinjan o distorsionen la competencia). Las operadoras, asesoradas por sus departamentos legales, suspendieron preventivamente el uso de la plataforma.

### Horizonte Estructural (3-5 años)

El boom de inversión RIGI resolvió el cuello de botella por la vía del hardware, no del software. Para 2028, la cuenca contaba con 45 sets de fractura operativos (vs. 28 en 2025), y la transición a e-frac (ProPetro, Liberty) redujo los tiempos de movilización inter-pad de 5 días a 36 horas. Los servicios de drilling se expandieron con la entrada de operadores chinos (Sinopec Oilfield Services) y omaníes que aportaron 12 torres adicionales. La utilización promedio de equipos cayó del 95% (saturación de 2025) al 72% (exceso de capacidad), eliminando el dolor que justificaba el marketplace. La escasez era coyuntural, no estructural.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Marcelo Galli — Ex-Gerente de Operaciones de Fractura Hidráulica, SLB Argentina
**Rol:** 20 años en operaciones de well services en la Cuenca Neuquina. Gestionó la flota de 8 sets de fractura de Schlumberger en Añelo. Conoce de primera mano la logística de movilización de equipos entre pads y las negociaciones comerciales con las operadoras.
**Justificación:** Puede evaluar si el concepto de "tiempo ocioso compartible" existe en la realidad operativa de Vaca Muerta, o si es una abstracción de software que no refleja cómo funcionan los contratos de servicios de campo.

### Agente 2: Abog. Laura Quinteros — Especialista en Derecho de la Competencia y Antitrust
**Rol:** Socia de un estudio jurídico de Buenos Aires con especialización en la Ley 27.442 de Defensa de la Competencia. Representó a operadoras petroleras ante la CNDC.
**Justificación:** El marketplace propone que empresas competidoras compartan información sobre capacidad instalada, cronogramas y precios. Este perfil debe evaluar si la plataforma constituye un "hub de intercambio de información competitivamente sensible" que viole las normas de defensa de la competencia.

### Agente 3: Lic. Andrés Barrionuevo — Analista Senior de Upstream, Oil & Gas Investment Banking
**Rol:** 12 años modelando flujos de caja de operadoras petroleras en Argentina. Cobertura directa de YPF, Vista, Tecpetrol y Pampa Energía.
**Justificación:** Debe evaluar si el TAM (Total Addressable Market) del marketplace sobrevive a la expansión de la flota de servicios que el propio RIGI está financiando, y si el modelo de ingresos (comisión por transacción de slot) puede generar un negocio sostenible.

### Agente 4: Ing. Silvia Ramírez — Especialista en Seguros Industriales y Responsabilidad Civil de Oil & Gas
**Rol:** Suscriptora senior de riesgos oil & gas en una reaseguradora internacional (Swiss Re). Diseñó pólizas de responsabilidad civil para operaciones de fractura hidráulica en Argentina.
**Justificación:** La tesis menciona que el marketplace debe gestionar "micro-pólizas de seguro dinámicas" cuando un equipo se cede temporalmente entre empresas. Este perfil debe evaluar si esas micro-pólizas son viables actuarialmente y si las aseguradoras emitirían cobertura para un equipo operado por un tercero no titular del contrato original.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Galli (Operaciones de Fractura)

**A) El detalle ignorado por optimismo:**
Se asumió que los equipos de fractura tienen "tiempo ocioso" que puede ser transaccionado. En la realidad operativa de Vaca Muerta, el "tiempo ocioso" de un set de fractura no es "downtime disponible": es tiempo de movilización entre pads, mantenimiento preventivo programado (cambio de plungers, inspección de líneas de alta presión, reemplazo de bombas centrífugas de hidratación) y espera de condiciones operativas (frentes de tormenta, condiciones de viento >50 km/h que impiden operaciones con grúas). Este "tiempo muerto" no es disponible para un tercero; es estructuralmente necesario para la operación segura del equipo.

Además, la movilización de un set de fractura entre pads del MISMO operador tarda 3-5 días. La movilización entre pads de DIFERENTES operadores (que pueden estar a 80-120 km de distancia en la cuenca) puede tardar 7-12 días por la logística de camiones de transporte especial, escolta vial, y re-calibración en sitio. El costo de movilización inter-operador es de US$ 150.000-300.000 por evento. Para que la transacción sea rentable, el slot cedido debe generar un ingreso neto superior al costo de movilización, lo que requiere un mínimo de 15-20 etapas de fractura continuas (10-15 días de trabajo efectivo). No existe un "slot de 3 días" que sea económicamente viable.

**B) Cadena de eventos hasta el fracaso:**
1. YPF publica un slot de 4 días disponible en un set de fractura en Loma Campana.
2. Vista Energy solicita el slot para completar 6 etapas en Bajada del Palo Este (a 75 km).
3. La movilización tarda 5 días (más que el slot disponible).
4. El set llega a Bajada del Palo, completa solo 3 etapas antes de que YPF lo necesite de vuelta.
5. La re-movilización de vuelta tarda otros 5 días.
6. Total: 10 días de movilización para 3 días de trabajo efectivo. Costo de movilización: US$ 280.000. Ingreso por 3 etapas: US$ 150.000 (a US$ 50.000/etapa).
7. La transacción generó una pérdida neta de US$ 130.000. Ambas partes culpan al marketplace.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| "Tiempo ocioso" no existe: es mantenimiento, movilización y espera operativa | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Costo de movilización inter-operador supera el ingreso neto del slot | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |
| Tiempo de movilización (7-12 días) incompatible con slots de corta duración | Alta (>60%) | Alta (20-50% Capex) | Fulminante (<30 días) |

---

### Agente 2: Abog. Quinteros (Derecho de la Competencia)

**A) El detalle ignorado por optimismo:**
El marketplace propone que operadoras petroleras que compiten directamente por áreas concesionadas en la misma cuenca compartan en una plataforma digital centralizada: (a) cronogramas de perforación y fractura, (b) ubicación y estado de sus equipos, (c) capacidad ociosa, y (d) precios de contratación de servicios. Esta información es la quintaesencia de lo que la Ley 27.442 y las guidelines internacionales de la OCDE denominan "competitively sensitive information" (CSI).

El Art. 1° de la Ley 27.442 prohíbe "los acuerdos entre dos o más competidores [...] que tengan por objeto o efecto [...] limitar, restringir, falsear o distorsionar la competencia". La CNDC ha interpretado consistentemente que el intercambio de información desagregada sobre precios, volúmenes y capacidad entre competidores directos constituye una "práctica concertada" incluso si no hay un acuerdo formal de precios. El marketplace, al ser el vehículo tecnológico que facilita este intercambio, puede ser considerado como "facilitador de colusión tácita" bajo la doctrina del "hub-and-spoke cartel".

**B) Cadena de eventos hasta el fracaso:**
1. El marketplace acumula datos de 5 operadoras (YPF, Vista, Tecpetrol, Pampa, Pluspetrol) sobre capacidad de fractura y precios de contratación.
2. Un analista de la CNDC detecta que, desde la adopción del marketplace, los precios de contratación de servicios de fractura convergieron un 12% (efecto algorítmico de transparencia de precios).
3. La CNDC abre una investigación por "facilitación de colusión tácita vía plataforma digital" (Art. 2° inc. a, Ley 27.442).
4. Las operadoras reciben notificaciones de inspección de la CNDC. Los departamentos legales corporativos emiten directiva inmediata de "cessation of use" de la plataforma.
5. El marketplace queda sin usuarios de un día para otro.
6. La CNDC impone multas de AR$ 200-500M a la plataforma y órdenes de cesación de la actividad.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Investigación por facilitación de colusión tácita (Ley 27.442) | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Intercambio de CSI (cronogramas, precios, capacidad) entre competidores directos | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Convergencia algorítmica de precios interpretada como "fijación concertada" | Media (30-60%) | Alta (20-50% Capex) | Gradual (6-18 meses) |

---

### Agente 3: Lic. Barrionuevo (Financiero / Upstream)

**A) El detalle ignorado por optimismo:**
La tesis asume que la escasez de equipos de fractura es un estado permanente que justifica la existencia del marketplace. En realidad, la escasez de 2024-2025 fue coyuntural y auto-correctiva. El RIGI está inyectando US$ 60.000M+ en upstream (YPF US$ 25.000M, Pluspetrol US$ 12.000M, Chevron US$ 10.000M, Pampa US$ 4.500M, etc.). Esta ola de inversión financia directamente la expansión de la flota de servicios:

- SLB anunció 4 sets de fractura nuevos para Argentina en 2026-2027 (US$ 120M).
- Halliburton adquirió la flota de San Antonio Internacional en 2025 y la expandió en un 40%.
- ProPetro y Liberty Oilfield desplegaron los primeros sets e-frac (eléctricos) en Añelo, con productividades 30% superiores a los diésel.
- El gobierno chino ofreció financiamiento blando para el despliegue de 6 torres de perforación Sinopec en Neuquén.

Para 2028, la cuenca pasará de 28 sets de fractura activos a 42-48. La utilización promedio caerá del 95% al 70-75%. En un mercado con exceso de capacidad, no hay "tiempo ocioso" que optimizar porque hay sets disponibles esperando trabajo. El marketplace se convierte en un catálogo inútil de sets desocupados compitiendo por precio a la baja.

**B) Cadena de eventos hasta el fracaso:**
1. El marketplace se lanza en Q3 2026 con una propuesta de valor: "ahorrá US$ 80.000/día de stand-by".
2. En Q1 2027, entran en servicio 8 sets nuevos de SLB, Halliburton y ProPetro.
3. La utilización promedio cae al 80%. Los precios de contratación bajan un 15% por la competencia.
4. Las operadoras descubren que ya no necesitan compartir equipos: hay sets disponibles en el mercado spot a precios competitivos.
5. El marketplace pierde su propuesta de valor. Los pocos usuarios lo usan como "benchmark de precios" gratuito, sin transaccionar.
6. Los ingresos por comisión (3-5% por transacción) nunca superan US$ 200K/año, insuficiente para cubrir el Opex del equipo de desarrollo.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Escasez coyuntural auto-correctiva: la flota se expande orgánicamente por el RIGI | Alta (>60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Utilización de equipos cae del 95% al 70-75%, eliminando la necesidad del marketplace | Alta (>60%) | Alta (20-50% Capex) | Gradual (6-18 meses) |
| Ingresos por comisión insuficientes para cubrir Opex de desarrollo | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |

---

### Agente 4: Ing. Ramírez (Seguros Industriales)

**A) El detalle ignorado por optimismo:**
La tesis menciona casualmente que el marketplace debe gestionar "micro-pólizas de seguro dinámicas" cuando un equipo se cede temporalmente. Esto no es un feature secundario; es la barrera más difícil de todo el modelo de negocio.

Un set de fractura hidráulica opera a presiones de 10.000-15.000 PSI con fluidos abrasivos a alta temperatura. Un accidente de campo (blow-out de línea de alta presión, falla de wellhead, incendio de bomba) puede causar: (a) muertes (la tasa de accidentes fatales en well services en Argentina es de 2-3/año), (b) daño ambiental por derrame de fluido de fractura con químicos BTEX, y (c) pérdida del pozo (US$ 10-20M).

La póliza de responsabilidad civil de un operador de well services cubre sus operaciones con su propio personal, sus propios procedimientos operativos estándar (SOP) y su propia cadena de supervisión. Cuando ese equipo opera temporalmente bajo la dirección de un TERCER operador (la empresa que "alquiló" el slot), ¿quién responde si hay un accidente? El owner del equipo (cuya póliza no cubre operación bajo terceros), el operador minero que contrató el slot (cuya póliza cubre generalmente solo daños propios y de su contratista directo), o el marketplace que intermedió la transacción?

Las reaseguradoras (Munich Re, Swiss Re, Lloyd's) no emiten pólizas de responsabilidad civil para "cesión temporal de equipos de alta presión a terceros no calificados" porque el riesgo moral es inaceptable: el operador temporal no tiene los mismos incentivos de mantenimiento preventivo que el owner, y los procedimientos de seguridad pueden diferir.

**B) Cadena de eventos hasta el fracaso:**
1. Vista Energy cede temporalmente un set de fractura a Tecpetrol vía el marketplace.
2. El set opera bajo el Company Man de Tecpetrol (no de Vista) con procedimientos de Tecpetrol.
3. Un plunger que Vista programó reemplazar la semana siguiente falla bajo la operación de Tecpetrol. La línea de alta presión revienta.
4. Un operario de Tecpetrol sufre quemaduras graves.
5. La ART de Tecpetrol reclama a Vista (owner del equipo) por "equipo defectuoso cedido sin certificado de aptitud".
6. La aseguradora de Vista rechaza el siniestro porque la póliza no cubría "cesión temporal del equipo a terceros no contratados".
7. La aseguradora de Tecpetrol rechaza el siniestro porque "el equipo no fue inspeccionado por nuestro equipo de HSE pre-operación".
8. El marketplace es demandado civilmente como "intermediario que facilitó una operación sin cobertura de seguro adecuada".
9. El caso se convierte en jurisprudencia que mata cualquier intento futuro de "sharing economy" en oil & gas.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Inexistencia de póliza de RC para "cesión temporal de equipos de alta presión" | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Accidente con equipo cedido genera litigio entre aseguradoras sin cobertura | Media (30-60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Marketplace responsabilizado como "facilitador" de operación sin seguro | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | "Tiempo ocioso" no existe: es mantenimiento y movilización | Galli | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Intercambio de CSI entre competidores viola Ley 27.442 | Quinteros | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 3 | Escasez coyuntural auto-correctiva por expansión RIGI | Barrionuevo | Estructural | Alta | Crítica | Gradual | **A×C** |
| 4 | Inexistencia de póliza de RC para cesión temporal de equipos | Ramírez | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 5 | Costo de movilización inter-operador supera ingreso del slot | Galli | Operativo | Alta | Alta | Rápida | **A×A** |
| 6 | Ninguna operadora quiere publicar sus tiempos ociosos | Galli | Operativo | Alta | Alta | Fulminante | **A×A** |
| 7 | Convergencia de precios interpretada como colusión tácita | Quinteros | Regulatorio | Media | Crítica | Gradual | **M×C** |
| 8 | Accidente con equipo cedido genera litigio sin cobertura | Ramírez | Operativo | Media | Crítica | Rápida | **M×C** |
| 9 | Utilización cae al 70-75%, eliminando necesidad del marketplace | Barrionuevo | Estructural | Alta | Alta | Gradual | **A×A** |
| 10 | Marketplace responsabilizado como facilitador sin seguro | Ramírez | Regulatorio | Media | Crítica | Gradual | **M×C** |
| 11 | Ingresos por comisión insuficientes para cubrir Opex | Barrionuevo | Operativo | Alta | Alta | Rápida | **A×A** |
| 12 | Investigación CNDC por facilitación de colusión | Quinteros | Regulatorio | Media | Crítica | Gradual | **M×C** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **LA UNIDAD ECONÓMICA NO EXISTE (Vectores #1, #5, #6):** El concepto de "slot disponible transaccionable" no existe en la operativa real de fractura hidráulica. Lo que se llama "tiempo ocioso" es mantenimiento, movilización y espera operativa — todo estructuralmente necesario y no cedible. Cuando sí existe un gap genuino, el costo de movilizar el equipo 80-120 km hasta el pad de otro operador (US$ 150-300K, 7-12 días) supera el ingreso neto del slot. Y las operadoras no quieren publicar sus ineficiencias. **El producto resuelve un problema que no existe en la forma en que lo modela.**

2. **BOMBA ANTITRUST (Vectores #2, #7, #12):** Un marketplace que centraliza cronogramas de perforación, capacidad de fractura y precios de contratación de 5 operadoras que compiten por las mismas áreas concesionadas es, bajo la óptica de la Ley 27.442, un "hub de información competitivamente sensible" que facilita la colusión tácita. La convergencia algorítmica de precios que genera la transparencia del marketplace puede ser interpretada por la CNDC como fijación concertada de precios. Las operadoras cancelarán su uso al primer contacto de la CNDC.

3. **MERCADO EN COLAPSO ESTRUCTURAL (Vectores #3, #4, #9):** La escasez de sets de fractura de 2024-2025 fue coyuntural y el RIGI está financiando su propia resolución: 14-20 sets nuevos entrarán en servicio en 2026-2028. Para cuando el marketplace esté maduro, la utilización habrá caído al 70-75% y no habrá dolor de mercado que resolver. Simultáneamente, la barrera de seguros (inexistencia de pólizas RC para cesión temporal de equipos de alta presión) hace que cada transacción sea una bomba de responsabilidad civil sin cobertura.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Pivote a "Marketplace de Servicios Tier 3" — No Equipos Pesados, Sino Servicios Complementarios

- **Acción específica:** Abandonar la transacción de equipos de alta presión (sets de fractura, towers de perforación). En su lugar, crear un marketplace para servicios complementarios de baja criticidad y bajo riesgo de responsabilidad: transporte de arena y proppant entre silos, servicios de wireline (perfilaje), operaciones de coiled tubing no críticas, alquiler de campamentos modulares, transporte de personal en camionetas 4x4, y servicios de catering/limpieza de campamento. Estos servicios SÍ tienen capacidad ociosa transaccionable, los costos de movilización son bajos (camionetas, no trailers de 120 toneladas), y no generan riesgos de responsabilidad civil de alta presión.
- **Responsable sugerido:** CEO del Marketplace Tier 2 (que debería renombrarse "Marketplace de Servicios Vaca Muerta").
- **Plazo de implementación:** MVP en 3-4 meses (reducción de scope vs. el diseño original).
- **Costo estimado:** US$ 500.000-1M (vs. US$ 5-8M del modelo con equipos pesados y motor InsurTech).
- **Métrica de éxito:** 50+ transacciones de servicios complementarios en los primeros 6 meses con un take rate de 5-8%.
- **Dependencias:** Aceptación de las Pymes de servicios de Añelo (el marketplace debe atraer primero a los proveedores, no a las operadoras).

### Antídoto #2: Rediseñar como "Analytics de Eficiencia de Flota" — Sin Transacción, Sin CSI

- **Acción específica:** Abandonar el marketplace transaccional (que genera el riesgo antitrust). Pivotar a una plataforma de analytics que cada operadora usa en forma AISLADA para optimizar la utilización de su PROPIA flota. No hay intercambio de información entre competidores. Cada operadora ve solo sus datos. El algoritmo optimiza la secuencia de pads, los tiempos de movilización, y el scheduling de mantenimiento preventivo para maximizar las horas productivas por set por mes. Modelo SaaS con suscripción mensual por set monitoreado.
- **Responsable sugerido:** CTO del Marketplace.
- **Plazo de implementación:** Prototipo en 4 meses. Piloto con YPF (que tiene la flota más grande y la mayor urgencia de eficiencia) en 6-8 meses.
- **Costo estimado:** US$ 800.000-1.5M (desarrollo de software + sensórica IoT por set).
- **Métrica de éxito:** Aumento demostrado de ≥10% en las horas productivas por set por mes vs. el baseline de YPF.
- **Dependencias:** Acceso a datos operativos de YPF (partnership estratégico necesario, posiblemente vía Y-TEC).

### Antídoto #3: Framework Legal Anti-Antitrust — "Clean Room" de Datos

- **Acción específica:** Si se insiste en el marketplace transaccional, implementar una arquitectura de "clean room" donde la plataforma nunca revele a ninguna operadora los datos de sus competidores. El matching algorítmico opera sobre datos anonimizados y agregados: la operadora que busca un set solo ve "set disponible en zona X, capacidad Y, precio Z", sin saber quién es el owner. La negociación ocurre a través de la plataforma con identidades reveladas solo al momento de la firma del contrato. Obtener un dictamen previo de la CNDC (procedimiento de "consulta previa" bajo Art. 13 de la Ley 27.442) que bendiga la arquitectura.
- **Responsable sugerido:** Director legal del Marketplace + estudio jurídico especializado en antitrust.
- **Plazo de implementación:** 4-6 meses para el dictamen de la CNDC + 3 meses de implementación técnica.
- **Costo estimado:** US$ 200.000-400.000 en honorarios legales + desarrollo de clean room.
- **Métrica de éxito:** Dictamen favorable de la CNDC que certifique la legalidad de la arquitectura de clean room.
- **Dependencias:** Voluntad de la CNDC de emitir un dictamen consultivo (no es vinculante y puede demorar 6-12 meses).

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Galli evalúa los antídotos:
- **Antídoto #1 (Servicios Tier 3):** Operativamente sólido. Los servicios complementarios (transporte de arena, wireline, campamentos) SÍ tienen capacidad ociosa real y tiempos de movilización de horas (no días). Las Pymes de servicios de Añelo serían los primeros beneficiarios. El dolor de mercado es real: hoy, un operador de wireline de Añelo pierde el 30% de su tiempo buscando clientes por WhatsApp. **Veredicto: el producto correcto para el mercado correcto.**
- **Antídoto #2 (Analytics aislado):** Técnicamente correcto, pero el TAM es limitado: 6-8 operadoras × US$ 100-200K/año × 3-5 sets cada una = US$ 1.8-8M/año. Viable como SaaS de nicho. **Sin riesgo de segundo orden.**

### Abog. Quinteros evalúa los antídotos:
- **Antídoto #1 (Servicios Tier 3):** El riesgo antitrust se reduce drásticamente porque los proveedores de servicios complementarios (Pymes de transporte, wireline, catering) no son competidores directos entre sí. La información compartida (disponibilidad de un camión de arena) no es "competitively sensitive" en los términos de la Ley 27.442. **Veredicto: legalmente limpio.**
- **Antídoto #3 (Clean room):** La consulta previa a la CNDC es una buena práctica pero no garantiza nada: el dictamen no es vinculante y una nueva administración de la CNDC podría revertirlo. Además, el anonimato se quiebra en el momento de la firma del contrato, y la base de datos centralizada sigue conteniendo CSI. **Riesgo de segundo orden: la clean room puede ser considerada insuficiente por la CNDC si los datos desanonimizados son accesibles post-firma.**

### Lic. Barrionuevo evalúa los antídotos:
- **Antídoto #1 (Servicios Tier 3):** El TAM de servicios complementarios en Vaca Muerta es de US$ 800M-1.200M anuales (transporte de arena: US$ 200M, wireline: US$ 150M, campamentos: US$ 100M, catering: US$ 80M, transporte de personal: US$ 50M, otros: US$ 220-620M). Con un take rate del 5%, el marketplace capturaría US$ 40-60M/año. Este es un negocio real. **Veredicto: unit economics viables.**
- **Antídoto #2 (Analytics):** Menor riesgo pero menor retorno. Recomendable como producto complementario del Antídoto #1, no como producto standalone.

### Ing. Ramírez evalúa los antídotos:
- **Antídoto #1 (Servicios Tier 3):** El riesgo de RC baja drásticamente. Transaccionar un camión de arena (presión atmosférica, carga inerte) no tiene la misma exposición de RC que un set de fractura (15.000 PSI, fluidos tóxicos). Las pólizas de seguro estándar de flota de transporte cubren cesión temporal de vehículos con un endoso simple (costo: US$ 500-2.000/año). **Veredicto: asegurable.**
- **Antídoto #3 (Clean room):** La clean room no resuelve el problema de seguros. Aunque el matching sea anónimo, el equipo de alta presión sigue operando bajo un tercero sin cobertura RC adecuada. **Sin parche posible para la capa de seguros de equipos Tier 1/2.**

---

## VEREDICTO FINAL DEL FACILITADOR

### 🔴 REDISEÑAR PLAN (con potencial de ABORTAR si no se pivotea el scope)

El modelo original del Marketplace Tier 2 (transacción de equipos de fractura y perforación entre operadoras competidoras) es **inviable en su forma actual** por cuatro razones simultáneas: (1) la unidad económica básica (el "slot transaccionable") no existe en la operativa real, (2) la plataforma constituye un hub de información anticompetitiva bajo la Ley 27.442, (3) la escasez de equipos es coyuntural y se resuelve orgánicamente por el RIGI, y (4) no existe cobertura de seguro RC para la cesión temporal de equipos de alta presión.

**Recomendación:** Ejecutar un **pivote radical de scope** hacia el **Antídoto #1: Marketplace de Servicios Tier 3/Complementarios**:

1. **Target:** Pymes de servicios de Añelo (no operadoras majors).
2. **Scope:** Transporte de arena, wireline, coiled tubing no crítico, campamentos, catering, transporte de personal — servicios de baja criticidad, baja RC, alta fragmentación.
3. **Valor real:** Reducir el 30% de tiempo improductivo que las Pymes de servicios pasan buscando clientes por WhatsApp.
4. **TAM:** US$ 800M-1.200M/año en servicios complementarios. Take rate 5% = US$ 40-60M/año en ingresos.
5. **Analytics como add-on:** Incorporar el Antídoto #2 como módulo premium para las operadoras que quieran optimizar internamente la utilización de sus propias flotas.

**El verdadero dolor de Vaca Muerta no es que falten sets de fractura; es que hay 3.000 Pymes de servicios en Añelo coordinando su trabajo por WhatsApp sin visibilidad de demanda ni gestión profesional de calendario.** Ahí es donde hay un marketplace real.

---

**Backlinks:** [[Marketplace_Tier2_VacaMuerta]], [[Vaca Muerta]], [[RIGI]], [[Proyecto LLL Oil]], [[Pre-Mortem Framework]].
