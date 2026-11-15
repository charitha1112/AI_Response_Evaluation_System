AI Response Evaluation System

Technology Stack

1. Programming Language

Python 3.11

Used for application development, evaluation agents, data processing, and embedding generation.

2. Frontend

Streamlit

- Provides the user interface.
- Accepts questions, AI responses, and optional reference information.
- Displays evaluation results.

3. Backend

FastAPI

- Handles frontend requests.
- Validates input.
- Connects the frontend with evaluation agents.
- Returns results in JSON format.

4. Data Validation


### Pydantic – Data Validation

| Field | Data Type | Description |
|---|---|---|
| question | String | User's question |
| ai_response | String | AI-generated response |
| reference_answer | Optional String | Reference answer for comparison |
| source | Optional String | Supporting source information |
5. Evaluation Modules

| Module | Purpose |
|---|---|
| Relevance Agent | Measures keyword overlap |
| Accuracy Agent | Compares with reference answer |
| Hallucination Agent | Estimates evidence overlap |
| Completeness Agent | Estimates response completeness |
| Verdict Agent | Calculates overall score |
| Orchestrator | Coordinates all agents |

6. Datasets

| Dataset | Purpose |
|---|---|
| TruthfulQA | Truthfulness evaluation research |
| SQuAD | Question-answer-context knowledge base |

7. Embedding and Vector Database

| Technology | Purpose |
|---|---|
| Sentence Transformers | Generates text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Stores embeddings and supports semantic search |

8. Development Tools

| Tool | Purpose |
|---|---|
| Visual Studio Code | Code development |
| Git | Version control |
| GitHub | Source-code hosting |
| Virtual Environment | Dependency isolation |
| pip | Package installation |

9. Evaluation Frameworks Studied

- RAG: Retrieval-Augmented Generation architecture.
- RAGAS: Framework studied for RAG evaluation.
- TruLens: Framework studied for AI application evaluation.

RAGAS and TruLens are studied but not integrated into the current implementation.

10. Main Python Dependencies

- streamlit
- fastapi
- uvicorn
- pydantic
- pandas
- requests
- sentence-transformers
- chromadb

11. Conclusion

The project uses Python, Streamlit, and FastAPI for application development, custom evaluation agents for response assessment, and Sentence Transformers with ChromaDB for the knowledge-base retrieval pipeline.