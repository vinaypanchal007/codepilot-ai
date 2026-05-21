import os

from ingestion.clone_repos import (
    clone_repository
)

from ingestion.read_files import (
    read_files
)

from ingestion.config import (
    REPOSITORIES,
    BASE_DIR
)

from processing.chunking import (
    chunk_documents
)

from embeddings.embedder import (
    create_embeddings
)

from vectorstore.chroma_store import (
    create_chroma_vectorstore
)

from retrieval.retriever import (
    get_retriever
)

from llm.generate_answer import (
    generate_response
)


def main():

    print(
        "\nStarting repository ingestion process...\n"
    )

    all_documents = []

    for repo in REPOSITORIES:

        repo = repo.strip()

        clone_repository(repo)

        repo_path = os.path.join(
            BASE_DIR,
            repo
        )

        documents = read_files(repo_path)

        all_documents.extend(documents)

    print(
        f"\nTotal files loaded: {len(all_documents)}"
    )

    chunks = chunk_documents(all_documents)

    print(
        f"\nTotal chunks created: {len(chunks)}"
    )

    embeddings = create_embeddings()

    print(
        "\nEmbeddings model loaded successfully."
    )

    vector_store = create_chroma_vectorstore(
        chunks,
        embeddings
    )

    print(
        "\nVector database created successfully."
    )

    retriever = get_retriever(vector_store)

    print("\nRAG System Ready 🚀\n")

    while True:

        query = input(
            "\nAsk Question (type exit to quit): "
        )

        if query.lower() == "exit":
            break

        retrieved_docs = retriever.invoke(query)

        context = "\n\n".join([
            doc.page_content
            for doc in retrieved_docs
        ])

        answer = generate_response(
            query,
            context
        )

        print("\nAI Response:\n")

        print(answer)


if __name__ == "__main__":
    main()