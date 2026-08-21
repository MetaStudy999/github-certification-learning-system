# 950 Progress — Master 학습 Dashboard (950 Progress — Master Learning Dashboard, PMLD)

6개 GitHub 자격증의 **Content Status와 실제 Learning Status를 분리**하여 관리하는 통합 Control Tower입니다.

## 빠른 시작 (Quick Start, QS)

1. 이 Dashboard에서 전체 상태를 확인합니다.
2. 실제 학습 세션은 [`010-study-session-template.md`](./010-study-session-template.md) 형식으로 기록합니다.
3. 실제 학습을 시작한 과정만 `Learning Status`를 변경합니다.
4. 상세 점수와 일일 기록은 각 과정의 `130-progress/`에서 관리합니다.
5. [`020-fast-track-dashboard.md`](./020-fast-track-dashboard.md)에서 6주 Fast Track을 추적합니다.
6. [`030-exam-plan.md`](./030-exam-plan.md)에 실제 시험 예약일을 기록합니다.
7. [`090-status-policy.md`](./090-status-policy.md)의 상태 정의를 기준으로 변경합니다.

## Master Dashboard

| 코드 | 자격증 | Content | Study | Lab | QBank | Mock | Exam | 학습 상태 (Learning Status, LS) |
|---:|---|---|---|---|---|---|---|---|
| 001 | GitHub 기초 (GitHub Foundations, GHF / GH-900) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | READY |
| 002 | GitHub 액션 (GitHub Actions, GHACT / GH-200) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 003 | GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 004 | GitHub 관리 (GitHub Administration, GHADM / GH-100) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 005 | GitHub 고급 보안 (GitHub Advanced Security, GHAS / GH-500) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 006 | GitHub 에이전틱 AI 개발자 (GitHub Agentic AI Developer, GHAI / GH-600) | **CONTENT-READY** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |

## 과정 Progress Links (Course Progress Links, CPL)

| 코드 | 상세 Progress |
|---:|---|
| 001 | [`Foundations`](../001-foundations/130-progress/) |
| 002 | [`Actions`](../002-actions/130-progress/) |
| 003 | [`Copilot`](../003-copilot/130-progress/) |
| 004 | [`Administration`](../004-administration/130-progress/) |
| 005 | [`Advanced Security`](../005-advanced-security/130-progress/) |
| 006 | [`Agentic AI Developer`](../006-agentic-ai-developer/130-progress/) |

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

## 핵심 구분

```text
CONTENT-READY
= Repository의 학습 콘텐츠 구축 완료

EXAM-READY
= 실제 학습자의 시험 준비도 Gate 통과

PASSED
= 자격시험 합격

CLEAR
= 시험 + 핵심 실습 + 프로젝트 + Evidence 완료
```

## 기록 원칙

- 학습하지 않은 항목을 완료 처리하지 않습니다.
- 점수는 실제 결과만 기록합니다.
- 시험 예약일·응시일·합격 여부는 확정된 정보만 기록합니다.
- `PASSED` 이후에도 프로젝트/Evidence가 미완료면 `CLEAR`로 변경하지 않습니다.

---
[통합 README](../README.md)