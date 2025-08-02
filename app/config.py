# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()
OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST", "localhost")
INDEX_NAME = os.getenv("INDEX_NAME", "docs-index")
