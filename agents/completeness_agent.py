from agents.gemini_judge import evaluate_with_gemini


def evaluate_completeness(question, ai_response, evidence=None):

    prompt = f"""
You are an expert answer-completeness evaluator.

Determine whether the AI response includes the important information needed to answer the question.

QUESTION:
{question}

AI RESPONSE:
{ai_response}

REFERENCE OR RETRIEVED CONTEXT:
{evidence if evidence else "No reference context available."}

RULES:
1. Identify the main points required to answer the question.
2. Check which important points are covered and which are missing.
3. Do not penalize a short answer if it covers everything necessary.
4. Do not reward unnecessary extra information.
5. Distinguish missing details from factual errors.
6. Use the reference when available, but do not require irrelevant details from it.
7. Explain missing information clearly.

SCORING:
9–10: Covers all or nearly all important points.
7–8: Covers the main points with minor omissions.
5–6: Covers some important points but misses significant details.
3–4: Incomplete answer with major omissions.
1–2: Very little of the required information is included.
0: Does not provide meaningful information.

Evaluate completeness, not factual accuracy or writing length.
"""

    return evaluate_with_gemini(prompt)