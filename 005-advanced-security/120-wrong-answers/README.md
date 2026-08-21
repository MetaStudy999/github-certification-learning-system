# 120 Wrong Answers — GH-500 오답 시스템

## Error Codes

| 코드 | 의미 |
|---|---|
| SUITE | Security Suite 역할 혼동 |
| SECRET | Secret Protection / Push Protection 오류 |
| SUPPLY | Dependency / SBOM / Supply Chain 오류 |
| CODEQL | CodeQL / SARIF / Setup 오류 |
| TRIAGE | Alert 우선순위·Dismissal 오류 |
| CAMPAIGN | Security Campaign / Remediation 오류 |
| ADMIN | Policy / Role / Scope / Rollout 오류 |
| READING | 문제 조건 해석 실패 |

## Files

- [`010-error-log-template.md`](./010-error-log-template.md) — 오답 1건 분석
- [`020-retry-queue.md`](./020-retry-queue.md) — +1일 / +7일 재시험 관리

## Retry Cycle

```text
오답
→ Error Code
→ Risk 1문장 정의
→ 올바른 Feature / Control
→ 왜 다른 선택이 덜 적절한지 설명
→ 공식문서
→ 관련 Lab
→ +1일 재시험
→ +7일 재시험
→ CLOSED
```

## Gate

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

정답 문자만 외운 경우에는 `CLOSED`로 처리하지 않습니다.

---
[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
