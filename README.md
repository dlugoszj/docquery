# docquery

Query your documents using RAG (Retrieval-Augmented Generation) powered by ChromaDB and Claude.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your Anthropic API key:

```bash
cp .env.example .env
```

Then edit `.env` and replace `your-api-key-here` with your actual key.
