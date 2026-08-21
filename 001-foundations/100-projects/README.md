# 100 Projects — Foundations 통합 프로젝트

## Project 001 — GitHub Collaboration Mini Project

### 목표

GitHub Foundations에서 학습한 Repository·Issue·Branch·Pull Request·Review·Documentation을 하나의 작은 프로젝트에서 연결합니다.

## Quick Start

1. 아래 Phase 1~6을 순서대로 수행합니다.
2. [`010-project-rubric.md`](./010-project-rubric.md)로 100점 기준 평가를 진행합니다.
3. [`020-evidence-checklist.md`](./020-evidence-checklist.md)로 결과물을 정리합니다.
4. 80점 이상이면 PASS, 90점 이상 + Evidence 완료 시 CLEAR 후보입니다.

## 결과물

아래 항목이 모두 존재하는 Repository를 만듭니다.

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
.github/
└── CODEOWNERS
```

그리고 GitHub에서 다음 이력을 남깁니다.

```text
Issue
→ Feature Branch
→ Commit
→ Push
→ Pull Request
→ Review
→ Merge
→ Issue Close
```

## Phase 1 — Repository Bootstrap

- [ ] Repository 생성
- [ ] README 작성
- [ ] 적절한 License 선택
- [ ] CONTRIBUTING 작성
- [ ] SECURITY 작성
- [ ] CODEOWNERS 목적 확인

## Phase 2 — Issue Driven Work

예시 Issue:

```text
Title: Add glossary page

Goal:
- GitHub Foundations 핵심 용어 10개 정리
- README에서 glossary 링크 추가
```

- [ ] Issue 생성
- [ ] Label 적용
- [ ] Assignee 지정

## Phase 3 — Branch & Commit

예시 Branch:

```text
feature/add-glossary
```

- [ ] Branch 생성
- [ ] 최소 2개의 의미 있는 Commit 작성
- [ ] Remote Push

## Phase 4 — Pull Request

PR 본문에는 다음을 적습니다.

```text
What
Why
How to verify
Linked issue
```

- [ ] Issue 연결
- [ ] 변경사항 설명
- [ ] Review 수행
- [ ] Merge

## Phase 5 — Project Management

- [ ] GitHub Projects에서 Item 추적
- [ ] Status Field 사용
- [ ] Issue와 PR의 상태 변화를 확인

## Phase 6 — Modern Development 관찰

Foundations에서는 깊은 구현보다 각 기능의 목적을 구분합니다.

- [ ] Actions 탭의 역할 설명
- [ ] Copilot의 역할 설명
- [ ] Codespaces의 역할 설명
- [ ] Branch Protection/Ruleset의 목적 설명

## 평가

상세 평가는 [`010-project-rubric.md`](./010-project-rubric.md)를 사용합니다.

| 점수 | 판정 |
|---:|---|
| 90–100 + Evidence | CLEAR 후보 |
| 80–89 | PASS |
| 70–79 | 보완 후 재평가 |
| <70 | 관련 Lab 재수행 |

## 최종 설명 과제

프로젝트 완료 후 다음 질문에 5분 이내로 답합니다.

> “이 Repository에서 GitHub Flow가 어떻게 동작했으며, 각 GitHub 기능이 어떤 문제를 해결했는가?”

증거자료는 [`../150-evidence/`](../150-evidence/)에 정리합니다.

---

[← 090 Final Review](../090-final-review/README.md) · [다음: 110 Mock Exams →](../110-mock-exams/README.md)
