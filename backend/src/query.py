"""
query.py - Document querying and RAG pipeline

Handles embedding a user query, retrieving relevant chunks from the
vector database, and generating an answer via the Anthropic API.
"""
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import anthropic
import chromadb

load_dotenv(override=True)

def embed_query(query: str):
    # Use sentence-transformers to generate an embedding vector for the user's query string
    # Return the embedding vector
    SentenceTransformerModel = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = SentenceTransformerModel.encode(query)

    return embedding


def retrieve_chunks(query_embedding, collection_name: str = "documents", n_results: int = 5):
    # Connect to ChromaDB and query the given collection using the query embedding
    # Return the top n_results most similar chunks as a list of strings
    client = chromadb.Client()

    collection = client.get_or_create_collection( name=collection_name )
    
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results["documents"][0]


def build_prompt(query: str, context_chunks: list[str]) -> str:
    # Combine the retrieved context chunks and the user's query into a single prompt string
    # The prompt should instruct the model to answer based only on the provided context
    # Return the assembled prompt string
    prompt = """
    A query will be provided to you, the start of the query will be signified by 'Query:'. Please answer the query by looking at the provided context chunks. 
    The start of the context chunks will be signified by 'Chunks'. Each chunk will be separated by the newline symbol \n
    """
    
    prompt += "Query: "
    prompt += query
    prompt += "\n Chunks: "
    for chunk in context_chunks:
        prompt += chunk
        prompt += "\n"

    return prompt



def generate_answer(prompt: str) -> str:
    # Load the ANTHROPIC_API_KEY from environment variables
    # Send the prompt to the Anthropic API using the anthropic client
    # Return the model's response text
    client = anthropic.Anthropic()
    
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text




def ask(query: str, collection_name: str = "documents") -> str:
    # Orchestrate the full query pipeline for a user question:
    # 1. Embed the query
    # 2. Retrieve relevant chunks from ChromaDB
    # 3. Build the prompt
    # 4. Generate and return the answer

    embedding = embed_query(query)
    chunks = retrieve_chunks(embedding, collection_name)
    prompt = build_prompt(query, chunks)
    return generate_answer(prompt)
