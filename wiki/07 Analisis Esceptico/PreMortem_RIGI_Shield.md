---
type: analysis
tags: [risk-analysis, opportunity, regulatory, infrastructure, methodology]
sources: [[RIGI_Shield_Seguridad]], [[Esceptico_Seguridad_RIGI]], [[RIGI]], [[Corredor Bioceanico]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: RIGI-Shield - SaaS de Inteligencia Logística y Escolta Virtual

> **Tesis bajo análisis:** [[RIGI_Shield_Seguridad]]
> **Análisis escéptico previo:** [[Esceptico_Seguridad_RIGI]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2027. El proyecto RIGI-Shield ha fracasado. La plataforma SaaS de inteligencia logística y escolta virtual nunca fue adoptada por las transportistas mineras. El prototipo de integración con los despachos de emergencias provinciales fue rechazado por los ministerios de seguridad de Salta, Jujuy y San Juan. Se perdieron US$ 1.5-3 millones y 14 meses de desarrollo.

### Horizonte Operativo (90 días desde el lanzamiento)
La unidad telemática instalada en 20 camiones mineros de prueba en la RN 51 (Salta-Paso Sico) funcionó correctamente durante las primeras 3 semanas. En la semana 4, una caravana de 8 camiones de concentrado de cobre de [[Taca Taca]] ingresó a la zona de sombra satelital de la Quebrada del Toro. Los dispositivos conmutaron correctamente a modo offline, pero al salir de la quebrada y reconectarse, descargaron simultáneamente 6 horas de telemetría acumulada contra el servidor. El sistema interpretó 8 reconexiones simultáneas con gaps de datos como 8 "eventos de pánico" separados y activó el protocolo de alerta a Gendarmería Nacional. Tres patrullas de GNA se desplegaron innecesariamente, interrumpiendo el tránsito en la ruta durante 4 horas y generando una queja formal de la empresa transportista contra RIGI-Shield por "falsa alarma que paralizó nuestra operación logística".

### Horizonte Regulatorio (12-18 meses)
La Res. 461/2026 que creó la Mesa de Coordinación resultó ser una resolución declarativa sin capacidad operativa real. La Mesa se reunió 3 veces en 2026 y se disolvió en 2027 por cambio de autoridades en el Ministerio de Seguridad tras la renuncia del ministro. No se creó ninguna API estatal, ningún protocolo digital de coordinación ni ningún canal de comunicación cifrada entre las fuerzas y las empresas. RIGI-Shield descubrió que su premisa central (integrar una interfaz gubernamental de seguridad) no tenía contraparte tecnológica del lado estatal. El Estado argentino coordinaba la seguridad de los convoyes por WhatsApp y radio VHF, y no tenía interés ni presupuesto para cambiar.

### Horizonte Estructural (3-5 años)
La conflictividad social en las rutas mineras no se resolvió con tecnología sino con negociación política directa entre las gobernaciones provinciales y los sindicatos/comunidades. Los acuerdos de reparto de regalías y empleo local redujeron un 60% los cortes de ruta en la Puna. Simultáneamente, Starlink desplegó cobertura masiva en los corredores andinos, eliminando la ventaja competitiva de la "conectividad híbrida Edge-to-Satellite" de RIGI-Shield: cualquier chofer con un celular y Starlink podía llamar a Gendarmería directamente. La capa de inteligencia logística se commoditizó.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Crio. (R) Jorge Villanueva — Ex-Jefe de Logística de Gendarmería Nacional Argentina
**Rol:** 25 años en GNA, los últimos 8 como jefe de la División Seguridad Vial y Escolta de Cargas Especiales en la Zona Noroeste (Salta-Jujuy-Tucumán).
**Justificación:** Conoce de primera mano cómo opera realmente la coordinación de seguridad de convoyes mineros en la Puna. Puede evaluar si la propuesta de "Shadow API gubernamental" tiene alguna correspondencia con la realidad operativa de las fuerzas federales argentinas.

### Agente 2: Lic. Gabriel Montero — Especialista en Geopolítica de Conflictos Territoriales
**Rol:** Investigador del CONICET en conflictividad social asociada a la minería de gran escala en el NOA argentino. Autor de 3 papers sobre cortes de ruta y negociación con comunidades originarias en Salinas Grandes.
**Justificación:** Puede evaluar si una plataforma de "monitoreo predictivo de protestas" es viable ética y políticamente, y si su uso por parte de empresas mineras no constituye una forma de vigilancia social que profundice el conflicto en lugar de mitigarlo.

### Agente 3: Ing. Diego Fuentes — Arquitecto de Sistemas de Telecomunicaciones Satelitales
**Rol:** Ingeniero senior en una empresa de comunicaciones satelitales que despliega redes VSAT y Starlink Business en zonas remotas de Latinoamérica. Diseñó la red de comunicaciones de la mina Veladero (Barrick) a 4.200 msnm en San Juan.
**Justificación:** Es el experto más calificado para evaluar la viabilidad de la "conectividad híbrida Edge-to-Satellite" en los corredores andinos, considerando las limitaciones reales de orografía, latitud y disponibilidad de Starlink en la Puna.

### Agente 4: Abog. Claudia Fernández — Especialista en Protección de Datos y Seguridad de la Información
**Rol:** Socia de un estudio jurídico de Buenos Aires especializado en Ley de Protección de Datos Personales (25.326) y regulación de sistemas de vigilancia. Asesora de la Agencia de Acceso a la Información Pública (AAIP).
**Justificación:** RIGI-Shield recolectaría geolocalización en tiempo real de personas (choferes), alertas de "pánico" y datos de inteligencia sobre protestas sociales. Este perfil puede evaluar el riesgo legal de violar la Ley 25.326 y los derechos de habeas data de los trabajadores y comunidades monitorizadas.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Crio. (R) Villanueva (Operaciones de Seguridad)

**A) El detalle ignorado por optimismo:**
Se asumió que existe una "Mesa de Coordinación" operativa con "despachos de seguridad provinciales y federales" que pueden recibir alertas automatizadas. La realidad es que la coordinación de seguridad de convoyes mineros en el NOA argentino funciona así: el transportista llama por celular al puesto de GNA más cercano (o por radio HF si no hay señal), informa que va a pasar con carga, y el gendarme de turno decide discrecionalmente si envía un móvil de escolta o no, según la disponibilidad de personal y combustible. No hay sistema digital, no hay API, no hay protocolo estandarizado. La Res. 461/2026 creó una mesa política, no una infraestructura tecnológica.

La propuesta de RIGI-Shield de "enviar geolocalización en tiempo real ante eventos de intrusión" asume que hay alguien del otro lado procesando esa telemetría en una pantalla. En la práctica, el gendarme de turno en el puesto de Abra Pampa tiene un celular personal (no institucional), una radio VHF portátil y un patrullero con 250.000 km encima. Si recibe una alerta push de RIGI-Shield, no tiene el equipamiento ni el protocolo para actuar en base a coordenadas GPS en tiempo real.

**B) Cadena de eventos hasta el fracaso:**
1. RIGI-Shield envía una alerta de "convoy detenido por bloqueo de ruta" con coordenadas GPS precisas a la central de GNA Salta.
2. La central recibe la alerta en un email institucional que nadie monitorea fuera de horario administrativo (8-14hs).
3. El operador de radio de turno recibe la alerta por redundancia SMS a su celular personal, pero no tiene autoridad para despachar un operativo sin orden del jefe de destacamento.
4. El jefe de destacamento está en Salta Capital a 350 km. Tarda 40 minutos en responder por teléfono.
5. Cuando autoriza el operativo, el patrullero más cercano está a 120 km por ripio de montaña (3 horas de viaje).
6. Para cuando llega GNA, el corte de ruta se disolvió solo (como ocurre en el 70% de los casos).
7. La transportista concluye que RIGI-Shield no aceleró la respuesta real y cancela la suscripción.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Inexistencia de contraparte tecnológica estatal (no hay API ni protocolo digital) | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Tiempos de respuesta reales de GNA incompatibles con alertas en tiempo real | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |
| Falsas alarmas por reconexión post-zona-de-sombra desacreditan el sistema | Media (30-60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |

---

### Agente 2: Lic. Montero (Geopolítica/Conflictos)

**A) El detalle ignorado por optimismo:**
El "Motor de Alertas Predictivas" de RIGI-Shield incluye "monitoreo algorítmico de cortes de ruta y protestas gremiales (sabotaje sindical)". Esto no es un feature técnico neutro. Es un sistema de vigilancia social que categoriza la protesta legítima de comunidades indígenas y trabajadores sindicalizados como "sabotaje" y la procesa como un "evento de seguridad" al mismo nivel que el crimen organizado. Esto tiene implicancias éticas, legales y estratégicas devastadoras.

