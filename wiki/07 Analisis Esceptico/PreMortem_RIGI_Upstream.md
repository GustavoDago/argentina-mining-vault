---
type: analysis
tags: [risk-analysis, opportunity, rigi, compliance, regulatory, oil-gas, red-team]
sources: [[Aprobacion RIGI Upstream Res 484-2026]], [[Esceptico_Aprobacion_RIGI_Res484]], [[Vaca Muerta]], [[RIGI]]
confidence: high
last_update: 2026-05-26
---

# Pre-Mortem: Aprobación RIGI Upstream — Middleware de Simulación y Algo-Compliance

> **Tesis bajo análisis:** [[Aprobacion RIGI Upstream Res 484-2026]]
> **Análisis escéptico previo:** [[Esceptico_Aprobacion_RIGI_Res484]]
> **Framework aplicado:** [[Pre-Mortem Framework]] (6 fases)
> **Fecha de ejecución:** 2026-05-26

---

## FASE 1: ESCENARIO CATASTRÓFICO

Es el 26 de mayo de 2028. La plataforma RegTech "RIGI Upstream Optimizer" (SaaS de simulación y algo-compliance para optimización del Cociente de Rentabilidad Proyectada - CRP) ha sido clausurada de manera definitiva. Ninguna operadora petrolera de Vaca Muerta (YPF, Vista, Tecpetrol, Pampa Energía) utiliza el software para estructurar sus solicitudes de adhesión al RIGI. La startup ha consumido US$ 3.2 millones de inversión semilla y se encuentra en liquidación judicial. Las operadoras enfrentan multas fiscales multimillonarias y la descalificación retroactiva de sus planes promocionales.

### Horizonte Operativo (90 días desde el lanzamiento)

Durante el despliegue del piloto de optimización con un operador independiente en la ventana Bajo del Toro Norte, se descubrió que los modelos geológicos reales y la variabilidad de la presión de reservorio no son variables que un algoritmo financiero pueda "retrasar" o "acelerar" a voluntad sin consecuencias físicas graves. El algoritmo del software sugirió retrasar sistemáticamente la terminación y fractura (*D&C timing*) de 4 pozos horizontales para inflar artificialmente el CAPEX de la fase inicial y desplazar la producción al año 4, buscando forzar que el CRP proyectado no superara el límite regulatorio del 35%. 

Sin embargo, al mantener los pozos ya perforados sin entubar ni fracturar durante 8 meses en estado de espera, el fluido de perforación remanente interactuó de manera adversa con las arcillas sensibles de la formación Vaca Muerta, provocando el colapso de las paredes del pozo en 2 de las ramas horizontales. El costo físico de reacondicionamiento y pesca de tuberías ascendió a US$ 4.2 millones por pozo, anulando cualquier ganancia fiscal obtenida por la adhesión al RIGI y dañando de forma permanente la productividad inicial (IP) del reservorio.

### Horizonte Regulatorio (12-18 meses)

La Unidad de Evaluación RIGI (UER) y la AFIP, mediante una auditoría asistida por inteligencia artificial, detectaron un patrón idéntico de modelado financiero en 12 solicitudes de adhesión de diferentes operadoras. Todas las solicitudes presentaban curvas de declino tipo sospechosamente homogéneas y cronogramas de Capex milimétricamente ajustados para arrojar un CRP del **34.8%** (apenas por debajo del límite legal de la Resolución 484/2026).

El Ministerio de Economía emitió la **Resolución Clarificatoria UER 210/2027**, que estableció un mecanismo de "Clawback de Estabilidad Fiscal". La norma dictaminó que si la curva de producción real del yacimiento difería en más de un 15% acumulado de la curva de declino tipo presentada en la solicitud original, se consideraría "abuso de derecho y maniobra de elusión fiscal algorítmica". La AFIP descalificó retroactivamente los proyectos de Bajo del Choique-La Invernada y forzó a las VPUs a devolver las exenciones del arancel de importación del 0% de los sets de fractura, aplicando intereses punitorios del 48% anual.

