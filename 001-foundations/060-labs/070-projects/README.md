# 실습 (Lab, LAB) 070 — GitHub 프로젝트 (GitHub Projects, GP)

> **Views · Fields · Filters · Issue/PR 연결**

## 000. 빠른 시작 (Quick Start, QS)

GitHub Projects는 Issue와 Pull Request를 업무 보드처럼 정리하고, 필드·보기·필터를 사용해 진행 상태를 추적하는 기능입니다.

## 010. Objective (목표)

완료 후 다음을 수행할 수 있어야 합니다.

- Project를 생성하거나 기존 Project를 탐색한다.
- Issue/PR을 Project에 추가한다.
- View(보기)를 구분한다.
- Field(필드)를 사용해 상태·우선순위 등을 관리한다.
- Filter(필터)로 필요한 항목만 추린다.

## 020. Concept (개념)

```text
Repository / Organization
        ↓
      Project
        ↓
   Issue / Pull Request
        ↓
Field · View · Filter
```

| 개념 | 의미 |
|---|---|
| Project | 작업 항목을 한곳에서 관리하는 공간 |
| Item | Project에 추가된 Issue, PR 또는 Draft item |
| Field | Status, Priority, Date 등 추가 정보 |
| View | Table, Board, Roadmap 등 표현 방식 |
| Filter | 조건에 맞는 Item만 표시 |

## 030. Practice (따라하기)

### 031. Project 만들기 또는 열기

Repository 또는 Organization에서 Projects 메뉴를 확인합니다.

새 Project를 만들 수 있다면 학습용으로 다음 이름을 사용합니다.

```text
GitHub Foundations Study
```

### 032. Item 추가

앞 Lab에서 만든 Issue 또는 PR을 Project에 추가합니다.

### 033. Status Field 사용

예시 상태:

```text
Todo
In Progress
Done
```

Issue를 상태별로 이동해 봅니다.

### 034. 사용자 정의 Field 만들기

가능한 경우 다음 중 하나를 추가합니다.

```text
Priority: High / Medium / Low
Exam Domain: 1 / 2 / 3 / ...
Study Day: Day 1 / Day 2 / ...
```

### 035. View 비교

사용 가능한 View를 확인하고 같은 Item이 어떻게 다르게 보이는지 비교합니다.

예:

```text
Table  → 전체 속성을 표로 확인
Board  → Status 같은 필드 기준으로 흐름 확인
Roadmap → 일정 정보가 있는 경우 시간축 관점 확인
```

UI와 제공 View는 계정·설정에 따라 달라질 수 있습니다.

### 036. Filter 연습

예시 조건으로 필터링합니다.

```text
Status = In Progress
Priority = High
```

## 040. Challenge (스스로 해보기)

GitHub 자격증 학습을 관리하는 Project를 직접 설계합니다.

필수 필드 예시:

```text
Certification
Domain
Status
Priority
Target Date
Score
```

그리고 다음 View를 설계합니다.

1. 전체 학습 목록
2. 진행 중 항목
3. 시험 직전 복습 항목

## 050. Verify (검증)

- [ ] Project와 Repository의 역할 차이를 설명할 수 있다.
- [ ] Issue 또는 PR을 Project에 연결했다.
- [ ] Field를 최소 1개 사용했다.
- [ ] View를 2개 이상 비교했다.
- [ ] Filter를 사용해 필요한 Item만 표시했다.

## 060. Evidence (증거 기록)

```text
Project URL:
사용한 View:
사용한 Field:
사용한 Filter:
연결한 Issue/PR:
배운 점:
```

## 070. 시험 포인트

다음 연결 관계를 기억합니다.

```text
Issue/PR = 실제 작업 단위
Project = 여러 작업 단위를 계획·추적하는 공간
Field = 작업의 추가 속성
View = 보여주는 방식
Filter = 골라 보는 조건
```

---

[← Lab 060](../060-collaboration/README.md) · [다음: Lab 080 →](../080-modern-development/README.md)
