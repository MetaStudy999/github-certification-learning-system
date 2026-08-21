# 050 Developer Productivity — 수행형 연습

## 목표

Copilot을 Code Generation에만 한정하지 않고 **Refactoring, Documentation, Testing, Debugging, Security, Performance**까지 SDLC 전반에 적용하되 결과를 검증합니다.

## 연습문제 (Exercises, EXR)

### E050-01 — Code Generation
작은 기능 요구사항을 작성하고 Copilot에 구현을 요청합니다. 생성 코드에서 `요구사항 충족 / Error Handling / Testability / Security`를 각각 확인하세요.

### E050-02 — Learning
익숙하지 않은 Framework API를 Copilot으로 학습한다고 가정합니다. AI 설명을 공식 문서와 교차 확인해야 하는 이유를 작성하세요.

### E050-03 — Refactoring
동작은 유지하면서 복잡한 함수의 구조를 개선하는 Prompt를 작성하세요. `Public API 유지`와 `기존 Test 통과` 조건을 포함합니다.

### E050-04 — Documentation
함수 Docstring 또는 README 초안을 Copilot에 요청한 뒤, 실제 코드와 다른 설명이 있는지 검증하는 절차를 적으세요.

### E050-05 — Legacy Modernization
오래된 Library 사용 코드를 현대화할 때 확인해야 할 호환성·Test·Deprecation 항목을 5개 작성하세요.

### E050-06 — Unit Test
Copilot이 만든 Unit Test에서 `Happy Path`만 있는 경우 추가해야 할 Edge Case 5개를 설계하세요.

### E050-07 — Integration Test
Unit Test와 Integration Test의 목적 차이를 설명하고 Copilot에 각각 어떤 Context를 제공할지 적으세요.

### E050-08 — Assertion Quality
다음 Test가 단순히 `에러가 안 난다`만 확인한다고 가정합니다. 더 강한 Assertion이 필요한 이유를 설명하세요.

### E050-09 — Security Suggestion
Copilot에 코드의 잠재 보안 문제를 찾아 달라고 요청하는 Prompt를 작성합니다. 결과를 Security Scanner 또는 수동 Review로 추가 검증해야 하는 이유를 적으세요.

### E050-10 — Performance Optimization
AI가 `더 빠르다`고 주장하는 Refactor를 제안했습니다. Benchmark와 정확성 Test를 통해 검증하는 절차를 작성하세요.

## 자가 검증

- [ ] Code Generation과 Verification을 분리한다.
- [ ] Refactoring은 동작 보존을 Test로 확인한다.
- [ ] Unit / Integration Test 목적을 구분한다.
- [ ] Edge Case와 Assertion 품질을 검토한다.
- [ ] Security/Performance 제안을 실제 도구·Test로 검증한다.

## 관련 Lab

- [`040-code-generation`](../../060-labs/040-code-generation/)
- [`050-explanation-documentation`](../../060-labs/050-explanation-documentation/)
- [`060-testing`](../../060-labs/060-testing/)
- [`070-debugging`](../../060-labs/070-debugging/)
- [`080-refactoring`](../../060-labs/080-refactoring/)

---
[← 040 Prompt & Context](../040-prompt-context/README.md) · [060 Privacy & Safeguards →](../060-privacy-safeguards/README.md)
