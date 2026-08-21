# 060 보안 기능 와 통합 — Q051–Q060 (060 Security Features & Integrations — Q051–Q060, SFIQ051Q060)

## Q051
자동화 서비스가 여러 Repository에 접근해야 하고 권한을 세밀하게 제한해야 한다. 가장 적절한 통합 방식은?

A. 공유 Classic PAT  B. GitHub App  C. 개인 Password  D. SSH Private Key 공유

**정답: B** — GitHub App은 설치 Scope와 Permission을 세밀하게 관리할 수 있습니다.

## Q052
OAuth App과 GitHub App 비교에서 GitHub App의 주요 장점은?

A. Repository 설치 단위 권한 제어  B. Audit 불가  C. 무제한 Owner 권한  D. Secret 불필요

**정답: A** — GitHub App은 세분화된 Permission/Installation 모델을 제공합니다.

## Q053
PAT를 사용할 수밖에 없는 경우 가장 중요한 보안 원칙은?

A. 최소 Scope·짧은 만료·안전한 저장  B. 영구 Token  C. 공개 README에 기록  D. 팀 공용 복사

**정답: A** — Credential 노출과 장기 권한을 최소화합니다.

## Q054
승인되지 않은 Third-party App 위험을 줄이려면?

A. Organization App 정책과 승인 절차  B. 모든 App 허용  C. Audit 비활성화  D. Owner 공유

**정답: A** — 중앙 통제와 승인 프로세스가 필요합니다.

## Q055
보안 Alert를 운영팀에 자동 전달할 때 가장 먼저 정해야 할 것은?

A. 책임 Owner와 Escalation 기준  B. Avatar  C. Repository Topic  D. Star 수

**정답: A** — Alert 처리 책임과 우선순위를 명확히 해야 합니다.

## Q056
Secret Scanning Alert의 올바른 대응 순서는?

A. 노출 Credential 폐기/회전 → 영향 확인 → 원인 제거  B. Alert 삭제만  C. Repo Public 전환  D. Audit 삭제

**정답: A** — 실제 Credential 위험을 먼저 제거합니다.

## Q057
외부 Integration에 Enterprise-wide Admin 권한이 필요하다고 요청받았다. FIRST 조치는?

A. 요구 기능을 분석해 최소 Permission으로 축소 가능한지 검토  B. 바로 승인  C. 모든 Owner 추가  D. SSO 해제

**정답: A** — Least Privilege 검토가 우선입니다.

## Q058
Security Feature 활성화 후 개발팀에서 오탐이 많다고 보고했다. 가장 적절한 대응은?

A. Feature 전체 비활성화  B. Alert 품질 분석 후 정당한 Suppression/Configuration 조정  C. Alert 무시  D. Secret 공유

**정답: B** — 위험을 유지한 채 신호 품질을 개선합니다.

## Q059
보안 Integration 변경 후 추적성을 확보하려면?

A. Change Ticket + Audit Log + Validation 기록  B. 개인 메모만  C. Token 원문 저장  D. 로그 삭제

**정답: A** — 변경의 승인·실행·검증 Evidence가 필요합니다.

## Q060
자동화 Identity와 사람 Identity를 분리하는 이유는?

A. 책임·권한·회전 정책을 명확히 하기 위해  B. Star 증가  C. PR 수 증가  D. Issue 감소

**정답: A** — Service Identity는 별도 Lifecycle과 Audit이 필요합니다.

---
[← Q041–Q050](../050-security-policies/README.md) · [다음 Q061–Q070 →](../070-actions-governance/README.md)
