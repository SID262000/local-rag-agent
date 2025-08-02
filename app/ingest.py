from docling import Document
from sentence_transformers import SentenceTransformer
from opensearchpy import OpenSearch
from app.config import OPENSEARCH_HOST, INDEX_NAME
import uuid, os

model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenSearch(hosts=[{"host": OPENSEARCH_HOST, "port": 9200}])

def parse_and_store(doc_path):
    doc = Document.from_file(doc_path)
    chunks = doc.text.split("\n\n")  # basic chunking
    embeddings = model.encode(chunks)

    for chunk, emb in zip(chunks, embeddings):
        doc_id = str(uuid.uuid4())
        client.index(index=INDEX_NAME, body={
            "text": chunk,
            "embedding": emb.tolist()
        })

if __name__ == "__main__":
    for file in os.listdir("docs/"):
        if file.endswith(".pdf"):
            parse_and_store(os.path.join("docs", file))
