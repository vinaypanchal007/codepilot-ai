from langchain_community.vectorstores import Chroma

def create_chroma_vectorstore(
    chunks,
    embeddings
):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vector_db",
    )
    
    vector_store.persist()
    return vector_store