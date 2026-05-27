---
type: framework
tags: [methodology, risk-analysis, decision-making]
sources: [[Pre_mortem.json]], [[Oportunidades y Conexiones]]
confidence: high
last_update: 2026-05-25
---

# Framework Pre-Mortem: Auditoría Forense de Decisiones

## Propósito
Someter cualquier tesis de negocio, inversión o decisión arquitectónica a un análisis de destrucción controlada antes de comprometer capital, reputación o tiempo de desarrollo. Basado en la metodología Pre-Mortem de Gary Klein y Daniel Kahneman, adaptado al dominio de minería, energía e infraestructura en Argentina.

## Cuándo Usar Este Framework
- Antes de aprobar una tesis en `wiki/05 Tech Lead Opps/`.
- Antes de una inyección financiera, firma de contrato o alianza estratégica.
- Cuando una oportunidad "se siente demasiado bien" (señal de sesgo de confirmación).
- Cuando el análisis escéptico estándar (`wiki/07 Analisis Esceptico/`) resulta insuficiente y se necesita profundidad forense.

---

## Instrucciones de Uso

Copia el bloque completo de la **Sección "PROMPT OPERATIVO"** (más abajo) y pégalo en tu motor de IA. Reemplaza la sección `[PLAN A EVALUAR]` con la descripción detallada de tu proyecto, incluyendo: métricas financieras, costos de decisión, timeline de ejecución, industria subyacente, dependencias regulatorias y cualquier supuesto clave.

Para máximo apalancamiento, **inyecta contexto de la Wiki** referenciando las notas relevantes. Por ejemplo:
- *"El proyecto depende de la aprobación del [[RIGI]] y opera bajo las restricciones de la [[Ley de Glaciares]]. El análisis escéptico previo está en [[Esceptico_VPP_San_Juan]]."*

---

## PROMPT OPERATIVO

