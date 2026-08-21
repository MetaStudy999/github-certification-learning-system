# 020 문제 세트 (Question Set, QS) — 저장소 와 비교 (Repositories & Compare, RC) (Q011–Q020)

## Q011
Write 권한이 없는 공개 Repository에 일반적으로 기여하려고 한다. 가장 적절한 시작은?

A. 원본 `main`에 직접 Push  
B. Repository를 Fork  
C. Organization 삭제  
D. GitHub Pages 활성화

<details><summary>정답 및 해설</summary>

**정답: B** — 자신의 계정으로 Fork한 뒤 Branch에서 변경하고 원본 Repository로 PR을 보내는 방식이 일반적입니다.
</details>

## Q012
`git clone`의 목적은?

A. GitHub 계정을 복제한다.  
B. Remote Repository의 작업 사본과 Git 이력을 Local에 만든다.  
C. Pull Request를 자동 승인한다.  
D. Repository Visibility를 변경한다.

<details><summary>정답 및 해설</summary>

**정답: B**
</details>

## Q013
Clone과 Fork의 차이를 가장 잘 설명한 것은?

A. 둘은 완전히 같은 작업이다.  
B. Clone은 Local 사본을 만들고, Fork는 GitHub에서 다른 계정/공간에 Repository 사본을 만든다.  
C. Fork는 Local에서만 동작한다.  
D. Clone은 공개 Repository에 사용할 수 없다.

<details><summary>정답 및 해설</summary>

**정답: B** — Clone은 Local 작업 사본, Fork는 GitHub 상의 별도 Repository 사본이라는 차이가 핵심입니다.
</details>

## Q014
프로젝트 사용법과 시작 방법을 가장 일반적으로 설명하는 문서는?

A. `README.md`  
B. `CODEOWNERS`  
C. `SECURITY.md`  
D. `.gitignore`

<details><summary>정답 및 해설</summary>

**정답: A**
</details>

## Q015
오픈소스 소프트웨어의 사용·수정·배포 조건을 명확히 하는 파일은?

A. `LICENSE`  
B. `README.md`  
C. `SECURITY.md`  
D. `CODEOWNERS`

<details><summary>정답 및 해설</summary>

**정답: A** — License는 법적 사용 조건을 명확히 합니다.
</details>

## Q016
새로운 기여자가 Issue/PR 작성 규칙과 개발 절차를 확인하려고 한다. 가장 적합한 파일은?

A. `CONTRIBUTING.md`  
B. `LICENSE`  
C. `SECURITY.md`  
D. `.git/config`

<details><summary>정답 및 해설</summary>

**정답: A** — Contribution 가이드는 프로젝트 기여 방법을 설명합니다.
</details>

## Q017
보안 취약점 신고 절차를 안내하는 데 가장 적합한 문서는?

A. `SECURITY.md`  
B. `README.md`  
C. `LICENSE`  
D. `CODEOWNERS`

<details><summary>정답 및 해설</summary>

**정답: A**
</details>

## Q018
특정 경로나 파일 변경 시 자동 Review 요청 대상이 될 책임자를 정의하는 파일은?

A. `CODEOWNERS`  
B. `SECURITY.md`  
C. `README.md`  
D. `LICENSE`

<details><summary>정답 및 해설</summary>

**정답: A** — CODEOWNERS는 코드 영역의 소유자/Review 책임자를 지정하는 데 사용됩니다.
</details>

## Q019
`origin`이라는 Remote 이름에 대한 설명으로 가장 적절한 것은?

A. Git이 강제하는 유일한 Remote 이름이다.  
B. Clone 시 기본적으로 자주 사용되는 Remote 이름이지만 변경할 수 있다.  
C. 항상 원본 오픈소스 Repository를 뜻한다.  
D. GitHub Organization만 사용할 수 있다.

<details><summary>정답 및 해설</summary>

**정답: B** — `origin`은 관례적으로 기본 Remote에 많이 쓰이지만 고정된 예약어는 아닙니다.
</details>

## Q020
Public Repository와 Private Repository의 차이에 대한 설명으로 가장 적절한 것은?

A. Public은 Git을 사용할 수 없고 Private만 Git을 사용한다.  
B. Public은 일반적으로 누구나 볼 수 있고, Private은 접근 권한이 있는 사용자에게 제한된다.  
C. Private Repository에는 Branch가 없다.  
D. Public Repository에는 Pull Request가 없다.

<details><summary>정답 및 해설</summary>

**정답: B**
</details>

## 자가 점검 (Self Check, SC)

- 9–10: PASS
- 8: 오답 복습
- 7 이하: Repository Exercise와 Lab 020/050 재수행

---

[← 010 Basics](../010-basics/README.md) · [다음: 030 Collaboration & Scenario →](../030-collaboration-scenario/README.md)
