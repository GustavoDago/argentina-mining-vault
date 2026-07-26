---
type: analysis
tags: [risk-analysis, opportunity, energy, oil-gas, methodology]
sources: [[ShaleFlow_Anelo_Supply]], [[Vaca Muerta]], [[RIGI]], [[Proyecto LLL Oil]], [[Pre-Mortem Framework]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: ShaleFlow Añelo - Micro-Hubs de Abastecimiento Predictivo

> **Tesis bajo análisis:** [[ShaleFlow_Anelo_Supply]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2027. El proyecto ShaleFlow Añelo ha fracasado. El micro-hub de manufactura aditiva en Añelo cerró operaciones. Los sensores predictivos fueron desinstalados de los trailers de fractura. Se perdieron 18 meses de desarrollo y un capital semilla estimado en US$ 3-5 millones.

### Horizonte Operativo (90 días desde el lanzamiento)
El hub físico de manufactura no logró fabricar una sola pieza que pasara la certificación de calidad metalúrgica exigida por las operadoras. Los primeros lotes de piezas impresas en metal (SLS) presentaron porosidad interna y micro-fisuras detectadas en los ensayos no destructivos (END). Los frack crews de YPF rechazaron las piezas piloto tras la primera inspección de calidad, citando el protocolo interno de "cero tolerancia a repuestos no-OEM" en equipos de alta presión (>10.000 PSI).

### Horizonte Regulatorio (12-18 meses)
El Decreto 105/2026 fue modificado por una resolución complementaria que estableció que los repuestos fabricados localmente bajo el RIGI deben contar con certificación de la OEM original o de un laboratorio metalúrgico acreditado internacionalmente (ej. DNV, Lloyd's, Bureau Veritas). El costo de esta certificación por pieza resultó ser de US$ 8.000-15.000, destruyendo la ventaja de costo de la manufactura local. Simultáneamente, SLB y Halliburton emitieron directivas corporativas globales prohibiendo el uso de piezas fabricadas por terceros no licenciados en sus bombas de fractura, bajo amenaza de anulación de garantía y seguro.

### Horizonte Estructural (3-5 años)
La curva de aprendizaje de Vaca Muerta redujo drásticamente las fallas mecánicas. Las nuevas generaciones de bombas eléctricas de fractura (e-frac) de ProPetro y Liberty Oilfield reemplazaron a las bombas diésel convencionales, reduciendo un 70% la tasa de roturas por fatiga mecánica. El mercado de repuestos se contrajo al mismo ritmo que la transición a e-frac se aceleró. Además, los grandes OEM (SLB, Halliburton) desplegaron sus propios almacenes de repuestos regionales en Neuquén, eliminando el cuello de botella logístico que justificaba la existencia de ShaleFlow.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Raúl Montes — Ingeniero de Operaciones Petrolero
**Rol:** 22 años de experiencia en completación de pozos y fractura hidráulica en Cuenca Neuquina. Ex-supervisor de mantenimiento de flota de fractura en SLB Argentina.
**Justificación:** Conoce de primera mano el régimen de certificación de piezas críticas en equipos de alta presión. Es el perfil ideal para evaluar si la manufactura aditiva puede realmente cumplir con las tolerancias metalúrgicas que exige el fracking industrial.

### Agente 2: Dra. Luciana Vega — Abogada Especialista en Propiedad Intelectual y Contratos OEM
**Rol:** Socia de estudio jurídico especializado en licenciamiento de tecnología industrial y propiedad intelectual en el sector energético.
**Justificación:** El modelo ShaleFlow depende de acceder a planos CAD/CAM de piezas cuya propiedad intelectual pertenece a las OEM. Sin un framework legal sólido, el proyecto puede enfrentar litigios por infracción de patentes antes de vender la primera pieza.

### Agente 3: Lic. Martín Quiroga — Analista Financiero de Commodities y Upstream
**Rol:** Analista senior en banca de inversión con cobertura del sector upstream argentino. Modeló los flujos de caja de las solicitudes RIGI de YPF, Vista y Pluspetrol.
**Justificación:** Debe validar si el modelo de ingresos de ShaleFlow (cobro por pieza fabricada) genera un flujo de caja suficiente para amortizar la inversión en maquinaria SLS/CNC de alta gama (US$ 500K-2M por máquina) dentro de un horizonte razonable.

### Agente 4: Ing. Sofía Pellegrini — Ingeniera de Materiales y Manufactura Aditiva
**Rol:** PhD en metalurgia de aleaciones de alta resistencia fabricadas por SLS. Investigadora de Y-TEC en el programa de desarrollo de proveedores locales.
**Justificación:** Es la persona técnicamente más calificada para evaluar si la impresión 3D de metal puede alcanzar las propiedades mecánicas (dureza Rockwell, resistencia a la fatiga, tolerancia a H₂S) requeridas para componentes de fractura hidráulica.

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Raúl Montes (Operaciones)

**A) El detalle ignorado por optimismo:**
Se asumió que la manufactura aditiva puede producir piezas "drop-in" para bombas de fractura. Esto ignora una realidad operativa fundamental: cada bomba Quintiplex de SLB tiene entre 12 y 18 componentes críticos de desgaste (liners, plungers, packing, válvulas de asiento y descarga) que operan bajo presiones de 10.000-15.000 PSI con temperaturas de hasta 120°C y exposición a fluidos abrasivos con proppant cerámico. La tolerancia dimensional exigida es de ±0.001" y la dureza superficial mínima es 58 HRC en acero 4140 tratado. La impresión SLS de metal rara vez alcanza estas tolerancias sin un costoso post-procesamiento (mecanizado CNC de precisión + tratamiento térmico + shot peening + recubrimiento Stellite).

**B) Cadena de eventos hasta el fracaso:**
1. Se instalan sensores predictivos en 5 trailers piloto de YPF.
2. El algoritmo Edge AI detecta correctamente una anomalía en un plunger y genera la orden de fabricación.
3. El hub de Añelo imprime la pieza en SLS de Inconel 625 en 14 horas.
4. La pieza requiere 8 horas adicionales de mecanizado CNC de precisión y tratamiento térmico.
5. Total lead time: 24-36 horas (vs. las "horas" prometidas).
6. La pieza fabricada pasa la inspección visual pero falla en el ensayo de fatiga cíclica a 100.000 ciclos (la OEM exige 500.000 ciclos mínimos).
7. El supervisor de SLB en campo rechaza la pieza y registra una no-conformidad que escala a la oficina regional.
8. SLB emite un boletín técnico global prohibiendo piezas no-OEM en sus equipos.
9. Las demás operadoras copian la directiva por liability chain.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Rechazo de piezas por no cumplir tolerancias metalúrgicas OEM | Alta (>60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Tiempo real de fabricación 10x mayor al prometido (24-36h vs "horas") | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |
| Prohibición corporativa global de piezas no-OEM por cadena de responsabilidad | Media (30-60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

### Agente 2: Dra. Luciana Vega (Propiedad Intelectual)

**A) El detalle ignorado por optimismo:**
Se planteó un "almacén virtual de planos CAD/CAM certificados" sin resolver la pregunta fundamental: ¿quién es el dueño de esos planos? Los diseños de componentes de bombas de fractura son propiedad intelectual estricta de SLB (Schlumberger), Halliburton, NOV (National Oilwell Varco) y Weir SPM. Estos diseños están protegidos por patentes activas, secretos industriales y acuerdos de confidencialidad con los fabricantes de acero. Crear un "almacén virtual" de estos planos sin licencia constituye infracción de propiedad intelectual bajo la Ley 24.481 (Patentes) y la Ley 24.766 (Confidencialidad).

**B) Cadena de eventos hasta el fracaso:**
1. ShaleFlow ingeniería inversa los diseños de piezas a partir de componentes usados (escaneo 3D).
2. Las primeras 50 piezas se fabrican y comercializan localmente.
3. NOV (National Oilwell Varco) detecta la actividad a través de su programa global anti-piratería de repuestos.
4. NOV inicia una demanda civil por US$ 5-10M ante la justicia federal de Neuquén y una denuncia penal por violación de secretos industriales.
5. Simultáneamente, notifica a YPF que el uso de piezas no licenciadas en sus equipos anula la garantía de los componentes premium.
6. YPF, para evitar el riesgo de responsabilidad cruzada, cancela el programa piloto y devuelve las piezas.
7. ShaleFlow queda atrapada entre un litigio de PI millonario y la pérdida total de su base de clientes.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Litigio por infracción de patentes/secretos industriales de OEMs | Alta (>60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Anulación de garantías OEM en equipos que usen piezas no licenciadas | Alta (>60%) | Alta (20-50% Capex) | Rápida (1-6 meses) |
| Imposibilidad de obtener licencia OEM a costo razonable (regalías prohibitivas) | Media (30-60%) | Alta (20-50% Capex) | Gradual (6-18 meses) |

---

### Agente 3: Lic. Martín Quiroga (Financiero)

**A) El detalle ignorado por optimismo:**
El modelo financiero asume un mercado de repuestos grande y estable. Pero el costo stand-by de US$ 80.000/día que justifica el price premium de ShaleFlow es un dato de 2024-2025, cuando la cuenca tenía déficit crónico de crews de fractura. Con la aprobación del RIGI y la inyección de US$ 47.000M (YPF + Pluspetrol + Chevron solo en upstream), las OEM están expandiendo agresivamente su infraestructura de soporte en Argentina. SLB inauguró un centro de reparación en Neuquén capital en Q1 2026; Halliburton amplió su almacén de Añelo. El cuello de botella de repuestos se está cerrando orgánicamente por la misma ola de inversión que ShaleFlow pretende explotar.

**B) Cadena de eventos hasta el fracaso:**
1. ShaleFlow asume un TAM (Total Addressable Market) de US$ 50-100M anuales en repuestos de desgaste.
2. En realidad, SLB y Halliburton cubren el 80% del mercado con stock propio desplegado en Neuquén.
3. El mercado residual accesible para un third-party manufacturer es de US$ 5-10M anuales.
4. Con un Capex inicial de US$ 3-5M en maquinaria SLS/CNC, el breakeven requiere fabricar >2.000 piezas/año a márgenes de 40%.
5. Sin acceso a planos OEM y con rechazo de las operadoras, el volumen real de pedidos es de 50-100 piezas/año.
6. Cash burn rate de US$ 200K/mes (alquiler del hub, salarios de operadores CNC, amortización de máquinas).
7. El proyecto quema el capital semilla en 15-18 meses sin alcanzar breakeven.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| TAM sobreestimado (mercado real 10x menor al proyectado) | Media (30-60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| OEMs despliegan almacenes propios en Neuquén, eliminando el cuello de botella | Alta (>60%) | Alta (20-50% Capex) | Gradual (6-18 meses) |
| Cash burn insostenible por volumen insuficiente de pedidos | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |

---

### Agente 4: Ing. Sofía Pellegrini (Materiales / Manufactura Aditiva)

**A) El detalle ignorado por optimismo:**
Se propone tecnología SLS (Selective Laser Sintering) como si fuera una impresora genérica. La realidad es que las piezas de desgaste de bombas de fractura requieren aleaciones muy específicas: acero 4140 pre-endurecido para cuerpos de válvula, Inconel 718 para asientos de válvula expuestos a H₂S, y acero inoxidable duplex para liners. Cada aleación requiere parámetros de impresión completamente diferentes (potencia de láser, velocidad de escaneo, temperatura de cama, estrategia de soporte). Dominar la metalurgia de una sola aleación en SLS requiere 6-12 meses de calibración y pruebas destructivas. ShaleFlow necesitaría dominar al menos 4-5 aleaciones distintas para cubrir la gama de piezas, lo que implica 2-3 años de I+D solo en calibración.

