from transformers import pipeline
from .utils import pdf_to_text

class DocumentClassifier:
    def __init__(self, model_path="models/classifier"):
        self.classifier = pipeline("text-classification", model=model_path)
    
    def classify(self, pdf_path):
        text = pdf_to_text(pdf_path)
        result = self.classifier(text)
        return result[0]['label']

# Ejemplo de uso
if __name__ == "__main__":
    classifier = DocumentClassifier()
    doc_type = classifier.classify("data/raw/contrato.pdf")
    print(f"Tipo de documento: {doc_type}")
