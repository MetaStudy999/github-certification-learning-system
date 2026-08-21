# Lab 010 — Git Basics

## Objective

Local Repository를 만들고 **수정 → Stage → Commit → Log 확인** 흐름을 직접 수행합니다.

## 준비

터미널에서 확인합니다.

```bash
git --version
```

사용자 정보가 없다면 설정합니다.

```bash
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
```

## Practice 1 — Repository 생성

```bash
mkdir github-foundations-lab
cd github-foundations-lab
git init
```

확인:

```bash
git status
```

## Practice 2 — 첫 파일 만들기

```bash
printf "# GitHub Foundations Lab\n" > README.md
git status
```

핵심 질문:

> Git이 파일을 알고는 있지만 아직 Commit에 포함하지 않은 상태는 무엇인가?

## Practice 3 — Staging

```bash
git add README.md
git status
```

## Practice 4 — Commit

```bash
git commit -m "docs: add initial README"
```

확인:

```bash
git log --oneline
```

## Practice 5 — 변경 후 두 번째 Commit

```bash
printf "\nLearning Git and GitHub basics.\n" >> README.md
git diff
git add README.md
git diff --staged
git commit -m "docs: describe lab purpose"
```

## 개념 연결

```text
Working Directory
     ↓ git add
Staging Area
     ↓ git commit
Local Repository
```

## Challenge

자료를 보지 않고 다음을 수행합니다.

1. `notes.md` 생성
2. 한 줄 작성
3. 변경 상태 확인
4. Stage
5. Commit
6. Commit 이력을 한 줄 형식으로 확인

## Verify

다음 결과를 확인합니다.

```bash
git status
git log --oneline --decorate -5
```

성공 기준:

- `git status`에 예상하지 않은 변경이 없다.
- 최소 3개의 Commit이 존재한다.
- 각 Commit Message가 작업 내용을 설명한다.

## Evidence

[`../../../150-evidence/`](../../../150-evidence/)에 다음을 기록할 수 있습니다.

- 실행 날짜
- 사용 OS
- `git --version`
- 마지막 `git log --oneline` 결과
- 어려웠던 점 1개
- 다시 설명할 개념 1개

## Exam Link

이 Lab은 다음 시험영역과 연결됩니다.

- Version Control의 목적
- Repository
- Commit
- Git 기본 개념

---

[← Labs](../README.md) · [다음 Lab 020 →](../020-remote-repository/README.md)
