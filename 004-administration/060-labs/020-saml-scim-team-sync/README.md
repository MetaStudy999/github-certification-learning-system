# 실습 (Lab, LAB) 020 — SAML SSO / SCIM / 팀 동기화 (SAML SSO / SCIM / Team Synchronization, SAMLSSOSCIMT)

## 목표 (Objective, OBJ)

SAML SSO, 2FA, SCIM, Team Synchronization, IdP를 **하나의 Identity Lifecycle**로 연결합니다.

## 개념 맵 (Concept Map, CM)

```text
Identity Provider (IdP)
├── SAML SSO → Authentication
├── SCIM → Provision / Deprovision
└── Group → Team Synchronization → Team Membership
```

## Practice 1 — 기능 선택

| 요구사항 | 선택 |
|---|---|
| 회사 계정으로 GitHub 로그인 | |
| 퇴사자 GitHub 접근 자동 회수 | |
| IdP 개발팀 그룹을 GitHub Team과 연결 | |
| 계정 인증을 추가 강화 | |

후보: `SAML SSO`, `SCIM`, `Team Synchronization`, `2FA`

## 실습 (Practice, PRAC) 2 — Joiner / Mover / Leaver

가상 직원 `Alice`의 수명주기를 설계합니다.

```text
Joiner
→ Account provision
→ SSO
→ Team membership
→ Repository access

Mover
→ IdP group change
→ Team / permission update

Leaver
→ Deprovision
→ Access removal
→ Audit verification
```

각 단계에서 GitHub와 IdP 중 누가 어떤 역할을 담당하는지 작성합니다.

## 실습 (Practice, PRAC) 3 — 실패 시나리오 (Failure Scenario, FS)

사용자는 SAML 인증에 성공하지만 올바른 Team에 들어가지 못합니다.

진단 순서:

1. Authentication 성공 여부
2. SCIM User 상태
3. IdP Group Membership
4. Team Sync 설정
5. Organization / Team 상태
6. Audit / Log 확인

## 도전 과제 (Challenge, CHL)

`SAML SSO가 있으면 SCIM은 필요 없다`라는 주장에 반박하세요.

## 검증 (Verify, VER)

- [ ] SAML / SCIM / Team Sync의 목적 구분
- [ ] IdP 역할 설명
- [ ] Joiner/Mover/Leaver 흐름 설명
- [ ] 2FA와 SSO를 동일 기능으로 오해하지 않음

## 안전

실제 기업 SSO/SCIM 설정을 학습 목적으로 변경하지 않습니다. Sandbox 또는 설계 문서로 수행합니다.

---
[← Lab 010](../010-identity-models/README.md) · [Lab 030 →](../030-roles-teams-permissions/README.md)