### Horizonte Estructural (3-5 años)

El colapso estructural definitivo provino de un cambio en el paradigma financiero de Wall Street y de las políticas de retorno de capital de las matrices internacionales. A partir de 2027, ante la consolidación de la transición energética y las presiones por la disciplina de capital, los accionistas exigieron a las petroleras de Vaca Muerta priorizar el **Flujo de Caja Libre inmediato (FCF)** y los retornos en el Corto Plazo por sobre los beneficios fiscales diferidos de estabilidad a 30 años.

Las operadoras abandonaron la estrategia de dilatar artificialmente la puesta en marcha de pozos super-productivos para calificar bajo el RIGI. El modelo de negocio del software de algo-compliance, basado en optimizar la tasa interna de retorno a largo plazo mediante retrasos operativos, quedó obsoleto. Las compañías prefirieron pagar la tasa ordinaria del impuesto a las Ganancias (35%) y obtener retornos rápidos de caja para distribuir dividendos a sus accionistas en Nueva York, haciendo inútil el SaaS de simulación.

---

## FASE 2: PANEL DE EXPERTOS

### Agente 1: Ing. Ramiro Ledesma — Ingeniero de Reservorios y Especialista en Producción Shale
* **Rol:** 22 años de experiencia en desarrollo de reservorios no convencionales en Chevron y Tecpetrol. Ex-Director de Simulación Numérica en Añelo.
* **Justificación:** Sabe perfectamente por qué no se puede mantener un pozo horizontal en Vaca Muerta sin completar y sin fracturar durante meses sin arriesgar la integridad mecánica de la formación y del pozo. Puede evaluar de forma implacable el daño de reservorio generado por la postergación operativa de la terminación de pozos sugerida por el algoritmo.

### Agente 2: Dra. Natalia Ruiz — Ex-Jefa de Asuntos Legales de la Secretaría de Energía de la Nación
* **Rol:** Redactora de las normativas de control de producción hidrocarburífera. Especialista en derecho administrativo minero y tributación de hidrocarburos en Argentina.
* **Justificación:** Es la experta ideal para predecir la reacción regulatoria de la AFIP y la UER ante patrones de modelado financiero sospechosos. Sabe cómo operan las fiscalizaciones de elusión tributaria y puede delimitar las fronteras de responsabilidad del algo-compliance.

### Agente 3: Lic. Esteban Gómez — Analista Financiero de Petróleo y Gas de Vaca Muerta
* **Rol:** Ex-director de análisis de acciones de energía en una firma de banca privada de Wall Street. Consultor de estructuración financiera para fusiones y adquisiciones en el Upstream andino.
* **Justificación:** Evaluará la tendencia macroeconómica global y el apetito de los inversores. Puede explicar por qué el FCF inmediato se devora a los incentivos de estabilidad a largo plazo bajo regímenes de alta incertidumbre y cómo esto afecta la demanda del SaaS.

### Agente 4: Ing. Claudio Peralta — Director de Arquitectura de Sistemas de Información e Integrador RegTech
* **Rol:** 15 años diseñando software de cumplimiento regulatorio integrado para el sector financiero e industrial. Especialista en auditorías de algoritmos fiscales y seguridad en el intercambio de información corporativa.
* **Justificación:** Evaluará la solidez del motor de simulación. Entiende por qué un software masificado que optimiza planillas impositivas es detectado de inmediato por los oráculos de validación del Estado y puede cuantificar el riesgo de "firma de autor de código".

---

## FASE 3: HISTORIAS DEL DESASTRE FORENSE

### Agente 1: Ing. Ledesma (Reservorios y Mecánica de Pozos)

**A) El detalle ignorado por optimismo:**
La tesis asumió con ligereza que las fechas de "Spud-to-IP" (perforación a producción inicial) son variables abstractas que se pueden mover libremente en una celda de Excel para acomodar el ratio de rentabilidad de la UER por debajo del 35%. Ignoraron la física del shale. En la formación Vaca Muerta, las arcillas ricas en materia orgánica son propensas a la hidratación y al hinchamiento si están expuestas de manera prolongada a los fluidos base agua de la perforación.

