# 030 Concepts — GitHub 관리 (GitHub Administration, GHADM / GH-100) 핵심 개념

## 1. Enterprise Hierarchy

```text
Enterprise
  ↓
Organization
  ↓
Team / Enterprise Team
  ↓
Repository
  ↓
User / App / Workflow
```

관리자는 각 계층에서 **누가, 무엇에, 어떤 권한으로, 어떤 정책 아래 접근하는지**를 설계합니다.

## 2. Authentication vs Authorization

```text
Authentication (AuthN)
= 누구인가?

Authorization (AuthZ)
= 무엇을 할 수 있는가?
```

예:

```text
SAML SSO → 기업 Identity로 인증
Role / Permission → Repository에서 가능한 작업 결정
```

## 3. SAML / SCIM / Team Sync

| 기능 | 중심 질문 | 목적 |
|---|---|---|
| SAML SSO | 누구인가? | 기업 IdP 인증 |
| SCIM | 계정이 존재해야 하는가? | Provision / Deprovision 자동화 |
| Team Synchronization | 어느 Team에 속해야 하는가? | IdP 그룹과 Team 멤버십 연결 |

같은 Identity 영역이지만 해결하는 문제가 다릅니다.

## 4. EMU vs Personal Accounts

### Enterprise Managed Users

```text
Enterprise / IdP 중심
→ 계정 수명주기 관리
→ 조직 업무용 Identity 통제 강화
```

### Personal Accounts

```text
개인이 소유한 GitHub 계정
→ Enterprise/Organization에 Member로 참여
→ 기업 관리 범위와 개인 계정 소유가 분리
```

배포 모델 선택은 Identity 전략과 연결됩니다.

## 5. Deployment Decision

```text
Cloud 운영 선호?
 ├─ YES → GHEC
 │          ├─ Enterprise-managed identity 필요 → EMU 고려
 │          ├─ 특정 지역 Data Residency 필요 → Data Residency + EMU 고려
 │          └─ Personal account 협업 모델 → GHEC personal accounts
 │
 └─ NO / Server control 필요 → GHES 검토
```

실제 선택은 Security, Compliance, Network, Operations, Data Location, Identity 요구사항을 종합합니다.

## 6. Policy vs Ruleset

```text
Policy
→ Enterprise / Organization이 허용·금지·운영 기준을 정의

Ruleset
→ Branch / Tag 등 구체적인 Git 변경 규칙을 강제
```

정책은 Governance 방향을, Ruleset은 구체적인 Repository 규칙 집행을 담당한다고 이해하면 쉽습니다.

## 7. Secure Software Development

```text
Governance Policy
      ↓
Repository Security Features
      ├── Vulnerability Alerts
      ├── Secret Scanning
      ├── CodeQL
      └── Dependabot
      ↓
Security Advisory / Response Plan
      ↓
Audit / Reporting / Compliance
```

관리자는 보안 기능을 직접 사용하는 개발자 관점뿐 아니라 **활성화, 범위, Policy, 대응, 보고** 관점에서 봅니다.

## 8. PAT / GitHub App / OAuth App

| 수단 | 중심 | 관리 관점 |
|---|---|---|
| PAT | 사용자 기반 Token | Scope, 수명, 정책, 최소 권한 |
| GitHub App | GitHub 리소스에 설치 | 세밀한 권한, Installation 기반 접근 |
| OAuth App | 사용자 위임 | 사용자가 App에 권한을 위임 |

관리자는 `어떤 Integration을 허용할 것인가?`, `어떤 권한이 필요한가?`, `정책으로 승인/거부해야 하는가?`를 판단합니다.

## 9. Enterprise Actions Governance

```text
Workflow Reuse
      ↓
Action / Workflow Policy
      ↓
Runner Group
      ↓
Network Boundary
      ↓
Secrets / Vault
      ↓
Monitoring / Troubleshooting
```

Self-hosted Runner는 내부 Network 접근에 유리할 수 있지만 **OS Patch, Isolation, Credential, Capacity, Monitoring 책임**이 조직에 생깁니다.

## 10. Admin vs GitHub Support

### Admin이 먼저 처리

- 설정·정책·권한 확인
- 사용자/Team/Repository 구성
- Audit Log 분석
- Runner/Workflow 설정 확인
- 표준 Diagnostics 수행

### Support Escalation 후보

- GitHub 서비스 자체 문제 의심
- 문서화된 Admin 조치로 해결되지 않는 Platform 문제
- Support Bundle/Diagnostics가 필요한 심층 문제

핵심은 **무조건 Support로 보내거나 무조건 Admin이 해결하려 하지 않는 것**입니다.

## 11. Monitor → Optimize

```text
Audit / API / Usage Data
       ↓
Adoption / Activity / Underuse 분석
       ↓
License / Metered Usage 확인
       ↓
Policy / Resource / License 조정
       ↓
Cost + Performance 최적화
```

## 반드시 비교

| A | B | 핵심 차이 |
|---|---|---|
| AuthN | AuthZ | 신원 확인 vs 권한 결정 |
| SAML | SCIM | 인증 vs 계정 수명주기 |
| SCIM | Team Sync | 사용자 Provisioning vs Team 멤버십 |
| EMU | Personal Account | 기업 관리 계정 vs 개인 소유 계정 |
| GHEC | GHES | GitHub Cloud 운영 vs 조직 Server 운영 |
| Policy | Ruleset | Governance 규칙 vs Git 변경 규칙 집행 |
| PAT | GitHub App | 사용자 Token vs App Installation 기반 통합 |
| GitHub App | OAuth App | 리소스 설치 중심 vs 사용자 위임 중심 |
| GitHub-hosted | Self-hosted Runner | GitHub 운영 vs 조직 운영 |
| Audit Log | Support Bundle | 이벤트 추적 vs Support 진단 자료 |

---
[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