**B) Cadena de eventos hasta el fracaso:**
1. Se adquiere una máquina SLS industrial (ej. EOS M290, US$ 800K-1.2M).
2. Se comienza la calibración con polvo de acero 4140 atomizado por gas.
3. Las primeras 200 piezas de prueba muestran variabilidad en densidad (95-98% vs. el 99.5% exigido por API).
4. Se descubre que la porosidad residual actúa como concentrador de tensiones en fatiga cíclica.
5. Se requiere tratamiento HIP (Hot Isostatic Pressing) post-impresión, pero no existe equipo HIP en toda la Patagonia argentina.
6. Enviar las piezas a Buenos Aires para HIP agrega 15 días y US$ 500-1.000 por pieza, destruyendo la propuesta de valor de "repuestos en horas".
7. La alternativa (invertir US$ 2-4M en un equipo HIP propio) quintuplica el Capex inicial.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Densidad insuficiente en piezas SLS sin tratamiento HIP | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Ausencia de equipo HIP en Patagonia, destruye la propuesta de valor de velocidad | Alta (>60%) | Alta (20-50% Capex) | Fulminante (<30 días) |
| 2-3 años de I+D necesarios para calibrar múltiples aleaciones | Media (30-60%) | Alta (20-50% Capex) | Lenta (>18 meses) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Rechazo de piezas por no cumplir tolerancias metalúrgicas OEM | Montes | Operativo | Alta | Crítica | Fulminante | **A×C** |
| 2 | Litigio por infracción de patentes/secretos industriales OEMs | Vega | Regulatorio | Alta | Crítica | Gradual | **A×C** |
| 3 | Cash burn insostenible por volumen insuficiente de pedidos | Quiroga | Operativo | Alta | Crítica | Rápida | **A×C** |
| 4 | Densidad insuficiente en piezas SLS sin HIP | Pellegrini | Operativo | Alta | Crítica | Rápida | **A×C** |
| 5 | Prohibición corporativa global de piezas no-OEM | Montes | Regulatorio | Media | Crítica | Rápida | **M×C** |
| 6 | OEMs despliegan almacenes propios en Neuquén | Quiroga | Estructural | Alta | Alta | Gradual | **A×A** |
| 7 | Ausencia de equipo HIP en Patagonia | Pellegrini | Operativo | Alta | Alta | Fulminante | **A×A** |
| 8 | TAM sobreestimado (mercado real 10x menor) | Quiroga | Estructural | Media | Crítica | Gradual | **M×C** |
| 9 | Anulación de garantías OEM en equipos | Vega | Regulatorio | Alta | Alta | Rápida | **A×A** |
| 10 | Imposibilidad de obtener licencia OEM a costo razonable | Vega | Regulatorio | Media | Alta | Gradual | **M×A** |
| 11 | Tiempo real de fabricación 10x mayor al prometido | Montes | Operativo | Alta | Alta | Rápida | **A×A** |
| 12 | I+D de 2-3 años para calibrar múltiples aleaciones | Pellegrini | Estructural | Media | Alta | Lenta | **M×A** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **BARRERA DE CERTIFICACIÓN OEM (Vectores #1, #5, #9):** El ecosistema de fractura hidráulica opera bajo un régimen de responsabilidad cruzada (liability chain) donde cada componente debe ser trazable hasta el fabricante original. Un componente no certificado que falle puede causar un blow-out que destruya un pozo de US$ 15M y genere responsabilidades civiles y ambientales catastróficas. Este régimen de cero tolerancia es sistémico e inamovible.

2. **VIABILIDAD METALÚRGICA DE LA MANUFACTURA ADITIVA (Vectores #4, #7, #12):** La brecha entre la promesa teórica del SLS y la realidad industrial en componentes de alta presión es enorme. Sin HIP, sin calibración de aleaciones y sin laboratorio de ensayos de fatiga in-situ, el hub de Añelo es una fábrica de prototipos, no de repuestos industriales.

3. **MERCADO EN CONTRACCIÓN ESTRUCTURAL (Vectores #3, #6, #8):** La misma ola RIGI que genera la oportunidad está financiando la eliminación del cuello de botella que ShaleFlow pretende explotar. Las OEM están resolviendo internamente el problema de logística de repuestos, y la transición a e-frac reduce la tasa de fallas mecánicas. ShaleFlow estaría ingresando a un mercado que se está cerrando.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Pivote a Licenciatario OEM Oficial
- **Acción específica:** Abandonar la ingeniería inversa. Negociar directamente con NOV (National Oilwell Varco) o Weir SPM un acuerdo de licencia de fabricación local de piezas de desgaste seleccionadas (ej. liners y packing de consumo masivo, no componentes críticos de válvulas). NOV tiene precedentes de licenciamiento regional en Brasil (Usiminas).
- **Responsable sugerido:** CEO/fundador de ShaleFlow + abogado de PI especializado en oil & gas.
- **Plazo de implementación:** Antes de invertir en maquinaria. Negociación debe cerrarse en 6-9 meses previos al lanzamiento.
- **Costo estimado:** US$ 150.000-300.000 en honorarios legales y viajes de negociación. Regalías de 8-15% por pieza fabricada.
- **Métrica de éxito:** Term sheet firmado con al menos 1 OEM para fabricar ≥10 SKUs de piezas de desgaste.
- **Dependencias:** Voluntad de la OEM de licenciar. Requiere demostrar capacidad metalúrgica certificable.

### Antídoto #2: Alianza Técnica con Y-TEC para Certificación Metalúrgica
- **Acción específica:** En lugar de invertir en I+D propio, formalizar un convenio con Y-TEC (brazo tecnológico de YPF) para utilizar sus laboratorios de ensayos metalúrgicos y de fatiga cíclica. Y-TEC tiene el mandato estatal de desarrollar proveedores locales y acceso al único equipo HIP operativo en Argentina (CNEA Constituyentes). Esto resuelve simultáneamente el problema de certificación y el acceso a HIP.
- **Responsable sugerido:** Director técnico de ShaleFlow + Gerente de Vinculación Tecnológica de Y-TEC.
- **Plazo de implementación:** Convenio marco en 3 meses. Primeras piezas certificadas en 9-12 meses.
- **Costo estimado:** US$ 200.000-400.000 anuales en contraparte de I+D compartido.
- **Métrica de éxito:** Primera pieza SLS con certificación metalúrgica Y-TEC que pase ensayo de fatiga de 500.000 ciclos.
- **Dependencias:** Aprobación interna de Y-TEC. Disponibilidad del equipo HIP de CNEA.

### Antídoto #3: Rediseño del Modelo de Negocio — De Fabricante a Integrador Predictivo
- **Acción específica:** Abandonar la capa de manufactura aditiva (alto Capex, alto riesgo). Pivotar al modelo puro de software: la capa Edge AI predictiva como un SaaS de mantenimiento predictivo que se integra con los almacenes existentes de las OEM. En lugar de fabricar la pieza, ShaleFlow predice qué pieza va a fallar y genera automáticamente la orden de compra al almacén regional de SLB/Halliburton, cobrando una suscripción mensual por trailer monitorizado.
- **Responsable sugerido:** CTO de ShaleFlow.
- **Plazo de implementación:** Prototipo en 4 meses. Piloto en 8 meses.
- **Costo estimado:** US$ 500.000-800.000 (vs. US$ 3-5M del modelo original con manufactura).
- **Métrica de éxito:** Reducción demostrada de ≥30% en horas de stand-by por falla de repuestos en 10 trailers piloto.
- **Dependencias:** Acceso a datos de vibración y presión de los trailers (requiere partnership con la operadora). APIs de inventario de las OEM.

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Montes evalúa los antídotos:
- **Antídoto #1 (Licenciatario OEM):** Viable técnicamente, pero las OEM rara vez licencian componentes de alta presión a third-parties en mercados pequeños. El precedente de Brasil (mercado 5x Argentina) no es directamente extrapolable. **Riesgo de segundo orden:** La negociación puede tomar 18-24 meses (no 6-9), durante los cuales ShaleFlow quema capital sin ingresos.
- **Antídoto #2 (Y-TEC):** Sólido, pero Y-TEC tiene una cultura burocrática de tiempos académicos. Conseguir prioridad en el equipo HIP de CNEA es un cuello de botella real: CNEA tiene 6-8 meses de cola de espera para ensayos. **Riesgo de segundo orden:** El ritmo de I+D de Y-TEC es incompatible con las urgencias operativas de la cuenca.
- **Antídoto #3 (Pivote a SaaS):** El más realista. Pero requiere que las operadoras abran acceso a los datos de vibración de sus trailers, que hoy consideran información competitiva sensible. YPF podría aceptarlo; las operadoras privadas (Vista, Tecpetrol) serán mucho más resistentes.

### Dra. Vega evalúa los antídotos:
- **Antídoto #1:** Resuelve el problema de PI, pero el acuerdo de licencia debe incluir cláusulas de exclusividad regional (Argentina/Cono Sur) para que ShaleFlow tenga un moat. Sin exclusividad, la OEM puede licenciar a un competidor al día siguiente. **Sin parche crítico necesario.**
- **Antídoto #3:** El modelo SaaS puro elimina el riesgo de PI sobre piezas, pero introduce un nuevo riesgo: los datos de vibración y presión recolectados de los trailers podrían ser considerados secreto industrial de la operadora. Se necesita un acuerdo de procesamiento de datos (DPA) robusto.

### Lic. Quiroga evalúa los antídotos:
- **Antídoto #3:** Financieramente es el más atractivo. Capex de US$ 500-800K vs. US$ 3-5M. Breakeven alcanzable con 50-80 trailers monitorizados a US$ 2.000/mes. El TAM de monitoreo predictivo en Vaca Muerta es de US$ 15-25M/año (1.700 etapas mensuales × ~200 trailers activos). **Veredicto: el único modelo con unit economics viables.**
- **Antídoto #1:** Los márgenes con regalías del 8-15% y costos de certificación de US$ 8-15K/pieza dejan un margen bruto de solo 15-20%, insuficiente para cubrir overheads.

### Ing. Pellegrini evalúa los antídotos:
- **Antídoto #2:** Técnicamente correcto, pero incompleto. Incluso con Y-TEC y HIP, la repetibilidad de piezas SLS en producción (no en laboratorio) requiere un sistema de calidad ISO 13485/AS9100 que cuesta US$ 300-500K implementar y tarda 12-18 meses en acreditarse. **Parche correctivo:** Incluir el costo y timeline de certificación ISO en el plan financiero.
- **Antídoto #3:** El pivote a SaaS es inteligente porque monetiza el conocimiento de falla (que es el verdadero IP de ShaleFlow) sin tocar la metalurgia. **Sin riesgo de segundo orden significativo.**

---

## VEREDICTO FINAL DEL FACILITADOR

### 🟡 REDISEÑAR PLAN

El modelo original de ShaleFlow (manufactura aditiva de repuestos + sensores predictivos) enfrenta 3 barreras sistémicas simultáneas que no pueden resolverse con ajustes incrementales: certificación OEM, viabilidad metalúrgica del SLS en alta presión, y contracción del mercado de repuestos por despliegue de almacenes OEM.

**Recomendación:** Adoptar el **Antídoto #3** como modelo base: pivotar a un SaaS puro de mantenimiento predictivo (Edge AI) sin manufactura propia. Si en el futuro Y-TEC valida la metalurgia SLS para piezas de baja criticidad (packing, juntas, adaptadores de baja presión), considerar reincorporar la manufactura como módulo complementario (no como core business).

**El verdadero IP de ShaleFlow no es la impresora 3D; es el algoritmo que sabe qué pieza va a fallar antes de que falle.** Monetizar la predicción, no la fabricación.

---

**Backlinks:** [[ShaleFlow_Anelo_Supply]], [[Vaca Muerta]], [[RIGI]], [[Proyecto LLL Oil]], [[Pre-Mortem Framework]].
