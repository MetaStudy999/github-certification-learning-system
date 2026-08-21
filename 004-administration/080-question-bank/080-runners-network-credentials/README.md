# 080 러너, 네트워크, 자격 증명 — Q071–Q080 (Runners, Network, Credentials — Q071–Q080, RNCQ071Q080)

## Q071
내부망 Database에 접근해야 하는 Workflow에 가장 현실적인 Runner 선택은?

A. 항상 Public GitHub-hosted Runner  B. 적절히 보호된 Self-hosted Runner  C. Local laptop  D. Anonymous runner

**정답: B** — 내부 네트워크 접근 요구가 있으면 Self-hosted Runner를 검토할 수 있습니다.

## Q072
Self-hosted Runner의 가장 중요한 추가 책임은?

A. GitHub가 OS 패치 전부 담당  B. 고객이 OS·Network·Hardening·Capacity 관리  C. Secret 불필요  D. Audit 불필요

**정답: B** — 운영·보안 책임이 증가합니다.

## Q073
Runner Group을 사용하는 주요 목적은?

A. Runner 접근 Scope를 조직/Repository별로 제어  B. README 생성  C. Issue 삭제  D. License 제거

**정답: A** — Runner 사용 대상을 제한할 수 있습니다.

## Q074
Cloud 배포에서 장기 Access Key를 줄이는 데 가장 적합한 방식은?

A. OIDC Federation  B. README Secret  C. Shared PAT  D. SSH Password

**정답: A** — OIDC를 통해 단기 자격증명을 발급받는 구조가 가능합니다.

## Q075
Third-party Vault 연동의 주요 목적은?

A. 장기 Secret을 GitHub에 직접 저장하지 않고 필요 시 안전하게 조회  B. 모든 Secret 공개  C. Audit 제거  D. Runner 삭제

**정답: A** — Credential 중앙관리와 회전을 개선합니다.

## Q076
Self-hosted Runner가 Queue에서 잡을 받지 못한다. FIRST로 확인할 것은?

A. Runner Online 상태·Label·Group Scope  B. README  C. PR 제목  D. Wiki

**정답: A** — 할당 조건과 가용 상태를 먼저 확인합니다.

## Q077
Runner를 여러 민감 환경이 공유할 때 위험을 줄이는 방법은?

A. Scope 분리와 Ephemeral/격리 전략 검토  B. 모든 Repo 허용  C. Admin Token 공유  D. 로그 삭제

**정답: A** — Trust Boundary를 분리합니다.

## Q078
Private Networking을 설계할 때 가장 먼저 정해야 할 것은?

A. 어떤 Workflow가 어떤 Private Resource에 접근해야 하는지  B. Star 수  C. Issue Label  D. Commit Emoji

**정답: A** — 네트워크 접근 Requirement와 최소 경로를 정의합니다.

## Q079
Credential이 Workflow Log에 노출되었다. 가장 적절한 FIRST 조치는?

A. Credential 폐기/회전  B. Log만 숨김  C. Repo 이름 변경  D. Runner 추가

**정답: A** — 노출 Credential의 유효성을 제거하는 것이 우선입니다.

## Q080
Runner 운영 Evidence로 적절하지 않은 것은?

A. Runner Group 정책  B. Health/Queue 기록  C. Secret 원문  D. 네트워크 설계 문서

**정답: C** — Secret 원문은 Evidence에 저장하지 않습니다.

---
[← Q061–Q070](../070-actions-governance/README.md) · [다음 Q081–Q090 →](../090-audit-usage-cost/README.md)
