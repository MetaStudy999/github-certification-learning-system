# Lab 020 — Remote Repository

## Objective

Local Repository와 GitHub Remote Repository의 관계를 이해하고 `remote`, `push`, `fetch`, `pull`을 구분합니다.

## 준비

GitHub에서 실습용 빈 Repository를 하나 준비합니다.

권장 이름:

```text
github-foundations-lab
```

## Practice 1 — Remote 연결

Lab 010에서 만든 Local Repository에서 실행합니다.

```bash
git remote -v
```

Remote가 없다면 연결합니다.

```bash
git remote add origin https://github.com/YOUR_ID/github-foundations-lab.git
```

확인:

```bash
git remote -v
```

## Practice 2 — 기본 Branch 확인

```bash
git branch --show-current
```

필요하면 `main`으로 이름을 맞춥니다.

```bash
git branch -M main
```

## Practice 3 — Push

```bash
git push -u origin main
```

GitHub 웹에서 Commit과 README가 보이는지 확인합니다.

## Practice 4 — Fetch 이해

```bash
git fetch origin
```

`fetch`는 Remote의 새 정보를 가져오지만 현재 작업 Branch에 자동 병합하지 않습니다.

## Practice 5 — Pull 이해

```bash
git pull origin main
```

`pull`은 Remote 변경을 가져와 현재 Branch에 통합하는 흐름입니다.

## 핵심 비교

| 명령 | 방향 | 자동 통합 |
|---|---|---|
| `push` | Local → Remote | 해당 없음 |
| `fetch` | Remote 정보 → Local | 아니오 |
| `pull` | Remote → Local | 예, 현재 Branch에 통합 |

## Clone과의 차이

새 디렉터리에서 Repository 전체를 복제하려면:

```bash
git clone https://github.com/YOUR_ID/github-foundations-lab.git
```

`clone`은 기존 Remote Repository의 작업 복사본을 처음 만들 때 주로 사용합니다.

## Challenge

1. GitHub 웹에서 `remote-note.md`를 생성하고 Commit
2. Local에서 `git fetch origin` 실행
3. 현재 파일이 바로 생겼는지 확인
4. `git pull origin main` 실행
5. `remote-note.md`가 Local에 나타나는지 확인

## Verify

```bash
git remote -v
git status
git log --oneline --all --decorate -10
```

자료 없이 다음을 설명하면 완료입니다.

- Clone과 Pull의 차이
- Fetch와 Pull의 차이
- Push가 필요한 이유
- `origin`의 의미

---

[← Lab 010](../010-git-basics/README.md) · [다음 Lab 030 →](../030-branch-workflow/README.md)
