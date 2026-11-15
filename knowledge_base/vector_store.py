import chromadb
import json


def store_embeddings(input_file):
    client = chromadb.PersistentClient(
        path="knowledge_base/chroma_db"
    )

    collection = client.get_or_create_collection(
        name="ai_evaluation_knowledge"
    )

    with open(input_file, "r", encoding="utf-8") as file:
        records = json.load(file)

    for start in range(0, len(records), 100):
        batch = records[start:start + 100]

        collection.upsert(
            ids=[
                f"chunk_{record['record_id']}_{record['chunk_id']}"
                for record in batch
            ],
            embeddings=[
                record["embedding"] for record in batch
            ],
            documents=[
                record["text"] for record in batch
            ]
        )

    print("Stored records:", collection.count())


if __name__ == "__main__":
    store_embeddings(
        "knowledge_base/data/squad_embeddings.json"
    )