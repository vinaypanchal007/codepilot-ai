from langchain_community.embeddings import OllamaEmbeddings

def load_ollama_embeddings():
    embedding =  OllamaEmbeddings(model="nomic-embed-text")
    return embedding
