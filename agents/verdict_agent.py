def generate_verdict(results):

    weights = {
        "relevance": 0.25,
        "accuracy": 0.35,
        "hallucination": 0.25,
        "completeness": 0.15
    }

    scores = {}

    for agent, weight in weights.items():
        score = float(results[agent]["score"])
        scores[agent] = max(0.0, min(10.0, score))

    final_score = sum(
        scores[agent] * weight
        for agent, weight in weights.items()
    )

    if final_score >= 9:
        grade = "Excellent"
        status = "Highly Reliable"

    elif final_score >= 7:
        grade = "Good"
        status = "Mostly Reliable"

    elif final_score >= 5:
        grade = "Average"
        status = "Needs Improvement"

    elif final_score >= 3:
        grade = "Poor"
        status = "Unreliable"

    else:
        grade = "Very Poor"
        status = "Highly Unreliable"

    return {
        "final_score": round(final_score, 2),
        "grade": grade,
        "status": status,
        "agent_scores": scores,
        "reasoning": (
            "Weighted evaluation: Relevance 25%, Accuracy 35%, "
            "Hallucination 25%, Completeness 15%."
        )
    }