# 080 Question Bank — GH-500 자체 문제은행

> 실제 시험 문항이나 Brain Dump를 복제하지 않습니다. Microsoft Learn의 **July 2026 GH-500 Skills Measured**를 기준으로 자체 제작한 학습 문제입니다.

## 100-질문 Structure (100-Question Structure, QS)

| Set | 문제 | 영역 |
|---:|---|---|
| 010 | Q001–Q010 | [Security Suites / Ecosystem](./010-security-suites-ecosystem/) |
| 020 | Q011–Q020 | [Secret Protection Basics](./020-secret-protection-basics/) |
| 030 | Q021–Q030 | [Secret Protection Operations](./030-secret-protection-operations/) |
| 040 | Q031–Q040 | [Supply Chain Basics](./040-supply-chain-basics/) |
| 050 | Q041–Q050 | [Dependency Review / SBOM](./050-supply-chain-review-sbom/) |
| 060 | Q051–Q060 | [Code Security Basics](./060-code-security-basics/) |
| 070 | Q061–Q070 | [CodeQL / SARIF / Setup](./070-codeql-sarif-setup/) |
| 080 | Q071–Q080 | [Security Operations](./080-security-operations/) |
| 090 | Q081–Q090 | [Administration / Governance](./090-administration-governance/) |
| 100 | Q091–Q100 | [Mixed Readiness Gate](./100-mixed-gate/) |

**현재 문제 수: 100문제**

## 사용 방법

```text
1회차: 개념 확인
→ 오답 원인 분류
→ 관련 공식문서 / Lab
→ 2회차: 자료 없이 재풀이
→ Mixed Gate
→ Mock Exam
```

## 점수 통과 기준 (Score Gate, SG)

- 1회차: **80/100 이상**
- 2회차: **85/100 이상**
- 최근 오답 재시험: **90% 이상**
- Mixed Gate: **8/10 이상**

## 문제 설계 원칙

- 기능 이름만 묻지 않고 `Risk → Feature → Response → Verification`을 연결합니다.
- Prevention / Detection / Triage / Remediation / Governance를 구분합니다.
- 실제 민감정보나 운영 자격증명을 사용하지 않습니다.
- 실제 시험문제 재현·유출문제·Brain Dump를 사용하지 않습니다.
- 일부 Set은 빠른 개념 확인용이므로 선택지 위치 암기가 아니라 **왜 정답인지 말로 설명하는 것**을 완료 기준으로 합니다.
- 실제 시험 시뮬레이션은 `110-mock-exams/`에서 선택지 위치와 Scenario를 다양화합니다.

## 질문 리뷰 Template (Question Review Template, QRT)

```text
ID:
Domain:
My answer:
Correct answer:
Why correct:
Why alternatives are less appropriate:
Risk:
Related feature:
Related official docs:
Related Lab:
Retry result:
```

---
[← 070 Exercises](../070-exercises/README.md) · [다음: 090 Final Review →](../090-final-review/README.md)
