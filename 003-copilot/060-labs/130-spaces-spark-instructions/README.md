# 실습 (Lab, LAB) 130 — Spaces / Spark / 지침 / 프롬프트 파일 (Spaces / Spark / Instructions / Prompt Files, SSIPF)

## 목표 (Objective, OBJ)

2026 GH-300에서 중요해진 **Spaces, Spark, Instructions Files, Prompt Files**를 각각의 목적에 맞게 구분합니다.

## 개념 맵 (Concept Map, CM)

```text
Persistent guidance
→ Instructions File

Reusable task prompt
→ Prompt File

Curated knowledge/context
→ Space

Natural-language app creation
→ GitHub Spark
```

## 실습 (Practice, PRAC) 1 — 지침 비교 프롬프트 파일 (Instruction vs Prompt File, IPF)

다음 두 요구를 분류합니다.

A. 이 Repository에서는 Python 3.12, type hint, pytest를 기본 규칙으로 사용한다.  
B. 매번 PR을 검토할 때 Correctness / Security / Test / Docs 순서로 분석한다.

예상 사고방식:

- 지속적으로 적용할 Repository 규칙 → **Instructions** 후보
- 반복 실행할 특정 작업 절차 → **Prompt File** 후보

직접 각각의 초안을 작성합니다.

### Instructions 초안 예시

```text
- Use Python 3.12 compatible syntax.
- Add type hints to public functions.
- Prefer pytest for tests.
- Do not change public APIs without explicit approval.
```

### Prompt File 초안 예시

```text
Goal: Review this change.
Check:
1. Correctness
2. Security
3. Tests
4. Maintainability
5. Documentation
Output: findings ordered by severity.
```

## Practice 2 — Space 설계

가상의 `Payments Service` 팀 Space에 넣을 Context를 설계합니다.

포함 후보:

- Architecture overview
- API conventions
- Error handling standard
- Security requirements
- Common design patterns

다음은 제외 또는 별도 관리해야 하는지 판단합니다.

- Production password
- Private access token
- 불필요한 개인정보

## 실습 (Practice, PRAC) 3 — Spark 시나리오 (Spark Scenario, SS)

다음 목표를 가정합니다.

> “간단한 학습 진도 Dashboard를 자연어 요구사항부터 빠르게 Prototype하고 싶다.”

Spark를 사용할 때의 장점과, 최종 Production 전 사람이 확인해야 할 항목을 각각 작성합니다.

```text
Prototype benefits:
- 
- 
- 

Human verification:
- Security
- Data handling
- Correctness
- Tests
- Deployment configuration
```

## 도전 과제 (Challenge, CHL)

다음 네 기능을 한 문장씩 비교하세요.

```text
Instructions
Prompt Files
Spaces
Spark
```

그리고 `Context를 많이 제공하면 항상 좋다`라는 주장이 왜 틀릴 수 있는지 설명합니다.

## 검증 (Verify, VER)

- [ ] Instructions와 Prompt File 차이를 설명 가능
- [ ] Space의 목적을 Context/Knowledge 관점에서 설명 가능
- [ ] Spark를 일반 Chat과 구분 가능
- [ ] 민감정보를 Context 자산에 넣지 않아야 하는 이유 설명
- [ ] 모든 AI-generated 결과에 Human Verification 적용

## 증빙 (Evidence, EVD)

```text
Date:
Instructions draft:
Prompt file draft:
Space design:
Spark scenario:
Privacy review:
What I learned:
```

---
[← Lab 120](../120-code-review-org-policy/README.md) · [060 Labs 홈](../README.md)