Si dejas un pozo perforado horizontal de 3.000 metros de rama lateral esperando "la ventana de Capex óptima sugerida por el algoritmo" durante más de 120 días sin realizar la fractura hidráulica y la posterior puesta en producción, la presión capilar y la interacción geoquímica degradan la estabilidad de la roca de cobertura. Esto provoca el agrietamiento de la matriz y el derrumbe de las paredes del pozo. Reabrir e instrumentar el pozo requiere operaciones de desvío (side-track) extremadamente costosas o el abandono completo de la sección lateral.

**B) Cadena de eventos hasta el fracaso:**
1. El software de AndesLogistics sugiere demorar 180 días la fractura de 3 pozos clave de Tecpetrol para diferir ingresos del año 1 al año 4.
2. Durante el período de espera, se produce el hinchamiento de las arcillas del intervalo productor.
3. Al ingresar el set de fractura, se descubre que la tubería de producción (casing) se ha colapsado mecánicamente en la sección de la curva de transición por empuje lateral geotectónico.
4. Dos pozos se declaran inutilizables. Pérdida directa de Capex de perforación de US$ 14 millones.
5. El operador suspende el uso de la herramienta algorítmica de optimización y regresa a los cronogramas físicos tradicionales dictados por la geología, no por la AFIP.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Daño mecánico de pozo y colapso de casing por esperas de terminación prolongadas | Alta (>60%) | Alta (45% Capex pozo) | Rápida (1-6 meses) |
| Degradación de la productividad inicial (IP) por hidratación de arcillas del shale | Alta (>60%) | Moderada (20% Capex pozo) | Rápida (1-6 meses) |

---

### Agente 2: Dra. Ruiz (Regulación y Penal Tributario)

**A) El detalle ignorado por optimismo:**
Se creyó que la UER y la AFIP son entes analógicos incapaces de detectar patrones algorítmicos repetitivos. El optimismo tecnológico cegó a los fundadores, haciéndoles creer que la UER procesa solicitudes de forma aislada. La AFIP cuenta con herramientas de cruce de datos masivo. Si 15 VPUs presentan esquemas de declino técnico idénticos ajustados sistemáticamente para lograr un CRP del 34.8%, la anomalía salta de inmediato en el panel de auditoría de riesgo fiscal de la AFIP.

La Ley de Procedimiento Tributario 11.683 y el Código Penal Tributario argentino contemplan el principio de **Realidad Económica**. Si la AFIP dictamina que los retrasos en las terminaciones no obedecen a razones técnicas u operativas reales, sino a una "maniobra algorítmica destinada a defraudar el umbral de rentabilidad del RIGI", puede declarar la nulidad del certificado de adhesión por simulación ilícita.

**B) Cadena de eventos hasta el fracaso:**
1. Diez operadoras presentan sus modelos financieros optimizados por el middleware de simulación.
2. La AFIP cruza las solicitudes y detecta un patrón geométrico de Capex e ingresos correlacionado con el uso de la plataforma SaaS de RIGI-LocalToken.
3. El fisco suspende cautelarmente los beneficios fiscales de las VPUs bajo sospecha de simulación de operaciones.
4. La AFIP emite la Resolución 210/2027 exigiendo el reintegro de aranceles aduaneros sobre los sets de fractura importados.
5. Las operadoras entran en litigios administrativos prolongados que paralizan las inversiones RIGI en Vaca Muerta.
6. El SaaS de optimización es catalogado por el mercado como "un vector de riesgo fiscal letal", forzando su desconexión comercial completa.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Descalificación retroactiva del RIGI (Clawback) por abuso del principio de realidad económica | Alta (>60%) | Crítica (>50% Capex) | Gradual (6-18 meses) |
| Denuncias penales tributarias por simulación fraudulenta de cronogramas de inversión | Media (30-60%) | Crítica (>50% Capex) | Lenta (>18 meses) |

