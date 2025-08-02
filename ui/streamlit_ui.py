import streamlit as st
from app.rag_agent import ask_question
from app.ingest import parse_and_store as ingest_docs

from docling import PDFParser

def parse_pdf(file_path: str) -> str:
    parser = PDFParser(file_path)
    pages = parser.parse()
    return "\n".join([page.text for page in pages])

st.set_page_config(page_title="Local RAG Agent", layout="wide")

st.title("🧠 Local RAG Agent")
st.markdown("Upload a PDF and ask questions based on its content.")

# Upload PDF file
uploaded_file = st.file_uploader("📄 Upload a PDF document", type=["pdf"])

# Handle PDF upload
if uploaded_file is not None:
    with st.spinner("Parsing PDF and ingesting content..."):
        # Save the uploaded file locally
        with open(f"data/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.read())

        # Use Docling to parse the file
        parsed_text = parse_pdf(f"data/{uploaded_file.name}")

        # Ingest into vector store (calls embedding + OpenSearch indexing)
        ingest_docs(parsed_text, source_name=uploaded_file.name)

        st.success(f"✅ Ingested: {uploaded_file.name}")

st.divider()

# Ask a question
question = st.text_input("❓ Ask a question from the uploaded PDF")

if st.button("🧠 Get Answer") and question:
    with st.spinner("Thinking..."):
        answer = ask_question(question)
        st.markdown(f"**Answer:** {answer}")
