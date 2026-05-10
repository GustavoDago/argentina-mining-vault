---
type: analysis-esceptico
tags: [red-team, energy, san-juan, vpp, mining]
sources: [[VPP_Mineria_San_Juan.md]]
confidence: medium
last_update: 2026-05-10
---

# Red Team: VPP Minería San Juan

1. **Idea central:** El cuello de botella no es tecnológico, es político y cultural. Las mineras operan en silos y consideran la energía un insumo crítico de seguridad nacional para sus operaciones. Venderles un SaaS de orquestación subestima drásticamente la barrera de adopción de ceder el control de su generación a un "single point of failure" externo.

2. **Trade-offs:** Se promete independencia del ENRE y de la red interconectada a cambio de forzar a las mineras a desviar capital (CAPEX) hacia generación off-grid compleja. Se sacrifica la simplicidad operativa por resiliencia.

3. **Riesgos críticos:** 
   - **Resistencia Comercial:** Desconfianza endémica entre corporaciones mineras competidoras (ej. Lundin vs McEwen) para compartir datos de demanda y generación en tiempo real.
   - **Riesgo Regulatorio:** Si el Estado o una APP resuelve sorpresivamente la ampliación de la línea de 500kV, el caso de negocio del VPP colapsa y la infraestructura off-grid se convierte en un activo varado (stranded asset).
   - **Fricción Técnica:** Integrar SCADAs cerrados y protocolos industriales legacy de distintos vendors (Siemens, ABB) es un infierno de integración, no un simple despliegue SaaS.

4. **Efectos de segundo orden:** Si el modelo triunfa, balcaniza la red eléctrica argentina. Los grandes consumidores abandonarán el SADI (Sistema Argentino de Interconexión) dejando a los usuarios residenciales soportando los costos fijos de un sistema desfinanciado.

5. **Próximo movimiento recomendado:** No escribir una sola línea de código para el "Balance de Carga Predictivo". El movimiento inicial debe ser puramente comercial: intentar conseguir un MoU (Memorándum de Entendimiento) vinculante entre al menos dos operadoras mineras en San Juan que accedan a mutualizar su generación. Si se niegan a firmar, no vale la pena hacer esto.
