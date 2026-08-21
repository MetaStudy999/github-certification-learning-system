# 080 Question Bank — 자체 문제은행

> 실제 시험 문항이나 Brain Dump를 복제하지 않습니다. 공식 GH-900 학습목표를 기반으로 자체 제작한 문제만 사용합니다.

## Quick Start

문제 하나를 다음 구조로 학습합니다.

```text
문제
→ 내 답
→ 정답
→ 왜 정답인가
→ 왜 다른 선택지는 아닌가
→ 관련 공식문서
→ 관련 Lab
```

## 문제 분류

| 코드 | 유형 | 목적 |
|---:|---|---|
| 010 | Basic | 기본 정의와 목적 |
| 020 | Compare | 유사 개념 비교 |
| 030 | Scenario | 상황에 맞는 기능 선택 |
| 040 | Workflow | 순서·흐름 판단 |
| 050 | Security/Admin | 보안·권한·관리 |
| 060 | Community | Open Source·Community |
| 090 | Random | 전 범위 랜덤 |

## Starter Questions

### Q001

Git과 GitHub의 관계를 가장 정확하게 설명한 것은?

A. Git은 GitHub의 웹 UI 이름이다.  
B. Git은 분산 버전 관리 시스템이고 GitHub는 Git Repository를 중심으로 협업 기능을 제공하는 플랫폼이다.  
C. GitHub를 사용하지 않으면 Git Commit을 만들 수 없다.  
D. Git은 Cloud Repository만 관리한다.

<details>
<summary>정답 및 해설</summary>

**정답: B**

Git은 독립적으로 Local에서도 사용할 수 있는 분산 버전 관리 시스템입니다. GitHub는 Git Repository 호스팅과 PR, Issue, Actions 등의 협업 기능을 제공합니다.

</details>

### Q002

Write 권한이 없는 공개 Repository에 기여할 때 일반적으로 가장 적절한 첫 GitHub 작업은?

A. 원본 `main`에 직접 Push  
B. Repository를 Fork  
C. Organization 생성  
D. GitHub Pages 활성화

<details><summary>정답 및 해설</summary>

**정답: B** — 자신의 GitHub 공간에 Fork한 뒤 Branch에서 변경하고 원본으로 PR을 보내는 방식이 일반적입니다.

</details>

### Q003

Remote Repository의 변경 정보를 가져오되 현재 Branch에 자동 병합하지 않는 Git 명령은?

A. `git push`  
B. `git fetch`  
C. `git commit`  
D. `git merge`

<details><summary>정답 및 해설</summary>

**정답: B** — `fetch`는 Remote 정보를 가져오지만 현재 Branch에 자동 병합하지 않습니다.

</details>

### Q004

명확한 버그 수정 작업을 담당자에게 배정하고 상태를 추적하려고 한다. 가장 적절한 기능은?

A. Discussion  
B. Issue  
C. Gist  
D. Star

<details><summary>정답 및 해설</summary>

**정답: B** — Issue는 버그·기능·작업 추적에 적합하고 Assignee, Label, Milestone 등을 사용할 수 있습니다.

</details>

### Q005

Repository의 보안 취약점 신고 절차를 안내하는 데 가장 적합한 파일은?

A. `README.md`  
B. `LICENSE`  
C. `SECURITY.md`  
D. `CODEOWNERS`

<details><summary>정답 및 해설</summary>

**정답: C** — SECURITY 문서는 보안 취약점 보고 정책과 절차를 안내합니다.

</details>

### Q006

Push 시마다 Test를 자동 실행하려고 한다. 가장 직접적인 GitHub 기능은?

A. GitHub Actions  
B. GitHub Pages  
C. GitHub Sponsors  
D. GitHub Discussions

<details><summary>정답 및 해설</summary>

**정답: A** — GitHub Actions는 Event 기반 Workflow 자동화에 사용됩니다.

</details>

### Q007

브라우저에서 사전 구성된 개발환경을 빠르게 실행하려고 한다. 가장 적합한 기능은?

A. Copilot  
B. Codespaces  
C. Projects  
D. Wiki

<details><summary>정답 및 해설</summary>

**정답: B** — Codespaces는 Cloud 기반 개발환경을 제공합니다.

</details>

### Q008

특정 Branch에 병합하기 전에 Review나 Check를 요구하도록 제한하려고 한다. 가장 관련 있는 개념은?

A. Branch Protection  
B. Star  
C. Gist  
D. Follow

<details><summary>정답 및 해설</summary>

**정답: A** — Branch Protection은 중요 Branch의 변경·병합 조건을 강제하는 데 사용됩니다.

</details>

### Q009

오픈소스 협업 방식을 회사 내부 개발에 적용하는 개념은?

A. Fork  
B. InnerSource  
C. Marketplace  
D. Codespaces

<details><summary>정답 및 해설</summary>

**정답: B** — InnerSource는 오픈소스의 협업 원칙을 조직 내부에 적용합니다.

</details>

### Q010

다음 중 Pull Request의 핵심 목적에 가장 가까운 것은?

A. Local Working Directory 생성  
B. 변경을 제안하고 Review·논의 후 Branch에 병합  
C. 사용자 계정에 2FA 설정  
D. 정적 웹사이트 배포

<details><summary>정답 및 해설</summary>

**정답: B**

</details>

## 다음 확장 목표

- Basic 30문제
- Compare 30문제
- Scenario 60문제
- Workflow 30문제
- Security/Admin 30문제
- Community 20문제

최종 목표: **200문제 자체 문제은행**

## 점수 기록

문제를 풀 때 다음 표를 복사해 사용합니다.

| 회차 | 정답 | 전체 | 정답률 | 약점 |
|---:|---:|---:|---:|---|
| 1 |  | 10 |  |  |
| 2 |  | 10 |  |  |

---

[← 070 Exercises](../070-exercises/README.md) · [다음: 090 Final Review →](../090-final-review/README.md)
