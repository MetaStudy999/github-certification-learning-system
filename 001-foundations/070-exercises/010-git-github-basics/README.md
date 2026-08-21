# 010 Exercise — Git & GitHub Basics

## 목표

Git과 GitHub의 역할을 구분하고 Local 작업 흐름을 직접 설명합니다.

## 문제

1. **Git**과 **GitHub**의 차이를 2문장으로 설명하세요.
2. Working Directory, Staging Area, Repository를 순서대로 연결하세요.
3. `git status`가 필요한 이유를 설명하세요.
4. 파일 수정 후 Commit까지 필요한 명령을 순서대로 작성하세요.
5. Commit과 Push의 차이를 설명하세요.
6. Branch를 사용하는 이유를 `main` 안정성 관점에서 설명하세요.
7. `git switch -c feature/docs`가 수행하는 일을 설명하세요.
8. Merge가 필요한 상황을 하나 만드세요.
9. `git fetch`와 `git pull`의 차이를 설명하세요.
10. 인터넷 연결이 없어도 가능한 Git 작업 3가지를 적으세요.

## 수행 과제

```bash
git init
git status
git add .
git commit -m "docs: add foundations practice"
git branch
git switch -c feature/practice
```

각 명령 실행 후 `git status` 또는 `git log --oneline --graph --decorate --all`로 상태를 확인하세요.

## 정답 확인 포인트

- Git = 분산 버전 관리 시스템
- GitHub = Git Repository를 중심으로 협업·호스팅 기능을 제공하는 플랫폼
- Commit = Local 이력 생성
- Push = Local Commit을 Remote로 전송
- Fetch = Remote 정보 가져오기, 자동 병합 없음
- Pull = 일반적으로 Fetch + 현재 Branch 통합

## 완료 기준

- [ ] 10문제 중 9문제 이상 설명 가능
- [ ] Local에서 Commit과 Branch 실습 완료
- [ ] Commit vs Push, Fetch vs Pull을 자료 없이 설명 가능

---

[← Exercises Index](../README.md) · [다음: 020 Repositories →](../020-repositories/README.md)