---

### Agente 3: Lic. Gómez (Mercados Financieros e Inversores Upstream)

**A) El detalle ignorado por optimismo:**
La tesis se basó en el supuesto estático de que las mineras y petroleras siempre priorizan la estabilidad fiscal a 30 años sobre la velocidad de retorno de caja. Esto ignora las presiones brutales que los fondos de inversión globales y los accionistas imponen en las asambleas de directores de empresas listadas en Wall Street. En un contexto global de transición energética, el valor residual de las reservas de hidrocarburos a 20 años es altamente incierto.

Los accionistas exigen maximizar el valor presente neto a tasas de descuento de dos dígitos. Diferir la terminación de un pozo super-productivo capaz de producir 2.000 bpd de petróleo liviano solo para calificar bajo el RIGI es una herejía financiera en el mercado actual de crudo alto. El costo de oportunidad de no vender ese petróleo hoy a US$ 75/bbl supera con creces el ahorro fiscal futuro descontado a valor presente.

**B) Cadena de eventos hasta el fracaso:**
1. El middleware sugiere retrasar la producción de 6 pozos de Vista en Vaca Muerta por 12 meses.
2. El CFO de Vista presenta el plan al directorio internacional en Nueva York.
3. Los representantes de los fondos de inversión (como BlackRock o Vanguard) vetan el plan, exigiendo producción máxima y flujo de caja libre inmediato para financiar recompras de acciones en el trimestre corriente.
4. El directorio prohíbe la alteración artificial de las curvas de producción por incentivos impositivos diferidos.
5. El mercado potencial de la plataforma se desploma a cero entre las operadoras de primera línea transadas en bolsa, limitando el TAM a pequeños operadores marginales locales sin masa crítica de Capex.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Veto de accionistas a la postergación de flujos de caja por costo de oportunidad | Alta (>60%) | Crítica (>50% Capex) | Rápida (1-6 meses) |
| Pérdida del 80% del TAM corporativo por exigencias de disciplina de capital | Alta (>60%) | Alta (40% Capex) | Rápida (1-6 meses) |

---

### Agente 4: Ing. Peralta (Arquitectura RegTech y Software)

**A) El detalle ignorado por optimismo:**
El optimismo de AndesLogistics asumió que vender un "SaaS de simulación" en la nube era el mejor modelo de distribución. Ignoraron que al subir los datos de planes de perforación confidenciales y curvas de productividad geológica de múltiples operadoras competidoras a un único servidor web SaaS centralizado de una startup de bajo presupuesto, creaban un riesgo de filtración de información y espionaje industrial inaceptable.

Los planes de inversión Upstream de Vaca Muerta son secretos comerciales de altísima criticidad. Ningún departamento de seguridad informática de YPF o Chevron autorizaría exportar sus planillas de ingeniería de reservorios y flujos financieros internos a una plataforma en la nube externa que carece de certificaciones SOC 2 Type II e ISO 27001.

**B) Cadena de eventos hasta el fracaso:**
1. RIGI Upstream Optimizer inicia operaciones comerciales como SaaS multi-inquilino en AWS.
2. Un ciberataque de secuestro de datos (Ransomware) compromete la base de datos de la startup, filtrando los planes de perforación no publicados de 3 competidores de Vaca Muerta.
3. Los precios de las acciones de los operadores afectados sufren fluctuaciones severas por divulgación de información confidencial.
4. Las operadoras inician demandas multimillonarias de responsabilidad contra la startup.
5. El mercado RegTech de Upstream se cierra definitivamente para cualquier software externo en la nube.

**C) Cuantificación:**

| Vector de Riesgo | Probabilidad | Severidad | Velocidad |
|---|---|---|---|
| Filtración de planes de inversión confidenciales Upstream por ciberseguridad deficiente | Media (30-60%) | Crítica (>50% Capex) | Fulminante (<30 días) |
| Rechazo de integración de software SaaS por departamentos de IT de operadoras | Alta (>60%) | Alta (30% Capex) | Fulminante (<30 días) |

