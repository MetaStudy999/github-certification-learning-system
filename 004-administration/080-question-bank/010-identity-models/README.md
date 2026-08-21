# 010 식별 모델 — Q001–Q010 (010 Identity Models — Q001–Q010, IMQ001Q010)

## Q001
Enterprise에서 IdP가 사용자 계정 Lifecycle을 중앙 통제하고 개인 GitHub 계정과 분리하려면 가장 적합한 모델은?

A. Personal account only  B. Enterprise Managed Users  C. Public organization  D. Repository collaborator

**정답: B** — EMU는 Enterprise가 관리하는 사용자 Identity 모델입니다.

## Q002
사용자가 GitHub에 로그인할 때 "누구인지" 확인하는 개념은?

A. Authorization  B. Authentication  C. Audit  D. Billing

**정답: B** — Authentication은 신원 확인입니다.

## Q003
로그인한 사용자가 특정 Repository를 수정할 수 있는지 결정하는 개념은?

A. Authentication  B. Authorization  C. Provisioning  D. Metering

**정답: B** — Authorization은 허용된 행동 범위를 결정합니다.

## Q004
Enterprise → Organization → Repository 계층에서 일반적으로 우선 검토해야 할 것은?

A. 가장 하위 설정만  B. 상위 Policy와 상속 관계  C. README  D. Issue Label

**정답: B** — 상위 정책이 하위 Scope의 선택을 제한할 수 있습니다.

## Q005
퇴사자의 접근을 신속히 회수해야 할 때 가장 중요한 운영 원칙은?

A. Manual review only  B. Identity lifecycle automation  C. Public repository  D. Fork

**정답: B** — Provisioning/Deprovisioning 자동화가 접근 회수 지연을 줄입니다.

## Q006
최소 권한 원칙에 가장 부합하는 방식은?

A. 모든 사용자 Owner  B. 필요한 Scope에 필요한 Role만 부여  C. 공용 PAT 공유  D. Admin 권한 기본값

**정답: B** — Least Privilege는 필요한 최소 권한만 부여합니다.

## Q007
Team을 사용해 권한을 관리하는 주요 이점은?

A. Commit 삭제  B. 사용자별 권한 반복 설정 감소  C. MFA 비활성화  D. Billing 제거

**정답: B** — Team 기반 권한은 일관성과 관리성을 높입니다.

## Q008
Enterprise Owner 권한은 어떻게 다뤄야 하는가?

A. 개발자 전원에게 부여  B. 최소 인원에게 제한  C. 외부 협력사에 기본 부여  D. Anonymous access 허용

**정답: B** — 고권한 Role은 최소 인원으로 제한해야 합니다.

## Q009
외부 협력사가 한 Repository만 사용해야 한다. 가장 적절한 접근은?

A. Enterprise Owner  B. Organization Owner  C. 필요한 Repository에 제한된 권한  D. 모든 Private Repo Read

**정답: C** — Scope를 최소화합니다.

## Q010
Identity 설계 검증 Evidence로 가장 적절한 것은?

A. 개인 Password  B. Role/Team/Scope 표와 Audit 기록  C. Secret 값  D. SSH Private Key

**정답: B** — 민감정보 없이 정책과 변경 근거를 남깁니다.

---
[← Question Bank](../README.md) · [다음 Q011–Q020 →](../020-saml-scim-roles/README.md)
