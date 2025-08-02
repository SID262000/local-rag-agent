import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.rag_agent import ask_question
from app.ingest import parse_and_store

from docling.document_converter import DocumentConverter

st.set_page_config(page_title="Local RAG Agent", layout="wide")

st.title("🧠 Local RAG Agent")
st.markdown("Upload a PDF and ask questions based on its content.")

# Upload PDF file
uploaded_file = st.file_uploader("📄 Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    if "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
        with st.spinner("Parsing PDF and ingesting content..."):
            # Save the uploaded file locally
            with open(f"data/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.read())

            # Ingest into vector store (calls embedding + OpenSearch indexing)
            parse_and_store(f"data/{uploaded_file.name}")

            st.session_state.last_uploaded = uploaded_file.name
            st.success(f"✅ Ingested: {uploaded_file.name}")

st.divider()

# Ask a question
question = st.text_input("❓ Ask a question from the uploaded PDF")

if st.button("🧠 Get Answer") and question:
    with st.spinner("Thinking..."):
        answer = ask_question(question)
        st.markdown(f"**Answer:** {answer}")
