---
type: analysis-esceptico
tags: [red-team, energy, enre, shadow-api]
sources: [[ENRE Prioridad de Despacho.md]]
confidence: high
last_update: 2026-05-10
---

# Red Team: ENRE Prioridad de Despacho (Bypass Off-Grid)

1. **Idea central:** La propuesta de orquestar microgrids para bypassar al ENRE asume que el Estado permitirá pasivamente que megaproyectos de miles de millones de dólares evadan el financiamiento del sistema eléctrico nacional (SADI). El Estado siempre busca capturar renta de los activos más rentables.

2. **Trade-offs:** Se obtiene independencia energética absoluta y cronogramas predecibles (sin litigios ante el ENRE), pero se triplica el costo del kilovatio-hora asumiendo el CAPEX de plantas GNL/Solares en alta montaña.

3. **Riesgos críticos:** 
   - **Peaje Fantasma:** CAMMESA o el ENRE podrían dictar una normativa que obligue a los grandes usuarios mineros a pagar un cargo por "reserva de capacidad del sistema" o un impuesto solidario, incluso si operan 100% off-grid, destruyendo la ventaja económica de la micro-red.
   - **Límites Logísticos del GNL:** Escalar operaciones off-grid de cobre exige volúmenes masivos de GNL. El transporte constante de camiones criogénicos por rutas mineras saturadas (ej. RN 51) introduce un nuevo cuello de botella logístico crítico.

4. **Efectos de segundo orden:** Fragmentación total de la infraestructura eléctrica nacional. Si los actores con mayor capacidad de pago (la minería) abandonan la red interconectada, el costo fijo del sistema nacional recaerá enteramente sobre los usuarios residenciales y pymes, generando un cisma político.

5. **Próximo movimiento recomendado:** Auditar el blindaje jurídico del RIGI. Antes de diseñar la micro-red, confirmar con estudios jurídicos si el marco de estabilidad del RIGI protege al proyecto contra la creación de nuevos "cargos fijos" eléctricos por parte de autoridades provinciales o nacionales. Si no hay blindaje, no vale la pena hacer esto.
