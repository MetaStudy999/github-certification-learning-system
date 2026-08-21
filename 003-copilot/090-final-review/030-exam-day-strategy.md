# 030 Exam-Day Strategy — GH-300

## 시험 전날

새로운 기능을 대량으로 외우지 않습니다.

```text
Official Study Guide
→ Confusion Matrix
→ 최근 오답
→ Mock 약점
→ 수면 / 시험 환경 확인
```

## 문제를 읽는 순서

### 1. Goal 찾기

무엇을 하려는가?

- 코드 작성?
- 대화형 분석?
- 다중 파일 변경?
- Agentic Task?
- 조직 관리?
- Privacy 통제?

### 2. Constraint 찾기

- IDE인가 CLI인가?
- Organization Policy가 필요한가?
- Data/Privacy 요구가 있는가?
- Human Approval이 필요한가?
- Tool/External Data 연결이 필요한가?

### 3. 질문의 단어 확인

```text
BEST
MOST appropriate
FIRST
PRIMARY
MOST likely
```

`가능한 답`이 아니라 **가장 직접적이고 적절한 답**을 선택합니다.

## 기능 선택 사고 순서

```text
단순 작성 중 제안
→ Inline Suggestion

대화형 설명·질문
→ Chat

다중 파일 편집 중심
→ Edits

다단계 실행·Tool 사용
→ Agent Mode

Terminal 중심
→ Copilot CLI

외부 Tool/Data 표준 연결
→ MCP
```

## Responsible AI 문제

AI가 생성했다고 해서 다음을 생략하는 선택지는 경계합니다.

- Human Review
- Test
- Security Check
- Privacy Review
- Requirement Verification

## Privacy 문제

다음 단순화는 피합니다.

```text
Content Exclusion = 파일 삭제        X
Content Exclusion = Secret 관리      X
Public Code Filter = 법무 검토 대체   X
AI Review = Human 책임 대체           X
```

## Data / Architecture 문제

세부 구현을 지나치게 추측하지 말고 공식 Study Guide 수준의 흐름을 기억합니다.

```text
Context
→ Prompt Building
→ Filtering / Proxy
→ LLM
→ Post-processing
→ Suggestion
```

## 시간 관리

1. 첫 회차에서는 확실한 문제를 빠르게 처리합니다.
2. 긴 Scenario는 `Goal / Constraint / BEST`를 표시하며 읽습니다.
3. 한 문제에 과도하게 오래 머무르지 않습니다.
4. 마지막 검토에서는 Flag한 문제와 유사 기능 비교 문제를 우선 봅니다.

## 마지막 5분 Check

- 기능 이름만 보고 선택하지 않았는가?
- `FIRST`와 `BEST`를 놓친 문제는 없는가?
- AI를 무조건 신뢰하는 선택지를 고르지 않았는가?
- Privacy와 Security를 혼동하지 않았는가?
- Chat / Edits / Agent / CLI / MCP를 목적에 맞게 구분했는가?

## 시험 후

실제 시험 문항을 Repository에 복제하거나 공유하지 않습니다.

기록 가능한 범위:

```text
Exam date:
Result:
Strong skill areas:
Weak skill areas:
Preparation lessons:
Next certification:
```
