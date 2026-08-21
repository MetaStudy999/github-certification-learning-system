# 120 Wrong Answers — GH-100 오답 시스템

## 오류 Codes (Error Codes, EC)

| 코드 | 의미 |
|---|---|
| IDENTITY | EMU / SAML / SCIM / Team / Role 혼동 |
| SCOPE | Enterprise / Organization / Repository Scope 오류 |
| DEPLOY | GHEC / GHES / Data Residency / Support 오류 |
| SECURITY | Ruleset / GHAS / Alert / Compliance 오류 |
| APP | GitHub App / OAuth App / PAT Governance 오류 |
| ACTIONS | Policy / Workflow / Runner / Permission 오류 |
| RUNNER | Runner Group / Network / Capacity 오류 |
| CREDENTIAL | Secret / OIDC / Vault / Token 오류 |
| AUDIT | Audit Log / Usage / API 분석 오류 |
| COST | License / Metered Product / Optimization 오류 |
| READING | 문제 조건·BEST/FIRST 해석 오류 |

## 재도전 주기 (Retry Cycle, RC)

```text
오답
→ Error Code
→ 틀린 이유 1문장
→ 올바른 개념 1문장
→ Scope 확인
→ 공식문서
→ 관련 Lab
→ +1일 재시험
→ +7일 재시험
```

## 통과 기준 (Gate, GATE)

최근 오답 재시험 **90% 이상**을 시험 응시 기준으로 사용합니다.

## 파일

- [`010-error-log-template.md`](./010-error-log-template.md)
- [`020-retry-queue.md`](./020-retry-queue.md)

---
[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
