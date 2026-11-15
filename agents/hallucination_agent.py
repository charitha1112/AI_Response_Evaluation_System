def evaluate_hallucination(ai_response, reference_answer=None, source=None):
    evidence = reference_answer or source

    if not evidence or not evidence.strip():
        return {
            "score": None,
            "explanation": "Cannot assess unsupported claims because no reference answer or source was provided."
        }

    response_words = set(ai_response.lower().split())
    evidence_words = set(evidence.lower().split())

    if not response_words:
        support_ratio = 0
    else:
        matched = response_words.intersection(evidence_words)
        support_ratio = len(matched) / len(response_words)

    score = round(support_ratio * 10, 2)

    return {
        "score": score,
        "explanation": (
            "Basic evidence-word overlap score. "
            "A low score may indicate unsupported content, "
            "but this is not definitive hallucination detection."
        )
    }