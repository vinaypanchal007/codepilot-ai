from langchain_community.vectorstores import FAISS

def create_faiss_vectorstore(
    chunks,
    embeddings
):
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vector_db",
    )
    
    return vector_store