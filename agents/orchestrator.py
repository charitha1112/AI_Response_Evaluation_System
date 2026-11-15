from agents.relevance_agent import evaluate_relevance
from agents.accuracy_agent import evaluate_accuracy
from agents.hallucination_agent import evaluate_hallucination
from agents.completeness_agent import evaluate_completeness
from agents.verdict_agent import generate_verdict
from knowledge_base.retrieval import retrieve_context


def run_evaluation(question, ai_response, reference_answer=None, source=None):

    # Retrieve supporting context from ChromaDB
    retrieved_context = retrieve_context(question) or []
    retrieved_source = "\n\n".join(retrieved_context)

    # Use retrieved context when no reference answer is provided
    accuracy_reference = reference_answer or retrieved_source or None

    # Use retrieved context when no source is provided
    hallucination_source = source or retrieved_source or None

    results = {
        "relevance": evaluate_relevance(question, ai_response),

        "accuracy": evaluate_accuracy(
            ai_response, accuracy_reference
        ),

        "hallucination": evaluate_hallucination(
            ai_response, reference_answer, hallucination_source
        ),

        "completeness": evaluate_completeness(
            question, ai_response
        )
    }

    verdict = generate_verdict(results)

    return {
        "evaluation_results": results,
        "final_verdict": verdict
    }