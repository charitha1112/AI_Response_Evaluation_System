import json


def create_chunks(input_file, output_file,
                  chunk_size=500, overlap=50):

    with open(input_file, "r", encoding="utf-8") as file:
        records = json.load(file)

    chunks = []

    for record_id, record in enumerate(records):

        question = record.get("question", "")
        answer = record.get("answer", "")
        context = record.get("context", "")

        words = context.split()

        for start in range(0, len(words), chunk_size - overlap):

            chunk_words = words[start:start + chunk_size]

            if not chunk_words:
                continue

            text = (
                f"Question: {question}\n"
                f"Answer: {answer}\n"
                f"Context: {' '.join(chunk_words)}"
            )

            chunks.append({
                "record_id": record_id,
                "chunk_id": start // (chunk_size - overlap),
                "text": text
            })

            if start + chunk_size >= len(words):
                break

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(chunks, file, indent=2, ensure_ascii=False)

    print("Total question-aware chunks:", len(chunks))


if __name__ == "__main__":

    create_chunks(
        "knowledge_base/data/squad_clean.json",
        "knowledge_base/data/squad_chunks.json"
    )
    