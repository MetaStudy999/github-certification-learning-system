# 150 Evidence — GH-200 학습·실습 증거

## 기록 대상

| 코드 | Evidence | 예시 |
|---:|---|---|
| 010 | Workflow | Workflow URL / Run URL |
| 020 | Trigger | Push / PR / Manual 실행 |
| 030 | Matrix / Artifact | Matrix Run, Artifact 결과 |
| 040 | Reuse | Reusable Workflow / Composite Action |
| 050 | Runner | Runner 선택·운영 설명 |
| 060 | Security | Permission / OIDC 설계 |
| 070 | Troubleshooting | 실패 → 원인 → 수정 → 성공 |
| 080 | Scores | Question Bank / Mock |
| 090 | Exam / Reflection | GH-200 결과와 회고 |

## Workflow Evidence Template

```text
Date:
Lab:
Repository:
Workflow file:
Workflow run URL:
Event:
Runner:
Expected result:
Actual result:
Verification:
What I learned:
Security notes:
```

## Troubleshooting Evidence

```text
Failure symptom:
Failed job / step:
Log clue:
Root cause:
Fix:
Successful run URL:
Prevention:
```

## 보안 원칙

- Secret 값 자체를 기록하지 않습니다.
- Token과 Cloud Credential을 Evidence에 저장하지 않습니다.
- 실제 Production 권한을 높여 실습하지 않습니다.
- 공개 Repository에서는 Workflow Log에 민감정보가 없는지 확인합니다.

## CLEAR 기준

- [ ] GH-200 PASS
- [ ] 핵심 Lab 완료
- [ ] CI/CD Project 80점 이상
- [ ] Security Evidence
- [ ] Troubleshooting Evidence
- [ ] Question / Mock 기록
- [ ] 최종 Reflection
