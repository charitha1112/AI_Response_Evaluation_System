import chromadb
import re
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "technical_docs"
DB_DIR = BASE_DIR / "chroma_db"
 # Collection name
COLLECTION_NAME = "technical_reference_knowledge"

# Chunk settings
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50




def create_chunks(text):
    """Split text into chunks while preserving complete sentences."""

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if not sentence:
            continue

        if len(current_chunk) + len(sentence) + 1 <= CHUNK_SIZE:
            current_chunk = (current_chunk + " " + sentence).strip()
        else:
            if current_chunk:
                chunks.append(current_chunk)

            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def ingest_documents():

    print("Connecting to ChromaDB...")

    client = chromadb.PersistentClient(
        path=str(DB_DIR)
    )

    embedding_function = DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"}
    )

    print("Reading technical documents...")

    files = list(DOCS_DIR.glob("*.txt"))

    if not files:
        print("No text files found!")
        return

    total_chunks = 0

    for file_path in files:

        text = file_path.read_text(encoding="utf-8")

        chunks = create_chunks(text)

        ids = [
            f"{file_path.stem}_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                "source_file": file_path.name,
                "chunk_number": i,
                "document_type": "technical_reference"
            }
            for i in range(len(chunks))
        ]

        if chunks:
            collection.upsert(
                ids=ids,
                documents=chunks,
                metadatas=metadatas
            )

        total_chunks += len(chunks)

        print(
            f"{file_path.name}: {len(chunks)} chunks added"
        )

    print("\nIngestion completed!")
    print("Total documents:", len(files))
    print("Total chunks processed:", total_chunks)
    print("Database records:", collection.count())


if __name__ == "__main__":
    ingest_documents()