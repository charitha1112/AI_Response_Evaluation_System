import chromadb
import re
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

STOP_WORDS = {
    "what", "is", "are", "was", "were", "the", "a", "an",
    "in", "on", "of", "to", "for", "and", "or", "how",
    "why", "who", "which", "with", "explain", "describe"
}


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", str(text).lower())
    return {
        word for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


def retrieve_context(question):

    print("\nConnecting to ChromaDB...")

    client = chromadb.PersistentClient(path=str(DB_DIR))
    embedding_function = DefaultEmbeddingFunction()

    query_embedding = np.array(
        embedding_function([question])[0],
        dtype=float
    )

    query_words = tokenize(question)
    all_results = []

    for collection_name in COLLECTIONS:

        try:
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

            documents = results.get("documents", [[]])[0]
            embeddings = results.get("embeddings", [[]])[0]
            metadatas = results.get("metadatas", [[]])[0]

            for doc, embedding, metadata in zip(
                documents, embeddings, metadatas
            ):

                if not doc or embedding is None:
                    continue

                doc_embedding = np.array(embedding, dtype=float)

                denominator = (
                    np.linalg.norm(query_embedding)
                    * np.linalg.norm(doc_embedding)
                )

                if denominator == 0:
                    continue

                semantic_score = float(
                    np.dot(query_embedding, doc_embedding)
                    / denominator
                )

                document_words = tokenize(doc)

                keyword_score = (
                    len(query_words & document_words)
                    / len(query_words)
                    if query_words else 0
                )

                combined_score = (
                    0.65 * semantic_score
                    + 0.35 * keyword_score
                )

                all_results.append({
                    "document": doc,
                    "similarity": semantic_score,
                    "keyword_score": keyword_score,
                    "combined_score": combined_score,
                    "source": collection_name,
                    "metadata": metadata
                })

        except Exception as error:
            print(
                f"Collection {collection_name} error: {error}"
            )

    all_results.sort(
        key=lambda item: item["combined_score"],
        reverse=True
    )

    relevant_results = [
        item for item in all_results
        if item["combined_score"] >= MIN_SIMILARITY
    ][:TOP_K]

    print("\nRelevant Retrieved Results:\n")

    if not relevant_results:
        print("No sufficiently relevant information found.")
        return []

    for index, result in enumerate(relevant_results, start=1):

        print(f"\nResult {index}")
        print("Source:", result["source"])
        print("Semantic Similarity:", round(result["similarity"], 4))
        print("Keyword Score:", round(result["keyword_score"], 4))
        print("Combined Score:", round(result["combined_score"], 4))
        print("Metadata:", result["metadata"])
        print("Context:")
        print(result["document"])
        print("-" * 60)

    return [
        result["document"]
        for result in relevant_results
    ]


if __name__ == "__main__":
    question = input("Enter your question: ")
    retrieve_context(question)