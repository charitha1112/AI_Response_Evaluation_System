from agents.gemini_judge import evaluate_all
from agents.verdict_agent import generate_verdict

from knowledge_base.retrieval import retrieve_context


def extract_context(retrieved_context):

    if not retrieved_context:
        return ""

    if isinstance(retrieved_context, str):
        return retrieved_context

    if isinstance(retrieved_context, dict):

        documents = retrieved_context.get("documents", [])

        if documents and isinstance(documents[0], list):
            documents = documents[0]

        return "\n".join(str(doc) for doc in documents if doc)

    if isinstance(retrieved_context, (list, tuple)):

        parts = []

        for item in retrieved_context:

            if isinstance(item, dict):
                content = (
                    item.get("text")
                    or item.get("document")
                    or item.get("content")
                    or item.get("page_content")
                )

                if content:
                    parts.append(str(content))

            else:
                parts.append(str(item))

        return "\n".join(parts)

    return str(retrieved_context)


def run_evaluation(
    question,
    ai_response,
    reference_answer=None,
    source=None
):

    # Prioritize user-provided evidence.
    evidence = reference_answer or source

    # Use the knowledge base when no evidence is supplied.
    if not evidence:
        retrieved_context = retrieve_context(question)
        evidence = extract_context(retrieved_context)

    evidence = str(evidence).strip() if evidence else None

    # ONE Gemini call evaluates all four criteria.
    evaluation_results = evaluate_all(
        question=question,
        ai_response=ai_response,
        evidence=evidence
    )

    # Calculate final weighted score locally.
    final_verdict = generate_verdict(evaluation_results)

    return {
        "evaluation_results": evaluation_results,
        "final_verdict": final_verdict
    }