---

## FASE 4: MATRIZ DE RIESGO CONSOLIDADA

| # | Vector de Riesgo | Agente | Horizonte | Prob. | Severidad | Velocidad | Score |
|---|---|---|---|---|---|---|---|
| 1 | Veto de accionistas a postergar producción por costo de oportunidad | Gómez | Estructural | Alta | Crítica | Rápida | **A×C** |
| 2 | Descalificación retroactiva RIGI (Clawback) por AFIP | Ruiz | Regulatorio | Alta | Crítica | Gradual | **A×C** |
| 3 | Daño de pozo y colapso de casing por esperas de terminación | Ledesma | Operativo | Alta | Alta | Rápida | **A×A** |
| 4 | Rechazo de integración SaaS por seguridad de datos corporativos (IT) | Peralta | Operativo | Alta | Alta | Fulminante | **A×A** |
| 5 | Pérdida del 80% del TAM por exigencia de FCF inmediato | Gómez | Estructural | Alta | Alta | Rápida | **A×A** |
| 6 | Filtración de planes confidenciales Upstream por ciberataques | Peralta | Operativo | Media | Crítica | Fulminante | **M×C** |
| 7 | Denuncias penales tributarias por simulación de cronogramas | Ruiz | Regulatorio | Media | Crítica | Lenta | **M×C** |
| 8 | Pérdida de productividad inicial (IP) por hinchamiento de arcillas | Ledesma | Operativo | Alta | Moderada | Rápida | **A×M** |

### 🔴 Top 3 Vectores de Riesgo Sistémico

