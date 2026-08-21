# 실습 (Lab, LAB) 030 — 역할 / 팀 / 권한 (Roles / Teams / Permissions, RTP)

## 목표 (Objective, OBJ)

Enterprise, Organization, Team, Repository 계층에서 **Role과 Permission을 최소 권한 원칙으로 설계**합니다.

## 개념 (Concept, CPT)

```text
User
 ↓
Enterprise / Organization Membership
 ↓
Team / Enterprise Team
 ↓
Repository Role
 ↓
Effective Permission
```

## 실습 (Practice, PRAC) — Access 매트릭스 (Access Matrix, AM)

가상 회사:

```text
Teams
├── platform
├── backend
├── security
└── auditors

Repositories
├── platform-infra
├── customer-api
└── security-policies
```

다음 Matrix를 작성하세요.

| Team | platform-infra | customer-api | security-policies | 근거 |
|---|---|---|---|---|
| platform | | | | |
| backend | | | | |
| security | | | | |
| auditors | | | | |

권한을 필요 이상으로 높이지 않습니다.

## 실습 (Practice, PRAC) — Access 리뷰 (Access Review, AR)

정기 점검 Checklist:

- [ ] Dormant / inactive user
- [ ] Direct repository access
- [ ] Team membership
- [ ] Elevated role
- [ ] External collaborator
- [ ] App access
- [ ] Stale PAT / integration

## 도전 과제 (Challenge, CHL)

개별 사용자에게 Repository 권한을 직접 반복 부여하는 방식과 Team 기반 부여 방식의 운영 차이를 설명하세요.

## 검증 (Verify, VER)

- [ ] Role과 Permission 차이 설명
- [ ] Team 기반 접근 관리의 장점 설명
- [ ] Least Privilege 적용
- [ ] Access Audit 절차 설명
- [ ] Policy / Ruleset이 권한과 다른 역할임을 설명

---
[← Lab 020](../020-saml-scim-team-sync/README.md) · [Lab 040 →](../040-deployment-licensing/README.md)
