import json
import chromadb
import os


def generate_embeddings(input_file, output_file):
    print("Loading dataset...")

    with open(input_file, "r", encoding="utf-8") as file:
        records = json.load(file)

    total = len(records)

    if total == 0:
        print("No chunks found.")
        return

    print("Loading ChromaDB embedding model...")

    embedding_function = (
        chromadb.utils.embedding_functions.DefaultEmbeddingFunction()
    )

    batch_size = 128

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print("Generating embeddings in batches...")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("[\n")

        first_record = True

        for start in range(0, total, batch_size):
            batch = records[start:start + batch_size]

            texts = [record["text"] for record in batch]
            embeddings = embedding_function(texts)

            for record, embedding in zip(batch, embeddings):
                record["embedding"] = [float(x) for x in embedding]

                if not first_record:
                    file.write(",\n")

                json.dump(record, file, ensure_ascii=False)
                first_record = False

            file.flush()

            completed = min(start + len(batch), total)
            print(f"Processed {completed}/{total} chunks")

        file.write("\n]")

    print("Embeddings generated:", total)


if __name__ == "__main__":
    generate_embeddings(
        "knowledge_base/data/squad_chunks.json",
        "knowledge_base/data/squad_embeddings.json"
    )