# 050 Guides — 입문자 학습 가이드

## 빠른 시작 (Quick Start, QS)

각 개념을 다음 순서로 이해합니다.

```text
왜 필요한가?
  ↓
무엇인가?
  ↓
언제 사용하는가?
  ↓
직접 해보기
  ↓
비슷한 개념과 비교
  ↓
시험 상황형 문제로 확인
```

## 1. Version Control을 왜 쓰는가?

파일 이름을 `final.py`, `final2.py`, `really-final.py`처럼 복사해서 관리하면 누가 무엇을 언제 바꿨는지 추적하기 어렵습니다.

Version Control (버전 관리)은 변경 이력을 체계적으로 기록해 **복구, 비교, 협업, 병렬 개발**을 가능하게 합니다.

## 2. Git은 무엇인가?

Git은 각 개발자가 Repository의 이력을 자신의 환경에 가지고 작업할 수 있는 **Distributed Version Control System, DVCS (분산 버전 관리 시스템)** 입니다.

가장 먼저 다음 흐름을 이해합니다.

```text
파일 수정
→ git add
→ git commit
→ git push
→ GitHub
```

## 3. GitHub는 무엇인가?

GitHub는 Git Repository 호스팅만 하는 서비스가 아닙니다.

```text
Git Repository
+
Collaboration
+
Project Management
+
Automation
+
Security
+
AI Development
```

을 하나의 플랫폼에서 제공합니다.

## 4. Branch는 왜 필요한가?

`main`에서 바로 모든 작업을 하면 미완성 변경이 안정된 코드에 섞일 수 있습니다.

Branch를 사용하면 작업을 분리할 수 있습니다.

```text
main ────────────────●
       \
        feature ─●─●─┘
```

## 5. Pull Request는 무엇인가?

Pull Request, PR (풀 리퀘스트)는 단순한 Merge 버튼이 아닙니다.

PR에서 할 수 있는 일:

- 변경 내용 설명
- 관련 Issue 연결
- 코드 Review
- 자동 Check 확인
- Discussion
- 승인 후 Merge

## 6. Issue와 Discussion은 어떻게 구분하는가?

**Issue**를 선택하기 쉬운 상황:

- 버그 수정
- 기능 개발
- 명확한 할 일
- 담당자·Label·Milestone이 필요한 작업

**Discussion**을 선택하기 쉬운 상황:

- 아이디어 제안
- Q&A
- 커뮤니티 의견 수렴
- 공지

## 7. Repository 문서를 왜 나누는가?

| 문서 | 질문 |
|---|---|
| README | 이 프로젝트는 무엇인가? |
| LICENSE | 이 자료를 어떻게 사용할 수 있는가? |
| CONTRIBUTING | 어떻게 기여하는가? |
| CODEOWNERS | 누가 이 변경을 검토해야 하는가? |
| SECURITY | 취약점을 어떻게 안전하게 신고하는가? |

## 8. Actions / Copilot / Codespaces 구분

### GitHub 액션 (GitHub Actions, GHACT / GH-200)

> 사람이 반복하던 Build, Test, Deploy 등을 자동화

### GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300)

> 개발자가 코드를 이해·작성·수정하는 과정을 AI로 보조

### GitHub Codespaces

> 개발환경을 클라우드에서 빠르게 준비하고 재현

## 9. 시험 문제를 읽는 방법

상황형 문제에서 먼저 **요구 목적**을 찾습니다.

예:

```text
"외부 사용자가 원본 Repository에 직접 쓰기 권한 없이 기여하려고 한다."
```

핵심어:

```text
외부 사용자
+ 원본 직접 쓰기 권한 없음
+ 기여
```

생각할 흐름:

```text
Fork
→ 자신의 Branch에서 변경
→ 원본 Repository로 Pull Request
```

## 10. 오답 분석 방법

오답마다 하나의 원인을 선택합니다.

```text
CONCEPT  개념을 몰랐다
COMPARE  비슷한 기능을 혼동했다
READING  문제 조건을 놓쳤다
MEMORY   알고 있었지만 기억하지 못했다
PRACTICE 실제 사용 경험이 부족했다
```

## 완료 체크

- [ ] Git과 GitHub의 차이를 초보자에게 설명할 수 있다.
- [ ] Issue → Branch → Commit → PR → Review → Merge를 설명할 수 있다.
- [ ] Clone과 Fork를 상황에 따라 고를 수 있다.
- [ ] Actions/Copilot/Codespaces를 구분할 수 있다.
- [ ] Repository 핵심 문서의 목적을 구분할 수 있다.

---

[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
