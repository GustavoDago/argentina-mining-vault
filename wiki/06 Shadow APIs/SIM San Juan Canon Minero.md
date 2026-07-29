---
type: shadow-api
tags: [reverse-engineering, regulatory, compliance, san-juan, RIGI]
sources: [[San Juan]], [[Josemaría]], [[Los Azules]], [[Veladero]], [[Oportunidades y Conexiones]]
confidence: high
last_update: 2026-07-23
---

# Shadow API: SIM San Juan (Canon y Concesiones Mineras)

Proceso regulatorio provincial de gestión de caducidades, pagos de canon minero y declaración de inversiones en el Sistema Integral Minero (SIM) de San Juan.

## Especificación del Proceso (Endpoint)
- **Autoridad Responsable (Backend):** Secretaría de Gestión Ambiental y Minera de San Juan, Escribanía de Minas y Juzgado de Minas provincial.
- **Input Requerido:** Presentación de comprobantes de pago de canon semestral, informes de avance de exploración/explotación y DDJJ de inversión en concesiones de cobre/oro (ej. **Josemaría** por US$ 9.700M, **Los Azules** por US$ 2.672M, **Veladero** por US$ 380M).
- **Output Esperado:** `200 OK | Certificado de Dominio Vigente y Mantenimiento de Concesión`.
- **Latencia Real:** En transición desde expedientes papel hacia el portal web del SIM; latencia real de **30 a 90 días** para la homologación final de los comprobantes de pago.

## Fricciones y Fallas (Error Codes)
- **`ERR_CANON_EXPIRATION`:** Pérdida o caducidad automática de pedimentos mineros valiosos por demoras administrativas en la acreditación bancaria del canon antes de la fecha límite.
- **`ERR_SIM_PORTAL_DOWN`:** Interrupción de servicio y fallas de carga de archivos adjuntos en la plataforma provincial web del SIM durante días de vencimiento masivo.
- **`ERR_TITLE_DISPUTE`:** Superposición de mensuras o vacíos documentales reclamados por terceros o competidores sobre áreas limítrofes (ej. zona de contacto Vicuña / Filo del Sol).

## Oportunidad de Abstracción (SFaaS)
**SaaS de Compliance Minero Aumentado ("SIM Compliance Ledger"):**
- **Arquitectura:** Desarrollar una solución de "Consultoría Legal Aumentada" asistida por software de control (Humano en el Bucle - HITL).
- **Funcionalidad:** Conector B2B que sincroniza los calendarios de vencimiento de canon y obligaciones ambientales de las mineras Tier 1 y Tier 2 con el SIM de San Juan, efectuando auditorías automáticas de pre-pago y notificando alertas tempranas a los departamentos legales.
- **Seguridad y Eximente:** Incorporación de cláusulas de exención restrictivas y generación de pistas de auditoría inalterables que evitan la caducidad por error humano o fallas del portal provincial.

