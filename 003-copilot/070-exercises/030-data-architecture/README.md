# 030 Data & Architecture — 수행형 연습

## 목표

Copilot이 Context를 수집하고 Prompt를 구성한 뒤 모델 응답을 처리하는 **개념적 Data Flow**를 이해합니다.

## 연습문제 (Exercises, EXR)

### E030-01 — Data Flow 정렬
다음 항목을 일반적인 개념 흐름으로 정렬하세요.

```text
LLM Response
Context Gathering
Post-processing
Prompt Building
Developer Input
Filtering / Proxy
Suggestion Display
```

### E030-02 — Context Gathering
IDE에서 Copilot이 유용한 응답을 만들기 위해 참고할 수 있는 Context의 예를 5개 작성하고, 불필요한 Context가 왜 문제가 될 수 있는지 설명하세요.

### E030-03 — Prompt Building
`사용자가 입력한 문장 = 모델에 전달되는 전체 Prompt`라고 단정하면 왜 부정확한지 설명하세요.

### E030-04 — Proxy / Filtering
Prompt 또는 Response가 서비스 계층에서 Filtering을 거칠 수 있는 이유를 안전·정책·공개 코드 일치 관점에서 설명하세요.

### E030-05 — Post-processing
LLM이 Response를 생성한 직후 곧바로 정답으로 확정되지 않는 이유를 적고 Post-processing의 목적을 설명하세요.

### E030-06 — Matching Public Code
공개 코드와 일치하는 제안을 다루는 Safeguard가 왜 필요한지 작성하세요.

### E030-07 — Context Window
Context Window가 제한되어 있을 때 지나치게 많은 파일을 제공하는 것이 왜 도움이 되지 않을 수 있는지 설명하세요.

### E030-08 — LLM Limitations
다음 각각에 대해 실제 개발 시 나타날 수 있는 예시를 하나씩 작성하세요.

- Hallucination
- Outdated knowledge
- Limited context
- Pattern bias
- Weak calculation/reasoning reliability

### E030-09 — Data Handling
개인용/조직용 Plan이나 기능에 따라 데이터 처리 정책이 달라질 수 있습니다. 시험 직전 어떤 공식 자료를 확인해야 하는지 기록하세요.

### E030-10 — Architecture 설명
기술 비전공자에게 Copilot의 Data Flow를 5문장 이내로 설명하세요. 단, `AI가 모든 Repository 파일을 무조건 학습한다` 같은 과도한 단순화를 피하세요.

## 자가 검증

- [ ] Context Gathering → Prompt Building → Filtering → LLM → Post-processing 흐름 설명
- [ ] 사용자 Prompt와 모델에 전달되는 전체 Context를 구분
- [ ] Context Window와 관련성의 중요성 설명
- [ ] LLM/Copilot 한계를 실제 사례로 설명

## 관련 Lab

- [`030-context-engineering`](../../060-labs/030-context-engineering/)
- [`090-responsible-ai-privacy`](../../060-labs/090-responsible-ai-privacy/)

---
[← 020 Copilot Features](../020-copilot-features/README.md) · [040 Prompt & Context →](../040-prompt-context/README.md)
