# Lab 080 — Modern Development on GitHub

> **GitHub Actions · GitHub Copilot · GitHub Codespaces 관찰과 역할 구분**

## 000. Quick Start

Foundations 시험에서는 각 도구를 깊게 구현하는 것보다 **무엇을 위해 사용하는지**를 구분하는 것이 우선입니다.

## 010. Objective (목표)

완료 후 다음 3개 기능의 목적을 설명할 수 있어야 합니다.

- GitHub Actions
- GitHub Copilot
- GitHub Codespaces

## 020. Concept (개념)

| 기능 | 한 문장 설명 |
|---|---|
| GitHub 액션 (GitHub Actions, GHACT / GH-200) | Repository 이벤트를 기반으로 빌드·테스트·배포 등 Workflow를 자동화 |
| GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) | 코드 작성·설명·수정 등을 지원하는 AI 기반 개발 도구 |
| GitHub Codespaces | Repository와 연결된 클라우드 개발환경 |

전체 흐름 예시:

```text
Repository
   │
   ├── Codespaces → 개발환경
   ├── Copilot    → AI 개발 지원
   └── Actions    → 자동화
```

## 030. Practice (따라하기)

### 031. GitHub 액션 (GitHub Actions, GHACT / GH-200) 관찰

Repository의 **Actions** 탭을 확인합니다.

가능하다면 학습용 Workflow 예시를 살펴봅니다.

```yaml
name: hello

on:
  workflow_dispatch:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello GitHub"
```

이 단계에서는 YAML 문법 암기보다 다음을 확인합니다.

```text
Event → Workflow → Job → Step
```

### 032. GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) 역할 정리

Copilot을 사용할 수 있는 환경이라면 다음 작업을 시험합니다.

- 코드 설명 요청
- 간단한 함수 생성
- 테스트 아이디어 생성
- 문서 초안 보조

사용할 수 없다면 공식 설명과 UI를 확인하고 역할만 정리합니다.

핵심:

```text
Copilot의 제안은 사람이 검토하고 검증해야 한다.
```

### 033. GitHub Codespaces 관찰

Repository의 **Code** 메뉴에서 Codespaces 관련 항목을 확인합니다.

사용 가능한 경우 새 Codespace를 생성하여 다음을 관찰합니다.

- Repository가 열리는 위치
- Terminal
- Source Control
- 개발환경이 로컬 PC와 분리되어 있다는 점

비용·사용량이 발생할 수 있으므로 실제 생성 전 계정의 현재 과금·사용 한도를 확인합니다.

## 040. Compare (비교)

다음 상황에 어떤 기능이 가장 적절한지 판단합니다.

| 상황 | 기능 |
|---|---|
| PR마다 자동 테스트 | Actions |
| 함수 작성 아이디어와 코드 보조 | Copilot |
| 브라우저 기반 개발환경 | Codespaces |

## 050. Challenge (스스로 해보기)

다음 문장을 완성합니다.

```text
GitHub Actions는 __________을 자동화한다.
GitHub Copilot은 __________을 AI로 지원한다.
GitHub Codespaces는 __________을 제공한다.
```

그 다음 세 기능을 함께 사용하는 개발 흐름을 직접 그려 봅니다.

## 060. Verify (검증)

- [ ] Actions의 목적을 설명할 수 있다.
- [ ] Copilot의 목적과 사람 검토 필요성을 설명할 수 있다.
- [ ] Codespaces가 클라우드 개발환경이라는 점을 설명할 수 있다.
- [ ] 세 기능을 상황별로 구분할 수 있다.
- [ ] Actions의 기본 흐름 `Event → Workflow → Job → Step`을 설명할 수 있다.

## 070. Evidence (증거 기록)

```text
Actions 관찰 내용:
Copilot 관찰/실습 내용:
Codespaces 관찰/실습 내용:
세 기능 비교 한 문장:
```

---

[← Lab 070](../070-projects/README.md) · [다음: Lab 090 →](../090-security-basics/README.md)
