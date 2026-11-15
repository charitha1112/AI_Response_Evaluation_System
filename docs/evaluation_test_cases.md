# Evaluation Test Cases

## Test 1: Incorrect Answer
Question: What is the capital of India?

AI Response: The capital of India is Mumbai.

Reference Answer: The capital of India is New Delhi.

Results:
- Relevance: 8.33
- Accuracy: 5.71
- Hallucination: 6.67
- Completeness: 3

## Test 2: Correct Answer
Question: What is the capital of India?

AI Response: The capital of India is New Delhi, which is the seat of the Indian government.

Reference Answer: The capital of India is New Delhi.

Results:
- Relevance: 8.83
- Accuracy: 8.57
- Hallucination: 5.45
- Completeness: 6

## Test 3: Missing Reference
Question: What is Artificial Intelligence?

AI Response: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.

Reference Answer: Not provided.

Results:
- Relevance: 8.33
- Accuracy: null
- Hallucination: null
- Completeness: 6

## Conclusion
The system successfully processes different input scenarios.
Accuracy and hallucination scores currently use basic word-overlap methods and require further improvement.