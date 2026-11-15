import chromadb
import re
import math
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).parent
DB_DIR = BASE_DIR / "chroma_db"

COLLECTIONS = [
    "ai_evaluation_knowledge",
    "technical_reference_knowledge"
]

CANDIDATES = 20
TOP_K = 3
RRF_K = 60


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def bm25_scores(query, documents):
    query_terms = tokenize(query)
    tokenized_docs = [tokenize(doc) for doc in documents]

    if not documents:
        return []

    doc_count = len(documents)
    avg_length = sum(map(len, tokenized_docs)) / doc_count or 1

    document_frequency = Counter()
    for tokens in tokenized_docs:
        document_frequency.update(set(tokens))

    scores = []

    for tokens in tokenized_docs:
        frequencies = Counter(tokens)
        score = 0
        doc_length = len(tokens)

        for term in query_terms:
            frequency = frequencies[term]
            if frequency == 0:
                continue

            df = document_frequency[term]
            idf = math.log(
                1 + (doc_count - df + 0.5) / (df + 0.5)
            )

            k1 = 1.5
            b = 0.75

            denominator = frequency + k1 * (
                1 - b + b * doc_length / avg_length
            )

            score += idf * (
                frequency * (k1 + 1) / denominator
            )

        scores.append(score)

    return scores


def hybrid_search(question):
    client = chromadb.PersistentClient(path=str(DB_DIR))
    candidates = []

    for collection_name in COLLECTIONS:
        try:
            collection = client.get_collection(collection_name)
        except Exception:
            print(f"Collection not found: {collection_name}")
            continue

        count = collection.count()
        if count == 0:
            continue

        results = collection.query(
            query_texts=[question],
            n_results=min(CANDIDATES, count),
            include=["documents", "metadatas"]
        )

        ids = results["ids"][0]
        documents = results["documents"][0]

        if not documents:
            continue

        keyword_scores = bm25_scores(question, documents)

        keyword_order = sorted(
            range(len(documents)),
            key=lambda i: keyword_scores[i],
            reverse=True
        )

        keyword_ranks = {
            index: rank + 1
            for rank, index in enumerate(keyword_order)
        }

        for index, document in enumerate(documents):
            semantic_rank = index + 1
            keyword_rank = keyword_ranks[index]

            rrf_score = (
                1 / (RRF_K + semantic_rank)
                + 1 / (RRF_K + keyword_rank)
            )

            candidates.append({
                "document": document,
                "source": collection_name,
                "rrf_score": rrf_score,
                "keyword_score": keyword_scores[index]
            })

    candidates.sort(
        key=lambda item: item["rrf_score"],
        reverse=True
    )

    top_results = candidates[:TOP_K]

    print("\nHybrid Search Results:\n")

    if not top_results:
        print("No results found.")
        return []

    for rank, result in enumerate(top_results, start=1):
        print(f"\nResult {rank}")
        print("Source:", result["source"])
        print("RRF Score:", round(result["rrf_score"], 5))
        print("BM25 Score:", round(result["keyword_score"], 4))
        print("Context:", result["document"])
        print("-" * 50)

    return [result["document"] for result in top_results]


if __name__ == "__main__":
    question = input("Enter your question: ")
    hybrid_search(question)