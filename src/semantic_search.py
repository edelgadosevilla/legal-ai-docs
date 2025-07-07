from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from .utils import pdf_to_text

class SemanticSearcher:
    def __init__(self, es_host="http://localhost:9200"):
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self.es = Elasticsearch(es_host)
        self.index_name = "legal_documents"
    
    def index_document(self, doc_id, text, metadata):
        embedding = self.model.encode(text).tolist()
        body = {
            "text": text,
            "embedding": embedding,
            **metadata
        }
        self.es.index(index=self.index_name, id=doc_id, body=body)
    
    def search(self, query, top_k=5):
        query_embedding = self.model.encode(query).tolist()
        script_query = {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": query_embedding}
                }
            }
        }
        response = self.es.search(
            index=self.index_name,
            body={"query": script_query, "size": top_k}
        )
        return [hit["_source"] for hit in response["hits"]["hits"]]

# Ejemplo de uso
if __name__ == "__main__":
    searcher = SemanticSearcher()
    results = searcher.search("¿Cuál fue la resolución en la acta numero XXX?")
    for res in results:
        print(f"Documento: {res['doc_type']}, Score: {res['_score']}")
