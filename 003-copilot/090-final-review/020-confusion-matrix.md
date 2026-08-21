# 020 Confusion 매트릭스 — GH-300 (020 Confusion Matrix — GH-300, CMGH-300)

시험 직전에는 정의를 따로 외우기보다 **서로 비슷한 기능의 선택 기준**을 비교합니다.

| A | B | A를 선택하기 좋은 상황 | B를 선택하기 좋은 상황 |
|---|---|---|---|
| Inline Suggestion | Chat | 현재 코드 작성 흐름의 빠른 Completion | 설명·질문·탐색·대화 |
| Chat | Edits | 문제 이해·질문·대안 비교 | 여러 파일 변경을 편집·검토 |
| Edits | Agent Mode | 변경 범위가 비교적 명확 | 조사→수정→실행→재수정의 다단계 Task |
| Chat | Agent Mode | 답변 중심 | 행동·Tool 사용 중심 |
| IDE | Copilot CLI | Editor 중심 개발 | Terminal 중심 작업·Script·File 관리 |
| Agent Mode | MCP | 작업을 수행하는 Agent 기능 | Agent가 외부 Tool/Data와 연결되는 Protocol |
| Agent Session | Sub-Agent | 하나의 Agent 작업 상태 유지 | 특정 하위 역할·Task 위임 |
| Code Review | PR Summary | 변경의 문제·개선점 검토 | 변경내용 빠른 이해·요약 |
| Instructions | Prompt File | 지속적인 Repository/조직 지침 | 반복 실행하는 Task Prompt |
| Spaces | Spark | 지식·Context 묶음 | 자연어 기반 앱 Prototype/개발 |
| Prompt | Context | 명시적 지시 | 응답에 참고되는 정보 |
| Prompt Crafting | Prompt Engineering | 개별 Prompt 작성 품질 | 반복 가능한 전략·Process 최적화 |
| Zero-shot | Few-shot | 예시 없이 Task 지시 | 원하는 패턴 예시 제공 |
| Explanation | Verification | 코드·결과 이해 | 실제 실행·Test·Security 확인 |
| Generate | Refactor | 새 코드 작성 | 기존 Behavior를 유지하며 구조 개선 |
| Unit Test | Integration Test | 작은 단위 | 구성요소 간 상호작용 |
| Test Generation | Test Validation | Test 초안 생성 | Coverage·Assertion·Edge Case 검증 |
| Privacy | Security | 데이터 수집·사용·보호 | 시스템·코드·접근 위험 방어 |
| Content Exclusion | Secret Management | Copilot Context 사용 제한 | Secret 저장·권한·회전·수명 관리 |
| Public Code Filter | License Review | 공개 코드 일치 제안 제어 | 법적·정책적 사용 가능성 판단 |
| AI Code Review | Human Review | 추가 자동 Review Signal | 최종 요구사항·Risk·책임 판단 |
| AI Suggestion | Correct Result | 후보·초안 | Test·검증을 통과한 결과 |

## 빠른 자가 질문

1. 여러 파일을 바꿔야 한다고 무조건 Agent Mode인가?
2. MCP 자체가 Agent인가?
3. Content Exclusion이 Secret Scanning/Management를 대체하는가?
4. Code Review가 Human Approval을 대체하는가?
5. Few-shot은 항상 Zero-shot보다 좋은가?
6. Test가 통과하면 AI Output이 항상 요구사항을 만족하는가?
7. Public Code Matching Filter가 법적 검토를 완전히 대체하는가?

위 질문에 모두 **“조건에 따라 다르며 목적과 한계를 봐야 한다”**는 관점으로 설명할 수 있어야 합니다.
