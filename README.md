AI Response Evaluation System

1. Project Overview

The AI Response Evaluation System is designed to evaluate AI-generated responses based on relevance, accuracy, hallucination indicators, and completeness.

It uses a modular architecture with multiple evaluation agents and a Retrieval-Augmented Generation (RAG) knowledge base.

2. Project Objectives

- Evaluate AI-generated responses automatically.
- Measure response relevance and accuracy.
- Identify potential hallucinations using available reference information.
- Assess response completeness.
- Retrieve relevant information from a knowledge base.
- Generate an overall evaluation score and verdict.

3. Technology Stack

Component| Technology
Programming Language| Python 3.11
Frontend| Streamlit
Backend| FastAPI
Data Validation| Pydantic
Vector Database| ChromaDB
Embeddings| ChromaDB Default Embedding Function
Datasets| TruthfulQA and SQuAD
Development Tool| Visual Studio Code
Version Control| Git and GitHub

4. System Modules

1. Evaluation Input Module: Accepts the question, AI response, optional reference answer, and source.
2. Relevance Agent: Evaluates the relationship between the question and response.
3. Accuracy Agent: Compares the response with the reference answer.
4. Hallucination Agent: Checks the response against available evidence.
5. Completeness Agent: Estimates response completeness.
6. Verdict Agent: Generates an overall evaluation verdict.
7. Orchestrator: Coordinates the evaluation agents.
8. Knowledge Base: Stores and retrieves relevant reference information.

5. Knowledge Base Pipeline

The knowledge base uses the following process:

1. Dataset loading.
2. Data preprocessing.
3. Text chunking.
4. Embedding generation.
5. Vector database storage.
6. Semantic retrieval.

Datasets used:

- TruthfulQA
- SQuAD

6. Project Architecture

The system follows a modular architecture:

User Input → Streamlit Frontend → FastAPI Backend → Evaluation Orchestrator → Evaluation Agents → Evaluation Results

The knowledge base provides relevant reference context through semantic retrieval.

7. Project Folder Structure

AI RESPONSE/
├── frontend/
│   └── app.py
├── backend/
│   └── api.py
├── agents/
│   ├── orchestrator.py
│   ├── relevance_agent.py
│   ├── accuracy_agent.py
│   ├── hallucination_agent.py
│   ├── completeness_agent.py
│   └── verdict_agent.py
├── knowledge_base/
│   ├── dataset_loader.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   └── data/
├── docs/
├── requirements.txt
└── README.md

8. Installation and Execution

Install dependencies:

pip install -r requirements.txt

Start the backend:

uvicorn backend.api:app --reload

Start the frontend in another terminal:

streamlit run frontend/app.py

9. Evaluation Techniques Studied

- Retrieval-Augmented Generation (RAG)
- RAGAS
- TruLens
- Hallucination detection methods
- LLM evaluation techniques

RAGAS and TruLens were studied as evaluation frameworks; they are not claimed as integrated components.

10. Implementation Status

### Implementation Status

The following components have been implemented:

**Evaluation Modules**
- Evaluation Input Module
- Relevance, Accuracy, Hallucination and Completeness Agents
- Verdict Generation Agent
- Evaluation Orchestrator

**Knowledge Base Development**
- TruthfulQA and SQuAD dataset preprocessing
- Text chunking and embedding generation
- ChromaDB vector storage
- Technical documentation knowledge base
- Semantic retrieval from multiple collections

**System Integration and Testing**
- ChromaDB retrieval integrated with the evaluation orchestrator
- Retrieved evidence used by Accuracy and Hallucination Agents when manual evidence is unavailable
- Basic evaluation and retrieval testing completed
-


11. Expected Outcome

The system aims to provide structured evaluation results that help assess the quality and reliability of AI-generated responses.
# Milestone 2 – AI Response Evaluation

## Overview

Milestone 2 enhances the AI Response Evaluation System using a multi-agent evaluation approach powered by the Gemini API.

## Implemented Features

- Semantic evaluation using Gemini API.
- Relevance Agent for checking question-response relevance.
- Accuracy Agent for evaluating factual correctness.
- Hallucination Agent for detecting unsupported claims.
- Completeness Agent for checking missing information.
- Orchestrator for coordinating evaluation agents.
- Weighted scoring mechanism.
- Final verdict generation.
- Knowledge retrieval using ChromaDB.
- Evaluation with or without a reference answer.
- Support for short and one-word answers.

## Evaluation Metrics

| Agent | Weight |
|---|---:|
| Relevance | 25% |
| Accuracy | 35% |
| Hallucination | 25% |
| Completeness | 15% |

## Testing

The system was tested using different response scenarios:

1. Correct answers.
2. Partially correct answers.
3. Incorrect answers.
4. Irrelevant answers.
5. Unsupported claims.
6. Evaluation without reference answers.
7. One-word answers.

## Technologies Used

- Python
- Streamlit
- FastAPI
- Gemini API
- ChromaDB
- Pydantic

## Result

The system generates individual agent scores, evaluation reasoning, supporting evidence when available, and an overall weighted evaluation score.