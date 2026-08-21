# 130 Progress — GH-100 진행률 Dashboard

## 상태 (Status, S)

- 콘텐츠 상태 (Content Status, CS): **CONTENT-READY**
- 학습 상태 (Learning Status, LS): **PLANNED**

> 콘텐츠 구축 상태와 실제 개인 학습 상태를 분리합니다. `CONTENT-READY`는 자료 준비 완료를 뜻하며 실제 시험 준비 완료를 뜻하지 않습니다.

## 학습 상태 흐름 (Learning Status Flow, LSF)

```text
PLANNED
→ READY
→ LEARNING
→ PRACTICING
→ REVIEWING
→ EXAM-READY
→ PASSED
→ CLEAR
```

## Skill 영역 Progress (Skill Area Progress, SAP)

| Skill Area | Weight | Theory | Lab | QBank | Review | Status |
|---|---:|---|---|---|---|---|
| Manage GitHub identities and access | 15–20% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Administer GitHub Enterprise environment | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Implement secure software development and compliance | 25–30% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Manage GitHub Actions | 20–25% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Monitor and optimize GitHub usage | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |

## 7일 단기 집중 과정 (7-Day Fast Track, 7DFT)

| Day | 목표 | 완료 | 점수/메모 |
|---:|---|---|---|
| 1 | Identity / EMU / SAML / SCIM / Role | ⬜ | |
| 2 | GHEC / GHES / Data Residency / Support | ⬜ | |
| 3 | Security Policy / Ruleset / GHAS | ⬜ | |
| 4 | GitHub App / OAuth App / PAT / Compliance | ⬜ | |
| 5 | Actions Policy / Runner / OIDC / Vault | ⬜ | |
| 6 | Audit / Usage / Cost + QBank + Mock 01 | ⬜ | |
| 7 | Mock 02 + Final Mock + Final Review | ⬜ | |

## 시험 Readiness Metrics (Exam Readiness Metrics, ERM)

| 지표 | 목표 | 현재 |
|---|---:|---:|
| 최신 Study Guide 확인 | 100% | ⬜ |
| 핵심 용어 설명 | 90%+ | - |
| 실습 (Labs, LAB) | 80%+ | - |
| 연습문제 (Exercises, EXR) | 80%+ | - |
| QBank 1회차 | 80%+ | - |
| QBank 2회차 | 85%+ | - |
| 최근 Mock 2회 | 85%+ | - |
| 최종 모의고사 (Final Mock, FM) | 90%+ 권장 | - |
| 오답 재시험 | 90%+ | - |
| Enterprise Blueprint | 80점+ | - |

상세 기록:

- [`010-daily-tracker.md`](./010-daily-tracker.md)
- [`020-readiness-gate.md`](./020-readiness-gate.md)
- [`030-score-log.md`](./030-score-log.md)

## 콘텐츠 Build Summary (Content Build Summary, CBS)

- Labs: **12개**
- Exercises: **50개**
- Question Bank: **100문제**
- Mock Exams: **3회 × 40문항 = 120문항**
- 자체 문제 총계: **220문항**
- Final Review: 완료
- Enterprise Administration Blueprint: 완료
- Wrong Answer / Retry System: 완료
- Evidence Templates: 완료

## PASSED 비교 CLEAR (PASSED vs CLEAR, PASSEDCLEAR)

`PASSED`: GH-100 시험 합격

`CLEAR`:

- [ ] GH-100 PASS
- [ ] 핵심 Lab 완료
- [ ] Enterprise Administration Blueprint 80점 이상
- [ ] Identity / Security / Actions / Audit Evidence 정리
- [ ] 핵심 Scope와 Policy 관계를 설명 가능
- [ ] 최종 Reflection 완료

---
[← 120 Wrong Answers](../120-wrong-answers/README.md) · [다음: 140 Resources →](../140-resources/README.md)
