# 100 혼합 통과 기준 — Q091–Q100 (Mixed Gate — Q091–Q100, MGQ091Q100)

## Q091
회사가 IdP 기반 사용자 Lifecycle 자동화와 SSO를 모두 원한다. 가장 적절한 조합은?

A. SAML + SCIM  B. SSH + Git  C. Wiki + Projects  D. Pages + Actions

**정답: A** — SAML은 SSO, SCIM은 Provisioning/Deprovisioning에 사용합니다.

## Q092
외부 서비스가 여러 Repository를 자동화해야 하지만 사용자 계정에 종속되면 안 된다. 가장 적절한 선택은?

A. GitHub App  B. 개인 Password  C. Owner 계정 공유  D. 공개 PAT

**정답: A** — App Identity와 세밀한 Permission을 사용할 수 있습니다.

## Q093
Enterprise-wide Actions 정책 변경 후 특정 조직만 실패한다. FIRST 조치는?

A. 상위 정책과 해당 조직 Workflow 요구사항의 차이 확인  B. 모든 정책 삭제  C. Owner 확대  D. Audit 비활성화

**정답: A** — 영향 Scope를 좁혀 원인을 확인합니다.

## Q094
Self-hosted Runner가 내부망에 접근하고 Production 배포도 수행한다. 가장 중요한 관리 항목은?

A. Runner 격리·네트워크·Credential 최소화  B. README  C. Star  D. Wiki

**정답: A** — Runner는 높은 Trust Boundary가 될 수 있습니다.

## Q095
Branch 보호를 예외 없이 강화했더니 긴급 Hotfix가 불가능해졌다. 가장 좋은 개선은?

A. 통제된 Break-glass 예외와 Audit 절차 설계  B. 보호 전체 해제  C. Owner 전원 추가  D. Public 전환

**정답: A** — 보안을 유지하며 비상 운영 절차를 만듭니다.

## Q096
퇴사자가 여전히 Repository에 접근 가능하다. 가장 먼저 점검할 영역은?

A. SCIM/Identity Deprovisioning 상태  B. Actions Cache  C. README  D. Issue Label

**정답: A** — 사용자 Lifecycle과 접근 회수가 핵심입니다.

## Q097
월간 Actions 비용이 2배가 되었다. 가장 적절한 분석 흐름은?

A. Usage Trend → Workflow Frequency → Runner/Storage → 실패 재실행  B. Star 확인  C. Repo 이름 변경  D. SSO 해제

**정답: A** — 직접 비용 동인을 순서대로 분해합니다.

## Q098
보안 감사에서 정책이 "문서상 존재"하는 것만으로 충분하지 않은 이유는?

A. 실제 적용과 변경 Evidence가 필요하기 때문  B. README가 짧아서  C. Star가 적어서  D. Fork가 많아서

**정답: A** — Policy + Enforcement + Audit Evidence가 연결되어야 합니다.

## Q099
Enterprise Admin이 모든 문제를 Owner 권한 확대만으로 해결하려 해서는 안 되는 이유는?

A. 최소 권한과 책임 분리가 무너지기 때문  B. Markdown 오류 때문  C. Issue가 늘어서  D. Git이 느려져서

**정답: A** — 고권한 남용은 사고 영향 범위를 키웁니다.

## Q100
GH-100 시험 준비가 가장 충분한 상태는?

A. 용어 암기만 완료  B. 5개 Skill Area를 Scenario로 설명하고 Lab/QBank/Mock Gate를 통과  C. README만 읽음  D. Admin 권한만 보유

**정답: B** — 개념·실습·판단·검증을 함께 요구합니다.

## 100-질문 Gate (100-Question Gate, QG)

- [ ] 1회차 80/100 이상
- [ ] 2회차 85/100 이상
- [ ] 오답 재시험 90% 이상
- [ ] 취약 영역 Lab 재수행

---
[← Q081–Q090](../090-audit-usage-cost/README.md) · [다음: 090 Final Review →](../../090-final-review/README.md)