En el contexto del NOA argentino, las comunidades Kolla, Atacama y Diaguita tienen derechos territoriales preexistentes reconocidos por el Art. 75 inciso 17 de la Constitución Nacional. Un sistema que monitorea algorítmicamente sus movimientos y los categoriza como "amenazas" para alertar a fuerzas de seguridad federales puede ser judicializado por organizaciones de derechos humanos como una forma de hostigamiento y vigilancia ilegal.

**B) Cadena de eventos hasta el fracaso:**
1. RIGI-Shield despliega el motor de alertas predictivas en el corredor RN 51 (Salta).
2. El algoritmo detecta "concentración anómala de personas" en un cruce de ruta cerca de San Antonio de los Cobres y genera una alerta de "riesgo de corte".
3. La "concentración anómala" era la Feria de la Pachamama, un evento cultural ancestral de la comunidad Atacameña.
4. GNA recibe la alerta y envía un operativo de prevención que se estaciona frente a la feria con actitud intimidante.
5. La comunidad denuncia a RIGI-Shield y a la empresa transportista ante la Defensoría del Pueblo de Salta y la Secretaría de Derechos Humanos de la Nación.
6. FARN (Fundación Ambiente y Recursos Naturales) presenta un amparo colectivo argumentando que el sistema constituye vigilancia ilegal de pueblos originarios.
7. El caso llega a medios internacionales (The Guardian, BBC). Las mineras que contratan RIGI-Shield enfrentan presión ESG de sus financiadores.
8. BHP, Rio Tinto y Glencore prohíben a sus contratistas usar la plataforma para evitar contaminación reputacional.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Categorización de protesta legítima como "sabotaje" genera denuncia por vigilancia ilegal | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Uso del sistema como evidencia de hostigamiento a comunidades originarias | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Presión ESG de financiadores internacionales prohíbe el uso de la plataforma | Media (30-60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

### Agente 3: Ing. Fuentes (Telecomunicaciones)

**A) El detalle ignorado por optimismo:**
La propuesta asume que la conectividad Starlink resuelve las zonas de sombra andinas. La realidad es más matizada. Starlink opera en bandas Ku/Ka (12-18 GHz / 26-40 GHz) que son altamente susceptibles a la atenuación por lluvia y nieve. En la Puna, las tormentas eléctricas de verano (noviembre-marzo) interrumpen la señal Starlink durante 2-4 horas por evento, precisamente cuando la visibilidad se reduce y la necesidad de comunicación es crítica. Además, la terminal Starlink convencional (Dishy McFlat v3) consume 50-75W de potencia continua, un problema serio para un camión que necesita esa energía para el sistema de frenos neumáticos, refrigeración de carga y calefacción de cabina a 4.000 msnm.

