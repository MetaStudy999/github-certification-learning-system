# 실습 (Lab, LAB) 100 — 커뮤니티 기여 (Community Contribution, CC)

> **Fork → Clone → Branch → Commit → Push → Pull Request**

## 000. 빠른 시작 (Quick Start, QS)

이 Lab에서는 다른 사람의 Repository에 직접 Push 권한이 없더라도 Fork를 이용해 변경을 제안하는 오픈소스 기여 흐름을 이해합니다.

실제 외부 프로젝트에 불필요한 PR을 보내지 마세요. 가능하면 본인의 연습 Repository 2개를 사용하거나 GitHub Skills 등 학습용 환경을 사용합니다.

## 010. Objective (목표)

완료 후 다음을 설명하고 수행할 수 있어야 합니다.

- Fork(포크)와 Clone(클론)의 차이
- Upstream과 Origin의 역할
- Fork 기반 Branch 작업
- 원본 Repository로 Pull Request를 보내는 흐름
- 오픈소스 기여 전 `CONTRIBUTING.md`를 확인해야 하는 이유

## 020. Concept (개념)

```text
Original Repository (upstream)
          │
          └── Fork
                ↓
      My GitHub Repository
             (origin)
                ↓
              Clone
                ↓
        Local Repository
                ↓
              Branch
                ↓
         Commit / Push
                ↓
         Pull Request
                ↓
      Original Repository
```

### Fork와 Clone 비교 (Fork vs Clone, FC)

| 구분 | Fork | Clone |
|---|---|---|
| 위치 | GitHub 서버 | 로컬 컴퓨터 |
| 목적 | 다른 Repository를 내 계정 영역에 복사 | Repository를 로컬에 내려받기 |
| 대표 상황 | 오픈소스 기여 | 로컬 개발 |

## 030. Practice (따라하기)

### 031. 학습용 원본 Repository 준비

다음 중 하나를 사용합니다.

1. 본인이 만든 별도 공개 연습 Repository
2. 기여가 허용된 공식 학습용 Repository
3. 이미 Fork 실습을 위해 준비한 Sandbox

실제 프로젝트의 기여 지침을 먼저 확인합니다.

```text
README.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
```

### 032. Fork 생성

GitHub 웹에서 **Fork**를 선택해 내 계정 아래에 복사본을 만듭니다.

확인:

```text
Original: <owner>/<repository>
Fork:     <my-account>/<repository>
```

### 033. Fork를 Clone

```bash
git clone <fork-url>
cd <repository>
git remote -v
```

기본적으로 내 Fork가 `origin`으로 연결되는지 확인합니다.

### 034. Upstream 추가

원본 Repository URL을 `upstream`으로 추가합니다.

```bash
git remote add upstream <original-repository-url>
git remote -v
```

개념:

```text
origin   = 내 Fork
upstream = 원본 Repository
```

### 035. Branch 생성

```bash
git switch -c docs/contribution-practice
```

작은 문서 변경을 수행합니다.

### 036. Commit과 Push

```bash
git status
git add .
git commit -m "docs: practice contribution workflow"
git push -u origin docs/contribution-practice
```

### 037. Pull Request 생성

GitHub에서 다음 방향을 반드시 확인합니다.

```text
base repository: original/upstream repository
head repository: my fork
```

기여 지침에 맞는 제목과 본문을 작성합니다.

학습용 Repository가 아니라면 유지관리자에게 불필요한 PR을 생성하지 않습니다.

### 038. Upstream 변경 가져오기 개념

원본이 변경되었다면 다음 개념을 이해합니다.

```bash
git fetch upstream
git switch main
git merge upstream/main
```

프로젝트 정책에 따라 rebase 또는 GitHub의 Sync fork 기능을 사용할 수도 있습니다.

이 Lab의 핵심은 명령어 한 가지를 외우는 것이 아니라 **Fork를 원본 변화와 동기화해야 할 수 있다는 점**입니다.

## 040. Challenge (스스로 해보기)

자료 없이 다음 흐름을 설명합니다.

```text
원본 Repository
→ Fork
→ Clone
→ upstream 설정
→ Branch
→ Commit
→ Push to origin
→ PR to upstream
```

그리고 다음 질문에 답합니다.

1. Fork와 Clone은 어디에 만들어지는가?
2. `origin`은 무엇을 가리키는가?
3. `upstream`은 무엇을 가리키는가?
4. 왜 원본 프로젝트의 CONTRIBUTING을 먼저 확인해야 하는가?

## 050. Verify (검증)

- [ ] Fork와 Clone의 차이를 설명할 수 있다.
- [ ] `origin`과 `upstream`을 구분할 수 있다.
- [ ] Fork 기반 Branch 작업을 수행했다.
- [ ] Pull Request의 base/head 방향을 설명할 수 있다.
- [ ] 기여 전 README/CONTRIBUTING을 확인해야 하는 이유를 설명할 수 있다.

## 060. Evidence (증거 기록)

```text
Original Repository:
Fork Repository:
origin:
upstream:
Branch:
Pull Request URL 또는 학습 결과:
배운 점:
```

## 070. Foundations 실습 완료 통과 기준 (Foundations Labs Completion Gate, FLCG)

Lab 010~100을 마쳤다면 다음을 확인합니다.

- [ ] Git 기본 작업
- [ ] Remote 연결
- [ ] Branch/Merge
- [ ] GitHub Flow
- [ ] Repository 문서
- [ ] Collaboration
- [ ] Projects
- [ ] Actions/Copilot/Codespaces 역할 구분
- [ ] Security 기본
- [ ] Fork 기반 Community Contribution

모두 설명·재현할 수 있다면 `060-labs` 단계의 상태를 **COMPLETED**로 기록할 수 있습니다.

---

[← Lab 090](../090-security-basics/README.md) · [Labs Index](../README.md)
