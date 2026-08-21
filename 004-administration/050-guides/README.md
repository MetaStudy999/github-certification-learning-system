# 050 Guides — GitHub 관리 (GitHub Administration, GHADM / GH-100) 입문자 가이드

## 빠른 시작 (Quick Start, QS)

Enterprise Administration은 화면 메뉴를 외우는 과정이 아니라 다음 질문에 답하는 과정입니다.

```text
누가 접근하는가?
→ 어떻게 인증하는가?
→ 무엇을 할 수 있는가?
→ 어떤 정책을 강제하는가?
→ 어떤 보안 기능을 켜는가?
→ 자동화는 어디에서 실행되는가?
→ 문제가 나면 누가 대응하는가?
→ 사용량과 비용은 적절한가?
```

## 1. Identity를 가장 쉽게 이해하기

```text
사람 / 계정
   ↓
IdP
   ↓
Authentication
   ↓
GitHub Enterprise
   ↓
Authorization
   ↓
Organization / Repository Access
```

### SAML SSO

`이 사람이 회사 구성원이 맞는가?`에 가까운 문제를 해결합니다.

### SCIM

`입사·이동·퇴사에 맞춰 GitHub 계정을 어떻게 생성·회수할 것인가?`에 가깝습니다.

### Team Sync

`IdP 그룹의 구성원을 어떤 GitHub Team에 넣을 것인가?`에 가깝습니다.

## 2. Access 설계

개별 사용자에게 직접 권한을 계속 주기보다 다음 구조를 우선 고려합니다.

```text
User
→ Team
→ Repository Role
→ Policy / Ruleset
```

원칙:

- Least Privilege
- Team 중심 관리
- 정기 Access Review
- 퇴사/이동 시 신속한 권한 회수

## 3. Deployment를 고르는 질문

```text
GitHub가 서비스 운영을 담당해도 되는가?
데이터 저장 지역 요구가 있는가?
계정을 Enterprise가 완전히 관리해야 하는가?
조직이 직접 Server를 운영해야 하는가?
```

이 질문으로 GHEC / EMU / Data Residency / GHES 선택을 좁힙니다.

## 4. Security Administrator 사고법

보안 기능 하나를 켜는 데서 끝나지 않습니다.

```text
Policy
→ Enable
→ Scope
→ Alert
→ Triage
→ Response
→ Audit / Report
```

예:

```text
Secret Scanning Alert
→ Owner 확인
→ Credential 폐기/회전
→ 노출 원인 수정
→ 재발 방지
→ Audit/Report
```

## 5. PAT / GitHub App / OAuth App 선택

### PAT

개별 사용자/Automation이 사용자 권한으로 API 접근해야 하는 제한적 Scenario.

### GitHub App

조직적으로 관리하는 Integration에 우선 검토할 수 있는 방식. Resource 설치와 세밀한 Permission 관리에 유리합니다.

### OAuth App

사용자가 애플리케이션에 자신의 GitHub 접근을 위임하는 Scenario.

시험 문제에서는 `무엇이 가능하냐`뿐 아니라 **더 관리 가능하고 최소 권한인 방식**을 찾습니다.

## 6. Actions 관리자 관점

개발자는 Workflow가 실행되는지 봅니다. 관리자는 다음을 봅니다.

```text
누가 어떤 Action을 쓸 수 있는가?
어떤 Workflow를 재사용할 것인가?
Runner를 누가 사용할 수 있는가?
어떤 Network에 접근할 수 있는가?
Secret Scope는 어디까지인가?
Runner Capacity와 장애는 어떤가?
```

## 7. Self-hosted Runner 주의

장점:

- 사내 Network 접근
- Custom Hardware/Software
- 운영 환경 제어

책임:

- OS Patch
- Runner Update
- Isolation
- Credential Exposure
- Capacity
- Monitoring
- Compromised Workflow Risk

따라서 `Self-hosted가 더 강력하니 항상 정답`이 아닙니다.

## 8. Admin vs Support

문제 발생 시:

```text
설정/권한/정책/로그 확인
→ Diagnostics 수행
→ 문서화된 Admin 해결 절차
→ Platform 문제 또는 미해결
→ GitHub Support + Support Bundle
```

## 9. Cost Optimization

비용 절감은 단순히 라이선스를 줄이는 것이 아닙니다.

```text
Usage Report
→ Active / Inactive
→ Metered Product Usage
→ Runner / Storage / Feature Utilization
→ Business Need
→ Optimize
```

## 10. 시험 Scenario 읽기

문제에서 먼저 찾습니다.

1. Deployment: Cloud / Server?
2. Identity: Managed / Personal?
3. Scope: Enterprise / Org / Repo?
4. Goal: Auth / Access / Security / Actions / Operations?
5. Constraint: Compliance / Network / Data Residency / Cost?
6. `FIRST`, `BEST`, `MOST appropriate`가 있는가?

---
[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
