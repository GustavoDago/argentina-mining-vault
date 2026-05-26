---
type: analysis
tags: [opportunity, technology, energy, oil-gas, software, predictive-maintenance]
sources: [[2026-05-25_news_mining_energy]], [[Vaca Muerta]], [[RIGI]], [[Proyecto LLL Oil]], [[PreMortem_ShaleFlow]]
confidence: high
last_update: 2026-05-26
---

# Opp: ShaleFlow Añelo - SaaS de Mantenimiento Predictivo e Integración con Inventarios OEM

## 1. Oportunidad de Negocio (High-Leverage)
El salto de escala física en Vaca Muerta, liderado por el megaproyecto RIGI de [[YPF]] en Loma La Lata (US$ 25.000M para perforar 1.152 pozos) y las 1.700 etapas de fractura mensuales, somete a las bombas de fractura y válvulas de alta presión a una fatiga mecánica sin precedentes. Las demoras en la importación de repuestos críticos paralizan frack crews con un costo stand-by diario de US$ 80.000. 

Tras la auditoría forense [[PreMortem_ShaleFlow]], se descartó el modelo de fabricación local (impresión 3D metal/CNC) por barreras insalvables de homologación de garantías y la ausencia de equipamiento HIP en la Patagonia. La verdadera oportunidad reside en capturar el valor de la **información de la falla**: un modelo SaaS puro que predice el desgaste y automatiza el abastecimiento sin asumir riesgo metalúrgico.

## 2. El Play Tecnológico
Consiste en un sistema de software B2B de dos capas:
- **Capa Predictiva (Edge AI):** Algoritmos entrenados para detectar anomalías estructurales mediante análisis de vibración armónica, temperatura y contrapresión de los sensores existentes en los trailers de fractura, generando alertas tempranas con un horizonte de 72 horas antes de la rotura.
- **Capa de Integración y Ruteo (Shadow API OEM):** En lugar de fabricar la pieza, la plataforma se integra mediante APIs seguras con los sistemas ERP y bases de datos de inventario regional de los propios fabricantes originales (OEMs como NOV, SLB, Halliburton, Weir SPM) en sus nuevos almacenes de Neuquén. Al predecir la falla, genera una orden de compra automatizada y rutea el repuesto desde el inventario del OEM hasta el pozo en tiempo récord, cobrando una suscripción por trailer monitoreado más un fee de intermediación logística.

## 3. Beneficios RIGI (Leverage)
- Al ser un desarrollo de software de alta tecnología enfocado en la eficiencia de recursos no convencionales, califica para los incentivos del **Súper RIGI** (reducción del impuesto a las ganancias al 15%).
- Los operadores petroleros pueden computar esta suscripción de software local dentro del requisito legal de contratación de proveedores locales (20% del Capex RIGI bajo el Decreto 105/2026).
- Cero barreras arancelarias, ya que no requiere importación de maquinaria compleja SLS ni insumos metálicos atomizados.

## 4. Riesgos Críticos
- **Soberanía y Acceso a Datos (Ley 25.326):** Las grandes operadoras de servicios (SLB, Halliburton) consideran los datos de vibración y telemetría vehicular como propiedad altamente confidencial. Se requiere un acuerdo de procesamiento de datos (DPA) restrictivo y un esquema de procesamiento local (Edge Computing) donde los datos crudos no salgan de la red del operador.
- **Incompatibilidad de Legacy APIs:** Los ERPs de los OEMs tradicionales en el país suelen ser opacos o carecer de endpoints modernos, requiriendo integraciones a medida (mediante web scrapers o middleware adaptados).

## 5. Próximo Movimiento Recomendado
**Estructuración de Piloto de Telemetría con Y-TEC:**
Proponer una alianza de co-desarrollo con Y-TEC para validar el algoritmo predictivo de fallas mecánicas en 10 trailers piloto operados por YPF en Loma La Lata, utilizando el laboratorio metalúrgico de Y-TEC para correlacionar las alertas algorítmicas con la fatiga real microscópica de las piezas de desgaste retiradas.

---
**Backlinks:** [[Vaca Muerta]], [[Proyecto LLL Oil]], [[YPF]], [[RIGI]], [[PreMortem_ShaleFlow]].
