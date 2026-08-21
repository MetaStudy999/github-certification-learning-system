# 010 문제 세트 (Question Set, QS) — 기초 (Basics, B) (Q001–Q010)

> 자체 제작 학습문제입니다. 먼저 답을 고른 뒤 해설을 펼치세요.

## Q001
Git과 GitHub의 관계를 가장 정확하게 설명한 것은?

A. Git은 GitHub 웹사이트의 다른 이름이다.  
B. Git은 분산 버전 관리 시스템이고 GitHub는 Git Repository를 중심으로 협업 기능을 제공하는 플랫폼이다.  
C. GitHub가 없으면 Git Commit을 만들 수 없다.  
D. Git은 Remote Repository에서만 사용할 수 있다.

<details><summary>정답 및 해설</summary>

**정답: B**

Git은 Local에서도 독립적으로 사용할 수 있습니다. GitHub는 Repository 호스팅, Issue, Pull Request, Actions 등의 협업 기능을 제공합니다.

**오답 포인트:** A/C/D는 Git을 GitHub에 종속된 기술로 잘못 이해합니다.
</details>

## Q002
파일을 수정한 뒤 다음 Commit에 포함할 변경을 준비하는 영역은?

A. Staging Area  
B. Discussion  
C. Organization  
D. Marketplace

<details><summary>정답 및 해설</summary>

**정답: A** — `git add`로 변경을 Staging Area에 올린 뒤 Commit합니다.

**오답 포인트:** B/C/D는 Git의 Local 변경 준비 영역이 아닙니다.
</details>

## Q003
현재 Working Tree와 Staging 상태를 확인하는 명령은?

A. `git status`  
B. `git push`  
C. `git clone`  
D. `git tag`

<details><summary>정답 및 해설</summary>

**정답: A** — 변경 파일, Staged 여부 등을 확인합니다.
</details>

## Q004
Local Repository에 변경 이력을 하나의 Snapshot으로 기록하는 작업은?

A. Fork  
B. Commit  
C. Watch  
D. Deploy

<details><summary>정답 및 해설</summary>

**정답: B** — Commit은 Local Git 이력에 변경을 기록합니다.
</details>

## Q005
Local Commit을 Remote Repository로 보내는 명령은?

A. `git fetch`  
B. `git log`  
C. `git push`  
D. `git diff`

<details><summary>정답 및 해설</summary>

**정답: C** — Push는 Local Commit을 Remote로 전송합니다.
</details>

## Q006
Branch를 사용하는 가장 일반적인 이유는?

A. 모든 사용자의 계정을 삭제하기 위해  
B. `main`과 분리된 공간에서 변경을 개발하기 위해  
C. Repository를 자동으로 Private으로 바꾸기 위해  
D. Git 설치를 대신하기 위해

<details><summary>정답 및 해설</summary>

**정답: B** — 기능·수정 작업을 별도 Branch에서 진행하면 기본 Branch의 안정성을 유지하기 쉽습니다.
</details>

## Q007
Remote의 변경 정보를 가져오지만 현재 Branch에 자동 통합하지 않는 명령은?

A. `git fetch`  
B. `git pull`  
C. `git push`  
D. `git commit`

<details><summary>정답 및 해설</summary>

**정답: A** — Fetch는 Remote 추적 정보를 갱신하지만 현재 Branch에 자동 Merge/Rebase하지 않습니다.

**오답 포인트:** Pull은 일반적으로 가져오기와 통합을 함께 수행합니다.
</details>

## Q008
새 Local Repository를 초기화하는 명령은?

A. `git init`  
B. `git merge`  
C. `git remote -v`  
D. `git restore`

<details><summary>정답 및 해설</summary>

**정답: A**
</details>

## Q009
Commit 이력을 한 줄 형식으로 확인하려고 한다. 가장 적합한 명령은?

A. `git add .`  
B. `git log --oneline`  
C. `git push -u origin main`  
D. `git clean`

<details><summary>정답 및 해설</summary>

**정답: B** — Commit SHA와 메시지를 간결하게 확인할 수 있습니다.
</details>

## Q010
다음 중 인터넷 연결 없이도 수행 가능한 작업은?

A. Local Commit 생성  
B. GitHub Pull Request 생성  
C. GitHub Discussion 게시  
D. Remote Repository Push

<details><summary>정답 및 해설</summary>

**정답: A** — Git의 Local 작업은 네트워크 없이도 가능합니다. B/C/D는 GitHub 또는 Remote 연결이 필요합니다.
</details>

## 자가 점검 (Self Check, SC)

- 9–10: PASS
- 8: 오답만 복습
- 7 이하: `070-exercises/010`과 Lab 010~030 재수행

---

[← Question Bank](../README.md) · [다음: 020 Repositories & Compare →](../020-repositories-compare/README.md)
