## GSM8K 정답률

|                | Direct Prompting | CoT Prompting | My Prompting |
|----------------|------------------|----------------|---------------|
| **0-shot**     | 0.2              | 0.58           | 0.68          |
| **3-shot**     | 0.2              | 0.68           | 0.74          |
| **5-shot**     | 0.2              | 0.5            | 0.70           |


## CoT Prompting이 Direct Prompting에 비해 왜 좋은지
Direct Prompting은 문제에 대한 정답만을 요구하는 반면, Chain-of-Thought (CoT) Prompting은 단계적인 추론을 유도하여 모델이 중간 사고 과정을 거치도록 한다.
그 결과로 계산 오류나 논리 비약이 줄어들고, 수학과 같은 논리적인 문제들을 훨씬 더 잘 해결하는 것을 확인할 수 있다.[1]


## My Prompting이 CoT Prompting에 비해 왜 좋은지

기존 CoT는 “step-by-step rationale“을 제시하라고 요구하면서 자연스러운 사고 전개를 유도하지만,
My Prompting은 이를 명시적으로 “Let's break this into parts step-by-step”이라고 명시적으로 유도하면서 작은 문제들로 나누도록 유도한다.[2]
또한 My Prompting은 정답을 낸 후 검산을 명시적으로 요구한다. 이 과정은 Self-verification의 과정으로 모델은 최종 정답을 다시 계산하며 중간 실수나 비약을 알아낼 수 있게 된다.[3] 

## 추후 개선 방안

CoT Prompting의 기본 구조 위에 Self-Consistency (SC) 기법을 결합한다면 더 나은 결과를 내놓을 수 있다. [4] 다양한 예제를 포함하여 프롬프트의 사고 다양성(variety)을 의도적으로 높이고, 그 중 다수결 혹은 안정적 패턴을 유도하여 더 일관된 정답에 도달하게 할 수 있다. 이번 과제에서는 LLM 사용 Limit으로 해보지 못했지만 사용한다면 좋은 결과를 보여줄 것으로 예상된다.


## 참고문헌

[1] Wei et al., 2022. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)  
[2] Nye et al., 2021. *Show Your Work: Scratchpads for Intermediate Computation in Language Models*. [arXiv:2112.00114](https://arxiv.org/abs/2112.00114)  
[3] Cobbe et al., 2021. *Training Verifiers to Solve Math Word Problems*. [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)  
[4] Wang et al., 2022. *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)