# LegalDocAI - Procesamiento Inteligente para Estudios Jurídicos

Herramienta de IA para acelerar el procesamiento de documentación legal mediante:

1. 🤖 **Clasificación Automática** de documentos
2. 🔍 **Extracción de Entidades** (fechas, firmantes, montos)
3. 🔎 **Búsqueda Semántica** en lenguaje natural

## Instalación

```bash
git clone https://github.com/tu-usuario/legal-ai-docs.git
cd legal-ai-docs
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt

Requisitos previos
Elasticsearch 8.x

Python 3.9+

Modelos de Hugging Face (se descargan automáticamente)

Uso
Iniciar la API:
uvicorn api.main:app --reload

Endpoints:
POST /upload: Subir documentos PDF

GET /search?query=...: Realizar búsquedas semánticas

Ejemplo de búsqueda:
python
import requests

response = requests.get(
    "http://localhost:8000/search",
    params={"query": "Mencione las actas con resoluciones sobre propiedad intelectual del 2023"}
)
print(response.json())
