import requests
import json
import os
import time


def load_all_records(dataset, config, split, filename):
    print(f"\nLoading {dataset}...")

    url = "https://datasets-server.huggingface.co/rows"
    batch_size = 100

    os.makedirs("knowledge_base/data", exist_ok=True)
    file_path = os.path.join("knowledge_base/data", filename)

    # Resume from records already saved
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            offset = sum(1 for line in f if line.strip())
    else:
        offset = 0

    total_records = offset
    print(f"Resuming from record: {offset}")

    with open(file_path, "a", encoding="utf-8") as file:
        while True:
            params = {
                "dataset": dataset,
                "config": config,
                "split": split,
                "offset": offset,
                "length": batch_size
            }

            try:
                response = requests.get(
                    url, params=params, timeout=60
                )

                if response.status_code == 429:
                    print("Rate limit reached. Waiting 60 seconds...")
                    time.sleep(60)
                    continue

                response.raise_for_status()
                rows = response.json().get("rows", [])

            except requests.RequestException as error:
                print("Request failed:", error)
                print("Waiting 30 seconds before retry...")
                time.sleep(30)
                continue

            if not rows:
                break

            for item in rows:
                json.dump(item["row"], file, ensure_ascii=False)
                file.write("\n")

            count = len(rows)
            total_records += count
            offset += count

            file.flush()
            print(f"Downloaded {total_records} records...")

            if count < batch_size:
                break

            time.sleep(3)

    print(f"Completed: {total_records} records saved.")
    return total_records

def load_truthfulqa():
    return load_all_records(
        "truthfulqa/truthful_qa",
        "generation",
        "validation",
        "truthfulqa.jsonl"
    )


def load_squad():
    return load_all_records(
        "rajpurkar/squad",
        "plain_text",
        "train",
        "squad.jsonl"
    )


if __name__ == "__main__":
    truthfulqa_count = load_truthfulqa()
    squad_count = load_squad()

    print("\nAll dataset downloads completed!")
    print("TruthfulQA records:", truthfulqa_count)
    print("SQuAD records:", squad_count)