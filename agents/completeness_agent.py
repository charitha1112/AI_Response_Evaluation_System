def evaluate_completeness(question, ai_response):
    if not ai_response.strip():
        score = 0
        explanation = "The response is empty."
    else:
        word_count = len(ai_response.split())

        if word_count < 10:
            score = 3
        elif word_count < 30:
            score = 6
        else:
            score = 8

        explanation = (
            f"The response contains {word_count} words. "
            "This is a basic length-based completeness estimate."
        )

    return {
        "score": score,
        "explanation": explanation
    }