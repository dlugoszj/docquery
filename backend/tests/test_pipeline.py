from src.ingest import load_txt, chunk_text, embed_chunks, ingest_file
from src.query import build_prompt, embed_query, ask

# Test loading
text = load_txt("tests/sample.txt")
print(f"Loaded {len(text)} characters")

# Test chunking
chunks = chunk_text(text)
print(f"Got {len(chunks)} chunks")
print("First chunk:", chunks[0][:100])

# Test embedding
embeddings = embed_chunks(chunks)
print(f"Embeddings shape: {embeddings.shape}")

# Test query embedding
query_embedding = embed_query("What is machine learning?")
print(f"Query embedding shape: {query_embedding.shape}")

# Test prompt building
prompt = build_prompt("What is machine learning?", chunks[:2])
print("Prompt preview:", prompt[:500])

# Test ingest_file and ask
print("final Test")
ingest_file("tests/sample.txt")
print(ask("What are the 3 main types of machine learning?"))
