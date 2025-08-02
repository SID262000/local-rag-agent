# 🧠 Local RAG Agent

A fully local Retrieval-Augmented Generation (RAG) system combining:

- **Docling** for PDF parsing
- **SentenceTransformers** for embeddings
- **OpenSearch** as the vector database
- **Ollama** for running local LLMs like LLaMA 3
- **FastAPI** to serve RAG responses as an API
- **Streamlit** to provide a clean interactive UI

---

## 📌 Features

✅ Fully Local (No OpenAI API needed)  
✅ Parse and index your documents with semantic understanding  
✅ Use any Ollama-supported LLM  
✅ FastAPI backend for structured use  
✅ Streamlit front-end for user interaction  
✅ Configurable and scalable  

---

## 🧱 Architecture

+------------+ +--------------------+
| PDF Docs | --→--→--| Docling |
+------------+ +--------------------+
↓
+--------------------+
| SentenceTransformers |
+--------------------+
↓
+------------------+
| OpenSearch DB |
+------------------+
↓
+-------------+ Query ↑ +---------------+
| Streamlit | -----------+---->| FastAPI |
+-------------+ | +---------------+
↓
+---------------+
| Ollama LLM |
+---------------+

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/yourusername/local-rag-agent.git
cd local-rag-agent
```
### 2. Install with uv

```
uv venv
uv pip install -r requirements.txt
```

### 3. Set Up Environment
Create a .env file:

```
OPENSEARCH_HOST=localhost
INDEX_NAME=docs-index
```

Ensure OpenSearch is running locally on port 9200. If not, use Docker:
```docker run -p 9200:9200 -e "discovery.type=single-node" opensearchproject/opensearch:latest```

### 4. Start Ollama (LLM runtime)

``` ollama run llama3 ```

### 5. Add PDFs

Place your .pdf files in the docs/ directory.

### 6. Ingest Documents

``` python app/ingest.py```

### 7. Run FastAPI Backend

``` uvicorn app.api:app --reload ```

### 8. Launch Streamlit UI

``` streamlit run ui/streamlit_ui.py ```

📦 Tech Stack

Embedding Model - sentence-transformers <br>
Vector DB - OpenSearch <br>
PDF Parser - Docling <br>
LLM Engine - Ollama + llama3 model <br>
Backend API - FastAPI <br>
UI - Streamlit <br>
Env Management - uv, .env <br>

🙋 FAQ
Q: Can I run this completely offline?
Yes, after installing dependencies and downloading the model via Ollama.

Q: How large can my documents be?
They're chunked into paragraphs. You can customize chunking logic in ingest.py.

Q: Can I use another model in Ollama?
Yes, just change "llama3" to any other supported model name in rag_agent.py.

📜 License
MIT License

🤝 Contributing
Contributions, issues and PRs are welcome!
To contribute, fork the repo and raise a PR.