from docling.document_converter import DocumentConverter
from sentence_transformers import SentenceTransformer
from opensearchpy import OpenSearch
from app.config import OPENSEARCH_HOST, INDEX_NAME
import uuid, os

model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenSearch(hosts=[{"host": OPENSEARCH_HOST, "port": 9200}])

def parse_and_store(doc_path):
    doc = DocumentConverter().convert(doc_path)
    text = doc.document.export_to_text()
    chunks = text.split("\n\n")  # Split by paragraphs or sections
    embeddings = model.encode(chunks)

    for chunk, emb in zip(chunks, embeddings):
        client.index(index=INDEX_NAME, body={
            "text": chunk,
            "embedding": emb.tolist()
        })

if __name__ == "__main__":
    for file in os.listdir("docs/"):
        if file.endswith(".pdf"):
            parse_and_store(os.path.join("docs", file))
