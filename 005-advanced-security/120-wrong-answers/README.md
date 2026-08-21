# 120 Wrong Answers — GH-500 오답 시스템

## Error Codes

| 코드 | 의미 |
|---|---|
| SUITE | Security Suite 역할 혼동 |
| SECRET | Secret Protection / Push Protection 오류 |
| SUPPLY | Dependency / SBOM / Supply Chain 오류 |
| CODEQL | CodeQL / SARIF / Setup 오류 |
| TRIAGE | Alert 우선순위·Dismissal 오류 |
| CAMPAIGN | Security Campaign / 대규모 Remediation 오류 |
| ADMIN | Policy / Role / Scope / Rollout 오류 |
| READING | 문제 조건 해석 실패 |

## Retry Cycle

```text
오답
→ Error Code
→ Risk 정의
→ 올바른 Feature
→ Remediation
→ 관련 공식문서
→ 관련 Lab
→ +1일 재시험
→ +7일 재시험
```

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

---
[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