Pero el problema principal es otro: Starlink ya está disponible. El chofer de cualquier transportista puede comprar un kit Starlink por US$ 600 y tener conectividad directa. La propuesta de RIGI-Shield de "conectividad híbrida Edge-to-Satellite" como ventaja competitiva se desvanece cuando la conectividad satelital se commoditiza.

**B) Cadena de eventos hasta el fracaso:**
1. RIGI-Shield instala unidades telemáticas con modem Starlink Business en 30 camiones.
2. Starlink funciona bien en el 70% del corredor. En las quebradas profundas (Quebrada del Toro, Quebrada de Humahuaca), la señal se pierde completamente por obstrucción topográfica del horizonte.
3. Se agrega un modem Iridium como redundancia (costo adicional: US$ 1.500/unidad + US$ 150/mes de suscripción por camión).
4. El costo total de conectividad por camión asciende a US$ 300-400/mes (Starlink Business + Iridium).
5. La transportista compara: un kit Starlink propio cuesta US$ 120/mes y le da conectividad para todo (llamadas, WhatsApp, GPS tracker).
6. RIGI-Shield cobra US$ 500-800/mes por camión (conectividad + plataforma). La transportista no percibe US$ 400-500 de valor agregado sobre lo que Starlink le da gratis.
7. El churn rate supera el 60% anual.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Commoditización de conectividad satelital (Starlink retail) destruye la ventaja | Alta (>60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Zonas de sombra topográfica irresolubles en quebradas profundas | Alta (>60%) | Moderada (5-20% Capex) | Fulminante (<30 días) |
| Costo de conectividad dual (Starlink + Iridium) por camión demasiado alto vs. valor percibido | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |

---

### Agente 4: Abog. Fernández (Protección de Datos)

**A) El detalle ignorado por optimismo:**
RIGI-Shield recolectaría tres categorías de datos extremadamente sensibles bajo la legislación argentina: (a) geolocalización en tiempo real de trabajadores (choferes) — dato personal protegido por la Ley 25.326 que requiere consentimiento informado, (b) datos de inteligencia sobre movimientos de comunidades y sindicatos — que pueden constituir "archivos o registros de datos referidos a personas por el solo hecho de su opinión política, condición social o pertenencia a organización alguna" (Art. 7 inc. 3 de la Ley 25.326, que PROHÍBE expresamente la recolección de estos datos), y (c) comunicaciones con fuerzas de seguridad que pueden ser clasificadas como información de seguridad nacional.

