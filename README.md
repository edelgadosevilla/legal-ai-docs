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
Estructura del Proyecto
text
📁 legal-ai-docs/
│
├── 📁 src/
│   ├── 📄 document_processing.py
│   ├── 📄 ner_extraction.py
│   ├── 📄 semantic_search.py
│   └── 📄 utils.py
│
├── 📁 api/
│   ├── 📄 main.py
│   └── 📄 schemas.py
│
├── 📁 models/
│   ├── 📄 classifier_model.py
│   └── 📄 ner_model.py
│
├── 📁 data/
│   ├── 📁 processed/
│   └── 📁 raw/
│
├── 📁 elasticsearch/
│   └── 📄 es_config.py
│
├── 📁 tests/
│   ├── 📄 test_classification.py
│   └── 📄 test_ner.py
│
├── 📄 requirements.txt
├── 📄 Dockerfile
├── 📄 .gitignore
└── 📄 README.md
Configuración Elasticsearch
Descargar y ejecutar Elasticsearch:

bash
docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.9.0
Modelos IA
Clasificación: distilbert-base-uncased (fine-tuned)

NER: bert-base-spanish-wwm-cased (fine-tuned)

Embeddings: paraphrase-multilingual-MiniLM-L12-v2

Licencia
MIT

text

4. Haz clic en "Commit changes"

#### Paso 5: Editar el .gitignore existente
1. Ve al archivo `.gitignore`
2. Haz clic en "Edit"
3. Agrega estas líneas adicionales al final:

```gitignore
# Datos y modelos
data/raw/*
!data/raw/.gitkeep
*.pdf
*.model
*.bin
*.h5
*.pth

# Entornos virtuales
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Elasticsearch
elasticsearch/data

# Sistema
.DS_Store
Haz clic en "Commit changes"

Paso 6: Agregar archivos de código
Para cada archivo de código:

Haz clic en "Add file" > "Create new file"

En "Name your file..." ingresa la ruta completa (ej: src/document_processing.py)

Copia el contenido correspondiente (del código que te proporcioné)

Haz clic en "Commit new file"
