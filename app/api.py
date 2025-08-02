# app/api.py
from fastapi import FastAPI, Query
from app.rag_agent import ask_question

app = FastAPI()

@app.get("/ask")
def ask(q: str = Query(...)):
    print(f"Received question: {q}")  # Debugging: print the received question
    answer = ask_question(q)
    return {"answer": answer}
