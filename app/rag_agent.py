# app/rag_agent.py
import httpx
from app.retriever import retrieve_relevant_docs

def query_ollama(prompt: str):
    response = httpx.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

def ask_question(question):
    chunks = retrieve_relevant_docs(question)
    context = "\n".join(chunks)
    prompt = f"Answer the following based on the context:\n\n{context}\n\nQuestion: {question}"
    return query_ollama(prompt)
