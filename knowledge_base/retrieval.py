import chromadb
import numpy as np
from pathlib import Path
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

BASE_DIR = Path(__file__).parent
DB_DIR = BASE_DIR / "chroma_db"

COLLECTIONS = [
    "ai_evaluation_knowledge",
    "technical_reference_knowledge"
]

TOP_K = 3
CANDIDATES_PER_COLLECTION = 10
MIN_SIMILARITY = 0.30


def retrieve_context(question):

    print("\nConnecting to ChromaDB...")

    client = chromadb.PersistentClient(path=str(DB_DIR))
    embedding_function = DefaultEmbeddingFunction()

    query_embedding = np.array(
        embedding_function([question])[0]
    )

    all_results = []

    for collection_name in COLLECTIONS:

        collection = client.get_collection(
            name=collection_name,
            embedding_function=embedding_function
        )

        count = collection.count()

        if count == 0:
            continue

        results = collection.query(
            query_texts=[question],
            n_results=min(CANDIDATES_PER_COLLECTION, count),
            include=["documents", "embeddings", "metadatas"]
        )

        for doc, embedding, metadata in zip(
            results["documents"][0],
            results["embeddings"][0],
            results["metadatas"][0]
        ):

            doc_embedding = np.array(embedding)

            similarity = np.dot(
                query_embedding, doc_embedding
            ) / (
                np.linalg.norm(query_embedding)
                * np.linalg.norm(doc_embedding)
            )

            all_results.append({
                "document": doc,
                "similarity": float(similarity),
                "source": collection_name,
                "metadata": metadata
            })

    all_results.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    relevant_results = [
        result for result in all_results
        if result["similarity"] >= MIN_SIMILARITY
    ][:TOP_K]

    print("\nRelevant Retrieved Results:\n")

    if not relevant_results:
     print("No sufficiently relevant information found.")
     return []

    for i, result in enumerate(relevant_results, start=1):

        print(f"\nResult {i}")
        print("Source:", result["source"])
        print("Similarity:", round(result["similarity"], 4))
        print("Metadata:", result["metadata"])
        print("Context:")
        print(result["document"])
        print("-" * 60)
    return [result["document"] for result in relevant_results]    


if __name__ == "__main__":
    question = input("Enter your question: ")
    retrieve_context(question)