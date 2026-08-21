# 020 Terms — GitHub 관리 (GitHub Administration, GHADM / GH-100) 핵심 용어

## 빠른 시작 (Quick Start, QS)

용어는 **영문 원문 + 약어 + 한국어 의미 + 관리 Scenario**로 학습합니다.

## Enterprise / Deployment

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| GitHub Enterprise | - | GitHub의 기업용 관리 범위 |
| GitHub Enterprise Cloud | GHEC | GitHub가 운영하는 Enterprise Cloud |
| GitHub Enterprise Server | GHES | 조직이 인프라에서 운영하는 Enterprise Server |
| Enterprise Managed Users | EMU | 기업 IdP 중심으로 관리되는 사용자 계정 방식 |
| Data Residency | - | 특정 지역에 기업 데이터 저장 위치를 관리하는 옵션/배포 특성 |
| Enterprise Account | - | 여러 Organization과 Enterprise 설정을 관리하는 상위 계정 |
| Organization | Org | Repository, Team, Member를 관리하는 조직 단위 |
| Enterprise Team | - | Enterprise 수준에서 관리·활용하는 Team 개념 |

## Identity / Authentication

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| Identity Provider | IdP | 사용자 인증 정보를 관리하는 외부 ID 제공자 |
| Authentication | AuthN | 사용자가 누구인지 확인 |
| Authorization | AuthZ | 사용자가 무엇을 할 수 있는지 결정 |
| Security Assertion Markup Language | SAML | SSO에 널리 쓰이는 인증 표준 |
| Single Sign-On | SSO | 하나의 기업 인증으로 여러 서비스 접근 |
| System for Cross-domain Identity Management | SCIM | 사용자 Provisioning/Deprovisioning 자동화 표준 |
| Team Synchronization | - | IdP 그룹과 GitHub Team의 멤버십 동기화 |
| Two-Factor Authentication | 2FA | 두 가지 요소를 사용하는 계정 인증 강화 |
| Provisioning | - | 사용자/계정을 생성·배정하는 과정 |
| Deprovisioning | - | 접근 권한과 계정을 회수·비활성화하는 과정 |

## Access / Governance

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| Role | - | 관리·사용자 역할 |
| Permission | - | 리소스에 허용되는 작업 수준 |
| Least Privilege | - | 필요한 최소 권한만 부여하는 원칙 |
| Policy | - | Enterprise/Organization 수준 사용 규칙 |
| Ruleset | - | Branch/Tag 등에 적용하는 규칙 집합 |
| Audit | - | 접근·설정·행동을 점검하는 활동 |
| Audit Log | - | 관리·사용 이벤트 기록 |

## Security / Compliance

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| GitHub 고급 보안 (GitHub Advanced Security, GHAS / GH-500) | GHAS | GitHub의 고급 보안 기능 묶음 |
| Secret Scanning | - | 노출된 Secret 탐지 |
| CodeQL | - | 코드 기반 보안 분석 기술 |
| Dependabot | - | Dependency 업데이트·취약점 관리 기능 |
| Security Advisory | - | 취약점의 비공개 협업·공개 안내 기능 |
| Security Response Plan | - | 보안 사고/취약점 대응 절차 |
| Personal Access Token | PAT | API/Git 인증 등에 사용하는 사용자 토큰 |
| GitHub App | - | GitHub 리소스에 설치해 권한을 부여하는 통합 방식 |
| OAuth App | - | 사용자 위임 OAuth 인증 기반 애플리케이션 |
| Rate Limit | - | API 호출량 제한 |

## Actions / Runner / Network

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| GitHub 액션 (GitHub Actions, GHACT / GH-200) | - | Workflow 자동화 플랫폼 |
| Reusable Workflow | - | 여러 Workflow에서 재사용 가능한 Workflow |
| Runner Group | - | Self-hosted Runner 접근 범위를 관리하는 그룹 |
| GitHub-hosted Runner | - | GitHub가 관리하는 Runner |
| Self-hosted Runner | - | 조직이 설치·운영하는 Runner |
| IP Allow List | - | 허용된 IP 범위로 접근을 제한하는 설정 |
| Azure Private Networking | - | Actions와 Azure Network를 Private하게 연결하는 방식 |
| Encrypted Secret | - | Workflow에서 사용하는 암호화된 Secret |
| Vault | - | Secret을 중앙 관리하는 외부 비밀 저장소 |

## Operations / Cost

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| Support Bundle | - | GitHub Support 문제 해결에 필요한 진단 자료 묶음 |
| Diagnostics | - | 시스템 상태를 분석하기 위한 진단 정보 |
| Metered Product | - | 사용량에 따라 비용이 측정되는 제품/기능 |
| License Consumption | - | 라이선스 사용 현황 |
| Adoption | - | 사용자·팀의 기능 채택 정도 |
| Utilization | - | 기능·라이선스·Resource 사용 정도 |

## 반드시 구분

```text
GHEC             ↔ GHES
EMU              ↔ Personal Account
Authentication   ↔ Authorization
SAML SSO         ↔ SCIM
SCIM             ↔ Team Synchronization
Role             ↔ Permission
Policy           ↔ Ruleset
GitHub App       ↔ OAuth App
PAT              ↔ GitHub App credential model
GitHub-hosted    ↔ Self-hosted Runner
Admin            ↔ GitHub Support
Audit Log        ↔ Diagnostics
License          ↔ Metered Usage
```

## 완료 기준

- [ ] `GHEC`, `GHES`, `EMU`, `IdP`, `SSO`, `SAML`, `SCIM`, `PAT`, `GHAS`를 풀어 말할 수 있다.
- [ ] SAML과 SCIM의 목적을 구분한다.
- [ ] GitHub App과 OAuth App을 구분한다.
- [ ] Admin과 GitHub Support의 책임 경계를 설명한다.
- [ ] Runner와 Secret 관리가 Enterprise Governance에 왜 필요한지 설명한다.

---
[← 010 Overview](../010-overview/README.md) · [다음: 030 Concepts →](../030-concepts/README.md)
