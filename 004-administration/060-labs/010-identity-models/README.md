# Lab 010 — Identity Models

## Objective

**Enterprise Managed Users (EMU)**와 **Personal Accounts** 기반 Enterprise 모델을 비교하고 Authentication / Authorization을 구분합니다.

## Concept

```text
Identity
→ Authentication
→ Enterprise membership
→ Authorization
→ Organization / Repository access
```

## Practice — Decision Table

다음 가상 요구사항을 비교합니다.

### Scenario A

- 회사가 사용자 계정 수명주기를 중앙 통제
- 입사/퇴사 시 기업 IdP 기준으로 계정 관리
- 업무용 GitHub Identity를 기업이 통제

### Scenario B

- 개발자가 기존 개인 GitHub 계정을 유지
- 회사 Organization에 Member로 초대
- 외부 오픈소스 활동과 회사 활동을 같은 개인 계정으로 수행 가능

표를 작성하세요.

| 기준 | EMU | Personal Account Model |
|---|---|---|
| 계정 관리 주체 | | |
| Provisioning | | |
| 기업 통제 | | |
| 개인 GitHub 활동 | | |
| 적합 Scenario | | |

## Challenge

다음 문장을 AuthN 또는 AuthZ로 분류합니다.

1. IdP가 사용자의 회사 Identity를 확인한다.
2. 사용자가 Repository에 Write할 수 있는지 확인한다.
3. SAML 로그인에 성공한다.
4. Team의 Repository Role이 `read`인지 `write`인지 결정한다.

## Verify

- [ ] EMU와 Personal Account의 핵심 차이 설명
- [ ] AuthN / AuthZ 구분
- [ ] Enterprise 요구사항으로 Identity Model 선택 이유 설명
- [ ] `기업 관리가 강할수록 무조건 EMU` 같은 단순화를 피함

## 증빙 (Evidence, EVD)

```text
Date:
Scenario:
Selected model:
Why:
AuthN controls:
AuthZ controls:
Risks:
Official docs checked:
```

---
[← Labs 홈](../README.md) · [Lab 020 →](../020-saml-scim-team-sync/README.md)
