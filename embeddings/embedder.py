from embeddings.ollama_embedding import load_ollama_embeddings

def create_embeddings():
    embeddings = load_ollama_embeddings()
    return embeddings