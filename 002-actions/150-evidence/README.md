# 150 Evidence — GH-200 학습·실습 증거

## 빠른 시작 (Quick Start, QS)

실습과 시험 결과를 단순 체크가 아니라 **재현 가능한 Evidence**로 남깁니다.

## Evidence 파일 (Evidence Files, EF)

- [010 Environment Template](./010-environment-template.md)
- [020 Workflow Evidence Template](./020-workflow-evidence-template.md)
- [030 Troubleshooting Evidence Template](./030-troubleshooting-evidence-template.md)
- [040 Exam & Reflection Template](./040-exam-reflection-template.md)
- [090 Content Verification](./090-content-verification.md)

## 기록 대상

| 코드 | 증빙 (Evidence, EVD) | 예시 |
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

---

[← 140 Resources](../140-resources/README.md) · [Actions 홈](../README.md)
