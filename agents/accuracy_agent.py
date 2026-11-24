from agents.gemini_judge import evaluate_with_gemini


def evaluate_accuracy(ai_response, evidence=None):

    prompt = f"""
You are an expert factual accuracy evaluator.

Evaluate whether the AI response contains factually correct information.

AI RESPONSE:
{ai_response}

REFERENCE ANSWER OR RETRIEVED EVIDENCE:
{evidence if evidence else "No reference evidence available."}

RULES:
1. Compare factual claims against the supplied reference or evidence.
2. If the answer is fully correct and supported, award a high score.
3. If it is partially correct, award a proportional score.
4. If it is incorrect or contradicts the evidence, award a low score.
5. Do not confuse relevance with accuracy.
6. Do not reward an answer merely because it sounds confident.
7. If no reliable evidence is available, explain that accuracy cannot be verified. Do not invent facts or claim certainty.

SCORING:
9–10: Fully correct and supported.
7–8: Mostly correct with minor errors.
5–6: Partially correct; some important information is missing.
3–4: Major factual errors.
1–2: Mostly incorrect.
0: Completely incorrect or directly contradicts the reference.

Evaluate the facts, not the answer length.
"""

    return evaluate_with_gemini(prompt)