1. **VETO FINANCIERO E INDUSTRIAL AL RETRASO OPERATIVO (Vectores #1, #5):** Las corporaciones de petróleo y gas cotizadas en mercados públicos internacionales priorizan el Flujo de Caja Libre inmediato. Alterar artificialmente la geología del reservorio y retrasar la extracción de petróleo de alta ley a US$ 75/bbl solo para encajar en un umbral fiscal del RIGI es una destrucción de valor financiero directo intolerable para los accionistas globales.

2. **BARRERA FISCAL DE LA REALIDAD ECONÓMICA Y CLAWBACK (Vectores #2, #7):** La AFIP posee un mandato claro para auditar maniobras de elusión algorítmica. Un patrón repetitivo en múltiples operadoras utilizando el mismo software RegTech para forzar un CRP del 34.8% gatilla auditorías masivas inmediatas bajo el principio de realidad económica, descalificando los proyectos y revocando retroactivamente exenciones impositivas con cargos punitorios severos.

3. **DAÑO FÍSICO GEOQUÍMICO DEL RESERVORIO DE SHALE (Vector #3, #8):** Vaca Muerta exige una continuidad mecánica rigurosa. Demorar la finalización hidráulica de ramas horizontales expone al pozo a la inestabilidad de las arcillas hidratadas y el empuje tectónico lateral, resultando en colapsos estructurales de tuberías (casings) con costos de remediación destructivos que superan cualquier exención fiscal RIGI.

---

## FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO

### Antídoto #1: Pivot a "Software de Simulación y Análisis de Estabilidad Fiscal de Reservas" (Sin Alteración Operativa)

* **Acción específica:** Rediseñar la plataforma para abandonar completamente cualquier sugerencia o algoritmo orientado a retrasar operativamente la producción o postergar pozos (*D&C timing*). Pivotar el software hacia un **simulador actuarial y tributario estricto de escenarios fiscales alternativos** que corre sobre la base del plan de perforación *geológicamente óptimo* e inalterado de la operadora. La herramienta servirá exclusivamente para calcular el LCOE, la rentabilidad esperada y el impacto de los incentivos RIGI vs. Ley de Inversiones Mineras ordinaria en tramos de 10, 20 y 30 años bajo volatilidad de precios internacionales. El software no altera la geología; asesora al departamento impositivo sobre la conveniencia financiera de adhesión bajo escenarios estáticos reales de perforación.
* **Responsable sugerido:** Director de Finanzas y Modelado Tributario + Lead de Ingeniería de Petróleo.
* **Plazo de implementación:** Inmediata.
* **Costo estimado:** US$ 120.000 en el re-desarrollo del motor algorítmico impositivo y eliminación de automatismos de retraso de pozos.
* **Métrica de éxito:** Aceptación e integración de la plataforma por parte de los CFOs de las operadoras sin generar observaciones técnicas por parte de los ingenieros de reservorio.
* **Dependencias:** Consistencia matemática del motor fiscal con las resoluciones complementarias vigentes de AFIP y UER.

### Antídoto #2: Modelo de Despliegue On-Premise e Infraestructura Criptográfica "Zero-Knowledge Proofs" (ZKP)

* **Acción específica:** Eliminar la arquitectura SaaS en la nube multi-inquilino de la startup. Desplegar el software como un **módulo informático local cerrado (On-Premise) instalable directamente dentro de los servidores seguros blindados (DMZ/Intranet) de cada operadora**. Para auditorías externas de validación sin revelar secretos geológicos comerciales confidenciales, el sistema debe implementar criptografía basada en **Pruebas de Conocimiento Cero (ZKP)**. La operadora puede generar un "Certificado Criptográfico de Consistencia Financiera RIGI" firmado por la plataforma que demuestra matemáticamente ante la UER que cumple con los ratios de rentabilidad exigidos por la Res. 484/2026, sin exponer ni transferir una sola celda del plan confidencial de coordenadas de pozos ni las curvas de declino tipo patentadas al fisco ni a terceros.
* **Responsable sugerido:** Arquitecto de Ciberseguridad y Criptógrafo.
* **Plazo de implementación:** Durante la fase de diseño de la arquitectura del software corporativo.
* **Costo estimado:** US$ 180.000 en el desarrollo del módulo criptográfico ZKP y auditorías de seguridad externas certificadas SOC 2.
* **Métrica de éxito:** Aprobación de la arquitectura de seguridad y datos por parte de los directores de IT (CISO) de operadoras multinacionales como YPF y Chevron.
* **Dependencias:** Capacidad de procesamiento computacional local compatible con las herramientas existentes en las operadoras.

### Antídoto #3: Protocolo de Validación Técnica Homologada por Tercero Independiente (Oráculo de Ingeniería)

* **Acción específica:** Para neutralizar de raíz la descalificación retroactiva de la AFIP por abuso del principio de realidad económica, la plataforma debe integrar obligatoriamente un **protocolo de validación geológica forense por parte de una certificadora geológica internacional independiente homologada (como Ryder Scott o DeGolyer and MacNaughton)**. El middleware de simulación obligará a que cualquier variación de la curva de declino tipo o retraso de pozos sugerida sea justificada y validada por la certificadora externa basándose en criterios puramente mecánicos o de saturación del sistema de compresión y transporte del yacimiento, emitiendo un "Dictamen Geológico Forense de Respaldo". Esto blinda a la operadora y al software ante fiscalizaciones impositivas, demostrando que los cronogramas presentados obedecen a realidades físicas y de capacidad de transporte, eliminando cualquier presunción de evasión fiscal algorítmica.
* **Responsable sugerido:** CCO (Chief Compliance Officer) + Ingeniero de Enlace de Certificadora Externa.
* **Plazo de implementación:** Fase preliminar al envío de la primera carpeta de adhesión a la UER.
* **Costo estimado:** Rango de US$ 250.000 (honorarios de certificación independiente por campaña de inversión).
* **Métrica de éxito:** Cero impugnaciones por parte de la Secretaría de Energía y la AFIP en las solicitudes de adhesión respaldadas por el protocolo.
* **Dependencias:** Acreditación formal de las consultoras de ingeniería ante la Secretaría de Energía de la Nación.

---

## FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO

### Ing. Ledesma evalúa los antídotos:
* **Antídoto #1 (Sin Alteración Operativa):** Excelente. Al eliminar la idea absurda de retrasar las terminaciones de los pozos por razones financieras, se anula en un 100% el riesgo de daño geoquímico al reservorio y colapso de casings. Los ingenieros de producción cooperarán activamente con el sistema impositivo si no interfiere con la física del pozo. **Veredicto: operativamente viable.**
* **Antídoto #3 (Validación por Tercero):** Muy valioso. Si una operadora tiene que diferir la terminación de pozos por restricciones mecánicas reales (como la falta de capacidad en la planta de tratamiento de crudo o gasoducto local), la validación de Ryder Scott lo certifica formalmente. Esto convierte la limitación física en un argumento fiscal inexpugnable.

### Dra. Ruiz evalúa los antídotos:
* **Antídoto #1 (Sin Alteración) y Antídoto #3 (Tercero):** Estos antídotos eliminan el riesgo de descalificación fiscal (Clawback). Si los datos de declino tipo y cronograma corresponden a la física real del pozo o están certificados por una consultora del prestigio de DeGolyer and MacNaughton, la AFIP carece de elementos técnicos para invocar el abuso del principio de realidad económica. Ya no hay "simulación" algorítmica; hay modelado técnico inexpugnable. **Veredicto: regulatoriamente blindado.**

### Lic. Gómez evalúa los antídotos:
* **Antídoto #1 (Sin Alteración):** Resuelve el conflicto fiduciario con los accionistas de Wall Street. Al no retrasar artificialmente la producción inicial, no hay costo de oportunidad en el flujo de caja corriente. Vista o YPF pueden seguir operando a máxima productividad física para maximizar retornos, y usar el simulador puramente como un optimizador de su estructura fiscal corporativa profunda. **Veredicto: financieramente viable.**

### Ing. Peralta evalúa los antídotos:
* **Antídoto #2 (On-Premise y ZKP):** Cumple con las exigencias informáticas más extremas. Al correr "On-Premise" dentro del firewall del operador, IT firmará la aprobación tecnológica en 48 horas. Criptografía ZKP permite certificar ante el fisco la consistencia impositiva sin revelar el secreto comercial de la geología profunda del yacimiento, reduciendo el riesgo de filtraciones y espionaje industrial a cero. **Veredicto: ciber-seguro y vendible.**

---

## VEREDICTO FINAL DEL FACILITADOR

### 🔴 REDISEÑAR PLAN

El plan original de RIGI Upstream Optimizer (SaaS en la nube de "algo-compliance" para forzar artificialmente el cumplimiento del ratio del 35% retrasando operativamente la completación de pozos) es **inviable físicamente por riesgo geoquímico de daño de reservorio, legalmente nulo ante la AFIP por simulación impositiva, y comercialmente invendible ante los boards de Wall Street por destrucción del flujo de caja.**

**Recomendación:** Rediseñar la empresa bajo la tesis de **"RIGI Fiscal Ledger"**:
1. **Fase Comercial y de Software (0-6 meses):** Pivotar el modelo de negocio al **Antídoto #1 (Simulador Actuarial Tributario Estático sin interferencia operativa)** y re-arquitecturar a un despliegue **On-Premise con criptografía ZKP (Antídoto #2)** para cumplir con los estándares de ciberseguridad corporativos.
2. **Homologación Técnica (0-6 meses):** Integrar de manera mandatoria el **Protocolo de Validación Técnica Homologada por Certificadora Internacional Independiente (Antídoto #3)** para anular cualquier presunción de elusión fiscal algorítmica ante la AFIP.

---

**Backlinks:** [[Aprobacion RIGI Upstream Res 484-2026]], [[Esceptico_Aprobacion_RIGI_Res484]], [[Vaca Muerta]], [[RIGI]], [[Pre-Mortem Framework]].