El diseño de RIGI-Shield cruza todas las líneas rojas de la ley de datos personales argentina y potencialmente del GDPR (si procesa datos de conductores europeos de empresas con casas matrices en la UE, como Glencore o BHP).

**B) Cadena de eventos hasta el fracaso:**
1. Un chofer de camión sindicalizado descubre que RIGI-Shield rastrea su ubicación GPS las 24 horas, incluso cuando está en descanso en la cabina.
2. El sindicato CAMIONEROS (Moyano) presenta una denuncia ante la AAIP (Agencia de Acceso a la Información Pública) por violación de la Ley 25.326.
3. La AAIP investiga y descubre que RIGI-Shield también recolecta datos de "concentraciones de personas" cerca de rutas mineras, lo que clasifica como procesamiento ilícito de datos sensibles (Art. 7).
4. La AAIP impone una multa de AR$ 5-10M y ordena la eliminación de toda la base de datos de geolocalización.
5. El sindicato CAMIONEROS convoca un paro de transportistas que afecta los convoyes mineros de Taca Taca, Los Azules y Rincón.
6. Las mineras culpan a RIGI-Shield por haber desencadenado un conflicto gremial innecesario y cancelan todos los contratos.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Violación de Ley 25.326 por geolocalización 24/7 de trabajadores sin consentimiento adecuado | Alta (>60%) | Alta (20-50% Capex) | Gradual (6-18 meses) |
| Procesamiento ilícito de datos sensibles (Art. 7) por monitoreo de protestas/sindicatos | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Conflicto gremial con CAMIONEROS por percepción de vigilancia laboral | Media (30-60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Inexistencia de contraparte tecnológica estatal | Villanueva | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Categorización de protesta legítima como "sabotaje" → denuncia | Montero | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 3 | Procesamiento ilícito de datos sensibles (Art. 7, Ley 25.326) | Fernández | Regulatorio | Alta | Crítica | Rápida | **A×C** |
| 4 | Commoditización de Starlink destruye ventaja de conectividad | Fuentes | Estructural | Alta | Crítica | Gradual | **A×C** |
| 5 | Tiempos de respuesta reales de GNA incompatibles con alertas RT | Villanueva | Operativo | Alta | Alta | Rápida | **A×A** |
| 6 | Conflicto gremial con CAMIONEROS por vigilancia laboral | Fernández | Regulatorio | Media | Crítica | Rápida | **M×C** |
| 7 | Presión ESG prohíbe el uso de la plataforma | Montero | Estructural | Media | Crítica | Rápida | **M×C** |
| 8 | Violación Ley 25.326 por geolocalización 24/7 de trabajadores | Fernández | Regulatorio | Alta | Alta | Gradual | **A×A** |
| 9 | Costo de conectividad dual por camión demasiado alto | Fuentes | Operativo | Alta | Alta | Rápida | **A×A** |
| 10 | Falsas alarmas por reconexión post-zona-de-sombra | Villanueva | Operativo | Media | Alta | Rápida | **M×A** |
| 11 | Uso del sistema como evidencia de hostigamiento a comunidades | Montero | Regulatorio | Media | Crítica | Gradual | **M×C** |
| 12 | Zonas de sombra topográfica irresolubles en quebradas | Fuentes | Operativo | Alta | Moderada | Fulminante | **A×M** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **AUSENCIA DE CONTRAPARTE ESTATAL (Vectores #1, #5):** La premisa central del negocio — integrar una "Shadow API gubernamental" — no tiene correlato en la realidad operativa del Estado argentino. La Res. 461/2026 es una mesa política, no una infraestructura digital. GNA coordina por radio VHF y WhatsApp. No hay CTO del otro lado de la API. RIGI-Shield estaría construyendo un cliente HTTP que apunta a un servidor que no existe.

2. **BOMBA LEGAL DE VIGILANCIA Y DATOS PERSONALES (Vectores #2, #3, #6, #8, #11):** El producto como está diseñado viola la Ley 25.326 en al menos dos artículos, puede ser judicializado como vigilancia de pueblos originarios y puede desencadenar un conflicto gremial con el sindicato de camioneros. La combinación de riesgo legal + riesgo social + riesgo gremial hace que el producto sea radioactivo para cualquier minera con estándares ESG.

3. **COMMODITIZACIÓN DE LA CONECTIVIDAD (Vectores #4, #9, #12):** Starlink ha destruido la barrera de entrada de "conectividad en zonas remotas". Cualquier camionero con US$ 600 y US$ 120/mes tiene conectividad satelital. La capa de conectividad de RIGI-Shield no genera valor diferencial. Y en las quebradas profundas donde Starlink falla, también falla RIGI-Shield.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Pivote a "Optimización Logística" — Eliminar la Capa de Seguridad
- **Acción específica:** Rediseñar RIGI-Shield como una plataforma pura de optimización logística y gestión de flota minera, NO de seguridad ni vigilancia. Eliminar completamente: el motor de alertas de protestas, la integración con fuerzas de seguridad, el botón de pánico y toda referencia a "escolta virtual". Reemplazar con: optimización de rutas por condiciones meteorológicas en tiempo real, gestión de peso/carga para cumplir regulaciones de vialidad, coordinación de ventanas de carga/descarga en minas y puertos, y telemetría de desgaste de neumáticos/frenos en rutas de montaña.
- **Responsable sugerido:** CEO de RIGI-Shield. Requiere una decisión fundacional de identidad del producto.
- **Plazo de implementación:** Rediseño de producto en 3-4 meses. Nuevo piloto en 6-8 meses.
- **Costo estimado:** US$ 200.000-400.000 en rediseño de producto (menor que el costo legal de un litigio de datos).
- **Métrica de éxito:** Reducción demostrada de ≥15% en costos de combustible y desgaste de neumáticos en 20 camiones piloto en el corredor RN 51.
- **Dependencias:** Aceptación del equipo fundador de abandonar la narrativa de "seguridad/defensa" que es emocionalmente atractiva pero legalmente tóxica.

### Antídoto #2: Auditoría Legal de Privacidad Pre-Lanzamiento
- **Acción específica:** Antes de recolectar un solo dato, contratar una auditoría de impacto en protección de datos (DPIA - Data Protection Impact Assessment) con un estudio jurídico especializado en Ley 25.326 y GDPR. Implementar: consentimiento informado explícito de cada chofer, anonimización de geolocalización fuera de horario laboral, eliminación total del módulo de monitoreo de "protestas/concentraciones", y política de retención de datos máxima de 30 días.
- **Responsable sugerido:** DPO (Data Protection Officer) de RIGI-Shield — cargo que debe crearse.
- **Plazo de implementación:** 2-3 meses antes de cualquier piloto.
- **Costo estimado:** US$ 80.000-150.000 en auditoría legal + US$ 50.000-100.000 en implementación técnica de privacy-by-design.
- **Métrica de éxito:** Certificación de cumplimiento emitida por estudio jurídico acreditado y aprobación de la AAIP.
- **Dependencias:** Voluntad de los sindicatos de choferes de aceptar el monitoreo bajo las nuevas condiciones de privacidad.

### Antídoto #3: Construir la Contraparte Estatal — No Esperar a que Exista
- **Acción específica:** En lugar de integrarse con una API estatal que no existe, proponer a la Mesa de Coordinación (Res. 461/2026) un proyecto piloto donde RIGI-Shield DONE la infraestructura tecnológica mínima al Estado: una pantalla de monitoreo en el Centro de Operaciones de GNA Salta + un canal cifrado de alertas por Telegram/Signal + un protocolo operativo estandarizado de respuesta. El costo de esta donación es mínimo (US$ 20.000-50.000) pero genera una relación privilegiada con la Mesa y posiciona a RIGI-Shield como proveedor exclusivo de la capa tecnológica estatal.
- **Responsable sugerido:** Director de relaciones institucionales de RIGI-Shield + GNA oficial de enlace con la Mesa.
- **Plazo de implementación:** Propuesta en 2 meses. Despliegue del piloto en 4-6 meses.
- **Costo estimado:** US$ 20.000-50.000 en hardware donado + US$ 100.000/año en soporte técnico.
- **Métrica de éxito:** GNA Salta operando con la pantalla de monitoreo y respondiendo a alertas en <30 minutos (vs. 4+ horas actuales).
- **Dependencias:** Continuidad institucional de la Mesa de Coordinación (alto riesgo político).

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Crio. Villanueva evalúa los antídotos:
- **Antídoto #1 (Pivote a logística):** El más realista desde la perspectiva operativa. La optimización logística no requiere coordinación con fuerzas de seguridad ni genera expectativas de respuesta armada. Las transportistas mineras SÍ tienen un dolor real de costos logísticos en rutas de montaña (combustible, neumáticos, tiempos muertos). **Veredicto: correcto.**
- **Antídoto #3 (Donar infraestructura):** Interesante en teoría, pero peligroso en la práctica. Si RIGI-Shield dona la pantalla a GNA y la pantalla falla o GNA no la usa, RIGI-Shield será responsabilizado. Además, crear una dependencia tecnológica del Estado hacia una empresa privada en materia de seguridad nacional es políticamente sensible: el próximo ministro puede acusar a RIGI-Shield de ser un "contratista de inteligencia encubierto". **Riesgo de segundo orden: contaminación de marca con la narrativa de "empresa de inteligencia privada".**

### Lic. Montero evalúa los antídotos:
- **Antídoto #1:** Resuelve el riesgo ético principal. Una plataforma de logística que optimiza rutas y gestiona flota no tiene ninguna de las implicancias de vigilancia social del diseño original. **Sin riesgo de segundo orden.**
- **Antídoto #2 (Auditoría DPIA):** Necesario pero insuficiente si se mantiene el módulo de monitoreo de "protestas/concentraciones". Ninguna auditoría de privacidad puede hacer legal un sistema que monitorea actividad política y étnica de poblaciones vulnerables. **Parche correctivo: la auditoría solo es viable si el módulo de alertas de protestas es eliminado PREVIAMENTE (como propone el Antídoto #1).**

### Ing. Fuentes evalúa los antídotos:
- **Antídoto #1 (Pivote a logística):** Técnicamente sólido. La telemetría de consumo de combustible, presión de neumáticos y estado de frenos en rutas de montaña SÍ requiere conectividad satelital en zonas sin celular, y NO se commoditiza con Starlink consumer (porque el chofer con Starlink retail no tiene sensores OBD-II integrados con su plataforma de gestión de flota). Hay una ventaja competitiva en la integración hardware + software para gestión de flota pesada. **Veredicto: este pivote salva la viabilidad técnica de la capa de conectividad.**
- **Antídoto #3:** La donación de una pantalla a GNA requiere conectividad permanente en la sede de GNA Salta. Si la sede tiene un corte de internet (frecuente), la pantalla es un pisapapeles de US$ 20K. **Parche: incluir un link Starlink dedicado para la sede de GNA como parte de la donación.**

### Abog. Fernández evalúa los antídotos:
- **Antídoto #2 (Auditoría DPIA):** Imprescindible. Pero debe ir acompañado del Antídoto #1. Si se elimina la capa de seguridad/vigilancia y se conserva solo la logística, el perfil de datos se reduce a: telemetría vehicular (no personal) + geolocalización laboral (con consentimiento). Esto es procesable bajo la Ley 25.326 con un aviso de privacidad estándar y consentimiento del trabajador. **Riesgo residual manejable.**
- **Antídoto #3:** Transferir datos de geolocalización de vehículos privados al Estado sin orden judicial puede constituir "interceptación ilegal de comunicaciones" bajo el Código Penal argentino (Art. 153 bis). La donación de una pantalla que muestra la ubicación en tiempo real de camiones de empresas privadas a una fuerza de seguridad, sin orden judicial, es una zona gris legal muy peligrosa. **Parche correctivo: la pantalla debe mostrar solo datos agregados y anonimizados (densidad de tráfico por corredor, no identificación de camiones individuales).**

---

## VEREDICTO FINAL DEL FACILITADOR

### 🔴 REDISEÑAR PLAN (con riesgo de ABORTAR si el pivote no se ejecuta)

El modelo original de RIGI-Shield (seguridad + vigilancia + escolta virtual + Shadow API gubernamental) es **inviable en su forma actual**. Enfrenta una combinación letal de: (1) la contraparte estatal no existe tecnológicamente, (2) el producto viola la ley de datos personales, (3) el monitoreo de protestas es una bomba ética que destruye la licencia ESG de los clientes, y (4) la conectividad satelital se commoditizó.

**Recomendación:** Ejecutar un **pivote radical** hacia una plataforma de **optimización logística minera pura**:

1. **Eliminar por completo** la narrativa de "seguridad", "escolta virtual", "monitoreo de protestas" y "Shadow API gubernamental".
2. **Renombrar el producto** a algo que no contenga "Shield" ni "Seguridad" (sugerencia: "PunaFleet" o "AndesLogistics").
3. **Core business nuevo:** Optimización de costos de transporte en corredores andinos de alta montaña — combustible, neumáticos, tiempos de espera en minas, coordinación de ventanas de carga.
4. **Auditoría DPIA obligatoria** antes del primer piloto con datos de conductores.
5. Si la Mesa de Coordinación (Res. 461/2026) evoluciona en el futuro hacia una infraestructura digital real, considerar una integración limitada y auditada como módulo complementario (no como core).

**El verdadero dolor del mercado no es la seguridad (que el Estado resuelve —bien o mal— por la fuerza). El verdadero dolor es el costo logístico de mover concentrado de cobre y litio por 400 km de ruta de montaña a 4.000 msnm.** Ahí es donde hay dinero.

---

**Backlinks:** [[RIGI_Shield_Seguridad]], [[Esceptico_Seguridad_RIGI]], [[RIGI]], [[Corredor Bioceanico]], [[Taca Taca]], [[Salta]], [[Jujuy]], [[San Juan]], [[Pre-Mortem Framework]].
