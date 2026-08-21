# 030 Concepts — 핵심 개념

## Quick Start

용어를 따로 암기하지 않고 **흐름과 관계**로 연결합니다.

## 1. Git과 GitHub

```text
Git
└─ 내 컴퓨터와 여러 환경에서 변경 이력을 관리하는 분산 버전 관리 시스템

GitHub
└─ Git Repository를 호스팅하고 협업·자동화·보안·프로젝트 관리를 제공하는 플랫폼
```

핵심: **Git은 버전 관리 기술, GitHub는 Git을 중심으로 협업하는 플랫폼**입니다.

## 2. Local → Remote 흐름

```text
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Local Repository
      ↓ git push
Remote Repository (GitHub)
```

반대 방향:

```text
GitHub Remote
   ↓ git fetch / git pull
Local Repository
```

## 3. Branch와 Pull Request

```text
main
 │
 └── feature/login
        │
        ├─ commit A
        ├─ commit B
        │
        └─ Pull Request
              ↓
            Review
              ↓
             Merge
              ↓
             main
```

Branch는 **작업 분리**, Pull Request는 **변경 제안·검토·논의·병합의 협업 단위**입니다.

## 4. GitHub Flow

```text
Issue / 작업 정의
   ↓
Branch 생성
   ↓
Commit
   ↓
Push
   ↓
Pull Request
   ↓
Review + Checks
   ↓
Merge
   ↓
Branch 정리
```

시험에서는 각 단계의 목적을 상황형으로 구분할 수 있어야 합니다.

## 5. Clone vs Fork

| 항목 | Clone | Fork |
|---|---|---|
| 목적 | Repository를 Local로 복제 | 다른 Repository를 자신의 GitHub 공간에 복제 |
| 위치 | Local | GitHub 계정/Organization |
| 일반적 사용 | 직접 개발 | 외부 프로젝트 기여·독립 실험 |
| 원본과의 관계 | 같은 Remote를 대상으로 작업 가능 | 원본(Upstream)과 별도 Repository |

## 6. Issue vs Discussion vs Pull Request

| 기능 | 주된 목적 |
|---|---|
| Issue | 버그·기능·작업 추적 |
| Discussion | 아이디어·질문·공지·커뮤니티 토론 |
| Pull Request | 코드/파일 변경 검토와 병합 |

## 7. Repository 문서의 역할

```text
README       → 이 프로젝트가 무엇인가?
LICENSE      → 어떻게 사용할 수 있는가?
CONTRIBUTING → 어떻게 기여하는가?
CODEOWNERS   → 누가 검토 책임자인가?
SECURITY     → 보안 문제는 어떻게 제보하는가?
```

## 8. GitHub 제품 구분

| 제품/기능 | 해결하는 문제 |
|---|---|
| Actions | 반복 작업·CI/CD 자동화 |
| Copilot | AI 기반 코드·개발 보조 |
| Codespaces | 어디서나 재현 가능한 클라우드 개발환경 |
| Projects | Issue·PR 기반 일정·업무 관리 |
| Pages | 정적 웹사이트 공개 |
| Wiki | Repository 지식 문서화 |
| Gist | 작은 코드·메모 공유 |

## 9. 계정과 관리 계층

```text
Enterprise
  └─ Organization
       ├─ Team
       │    └─ Members
       └─ Repository
```

- **Enterprise:** 여러 Organization의 상위 거버넌스
- **Organization:** Repository·Team·구성원을 공동 관리
- **Team:** 구성원을 목적별 그룹화
- **Repository:** 실제 프로젝트 단위

## 10. Role과 Permission

Role은 관리상 맡은 역할을, Permission은 특정 Resource에서 할 수 있는 작업 범위를 설명할 때 사용합니다.

시험에서는 다음 관점으로 구분합니다.

```text
누구인가?        → User / Member / Team
어디에 속하는가? → Organization / Repository
무엇을 할 수 있나? → Role / Permission
어떤 규칙인가?   → Policy / Ruleset / Branch Protection
```

## 11. 기본 보안 흐름

```text
Account Security
 ├─ Strong authentication
 ├─ 2FA
 └─ Passkey

Repository Security
 ├─ Visibility
 ├─ Permissions
 ├─ Branch Protection
 └─ Rulesets
```

## 12. Open Source와 InnerSource

- **Open Source:** 조직 경계를 넘어 공개적으로 협업
- **InnerSource:** 오픈소스 협업 원칙을 조직 내부 코드에 적용

## 핵심 비교 자가시험

자료 없이 다음을 설명해 보세요.

1. Git vs GitHub
2. Clone vs Fork
3. Fetch vs Pull
4. Branch vs Fork
5. Issue vs Discussion
6. PR vs Merge
7. Organization vs Enterprise
8. Role vs Permission
9. Actions vs Codespaces
10. Open Source vs InnerSource

---

[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
