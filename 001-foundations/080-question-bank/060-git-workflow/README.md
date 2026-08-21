# 060 Git Workflow — Q051–Q060

> GH-900 학습목표 기반 자체 제작 문제입니다.

### Q051
새 Repository에서 Git 추적을 시작하는 명령은?
A. `git init`  
B. `git push`  
C. `git fetch`  
D. `git fork`

<details><summary>정답</summary>

**A** — `git init`은 현재 디렉터리를 Git Repository로 초기화합니다.
</details>

### Q052
현재 변경 상태와 Staging 여부를 확인하는 명령은?
A. `git status`  
B. `git merge`  
C. `git tag`  
D. `git clone`

<details><summary>정답</summary>

**A** — `git status`는 Working Tree와 Staging 상태를 보여 줍니다.
</details>

### Q053
현재 Branch에서 새 Branch를 만들고 바로 전환하려면?
A. `git switch -c feature/docs`  
B. `git fetch -c feature/docs`  
C. `git add feature/docs`  
D. `git commit feature/docs`

<details><summary>정답</summary>

**A** — `git switch -c`는 Branch 생성과 전환을 함께 수행합니다.
</details>

### Q054
Local Commit을 Remote Repository로 보내는 명령은?
A. `git push`  
B. `git fetch`  
C. `git status`  
D. `git log`

<details><summary>정답</summary>

**A** — Push는 Local Commit을 Remote로 전송합니다.
</details>

### Q055
Remote 변경을 가져와 현재 Branch에 통합하려면?
A. `git pull`  
B. `git add`  
C. `git init`  
D. `git remote -v`

<details><summary>정답</summary>

**A** — Pull은 Remote 변경 가져오기와 통합을 수행합니다.
</details>

### Q056
Remote URL을 확인하는 명령은?
A. `git remote -v`  
B. `git status -u`  
C. `git branch --url`  
D. `git pull --show`

<details><summary>정답</summary>

**A** — `git remote -v`는 연결된 Remote 이름과 URL을 표시합니다.
</details>

### Q057
Commit 이력을 한 줄 형식으로 확인하는 명령은?
A. `git log --oneline`  
B. `git push --short`  
C. `git status --log`  
D. `git add --history`

<details><summary>정답</summary>

**A** — `git log --oneline`은 Commit 이력을 압축해 표시합니다.
</details>

### Q058
`git fetch` 후 현재 Branch에 변경을 적용하려면 추가로 필요한 것은?
A. Merge 또는 Rebase 같은 통합 작업  
B. Fork  
C. Star  
D. Discussion 생성

<details><summary>정답</summary>

**A** — Fetch는 변경 정보를 가져오지만 현재 Branch에 자동 반영하지 않습니다.
</details>

### Q059
같은 Repository에서 기능별 변경을 독립적으로 관리하는 가장 적절한 방법은?
A. Branch  
B. 매번 새 Enterprise 생성  
C. Star  
D. Wiki

<details><summary>정답</summary>

**A** — Branch는 같은 Repository 안에서 독립 작업선을 제공합니다.
</details>

### Q060
Merge의 목적은?
A. 한 Branch의 변경을 다른 Branch에 통합  
B. Repository를 Fork  
C. GitHub 계정을 생성  
D. Issue를 Label로 변경

<details><summary>정답</summary>

**A** — Merge는 Branch 간 변경 이력을 통합합니다.
</details>

**관련 Lab:** `../../060-labs/010-git-basics/`, `020-remote-repository/`, `030-branch-workflow/`
