from langchain_chroma import Chroma    # ← new package

def create_chroma_vectorstore(chunks, embeddings, path="chroma_db"):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=path
    )
    return vectorstore

def load_chroma_vectorstore(embeddings, path="chroma_db"):
    vectorstore = Chroma(
        persist_directory=path,
        embedding_function=embeddings
    )
    return vectorstore