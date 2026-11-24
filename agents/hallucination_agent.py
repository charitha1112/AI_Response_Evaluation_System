from agents.gemini_judge import evaluate_with_gemini


def evaluate_hallucination(ai_response, reference_answer=None, source=None):

    evidence = reference_answer or source

    prompt = f"""
You are an expert hallucination detection evaluator.

Your task is to identify factual claims in the AI response that are unsupported or contradicted by the available evidence.

AI RESPONSE:
{ai_response}

REFERENCE OR SOURCE EVIDENCE:
{evidence if evidence else "No reliable evidence provided."}

RULES:
1. Identify factual claims, not opinions or writing style.
2. Compare each factual claim with the supplied evidence.
3. A claim that contradicts the evidence is a serious hallucination.
4. A claim that is not supported by the evidence should be treated as unverified, not automatically false.
5. Do not invent supporting evidence.
6. If no evidence is available, clearly state that hallucination detection is limited.
7. Do not confuse missing information with hallucination.

SCORING:
10: No unsupported or contradictory claims found.
8–9: Mostly supported; minor uncertainty.
6–7: Some claims cannot be verified.
3–5: Several unsupported claims.
1–2: Major unsupported or contradictory claims.
0: Entire response is fabricated or directly contradicts the evidence.

IMPORTANT:
A higher score means fewer hallucinations.
"""

    return evaluate_with_gemini(prompt)