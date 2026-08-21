# 010 Responsible AI — 수행형 연습

## 목표

Generative AI의 위험과 한계를 설명하고, Copilot Output을 책임감 있게 검증하는 판단력을 기릅니다.

## 연습문제 (Exercises, EXR)

### E010-01 — AI Output 검증
Copilot이 생성한 함수가 읽기 쉽고 문법 오류도 없습니다. 바로 Production에 반영하면 안 되는 이유를 **정확성·보안·요구사항·Test** 관점에서 4가지 작성하세요.

### E010-02 — Hallucination
Copilot이 존재하지 않는 Python API를 제안했습니다. 이것을 어떤 AI 한계로 분류하고 어떻게 확인할지 작성하세요.

### E010-03 — Bias
사용자 위험 등급을 분류하는 코드/규칙을 AI가 제안했습니다. Bias와 Fairness를 확인하기 위한 최소 검토 항목 5개를 작성하세요.

### E010-04 — Secure Code
AI가 입력 검증 없이 SQL 문자열을 조합하는 코드를 제안했습니다. 사람 Reviewer가 해야 할 행동을 순서대로 작성하세요.

### E010-05 — Privacy
Debugging을 위해 실제 고객 데이터 전체를 Prompt에 넣으려 합니다. 문제점과 더 안전한 대안을 작성하세요.

### E010-06 — Transparency
AI가 왜 특정 구현을 선택했는지 설명하도록 요구하는 것이 어떤 장점이 있는지, 그리고 설명만으로 검증이 끝나지 않는 이유를 적으세요.

### E010-07 — Human Accountability
`Copilot이 추천했기 때문에 책임은 AI에게 있다`는 주장에 반박하는 문장 3개를 작성하세요.

### E010-08 — Risk Mitigation
다음 위험별 완화책을 1개 이상 연결하세요.

| Risk | Mitigation |
|---|---|
| Hallucination | |
| Insecure code | |
| Privacy exposure | |
| Bias | |
| Outdated information | |

### E010-09 — Accept / Modify / Reject
Copilot 제안을 각각 `Accept`, `Modify`, `Reject`해야 할 예시를 하나씩 작성하고 판단 근거를 설명하세요.

### E010-10 — Responsible AI Checklist
본인이 실제 개발에 사용할 **10항목 Responsible AI Checklist**를 작성하세요.

## 자가 검증

- [ ] AI Output을 `정답`이 아니라 `제안`으로 설명한다.
- [ ] Bias / Fairness / Privacy / Security / Transparency 위험을 구분한다.
- [ ] 위험별 완화책을 제시한다.
- [ ] Human Review와 Test의 필요성을 설명한다.

## 관련 Lab

- [`090-responsible-ai-privacy`](../../060-labs/090-responsible-ai-privacy/)
- [`100-end-to-end-development`](../../060-labs/100-end-to-end-development/)

---
[← Exercises 홈](../README.md) · [020 Copilot Features →](../020-copilot-features/README.md)
