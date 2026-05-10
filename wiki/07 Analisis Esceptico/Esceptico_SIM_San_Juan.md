---
type: analysis-esceptico
tags: [red-team, regulatory, compliance, san-juan, shadow-api]
sources: [[SIM San Juan Canon Minero.md]]
confidence: high
last_update: 2026-05-10
---

# Red Team: SIM San Juan (Canon Minero)

1. **Idea central:** Se sobrestima el valor de automatizar un proceso administrativo de baja frecuencia. Pagar el canon y cargar comprobantes en el SIM no es un cuello de botella de escala como la logística o la energía; es una tarea que un equipo de paralegales resuelve con herramientas estándar. El riesgo real de perder una concesión minera rara vez es por "olvidar hacer click", sino por disputas sobre la interpretación legal de la inversión mínima exigida. Un software no te defiende en un tribunal.

2. **Trade-offs:** Se ahorran horas de trabajo manual (data entry) a cambio de asumir un riesgo de responsabilidad civil (liability) asimétrico. Si el "conector privado" falla, hay un bug, o el SIM cambia su interfaz sin aviso y la minera pierde una concesión de US$ 3.000 millones, el proveedor del SaaS será el blanco de la demanda.

3. **Riesgos críticos:** 
   - **Fragilidad de la Contraparte Estatal:** Los sistemas provinciales (como el SIM) raramente tienen APIs estables, versionadas o documentadas. Un simple cambio en el frontend del portal romperá el scraper/conector, generando falsos positivos de "compliance" justo antes de un vencimiento.
   - **Problema de TAM (Total Addressable Market):** La cantidad de clientes corporativos en San Juan que necesitan esto y pueden pagar un ticket alto es extremadamente baja. No hay volumen para justificar el mantenimiento de software B2B complejo.

4. **Efectos de segundo orden:** Si una plataforma concentra el compliance de todos los megaproyectos de cobre, se convierte en un objetivo de ciberataques (para extorsión o sabotaje corporativo). El Estado podría, además, prohibir el uso de intermediarios algorítmicos para forzar la validación humana (firma digital) en cada paso.

5. **Próximo movimiento recomendado:** No construir el producto como un SaaS autónomo (SFaaS). Si se decide explorar, debe venderse como "Consultoría Legal Aumentada": el software es solo una herramienta interna operada por un estudio jurídico especializado en minería, el cual asume el riesgo profesional (y cobra los honorarios correspondientes).
