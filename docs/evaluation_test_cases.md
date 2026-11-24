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

# MILESTONE 2 – BENCHMARK EVALUATION RESULTS

## 1. Objective

To evaluate the performance of the AI Response Evaluation System using different types of responses and verify the behaviour of its evaluation agents.

## 2. Benchmark Test Results

| Test | Test Scenario | Final Score |
|:---:|---|:---:|
| 1 | Correct Answer | 10.00/10 |
| 2 | Partially Correct Answer | 8.60/10 |
| 3 | Incorrect Answer | 4.00/10 |
| 4 | Irrelevant Answer | 2.50/10 |
| 5 | Unsupported Claims | 5.75/10 |
| 6 | Without Reference Answer | 9.85/10 |
| 7 | One-Word Correct Answer | 10.00/10 |

## 3. Individual Agent Results – Test 5

| Evaluation Agent | Score |
|---|:---:|
| Relevance | 10/10 |
| Accuracy | 5/10 |
| Hallucination | 0/10 |
| Completeness | 10/10 |

## 4. Key Observations

1. Correct answers receive high evaluation scores.
2. Partially correct answers receive moderate scores.
3. Incorrect and irrelevant answers receive lower scores.
4. Unsupported claims are penalized by the Hallucination Agent.
5. The system supports evaluation without a manually entered reference answer.
6. Correct one-word answers can receive full marks.
7. The system generates individual agent scores and a weighted final score.

## 5. Conclusion

The benchmark tests demonstrate that the AI Response Evaluation System can evaluate different types of responses, including correct, partially correct, incorrect, irrelevant, and unsupported responses. It also supports evaluation without a manually supplied reference answer and handles short answers.