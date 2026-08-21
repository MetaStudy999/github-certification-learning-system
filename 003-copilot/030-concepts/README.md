# 030 Concepts — GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) 핵심 개념

## 빠른 시작 (Quick Start, QS)

GH-300에서는 `기능 이름 → 정의`만 외우기보다 **입력 → Context → AI 처리 → Output → Human Verification**의 흐름으로 이해합니다.

## 1. 기본 Copilot 흐름

```text
Developer Intent
  ↓
Prompt + Editor / Repository Context
  ↓
Prompt Building
  ↓
Copilot Service / Filtering
  ↓
LLM
  ↓
Post-processing
  ↓
Suggestion / Chat Response
  ↓
Human Review
  ↓
Run / Test / Verify
```

핵심은 마지막 단계입니다.

> **AI Output은 제안이며, 실행·테스트·보안검토를 통과해야 신뢰할 수 있습니다.**

## 2. IDE 기능 선택

| 상황 | 우선 고려 기능 | 이유 |
|---|---|---|
| 현재 줄의 다음 코드를 빠르게 작성 | Inline Suggestion | 흐름을 끊지 않는 자동 제안 |
| 코드의 의미·오류를 질문 | Chat | 대화형 설명과 탐색 |
| 여러 파일의 변경안을 편집 중심으로 적용 | Copilot Edits | 다중 변경을 검토하며 적용 |
| 목표를 주고 여러 단계 작업 수행 | Agent Mode | 계획·도구 사용·반복 실행이 필요한 작업 |
| Terminal에서 명령·스크립트·파일 작업 | Copilot CLI | CLI 중심 Workflow |

## 3. Agent Mode와 MCP

```text
Goal
 ↓
Agent Mode
 ├── Context
 ├── Instructions
 ├── Tools
 ├── MCP Servers
 ├── Agent Session
 └── Sub-Agents
        ↓
   Code / File / Tool Actions
        ↓
   Human Review
```

- **Agent Mode**: 단일 답변을 넘어서 여러 단계 작업을 수행합니다.
- **MCP (Model Context Protocol)**: Agent가 외부 도구·데이터와 연결되는 표준 인터페이스 역할을 할 수 있습니다.
- **Sub-Agent**: 특정 하위 작업을 위임해 Context와 역할을 분리할 수 있습니다.
- Agent가 행동할 수 있다는 것은 **검증 책임이 더 커진다는 뜻**입니다.

## 4. Prompt와 Context

```text
Prompt = 내가 명시적으로 주는 지시
Context = 모델이 답을 만들 때 참고하는 정보
```

좋은 결과는 둘 모두에 의존합니다.

```text
좋은 Prompt
+ 관련성 높은 Context
+ 명확한 Constraints
+ 검증 기준
= 더 유용한 Output 가능성 증가
```

하지만 정확성을 보장하지는 않습니다.

## 5. Instructions와 Prompt File

| 항목 | 목적 |
|---|---|
| Instruction File | Repository·조직의 지속적인 코딩/검토 지침 제공 |
| Prompt File | 반복 사용하는 특정 Prompt Workflow를 파일로 재사용 |

둘 다 일관성을 높이지만 **사용 목적과 적용 범위**가 다릅니다.

## 6. Zero-shot vs Few-shot

```text
Zero-shot
→ 예시 없이 목표와 조건만 제시

Few-shot
→ 원하는 패턴의 예시를 함께 제공
```

출력 형식이나 스타일이 중요한 경우 Few-shot이 도움이 될 수 있지만, 불필요한 예시는 Context를 낭비할 수 있습니다.

## 7. Data / Architecture 개념

Copilot이 단순히 `내 코드 전체를 모델에 넣는다`고 이해하면 안 됩니다. 시험에서는 다음 개념적 흐름을 봅니다.

1. 사용자 입력과 사용 가능한 Context를 수집합니다.
2. 서비스가 Prompt를 구성합니다.
3. 정책·필터링 과정을 거칩니다.
4. LLM이 응답을 생성합니다.
5. 응답은 Post-processing / Matching Check 등을 거칠 수 있습니다.
6. 최종 제안이 사용자에게 표시됩니다.

제품의 실제 데이터 처리 세부사항은 Plan·기능·정책 변화에 따라 달라질 수 있으므로 공식 문서를 기준으로 확인합니다.

## 8. Productivity와 Verification

Copilot이 잘하는 영역:

- Boilerplate / Code Generation
- Refactoring 아이디어
- Documentation 초안
- Test 초안
- Debugging 가설
- Legacy Code 설명·현대화 보조
- Security / Performance 개선 아이디어

사람이 반드시 확인할 영역:

- 요구사항 정확성
- 보안 취약점
- Edge Case
- 라이선스·정책
- 개인정보
- 실제 실행 결과
- Test Coverage와 Assertion 품질

## 9. Responsible AI

```text
Risk 발견
→ Harm 가능성 평가
→ 최소화 전략
→ Human Review
→ Verification
→ Feedback / Improvement
```

대표 위험:

- Bias
- Hallucination
- Insecure Code
- Privacy Exposure
- 불투명한 근거
- 오래되거나 부정확한 기술 제안

## 10. Privacy와 Content Exclusion

`Content Exclusion`은 특정 콘텐츠가 Copilot Context로 사용되지 않도록 관리하는 수단입니다.

그러나 다음과 혼동하면 안 됩니다.

```text
Content Exclusion ≠ 원본 파일 삭제
Content Exclusion ≠ 모든 보안 문제 해결
Content Exclusion ≠ Secret 관리 대체
```

시험에서는 **설정 목적, 적용 방식, 한계, 문제 해결 방법**까지 구분합니다.

## 반드시 구분

| A | B | 핵심 차이 |
|---|---|---|
| Completion | Chat | 작성 중 자동 제안 vs 대화형 문제 해결 |
| Chat | Edits | 설명·대화 vs 변경 적용 중심 |
| Edits | Agent Mode | 편집 중심 vs 자율적 다단계 작업 |
| Prompt | Context | 직접 지시 vs AI가 참고하는 정보 |
| Instruction File | Prompt File | 지속 지침 vs 재사용 Prompt |
| Zero-shot | Few-shot | 예시 없음 vs 예시 포함 |
| Generate | Refactor | 새 코드 생성 vs 기존 코드 구조 개선 |
| Explanation | Verification | 설명 vs 실행·Test 검증 |
| Privacy | Security | 데이터 보호 vs 시스템·코드 위험 방어 |
| Content Exclusion | Delete | Context 제외 vs 원본 삭제 |
| AI Suggestion | Correct Answer | 확률적 제안 vs 검증된 결과 |

## 완료 기준

- [ ] Copilot의 개념적 Data Flow를 그림 없이 설명할 수 있다.
- [ ] IDE / CLI / Agent Mode 사용 시나리오를 구분한다.
- [ ] MCP가 Agentic Workflow에 연결되는 이유를 설명한다.
- [ ] Prompt와 Context의 차이를 예시로 설명한다.
- [ ] Human Review가 왜 필수인지 설명한다.
- [ ] Content Exclusion의 목적과 한계를 설명한다.

---
[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
