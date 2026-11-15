import json
import os
import re


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def preprocess_truthfulqa(input_file, output_file):
    records = []

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)

            records.append({
                "question": clean_text(data.get("question", "")),
                "best_answer": clean_text(data.get("best_answer", "")),
                "category": clean_text(data.get("category", ""))
            })

    save_records(records, output_file)
    return len(records)


def preprocess_squad(input_file, output_file):
    records = []

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)

            records.append({
                "question": clean_text(data.get("question", "")),
                "context": clean_text(data.get("context", "")),
                "answer": clean_text(
                    data.get("answers", {}).get("text", [""])[0]
                )
            })

    save_records(records, output_file)
    return len(records)


def save_records(records, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    truthfulqa_count = preprocess_truthfulqa(
        "knowledge_base/data/truthfulqa.jsonl",
        "knowledge_base/data/truthfulqa_clean.json"
    )

    squad_count = preprocess_squad(
        "knowledge_base/data/squad.jsonl",
        "knowledge_base/data/squad_clean.json"
    )

    print("Preprocessing completed!")
    print("TruthfulQA:", truthfulqa_count)
    print("SQuAD:", squad_count)