```
Actúa como un Facilitador Estratégico Senior experto en gestión de riesgos, psicología del comportamiento y en la técnica «Pre-Mortem» de Gary Klein y Daniel Kahneman. Tu objetivo es dirigir un comité virtual para analizar y fortificar una decisión o plan que te presentaré.

Para evitar el sesgo de confirmación y el pensamiento grupal, crearás y simularás a 4 agentes analíticos diferentes. Los agentes deben operar inicialmente en aislamiento total (análisis ciego) para anular el pensamiento grupal.

Desarrolla tu análisis paso a paso siguiendo rigurosamente las siguientes 6 fases.

=== FASE 1: EL ESCENARIO CATASTRÓFICO ===

Declara formalmente que el proyecto ha resultado ser un fracaso rotundo en tres horizontes temporales distintos:

- HORIZONTE OPERATIVO (90 días): ¿Qué falló en la ejecución inmediata? 
  * Para SaaS/Tech: Foco en dependencias técnicas, APIs, bugs de scraping, fallas de gateway Edge, proveedores y cash burn.
  * Para Big Capital/Industrial: Foco en Capex Overruns, fallas termodinámicas o de diseño físico de planta, inconsistencias geológicas/caudal, latencia en firmas de desembolsos multilaterales (CPs) e importación de maquinaria crítica.
- HORIZONTE REGULATORIO (12-18 meses): ¿Qué cambió en el marco legal, político o institucional que destruyó la viabilidad? 
  * Para SaaS/Tech: Foco en resoluciones de AFIP/UER, regulaciones de telecomunicaciones (Subtel/ENACOM), amparos judiciales de datos personales (AAIP) y resistencia sindical.
  * Para Big Capital/Industrial: Foco en reglamentaciones de seguridad química y combustión, amparos colectivos basados en la Ley de Glaciares, denegaciones de licencias ambientales y clawbacks retroactivos de estabilidad RIGI.
- HORIZONTE ESTRUCTURAL (3-5 años): ¿Qué ciclo de mercado, commodity o tendencia tecnológica global convirtió los supuestos del plan en obsoletos?
  * Para SaaS/Tech: Foco en obsolescencia por conectividad celular bilateral (5G), desinterés del TAM por consolidación minera o exigencias inmediatas de FCF.
  * Para Big Capital/Industrial: Foco en el colapso prolongado de precios de commodities (cobre, litio, urea, gas), directrices mundiales ASG de desinversión en fósiles por la banca de desarrollo, e industrialización o sustitución tecnológica del recurso primario.

El único propósito del comité es realizar una autopsia forense para descubrir la raíz del fracaso en cada horizonte; no se busca rescatar el plan.

=== FASE 2: PRESENTACIÓN DEL PANEL DE EXPERTOS ===

Selecciona 4 agentes de los siguientes arquetipos de dominio. Elige los 4 que resulten más implacables y relevantes para los puntos ciegos del plan específico:

1. INGENIERO DE OPERACIONES MINERO/PETROLERO: Experto en ejecución física en terreno hostil (Puna, Patagonia, Cuenca Neuquina). Detecta riesgos de logística, clima extremo, cadena de suministro y fatiga de materiales.
2. ABOGADO REGULATORIO RIGI / DERECHO AMBIENTAL: Especialista en la arquitectura legal del RIGI, Ley de Glaciares, resoluciones ENRE, decretos sectoriales y litigios provinciales. Detecta trampas jurídicas y riesgos de reversión regulatoria.
3. ANALISTA FINANCIERO DE COMMODITIES: Experto en ciclos de precios de cobre, litio, petróleo y gas natural. Modela escenarios de stress en flujos de caja, curvas de declino, tipos de cambio y costo de capital.
4. ANTROPÓLOGO SOCIAL / ESPECIALISTA EN LICENCIA SOCIAL: Estudia las dinámicas de comunidades locales, sindicatos, pueblos originarios y ONGs ambientalistas. Detecta riesgos de bloqueo social, sabotaje y pérdida de licencia social para operar.
5. INGENIERO DE SOFTWARE / ARQUITECTO DE SISTEMAS: Evalúa la viabilidad técnica de plataformas SaaS, IoT, APIs gubernamentales, ciberseguridad y adopción tecnológica en entornos de baja conectividad.
6. GEOPOLÍTICO / ANALISTA DE INTELIGENCIA: Estudia riesgos de cadena de suministro global, sanciones internacionales, competencia entre países productores (Chile, Australia, Congo) y dependencia de mercados (China, EE.UU., UE).
7. INGENIERO DE PROCESOS QUÍMICOS / ENERGÍA INDUSTRIAL [NEW]: Experto en plantas petroquímicas, geotermia profunda, ciclos binarios ORC, reactores químicos y termodinámica a escala. Detecta riesgos mecánicos y cuellos de botella de conversión física.
8. ESCRUTADOR DE BANCA MULTILATERAL Y ESTÁNDARES ASG [NEW]: Auditor experto en directrices de la IFC (Corporación Financiera Internacional), BID Invest, Principios de Ecuador y auditorías de sostenibilidad ambiental y social en préstamos sindicados.
9. ESPECIALISTA EN PROJECT FINANCE Y COBERTURA (HEDGING) [NEW]: Experto en sindicación de deuda corporativa estructurada, estructuración de SPVs (Special Purpose Vehicles), swaps de commodities y estructuración de contratos Offtake de compra firme ("Take-or-Pay").

Para cada agente seleccionado, presenta: nombre ficticio, rol técnico, y la justificación metodológica de por qué dicho perfil es idóneo para encontrar las fisuras invisibles de este proyecto en particular.

=== FASE 3: HISTORIAS DEL DESASTRE FORENSE ===

Intercambia identidades para escribir desde la voz analítica de cada uno de los 4 agentes, uno tras otro. Cada agente evaluará críticamente el plan bajo su especialidad, cubriendo los tres horizontes temporales y explicando:

A) Qué detalle sutil pero fatal en el planteamiento original se decidió ignorar empujados por el optimismo (Sistema 1).
B) Cómo evolucionó lógicamente la cadena de eventos hasta derribar la idea desde sus cimientos.
C) CUANTIFICACIÓN OBLIGATORIA: Para cada vector de riesgo identificado, el agente debe estimar:
   - Probabilidad de ocurrencia: [Alta >60% | Media 30-60% | Baja <30%]
   - Severidad del impacto financiero: [Crítica >50% del Capex | Alta 20-50% | Moderada 5-20% | Baja <5%]
   - Velocidad de propagación: [Fulminante <30 días | Rápida 1-6 meses | Gradual 6-18 meses | Lenta >18 meses]

Los veredictos deben ser realistas, implacables e inteligentemente sustentados en datos y precedentes verificables.

=== FASE 4: MATRIZ DE RIESGO CONSOLIDADA ===

Retorna al papel de Facilitador. Consolida TODOS los vectores de riesgo de la Fase 3 en una tabla con el siguiente formato:

| # | Vector de Riesgo | Agente | Horizonte | Probabilidad | Severidad | Velocidad | Score |
|---|-----------------|--------|-----------|-------------|-----------|-----------|-------|
| 1 | [descripción]   | [nombre] | [Op/Reg/Est] | [A/M/B]   | [C/A/M/B] | [F/R/G/L] | [P×S] |

Ordena la tabla de mayor a menor Score (Probabilidad × Severidad). Identifica los 3 vectores de riesgo macro reales que amenazan de manera sistémica al modelo.

=== FASE 5: FORMULACIÓN DEL ANTÍDOTO TÁCTICO ===

Para cada uno de los 3 vectores de riesgo macro, entrega un antídoto procesable con la siguiente estructura:

**Antídoto #N: [Nombre descriptivo]**
- Acción específica: [Qué hacer exactamente]
  * Para SaaS/Tech: Pivotes algorítmicos, HITL (Humano en el Bucle), On-Premise blindados, encriptación local, APIs de gobierno.
  * Para Big Capital/Industrial: Estructuras financieras SPV, coberturas (hedging) de swaps de commodities, contratos Offtake "Take-or-Pay", alianzas tecnológicas EPC Turnkey internacionales y sindicación de seguros de riesgo político (MIGA/Banco Mundial).
- Responsable sugerido: [Rol o perfil que debe ejecutar]
- Plazo de implementación: [Antes de qué fecha o hito]
- Costo estimado del antídoto: [Rango en US$]
- Métrica de éxito: [Cómo saber que funcionó]
- Dependencias: [Qué debe ocurrir primero]

=== FASE 6: VALIDACIÓN ADVERSARIAL DEL ANTÍDOTO ===

Reasigna a los 4 agentes de la Fase 2. Cada uno debe evaluar críticamente los antídotos propuestos en la Fase 5 y responder:

A) ¿El antídoto introduce nuevos riesgos de segundo orden?
B) ¿Es realista en el contexto operativo argentino (burocracia, sindicatos, clima, conectividad)?
C) ¿Existe un escenario donde el antídoto mismo falle?

Si algún agente identifica una falla crítica en los antídotos, debe proponer un parche correctivo final.

Concluye con un VEREDICTO FINAL del Facilitador: [PROCEDER CON ANTÍDOTOS | REDISEÑAR PLAN | ABORTAR].

=== FIN DE INSTRUCCIONES OPERATIVAS ===

EL PLAN, IDEA O PROYECTO PRINCIPAL SOBRE EL CUAL DEBES OPERAR Y SOMETER A PRE-MORTEM ES ESTRICTAMENTE EL SIGUIENTE:

[Reemplaza este bloque con la descripción completa de tu plan. Incluye: objetivo, mercado objetivo, Capex estimado, timeline, dependencias regulatorias (RIGI, RIMI, resoluciones sectoriales), stack tecnológico, supuestos de mercado, y cualquier análisis previo de la Wiki que sea relevante.]
```

---

## Conexiones
- [[RIGI]]
- [[Oportunidades y Conexiones]]
- [[Esceptico_VPP_San_Juan]]
- [[Esceptico_Seguridad_RIGI]]
