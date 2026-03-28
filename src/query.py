"""
query.py - Document querying and RAG pipeline

Handles embedding a user query, retrieving relevant chunks from the
vector database, and generating an answer via the Anthropic API.
"""


def embed_query(query: str):
    # Use sentence-transformers to generate an embedding vector for the user's query string
    # Return the embedding vector
    pass


def retrieve_chunks(query_embedding, collection_name: str = "documents", n_results: int = 5):
    # Connect to ChromaDB and query the given collection using the query embedding
    # Return the top n_results most similar chunks as a list of strings
    pass


def build_prompt(query: str, context_chunks: list[str]) -> str:
    # Combine the retrieved context chunks and the user's query into a single prompt string
    # The prompt should instruct the model to answer based only on the provided context
    # Return the assembled prompt string
    pass


def generate_answer(prompt: str) -> str:
    # Load the ANTHROPIC_API_KEY from environment variables
    # Send the prompt to the Anthropic API using the anthropic client
    # Return the model's response text
    pass


def ask(query: str, collection_name: str = "documents") -> str:
    # Orchestrate the full query pipeline for a user question:
    # 1. Embed the query
    # 2. Retrieve relevant chunks from ChromaDB
    # 3. Build the prompt
    # 4. Generate and return the answer
    pass
