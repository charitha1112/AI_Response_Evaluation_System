import re


def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))


def evaluate_relevance(question, ai_response):
    question_words = tokenize(question)
    response_words = tokenize(ai_response)

    if not question_words or not response_words:
        score = 0
    else:
        matched_words = question_words.intersection(response_words)
        score = round(
            (len(matched_words) / len(question_words)) * 10, 2
        )

    return {
        "score": score,
        "explanation": (
            "Measures keyword overlap between the question and AI response. "
            "This is a basic baseline, not a full semantic relevance judgment."
        )
    }