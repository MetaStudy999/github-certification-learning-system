# Lab 030 — Branch Workflow

## Objective

Branch를 만들어 작업을 분리하고 Merge하는 기본 흐름을 익힙니다.

## Practice 1 — 현재 Branch 확인

```bash
git branch
git branch --show-current
```

## Practice 2 — 새 Branch 생성과 전환

```bash
git switch -c feature/profile
```

확인:

```bash
git branch
```

## Practice 3 — Branch에서 변경

```bash
printf "\n## Profile\nBranch workflow practice.\n" >> README.md
git add README.md
git commit -m "feat: add profile section"
```

## Practice 4 — main으로 돌아가기

```bash
git switch main
```

`README.md`를 확인해 `feature/profile`의 변경이 아직 `main`에 없는 것을 확인합니다.

## Practice 5 — Merge

```bash
git merge feature/profile
```

확인:

```bash
git log --oneline --graph --all --decorate
```

## Practice 6 — Branch 정리

```bash
git branch -d feature/profile
```

## 핵심 개념

```text
main
  │
  ├──── feature/profile
  │        │
  │        └─ commit
  │
  └──────── merge
```

Branch는 Repository를 통째로 복사하는 것이 아니라 **같은 Repository 안에서 독립적인 변경 흐름을 만드는 기능**입니다.

## Challenge

자료 없이 다음을 수행합니다.

1. `docs/terms` Branch 생성
2. `terms.md` 작성
3. Commit
4. `main`으로 이동
5. Merge
6. 작업 Branch 삭제

## Verify

```bash
git status
git branch
git log --oneline --graph --decorate --all -10
```

완료 질문:

- Branch와 Fork는 어떻게 다른가?
- Merge는 어떤 문제를 해결하는가?
- 왜 `main`에서 모든 작업을 직접 하지 않는가?

## Next Step

다음 실습에서는 이 Local Branch 흐름을 GitHub의 **Issue → Pull Request → Review → Merge** 협업 흐름으로 확장합니다.

---

[← Lab 020](../020-remote-repository/README.md) · [Labs 홈](../README.md)
