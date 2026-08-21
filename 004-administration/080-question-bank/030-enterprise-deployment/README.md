# 030 엔터프라이즈 배포 — Q021–Q030 (030 Enterprise Deployment — Q021–Q030, EDQ021Q030)

## Q021
GitHub Enterprise Cloud와 GitHub Enterprise Server의 가장 큰 운영 차이는?

A. 둘 다 GitHub가 인프라 전부 운영  B. Cloud는 SaaS, Server는 고객이 인프라 운영  C. 둘 다 On-prem only  D. 둘 다 Public only

**정답: B** — GHES는 고객이 배포·업그레이드·백업 등 운영 책임을 가집니다.

## Q022
데이터 위치 요구사항이 엄격한 Enterprise에서 먼저 검토할 항목은?

A. Repository 이름  B. Data Residency와 배포 모델  C. Emoji  D. Issue Template

**정답: B** — 데이터 저장 위치와 서비스 배포 모델을 요구사항과 맞춰야 합니다.

## Q023
GHES 업그레이드 계획에서 가장 먼저 확인할 것은?

A. Release Notes와 지원되는 Upgrade Path  B. Star 수  C. Fork 수  D. README

**정답: A** — 버전별 지원 경로와 변경사항 검토가 우선입니다.

## Q024
Enterprise 배포 전 Pilot 환경을 사용하는 주요 이유는?

A. Production 설정 삭제  B. 정책·통합·사용자 흐름을 제한된 Scope에서 검증  C. 비용 무시  D. 권한 최대화

**정답: B** — 변경 영향과 위험을 줄입니다.

## Q025
Enterprise 계층에서 여러 Organization에 공통 정책을 강제하려면 어디에서 먼저 설계해야 하는가?

A. 개인 Profile  B. Enterprise Scope  C. 특정 Issue  D. Local Git Config

**정답: B** — 공통 정책은 가능한 상위 Scope에서 관리합니다.

## Q026
GHES 운영에서 백업 계획이 중요한 이유는?

A. Markdown 렌더링  B. 장애·데이터 손실 시 복구  C. Star 증가  D. Branch 이름 표준화

**정답: B** — Recovery 목표와 절차가 필요합니다.

## Q027
Enterprise 도입 시 License 수요를 예측할 때 가장 중요한 입력은?

A. 조직 사용자·사용 계획·성장률  B. README 길이  C. Commit 색상  D. Avatar 수

**정답: A** — 실제 사용자 규모와 성장 시나리오로 License를 계획합니다.

## Q028
Cloud와 Server를 혼합해 사용하는 환경에서 중요한 운영 원칙은?

A. 정책을 각각 무관하게 관리  B. Identity·Policy·Audit 경계를 명확히 문서화  C. 모든 Repo Public  D. 공용 Admin 계정 사용

**정답: B** — Hybrid 환경에서는 관리 경계와 책임소재가 중요합니다.

## Q029
Enterprise 설정 변경 전 가장 적절한 절차는?

A. 바로 Production 변경  B. 영향 분석 → 승인 → Pilot → 적용 → 검증  C. Owner 추가  D. Audit 비활성화

**정답: B** — Change Management 기본 흐름입니다.

## Q030
Deployment Architecture 문서에 반드시 포함할 항목은?

A. Identity, Network, Data, Policy, Backup/Recovery  B. Emoji  C. Personal Password  D. Private Key

**정답: A** — 운영에 필요한 구조와 책임을 기록합니다.

---
[← Q011–Q020](../020-saml-scim-roles/README.md) · [다음 Q031–Q040 →](../040-support-licensing-standards/README.md)
