# 040 Prompt & Context — 수행형 연습

## 목표

Prompt를 명확하게 작성하고, 필요한 Context를 선택하며, Zero-shot / Few-shot / Chat History / Instructions를 상황에 맞게 활용합니다.

## 연습문제 (Exercises, EXR)

### E040-01 — 모호한 Prompt 개선
다음 Prompt를 개선하세요.

```text
이 코드 고쳐 줘.
```

`Goal / Context / Constraints / Output / Verification` 다섯 요소를 포함합니다.

### E040-02 — Goal과 Constraint
`빠르게 정렬 함수를 만들어 줘`라는 요청에 필요한 Constraint를 최소 4개 추가하세요. 예: 입력 크기, 안정 정렬 여부, 표준 라이브러리 허용 여부 등.

### E040-03 — Relevant 컨텍스트 (Relevant Context, RC)
버그가 특정 함수에서 발생합니다. 다음 중 어떤 Context를 우선 제공할지 순위를 매기고 이유를 설명하세요.

- 오류 Stack Trace
- 관련 함수
- 무관한 README 전체
- 실패 Test
- 사용 중인 Library Version
- 다른 프로젝트의 유사 코드

### E040-04 — Zero-shot 비교 Few-shot (Zero-shot vs Few-shot, ZF)
응답 형식을 엄격하게 맞추고 싶을 때 Few-shot이 도움이 되는 이유와 예시를 작성하세요.

### E040-05 — Few-shot의 역효과
잘못된 예시나 오래된 예시를 제공하면 어떤 문제가 생길 수 있는지 설명하세요.

### E040-06 — Chat History
이전 대화가 현재 질문에 잘못된 가정을 남길 수 있습니다. Context를 Reset/Clarify해야 할 상황을 2개 작성하세요.

### E040-07 — Verification을 Prompt에 포함
AI에게 코드만 요청하는 Prompt와 `테스트·성공조건도 함께 요청`하는 Prompt의 차이를 설명하세요.

### E040-08 — 지침 (Instructions, I)
Repository 공통 지침으로 적합한 항목 5개를 작성하세요. 단, 특정 1회성 Task 지시는 제외합니다.

### E040-09 — 프롬프트 파일 (Prompt File, PF)
반복 가능한 `PR Review Prompt`를 작성하세요. 출력은 Severity, Finding, Evidence, Recommendation 형식으로 제한합니다.

### E040-10 — 프롬프트 Quality 리뷰 (Prompt Quality Review, PQR)
본인이 작성한 Prompt 하나를 다음 기준으로 10점 만점 평가하세요.

| 항목 | 0–2점 |
|---|---:|
| Goal 명확성 | |
| Context 관련성 | |
| Constraints | |
| Output 형식 | |
| Verification | |

## 자가 검증

- [ ] Prompt와 Context를 구분한다.
- [ ] Goal / Context / Constraints / Output / Verification 구조를 사용한다.
- [ ] Zero-shot / Few-shot 차이를 설명한다.
- [ ] Chat History가 Context에 미치는 영향을 설명한다.
- [ ] Instructions / Prompt File을 구분한다.

## 관련 Lab

- [`020-prompt-fundamentals`](../../060-labs/020-prompt-fundamentals/)
- [`030-context-engineering`](../../060-labs/030-context-engineering/)
- [`130-spaces-spark-instructions`](../../060-labs/130-spaces-spark-instructions/)

---
[← 030 Data & Architecture](../030-data-architecture/README.md) · [050 Developer Productivity →](../050-developer-productivity/README.md)
