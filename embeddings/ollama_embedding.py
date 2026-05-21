from langchain_ollama import OllamaEmbeddings   # ← new package

def load_ollama_embeddings():
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    return embedding