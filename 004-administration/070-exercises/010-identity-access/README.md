# 010 Identity & Access — 수행형 연습

## E010-01 — EMU 비교 Personal (EMU vs Personal, EMUP)
직원이 기존 개인 GitHub 계정과 업무 계정을 분리해야 하고, 회사가 업무 계정의 수명주기를 통제하려 합니다. EMU와 Personal Account 모델을 비교하고 선택 근거를 작성하세요.

## E010-02 — AuthN 비교 AuthZ (AuthN vs AuthZ, AA)
다음을 분류하세요.

1. SAML로 회사 사용자임을 확인
2. Repository Write 권한 확인
3. IdP 로그인 성공
4. Team Role 결정

## E010-03 — SAML SSO
여러 SaaS에서 기업 IdP 인증을 사용하려 합니다. SAML SSO가 해결하는 문제와 해결하지 않는 문제를 각각 3개 적으세요.

## E010-04 — SCIM
입사·이동·퇴사에 따른 계정 Provisioning/Deprovisioning 흐름을 6단계로 설계하세요.

## E010-05 — 팀 동기화 (Team Synchronization, TS)
IdP의 `backend-team` 그룹과 GitHub Team을 연결할 때 Team Sync가 SCIM과 다른 이유를 설명하세요.

## E010-06 — 2FA
SSO가 이미 있는데도 2FA 요구사항을 별도로 검토할 수 있는 이유를 설명하세요.

## E010-07 — Access 매트릭스 (Access Matrix, AM)
`platform`, `backend`, `security`, `auditor` Team과 3개 Repository를 대상으로 최소 권한 Matrix를 작성하세요.

## E010-08 — 엔터프라이즈 팀 (Enterprise Teams, ET)
Enterprise 수준 Team 관리가 여러 Organization에 걸친 운영에서 어떤 장점을 줄 수 있는지 작성하세요.

## E010-09 — Access 감사 (Access Audit, AA)
분기별 Access Review Checklist를 10개 항목으로 작성하세요. Direct Access, Elevated Role, External Collaborator를 포함합니다.

## E010-10 — Incident 시나리오 (Incident Scenario, IS)
퇴사자가 여전히 Repository를 볼 수 있습니다. IdP → SCIM → Membership → Team → Direct Access → Audit 순서로 조사 계획을 작성하세요.

## 검증 (Verify, VER)

- [ ] EMU / Personal Accounts 구분
- [ ] SAML / SCIM / Team Sync 구분
- [ ] AuthN / AuthZ 구분
- [ ] Role / Permission / Team을 연결
- [ ] Access Audit 수행 가능

---
[← Exercises](../README.md) · [020 Enterprise Environment →](../020-enterprise-environment/README.md)
