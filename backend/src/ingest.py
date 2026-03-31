"""
ingest.py - Document ingestion pipeline

Handles loading, parsing, chunking, embedding, and storing documents
into the vector database for later retrieval.
"""
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import docx

def load_pdf(file_path: str):
    # Load a PDF file from the given path and return its raw text content
    readPDF = PdfReader(file_path)
    PDFText = ""
    for page in readPDF.pages:
        PDFText += page.extract_text()
    return PDFText

def load_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_file(file_path: str) -> str:
    ext = file_path.rsplit(".", 1)[-1].lower()
    loaders = {
        "pdf": load_pdf,
        "docx": load_docx,
        "txt": load_txt,
    }
    if ext not in loaders:
        raise ValueError(f"Unsupported file type: .{ext}")
    return loaders[ext](file_path)



def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    # Split the raw text into overlapping chunks of approximately chunk_size characters
    # overlap controls how many characters are shared between adjacent chunks
    # Return a list of text chunk strings
    textChunks = []

    start = 0
    while start < len(text):
        textChunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return textChunks


def embed_chunks(chunks: list[str]):
    SentenceTransformerModel = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = SentenceTransformerModel.encode(chunks)

    return embeddings


def store_chunks(chunks: list[str], embeddings, collection_name: str = "documents"):
    # Connect to ChromaDB and upsert the chunks and their embeddings into the given collection
    # Assign a unique ID to each chunk (e.g. based on index or a hash)
    client = chromadb.Client()

    collection = client.get_or_create_collection( name=collection_name )

    collection.add(
        ids = [str(i) for i in range(len(chunks))],
        documents= chunks,
        embeddings=embeddings
    )
    


def ingest_file(file_path: str, collection_name: str = "documents"):
    # Orchestrate the full ingestion pipeline for a single file:
    # 1. Load the PDF
    # 2. Chunk the text
    # 3. Embed the chunks
    # 4. Store into ChromaDB
    PDFText = load_file(file_path)
    chunks = chunk_text(PDFText)
    embeddings = embed_chunks(chunks)
    store_chunks(chunks, embeddings, collection_name)
