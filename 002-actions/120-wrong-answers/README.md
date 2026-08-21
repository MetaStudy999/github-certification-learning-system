# 120 Wrong Answers — GH-200 오답 시스템

## 빠른 시작 (Quick Start, QS)

오답을 정답 암기로 끝내지 않고 **원인 → 개념 → 공식문서 → Lab → 재시험**으로 연결합니다.

- [010 Error Log Template](./010-error-log-template.md)
- [020 Retry Queue](./020-retry-queue.md)

## 오류 Codes (Error Codes, EC)

| 코드 | 의미 |
|---|---|
| CONCEPT | 개념 부족 |
| YAML | YAML 구조·문법 오류 |
| CONTEXT | Context / Expression 혼동 |
| REUSE | Reusable Workflow / Action 혼동 |
| RUNNER | Runner 운영 개념 혼동 |
| SECURITY | Permission / Secret / OIDC / Pinning 오류 |
| TROUBLE | Log·실패 원인 분석 오류 |
| READING | 문제 조건 해석 실패 |

## Retry Cycle

```text
오답
→ 원인 코드
→ 정답 개념 1문장
→ 공식문서
→ 관련 Lab
→ +1일 재시험
→ +7일 재시험
→ FIXED
```

## Priority

1. 같은 개념 2회 이상 오류
2. Workflow / Enterprise 고비중 Domain
3. Security / Runner / Reuse 오류
4. Troubleshooting `FIRST` 오류
5. 단순 YAML/기억 실수

## 시험 Gate (Exam Gate, EG)

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

---

[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
