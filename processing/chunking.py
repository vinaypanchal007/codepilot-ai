from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_documents(document):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    final_chunks = []
    for doc in document:
        chunks = splitter.split_text(doc["content"])
        for chunk in chunks:
            final_chunks.append(Document(page_content=chunk, metadata=doc["metadata"]))
            
    return final_chunks