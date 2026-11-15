def generate_verdict(results):
    scores = [
        result["score"]
        for result in results.values()
        if result["score"] is not None
    ]

    if not scores:
        return {
            "overall_score": None,
            "verdict": "Insufficient information"
        }

    overall_score = round(sum(scores) / len(scores), 2)

    if overall_score >= 8:
        verdict = "Good"
    elif overall_score >= 5:
        verdict = "Needs Improvement"
    else:
        verdict = "Poor"

    return {
        "overall_score": overall_score,
        "verdict": verdict
    }