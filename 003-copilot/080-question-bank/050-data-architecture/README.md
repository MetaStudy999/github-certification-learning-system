# 050 데이터 와 아키텍처 — Q041–Q050 (050 Data & Architecture — Q041–Q050, DAQ041Q050)

> Skill Area: **Understand GitHub Copilot data and architecture**

## Q041

Copilot의 코드 제안 lifecycle을 개념적으로 가장 잘 나타낸 것은?

A. Suggestion → Prompt → Context → LLM  
B. Developer Input/Context → Prompt Building → Filtering/Proxy → LLM → Post-processing → Suggestion  
C. LLM → Git Commit → Audit Log → Prompt  
D. Repository → 자동 학습 → 항상 정답

<details><summary>정답</summary>

**B.** 최신 Study Guide는 Context 수집, Prompt 구성, Proxy/Filtering, LLM Response, Post-processing 흐름을 이해하도록 요구합니다.
</details>

## Q042

`사용자가 입력한 Chat 문장`과 `모델에 전달되는 전체 Prompt`의 관계를 가장 정확하게 설명한 것은?

A. 항상 완전히 동일하다.  
B. 서비스가 사용자 입력과 Context 등을 조합해 Prompt를 구성할 수 있다.  
C. 사용자의 입력은 전혀 사용되지 않는다.  
D. 전체 Repository가 항상 그대로 전달된다.

<details><summary>정답</summary>

**B.** Copilot은 사용자 입력 외에도 사용 가능한 Context를 활용해 Prompt를 구성합니다.
</details>

## Q043

Context Window의 한계가 의미하는 것은?

A. 모델이 무한한 모든 파일을 동시에 정확히 고려한다.  
B. 한 번에 고려할 수 있는 Context가 제한되므로 관련성 높은 정보 선택이 중요하다.  
C. Prompt를 쓸 수 없다.  
D. Copilot CLI만 사용할 수 있다.

<details><summary>정답</summary>

**B.** 제한된 Context 용량 때문에 관련성 높은 정보가 중요합니다.
</details>

## Q044

Proxy/Filtering 단계의 목적과 가장 가까운 것은?

A. Branch 이름을 자동 변경  
B. Prompt/Response를 서비스 정책과 보호 기준에 따라 처리  
C. 모든 Repository를 Public으로 전환  
D. Unit Test 삭제

<details><summary>정답</summary>

**B.** Filtering은 안전·정책·Matching 같은 처리 흐름과 연결됩니다.
</details>

## Q045

Post-processing을 이해하는 가장 적절한 설명은?

A. LLM 응답 후 추가 처리·검사 과정을 수행할 수 있다.  
B. Prompt를 작성하기 전 Git Commit을 만든다.  
C. Human Review를 영구 제거한다.  
D. 모든 Output을 동일하게 만든다.

<details><summary>정답</summary>

**A.** 모델 Response가 사용자에게 표시되기 전 서비스 수준의 추가 처리가 있을 수 있습니다.
</details>

## Q046

Copilot과 LLM의 한계로 가장 적절한 것은?

A. 항상 최신 Library API를 정확히 안다.  
B. 제한된 Context와 오래되거나 부정확한 패턴으로 인해 잘못된 제안을 할 수 있다.  
C. Bias가 절대 없다.  
D. 수학 계산은 항상 정확하다.

<details><summary>정답</summary>

**B.** 최신성, Context, Bias, Hallucination 등의 한계를 전제로 검증해야 합니다.
</details>

## Q047

관련 없는 대형 파일 여러 개를 Context에 추가했더니 답변 품질이 낮아졌다. 가장 타당한 설명은?

A. Context는 많을수록 항상 좋으므로 다른 원인이 있다.  
B. 불필요하거나 충돌하는 Context가 모델의 주의를 분산시킬 수 있다.  
C. Copilot은 파일 Context를 사용하지 않는다.  
D. 모든 파일이 자동 삭제된다.

<details><summary>정답</summary>

**B.** Context는 양보다 관련성과 명확성이 중요합니다.
</details>

## Q048

공개 코드와 일치하는 제안을 다루는 Matching 기능을 Data Flow에서 이해할 때 가장 적절한 것은?

A. 응답 처리·Safeguard의 일부로 볼 수 있다.  
B. Git Branch Merge 기능이다.  
C. Subscription 결제 방식이다.  
D. Test Framework다.

<details><summary>정답</summary>

**A.** 공개 코드 Matching은 제안 처리의 보호장치와 연결됩니다.
</details>

## Q049

Copilot의 데이터 처리 정책을 공부할 때 가장 안전한 접근은?

A. 오래된 블로그 하나만 암기한다.  
B. 현재 Plan과 기능의 공식 Documentation을 확인한다.  
C. 모든 Plan의 데이터 처리가 영원히 같다고 가정한다.  
D. 시험 Dump를 따른다.

<details><summary>정답</summary>

**B.** 제품·Plan 정책은 변할 수 있으므로 최신 공식 자료가 기준입니다.
</details>

## Q050

다음 중 Copilot Architecture 이해와 가장 거리가 먼 설명은?

A. Context Gathering  
B. Prompt Building  
C. LLM Response  
D. AI Output은 검증 없이 항상 Correct

<details><summary>정답</summary>

**D.** Architecture를 이해해도 Output 정확성은 자동 보장되지 않습니다.
</details>

---
[← 040 Organization & Governance](../040-org-feature-governance/README.md) · [060 Prompt & Context →](../060-prompt-context/README.md)
