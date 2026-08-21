# 120 Wrong Answers — GH-300 오답 시스템

## 목적

오답을 `정답 B`로 외우지 않습니다.

```text
왜 틀렸나?
→ 어떤 개념을 혼동했나?
→ 최신 공식 범위에서 무엇을 확인해야 하나?
→ 어떤 Lab을 다시 해야 하나?
→ +1일 / +7일 재시험에서 다시 맞히는가?
```

## Error Codes

| 코드 | 의미 | 대표 예시 |
|---|---|---|
| RAI | Responsible AI 오류 | Validation 필요성 놓침 |
| FEATURE | IDE/CLI/제품 기능 혼동 | Chat vs Edits |
| AGENT | Agent/MCP/Sub-Agent 혼동 | MCP를 Agent 자체로 오해 |
| ORG | Policy/Audit/Organization 기능 혼동 | Audit Log 목적 혼동 |
| ARCH | Data Flow/Architecture 오류 | Prompt Building 순서 혼동 |
| CONTEXT | Context 선택 오류 | 무관 Context를 많이 제공 |
| PROMPT | Prompt Engineering 오류 | Constraint/Verification 누락 |
| USECASE | Developer Use Case 오류 | Refactor vs Generate 혼동 |
| TEST | Testing 오류 | Unit/Integration/Edge Case 혼동 |
| PRIVACY | Privacy/Exclusion 오류 | Exclusion을 Secret 관리로 오해 |
| SAFEGUARD | Filter/Ownership/Safeguard 오류 | Public code filter 과신 |
| READING | 문제 조건 해석 실패 | `FIRST`, `BEST` 놓침 |
| STALE | 오래된 시험 범위/제품 정보 | 이전 7 Domain 비중 암기 |

## 한 문제 처리 Template

[`010-error-log-template.md`](./010-error-log-template.md)를 복사해서 사용합니다.

```text
ID:
Source: QBank / Mock 01 / Mock 02 / Final
Skill area:
Question summary:
My answer:
Correct answer:
Confidence: HIGH / MEDIUM / LOW
Error code:
Why wrong:
Correct concept in one sentence:
Why alternatives are less appropriate:
Official source checked:
Related exercise:
Related lab:
+1 day retry:
+7 day retry:
```

## Retry Cycle

```text
오답 발생
  ↓
Error Code 지정
  ↓
정답 근거를 1문장으로 재정의
  ↓
공식 Study Guide / Docs 확인
  ↓
Exercise 또는 Lab 재수행
  ↓
+1일 재시험
  ↓
+7일 재시험
  ↓
90%+ 유지
```

## Priority Rule

먼저 고칠 오답:

1. 같은 개념을 2회 이상 틀림
2. **Copilot Features 25–30%** 고비중 영역 오류
3. Responsible AI 오류
4. Agent / MCP / CLI 등 2026 개정 핵심 기능 오류
5. Privacy / Safeguard 오류
6. `FIRST / BEST` Reading 오류
7. 단순 Memory 오류

## Confidence Error

정답을 맞혔더라도 근거를 설명하지 못했다면 `UNCERTAIN`으로 기록합니다.

```text
Correct + no reasoning
→ Lucky guess 가능성
→ Retry Queue에 추가
```

## Exam Gate

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

- [ ] +1일 Queue 90%+
- [ ] +7일 Queue 90%+
- [ ] 반복 오류 0개 또는 설명 가능
- [ ] STALE 오류 없음

---
[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
