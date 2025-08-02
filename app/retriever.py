# app/retriever.py
from sentence_transformers import SentenceTransformer
from opensearchpy import OpenSearch
from app.config import OPENSEARCH_HOST, INDEX_NAME

model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenSearch(hosts=[{"host": OPENSEARCH_HOST, "port": 9200}])

def retrieve_relevant_docs(query, k=3):
    query_vector = model.encode(query).tolist()
    body = {
        "size": k,
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_vector,
                    "k": k
                }
            }
        }
    }
    response = client.search(index=INDEX_NAME, body=body)
    return [hit["_source"]["text"] for hit in response["hits"]["hits"]]
