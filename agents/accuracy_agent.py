def evaluate_accuracy(ai_response, reference_answer=None):
    if not reference_answer or not reference_answer.strip():
        return {
            "score": None,
            "explanation": "Accuracy cannot be compared because no reference answer was provided."
        }

    response_words = set(ai_response.lower().split())
    reference_words = set(reference_answer.lower().split())

    if not reference_words:
        score = 0
    else:
        matched = response_words.intersection(reference_words)
        score = round((len(matched) / len(reference_words)) * 10, 2)

    return {
        "score": score,
        "explanation": "Basic word-overlap comparison with the reference answer. This is not a verified factuality score."
    }