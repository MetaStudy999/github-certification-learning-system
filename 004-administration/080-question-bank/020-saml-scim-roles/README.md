# 020 SAML, SCIM, 역할 — Q011–Q020 (020 SAML, SCIM, Roles — Q011–Q020, SAMLSCIMRQ01)

## Q011
Enterprise에서 IdP 기반 SSO 인증을 구현할 때 핵심 표준은?

A. SMTP  B. SAML  C. FTP  D. DNS

**정답: B** — SAML은 IdP와 Service Provider 간 SSO에 사용됩니다.

## Q012
사용자 계정 생성·변경·비활성화를 자동화하는 표준은?

A. SCIM  B. SSH  C. TLS  D. YAML

**정답: A** — SCIM은 Identity Provisioning Lifecycle 자동화에 사용됩니다.

## Q013
SAML과 SCIM의 관계를 가장 잘 설명한 것은?

A. 둘 다 CI 도구  B. SAML은 인증, SCIM은 계정 Lifecycle  C. 둘 다 Branch 보호  D. 둘 다 Billing

**정답: B** — 인증과 Provisioning 역할이 다릅니다.

## Q014
Team Sync를 사용하는 주요 목적은?

A. Repo 삭제  B. IdP Group과 GitHub Team Membership 동기화  C. Secret 생성  D. Actions Cache 삭제

**정답: B** — 그룹 기반 접근관리를 일관되게 유지합니다.

## Q015
SSO 적용 후 사용자가 Repository 접근에 실패한다. FIRST로 볼 항목은?

A. README 길이  B. IdP Assignment와 SAML 상태  C. Commit message  D. Issue count

**정답: B** — 인증/할당 상태를 먼저 확인합니다.

## Q016
SCIM Deprovisioning이 실패하면 가장 큰 위험은?

A. Markdown 오류  B. 퇴사자 접근이 남을 수 있음  C. Branch 이름 변경  D. Cache Miss

**정답: B** — 접근 회수 지연은 보안 위험입니다.

## Q017
Organization Owner를 지정할 때 가장 적절한 원칙은?

A. 모든 Member에게 부여  B. 운영상 필요한 최소 인원  C. 외부 사용자를 기본 Owner  D. Bot에게 Owner 공유

**정답: B** — Privileged Role은 제한합니다.

## Q018
Repository Role 설계에서 가장 먼저 정의해야 할 것은?

A. 사용자 취향  B. 업무 Requirement와 필요한 작업 범위  C. Avatar  D. Star 수

**정답: B** — Role은 업무 요구에서 역산해야 합니다.

## Q019
Team 권한이 Repository 직접 권한과 충돌해 예상보다 높은 접근을 제공한다. 가장 적절한 조치는?

A. 무시  B. Effective Permission 경로를 모두 점검  C. 모든 Team 삭제  D. Public 전환

**정답: B** — Team·직접 권한·상위 Role을 함께 검토합니다.

## Q020
Identity 변경 검증 시 가장 유용한 기록은?

A. Audit Log  B. Local shell history only  C. Screenshot only  D. Password list

**정답: A** — 누가 언제 무엇을 변경했는지 추적할 수 있습니다.

---
[← Q001–Q010](../010-identity-models/README.md) · [다음 Q021–Q030 →](../030-enterprise-deployment/README.md)
