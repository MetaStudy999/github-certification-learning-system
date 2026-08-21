# 120 Wrong Answers — GH-200 오답 시스템

## Error Codes

| 코드 | 의미 |
|---|---|
| CONCEPT | 개념 부족 |
| YAML | YAML 구조·문법 오류 |
| CONTEXT | Context / Expression 혼동 |
| REUSE | Reusable Workflow / Action 혼동 |
| RUNNER | Runner 운영 개념 혼동 |
| SECURITY | Permission / Secret / OIDC 오류 |
| TROUBLE | Log·실패 원인 분석 오류 |
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
