# Lab 080 — PAT / GitHub Apps / OAuth Apps / Integrations

## Objective

API와 Integration 접근 방식을 **사용자 Token, GitHub App, OAuth App** 관점에서 비교하고 최소 권한 Policy를 설계합니다.

## Concept

| 방식 | 중심 Identity | 관리 관점 |
|---|---|---|
| PAT | 사용자 | Scope, Expiration, Rotation, Policy |
| GitHub App | App Installation | 세밀한 Resource Permission, Installation Scope |
| OAuth App | 사용자 위임 | User Authorization / OAuth Scope |

## Practice 1 — Integration Decision

### Scenario A

CI 관리 서비스가 여러 Organization Repository의 Issue를 읽고 일부 PR Status를 관리합니다.

질문:

- 개인 PAT보다 GitHub App을 검토할 이유는?
- 어떤 최소 Permission이 필요한가?
- Installation Scope는 어디까지인가?

### Scenario B

외부 웹 앱이 사용자의 GitHub Profile과 Repository 정보를 사용자 동의 하에 읽습니다.

OAuth App Scenario와 비교합니다.

## Practice 2 — PAT Governance

가상의 정책을 작성합니다.

```text
Allowed PAT type/scope:
Maximum lifetime:
Approval requirement:
Rotation requirement:
Revocation process:
Owner:
Audit evidence:
```

## Practice 3 — Rate Limits

PAT와 GitHub App이 API Rate Limit을 가질 수 있음을 전제로 다음을 설계합니다.

```text
Current API usage:
Expected growth:
Rate-limit response handling:
Retry/backoff:
Monitoring:
```

## Practice 4 — App Approval

외부 App 요청을 다음 기준으로 평가합니다.

- Business need
- Publisher trust
- Requested Permissions
- Repository Scope
- Data accessed
- Write capability
- Secret/Key management
- Revocation plan

## Challenge

`자동화에는 PAT가 가장 간단하므로 항상 PAT가 최선이다`라는 주장에 반박하세요.

## Verify

- [ ] PAT / GitHub App / OAuth App 차이 설명
- [ ] GitHub App의 Installation/Permission 모델 설명
- [ ] PAT 최소 권한·수명 관리 설명
- [ ] Rate Limit이 Integration 설계에 미치는 영향 설명
- [ ] App Approval / Denial Policy 기준 작성

## 안전

실제 Token, Client Secret, Private Key 값을 Repository에 저장하지 않습니다.

---
[← Lab 070](../070-security-features-response/README.md) · [Lab 090 →](../090-actions-governance/README.md)
