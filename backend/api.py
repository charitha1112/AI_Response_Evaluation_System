from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from agents.orchestrator import run_evaluation

app = FastAPI(title="AI Response Evaluation API")


class EvaluationInput(BaseModel):
    question: str
    ai_response: str
    reference_answer: Optional[str] = None
    source: Optional[str] = None


@app.get("/")
def home():
    return {"message": "AI Response Evaluation API is running"}


@app.post("/evaluate")
def evaluate_response(data: EvaluationInput):

    result = run_evaluation(
        question=data.question,
        ai_response=data.ai_response,
        reference_answer=data.reference_answer,
        source=data.source
    )

    return {
        "message": "Evaluation completed successfully",
        "question": data.question,
        "ai_response": data.ai_response,
        "evaluation": result
    }