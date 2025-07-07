from transformers import pipeline
from .utils import pdf_to_text

class EntityExtractor:
    def __init__(self, model_path="models/ner"):
        self.ner = pipeline("ner", model=model_path, aggregation_strategy="simple")
    
    def extract(self, pdf_path, doc_type):
        text = pdf_to_text(pdf_path)
        entities = self.ner(text)
        return self._format_entities(entities, doc_type)
    
    def _format_entities(self, entities, doc_type):
        # Lógica específica por tipo de documento
        formatted = {}
        for entity in entities:
            label = entity['entity_group']
            value = entity['word']
            if label not in formatted:
                formatted[label] = []
            formatted[label].append(value)
        return formatted

# Ejemplo de uso
if __name__ == "__main__":
    extractor = EntityExtractor()
    entities = extractor.extract("data/raw/resolucion.pdf", "RESOLUCIÓN")
    print(entities)
