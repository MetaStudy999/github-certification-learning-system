# 실습 (Lab, LAB) 040 — GitHub 플로 (GitHub Flow, GF)

> **Issue → Branch → Commit → Pull Request → Review → Merge**

## 000. 빠른 시작 (Quick Start, QS)

이 Lab의 목적은 GitHub 협업의 핵심 흐름을 한 번 끝까지 수행하는 것입니다.

권장 실습 Repository: `github-foundations-lab`

## 010. Objective (목표)

완료 후 다음을 설명하고 직접 수행할 수 있어야 합니다.

- Issue(이슈)를 작업의 시작점으로 사용한다.
- 작업용 Branch(브랜치)를 분리한다.
- Commit(커밋)으로 변경 이력을 남긴다.
- Pull Request, PR(풀 리퀘스트)로 변경을 제안한다.
- Review(리뷰) 후 Merge(병합)한다.
- Issue와 PR의 관계를 설명한다.

## 020. Concept (개념)

```text
Issue
  ↓
Branch
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Review / Checks
  ↓
Merge
  ↓
Issue Close
```

GitHub Flow는 짧게 유지되는 Branch와 Pull Request 중심의 협업 방식입니다.

## 030. Practice (따라하기)

### 031. Issue 만들기

Repository의 **Issues**에서 다음 예시로 Issue를 생성합니다.

```text
Title: docs: add study goal

Body:
- Add a study goal section to README.md
- Verify Markdown rendering
```

생성된 Issue 번호를 기록합니다.

```text
Issue: #____
```

### 032. Branch 만들기

로컬에서:

```bash
git switch main
git pull
git switch -c docs/add-study-goal
```

확인:

```bash
git branch
```

### 033. 파일 수정과 Commit

`README.md`에 간단한 학습 목표를 추가한 뒤:

```bash
git status
git add README.md
git commit -m "docs: add study goal"
```

### 034. Remote에 Push

```bash
git push -u origin docs/add-study-goal
```

### 035. Pull Request 생성

GitHub에서 새 Pull Request를 생성합니다.

예시 제목:

```text
docs: add study goal
```

본문에 Issue 연결 문구를 넣습니다.

```text
Closes #<issue-number>
```

### 036. 리뷰 (Review, R)

PR에서 다음을 확인합니다.

- 변경 파일(Files changed)
- Commit
- Conversation
- Checks가 있는 경우 결과

가능하다면 Review Comment를 하나 남기고 수정 후 다시 Push합니다.

### 037. 병합 (Merge, M)

검토가 끝났다면 PR을 Merge합니다.

그 후:

```bash
git switch main
git pull
```

Issue가 자동으로 닫혔는지 확인합니다.

## 040. Challenge (스스로 해보기)

자료를 보지 않고 다음 작업을 다시 수행합니다.

1. 새 Issue 생성
2. 새 Branch 생성
3. 파일 수정
4. Commit
5. Push
6. PR 생성
7. Issue 연결
8. Review
9. Merge
10. Local `main` 동기화

## 050. Verify (검증)

- [ ] Issue를 작업 단위로 만들었다.
- [ ] `main`에서 직접 작업하지 않고 Branch를 사용했다.
- [ ] Commit 메시지가 변경 목적을 설명한다.
- [ ] Pull Request를 생성했다.
- [ ] PR에서 Issue를 연결했다.
- [ ] 변경 내용을 Review했다.
- [ ] Merge 후 Local `main`을 최신 상태로 만들었다.

## 060. Evidence (증거 기록)

`../../150-evidence/`에 다음을 기록합니다.

```text
Issue URL:
Branch:
Commit SHA:
Pull Request URL:
Merge Commit / Result:
배운 점:
```

## 070. 시험 포인트

다음을 서로 구분할 수 있어야 합니다.

- Issue vs Pull Request
- Branch vs Fork
- Commit vs Merge
- Review vs Merge
- Local Branch vs Remote Branch

---

[← Labs](../README.md) · [다음: Lab 050 →](../050-repository-documentation/README.md)
