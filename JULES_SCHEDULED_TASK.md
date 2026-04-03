# JULES_SCHEDULED_TASK.md - Configuración de Tarea Programada Diaria

## Objetivo
Configurar una tarea automatizada para que el agente Jules (experto en Energía y Minería en Argentina) actualice diariamente la base de conocimiento en Obsidian.

## 1. Prompt de la Tarea Diaria (Scheduled Task)
Copie y pegue el siguiente prompt para ejecutar la actualización:

> "Actúa como Jules, el experto en energía y minería en Argentina. Realiza la siguiente tarea diaria:
>
> 1. **Investigación:** Busca noticias de hoy sobre Vaca Muerta, Cobre (Taca Taca, Los Azules, Josemaría), Litio (Catamarca, Salta, Jujuy), RIGI y Corredor Bioceánico de Capricornio en las fuentes prioritarias (discoveryalert.com.au, mineriaenergia.com, argenports.com, vacamuertaonline.com.ar, vacamuertanews.com, panorama-minero.com/es, camaraminerasj.com.ar, visec.com.ar, fuerzaminera.com, tiempodesanjuan.com, shale24.com, econojournal.com.ar, mase.lmneuquen.com, rumbominero.com, newswire.ca, guiavacamuerta.com).
> 2. **Ingestión:** Guarda el texto bruto recolectado en `raw/` con el nombre de archivo `YYYY-MM-DD_news_mining_energy.md`.
> 3. **Procesamiento:** Actualiza las notas existentes en `wiki/` (01 Projects, 02 Frameworks, 03 Analysis y 04 Daily) basándote en la nueva información. Si surge un proyecto o marco regulatorio nuevo, crea la nota correspondiente.
> 4. **Mantenimiento:** Mantén los backlinks `[[ ]]` entre notas y actualiza los diagramas Mermaid si hay nuevas conexiones estratégicas.
> 5. **Reporte:** Genera el resumen diario en `wiki/04 Daily/YYYY-MM-DD_Daily_Report.md`.
> 6. **Commit:** Realiza el commit de todos los cambios con un mensaje descriptivo."

## 2. Opciones de Configuración

### Opción A: GitHub Actions (Recomendado para Nube)
Si el repositorio está en GitHub, cree un archivo `.github/workflows/daily_update.yml`:

```yaml
name: Daily Knowledge Base Update
on:
  schedule:
    - cron: '0 9 * * *' # Ejecuta todos los días a las 09:00 UTC
  workflow_dispatch: # Permite ejecución manual

jobs:
  update-wiki:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Jules Agent
        # Aquí se integraría la llamada a la API del agente con el Prompt indicado arriba.
        run: |
          echo "Ejecutando actualización diaria..."
          # Integración con el sistema de agentes correspondiente
```

### Opción B: Entorno Local (Linux/Mac - Cron)
Añada la siguiente línea a su `crontab -e`:

```bash
0 9 * * * cd /ruta/a/tu/obsidian/vault && [Comando_Para_Ejecutar_Jules] "[Prompt_De_Tarea_Diaria]"
```

### Opción C: Windows (Task Scheduler)
1. Cree un script `.bat` o `.ps1` que navegue al directorio del repo.
2. Configure el programador de tareas para ejecutar el script diariamente.

## 3. Consideraciones Críticas
- **Fuentes Prioritarias:** El agente debe dar prioridad a las fuentes argentinas mencionadas para capturar noticias locales (shale24, econojournal, etc.).
- **Backlinks:** Es vital que el agente use corchetes dobles `[[ ]]` para que Obsidian pueda mapear el grafo de conocimiento correctamente.
- **Formato Mermaid:** Los diagramas en `wiki/03 Analysis/` deben mantenerse legibles y actualizados.
