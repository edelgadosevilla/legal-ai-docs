from fastapi import FastAPI, UploadFile, File
from src.document_processing import DocumentClassifier
from src.ner_extraction import EntityExtractor
from src.semantic_search import SemanticSearcher
from schemas import DocumentMetadata

app = FastAPI()

classifier = DocumentClassifier()
extractor = EntityExtractor()
searcher = SemanticSearcher()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Guardar PDF
    file_path = f"data/raw/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Procesar documento
    doc_type = classifier.classify(file_path)
    entities = extractor.extract(file_path, doc_type)
    
    # Indexar para búsqueda
    text = pdf_to_text(file_path)
    metadata = DocumentMetadata(
        type=doc_type,
        entities=entities,
        filename=file.filename
    ).dict()
    searcher.index_document(file.filename, text, metadata)
    
    return {"type": doc_type, "entities": entities}

@app.get("/search")
def search(query: str):
    return searcher.search(query)
