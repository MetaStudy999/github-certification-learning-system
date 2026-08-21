# 120 Wrong Answers — GH-300 오답 시스템

## Error Codes

| 코드 | 의미 |
|---|---|
| FEATURE | 제품 기능·Plan 혼동 |
| CONTEXT | Context / Data Flow 혼동 |
| PROMPT | Prompt Engineering 오류 |
| USECASE | 개발 Use Case 선택 오류 |
| TEST | Testing 개념 오류 |
| RAI | Responsible AI 오류 |
| PRIVACY | Privacy / Exclusion 오류 |
| READING | 문제 조건 해석 실패 |

## Template

```text
ID:
Domain:
Question summary:
My answer:
Correct answer:
Error code:
Why wrong:
Correct concept in one sentence:
Why alternatives are less appropriate:
Related official docs:
Related Lab:
+1 day retry:
+7 day retry:
```

## Retry Cycle

```text
오답
→ 원인 코드
→ 개념 1문장
→ 공식문서
→ 관련 Lab
→ +1일 재시험
→ +7일 재시험
```

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

---
[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
