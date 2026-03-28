"""
ingest.py - Document ingestion pipeline

Handles loading, parsing, chunking, embedding, and storing documents
into the vector database for later retrieval.
"""


def load_pdf(file_path: str):
    # Load a PDF file from the given path and return its raw text content
    pass


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    # Split the raw text into overlapping chunks of approximately chunk_size characters
    # overlap controls how many characters are shared between adjacent chunks
    # Return a list of text chunk strings
    pass


def embed_chunks(chunks: list[str]):
    # Use sentence-transformers to generate an embedding vector for each chunk
    # Return a list of embedding vectors (one per chunk)
    pass


def store_chunks(chunks: list[str], embeddings, collection_name: str = "documents"):
    # Connect to ChromaDB and upsert the chunks and their embeddings into the given collection
    # Assign a unique ID to each chunk (e.g. based on index or a hash)
    pass


def ingest_file(file_path: str, collection_name: str = "documents"):
    # Orchestrate the full ingestion pipeline for a single file:
    # 1. Load the PDF
    # 2. Chunk the text
    # 3. Embed the chunks
    # 4. Store into ChromaDB
    pass
