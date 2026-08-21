# 020 Terms — 필수 용어

## 빠른 시작 (Quick Start, QS)

용어는 **영문 원문 → 약어 → 한국어 뜻 → 한 문장 설명** 순서로 학습합니다.

## A. Git / 버전 제어 (Git / Version Control, GVC)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| Version Control | 버전 관리 | 파일의 변경 이력을 기록하고 과거 상태를 추적하는 방식 |
| Git | 깃 | 분산 버전 관리 시스템 |
| Repository, Repo | 저장소 | 프로젝트 파일과 변경 이력을 보관하는 단위 |
| Working Directory | 작업 디렉터리 | 현재 직접 수정하는 파일 영역 |
| Staging Area / Index | 스테이징 영역 | 다음 Commit에 포함할 변경을 준비하는 영역 |
| Commit | 커밋 | 특정 시점의 변경사항을 기록한 단위 |
| Branch | 브랜치 | 독립적인 작업 흐름을 만드는 분기 |
| Merge | 병합 | 서로 다른 Branch의 변경을 결합하는 작업 |
| Clone | 복제 | Remote Repository를 Local로 내려받는 작업 |
| Remote | 원격 저장소 | 네트워크를 통해 접근하는 Repository 위치 |
| Push | 푸시 | Local Commit을 Remote에 올리는 작업 |
| Pull | 풀 | Remote 변경을 가져와 현재 Branch에 통합하는 작업 |
| Fetch | 페치 | Remote 변경 정보를 가져오되 자동 병합하지 않는 작업 |
| Tag | 태그 | 특정 Commit에 버전명 등 고정 표식을 붙이는 기능 |

## B. GitHub 저장소 (GitHub Repository, GR)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| README | 소개 문서 | Repository의 목적·사용법을 설명하는 대표 문서 |
| LICENSE | 라이선스 | 코드·콘텐츠의 사용 조건을 명시하는 문서 |
| CONTRIBUTING | 기여 가이드 | 프로젝트에 기여하는 방법과 규칙을 설명하는 문서 |
| CODEOWNERS | 코드 소유자 | 특정 경로의 검토 책임자를 정의하는 파일 |
| SECURITY | 보안 정책 | 취약점 제보 방법 등 보안 정책을 설명하는 문서 |
| Repository Template | 저장소 템플릿 | 유사 Repository를 빠르게 생성하기 위한 원본 |
| Visibility | 공개 범위 | Public, Private 등의 Repository 접근 수준 |
| Branch Protection | 브랜치 보호 | 중요한 Branch의 변경·병합 조건을 강제하는 규칙 |
| Ruleset | 규칙 집합 | Branch나 Tag에 적용할 정책을 중앙에서 정의하는 기능 |

## C. 협업 (Collaboration, C)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| Issue | 이슈 | 버그·작업·요구사항을 추적하는 협업 단위 |
| Pull Request, PR | 풀 리퀘스트 | Branch 변경을 검토하고 병합하도록 제안하는 기능 |
| Review | 리뷰 | Pull Request의 코드·변경을 검토하는 과정 |
| Discussion | 토론 | Q&A·아이디어·공지 등 장기적인 커뮤니티 대화 공간 |
| Mention | 멘션 | `@username`으로 사용자의 주의를 호출하는 기능 |
| Assignee | 담당자 | Issue 또는 PR의 책임자로 지정된 사용자 |
| Label | 라벨 | Issue·PR을 분류하는 태그 |
| Milestone | 마일스톤 | 여러 Issue·PR을 특정 목표나 기간으로 묶는 기능 |
| Notification | 알림 | 관심 Repository와 협업 활동의 업데이트 전달 기능 |
| Fork | 포크 | 다른 Repository를 자신의 계정 공간으로 복제해 독립 개발하는 방식 |

## D. GitHub 제품 / 현대적 개발 (GitHub Products / Modern Development, GPMD)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| GitHub 액션 (GitHub Actions, GHACT / GH-200) | 깃허브 액션 | Workflow 기반 CI/CD와 자동화 플랫폼 |
| Workflow | 워크플로 | Event에 의해 실행되는 자동화 정의 |
| GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) | 깃허브 코파일럿 | AI 기반 개발 보조 기능 |
| GitHub Codespaces | 깃허브 코드스페이스 | 클라우드 기반 개발 환경 |
| Dev Container | 개발 컨테이너 | 재현 가능한 개발환경을 코드로 정의하는 방식 |
| GitHub Projects | 깃허브 프로젝트 | Issue·PR 중심의 프로젝트 관리 도구 |
| GitHub Pages | 깃허브 페이지 | Repository 콘텐츠로 정적 웹사이트를 배포하는 기능 |
| GitHub Gist | 깃허브 기스트 | 코드 조각·메모를 간단히 공유하는 기능 |
| GitHub Wiki | 깃허브 위키 | Repository별 장문 문서 공간 |

## E. 계정 / 보안 / 관리 (Account / Security / Administration, ASA)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| Personal Account | 개인 계정 | 개인 사용자의 GitHub 계정 |
| Organization | 조직 | 여러 사용자·Team·Repository를 공동 관리하는 단위 |
| Enterprise | 엔터프라이즈 | 여러 Organization과 정책을 상위 수준에서 관리하는 단위 |
| Team | 팀 | Organization 내부 사용자 그룹 |
| Role | 역할 | 사용자가 수행할 수 있는 관리 범위를 나타내는 역할 |
| Permission | 권한 | 특정 자원에 Read/Write/Admin 등으로 접근 가능한 수준 |
| Two-Factor Authentication, 2FA | 2단계 인증 | 비밀번호 외 추가 인증 요소를 요구하는 보안 방식 |
| Passkey | 패스키 | 공개키 암호 기반의 비밀번호 대체 인증 방식 |
| Enterprise Managed Users, EMU | 엔터프라이즈 관리 사용자 | 기업이 사용자 계정 생명주기를 중앙 관리하는 방식 |

## F. 커뮤니티 / 오픈 소스 (Community / Open Source, COS)

| 용어 | 한국어 | 한 문장 설명 |
|---|---|---|
| Open Source | 오픈 소스 | 소스코드를 공개하고 라이선스에 따라 사용·기여하는 개발 방식 |
| InnerSource | 이너소스 | 조직 내부 개발에 오픈소스 협업 방식을 적용하는 방법 |
| GitHub Sponsors | 깃허브 스폰서 | 오픈소스 개발자를 재정적으로 후원하는 기능 |
| GitHub Marketplace | 깃허브 마켓플레이스 | GitHub와 연동되는 App·Action 등을 찾는 공간 |
| Star | 스타 | Repository에 관심을 표시하고 나중에 찾기 쉽게 하는 기능 |
| Watch | 구독 | Repository 활동 알림을 받도록 설정하는 기능 |

## 암기보다 중요한 비교

- **Git ≠ GitHub**
- **Clone ≠ Fork**
- **Fetch ≠ Pull**
- **Issue ≠ Discussion**
- **Organization ≠ Enterprise**
- **Role ≠ Permission**
- **GitHub Pages ≠ Wiki ≠ Gist**
- **Actions ≠ Codespaces ≠ Copilot**

## 완료 체크

- [ ] 위 용어를 보고 1문장으로 설명할 수 있다.
- [ ] 영문 용어를 보고 한국어 의미를 말할 수 있다.
- [ ] 유사 개념 비교 8개를 설명할 수 있다.
- [ ] 실제 GitHub 화면에서 주요 기능 위치를 찾을 수 있다.

---

[← 010 Overview](../010-overview/README.md) · [다음: 030 Concepts →](../030-concepts/README.md)
