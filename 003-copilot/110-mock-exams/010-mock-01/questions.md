# GH-300 Mock 01 — 질문 (GH-300 Mock 01 — Questions, GH-300MQ)

**40문항 / 자체 제작 / 진단용**  
정답은 모든 문제를 푼 뒤 [`answers.md`](./answers.md)에서 확인합니다.

## 문제 01 (Question 01, Q01)
Copilot이 생성한 코드가 모든 기존 Test를 통과했다. Production 반영 전 BEST 행동은?  
A. 즉시 Merge  
B. Requirement·Security·Privacy·새 Edge Case를 Human Review  
C. Test 삭제  
D. AI에게 `확실해?`만 질문

## 문제 02 (Question 02, Q02)
존재하지 않는 API를 그럴듯하게 제안하는 현상은?  
A. Audit  
B. Hallucination  
C. Exclusion  
D. Refactor

## 문제 03 (Question 03, Q03)
AI가 특정 사용자 집단에 불리한 분류를 반복한다. 우선 검토할 위험은?  
A. Bias/Fairness  
B. Git Conflict  
C. Billing  
D. Cache

## 문제 04 (Question 04, Q04)
Debugging을 위해 실제 API Key를 Prompt에 넣으려 한다. BEST 대안은?  
A. Base64로 변환  
B. Key를 제거·마스킹하고 재현 가능한 비민감 예제 사용  
C. Public Repository에 저장  
D. Chat History만 삭제

## 문제 05 (Question 05, Q05)
AI Output의 설명이 자세하다. 이 사실이 의미하는 것은?  
A. 정확성이 보장됨  
B. Review에 도움되지만 실행·Test 검증은 여전히 필요  
C. Privacy 보장  
D. Bias 제거

## 문제 06 (Question 06, Q06)
Responsible AI의 Human Accountability와 가장 가까운 설명은?  
A. 최종 판단 책임을 AI에 위임  
B. 사람이 AI Output 사용 결과를 검토·책임  
C. Test를 AI가 만들면 책임 종료  
D. Prompt를 길게 쓰면 책임 종료

## 문제 07 (Question 07, Q07)
오래된 Framework API를 Copilot이 제안했다. FIRST 행동은?  
A. 최신 공식 Documentation 확인  
B. 그대로 Deploy  
C. Repository 삭제  
D. Secret 추가

## 문제 08 (Question 08, Q08)
현재 함수의 다음 몇 줄을 빠르게 제안받고 싶다. BEST 기능은?  
A. Inline Suggestion  
B. Audit Log  
C. Space  
D. Content Exclusion

## 문제 09 (Question 09, Q09)
코드 원인을 대화형으로 탐색하고 후속 질문을 이어가고 싶다. BEST 기능은?  
A. Chat  
B. Spark  
C. Billing API  
D. Exclusion

## 문제 10 (Question 10, Q10)
여러 파일의 정해진 변경안을 편집 중심으로 적용·검토하고 싶다. 우선 고려할 기능은?  
A. Edits  
B. Audit Log  
C. Public Code Filter  
D. Git Tag

## 문제 11 (Question 11, Q11)
실패 Test 원인을 조사하고 파일을 찾아 수정한 뒤 Test를 다시 실행하는 다단계 작업은?  
A. Agent Mode  
B. Inline Suggestion  
C. Content Exclusion  
D. Space

## 문제 12 (Question 12, Q12)
Terminal에서 명령 설명과 Script 초안을 받고 싶다. BEST 기능은?  
A. Copilot CLI  
B. PR Summary  
C. Audit Log  
D. Spark

## 문제 13 (Question 13, Q13)
Agent가 외부 Issue Tracker와 표준 방식으로 연결되어 Tool을 사용하게 하고 싶다. 관련 기술은?  
A. MCP  
B. Git Rebase  
C. Pages  
D. CODEOWNERS

## 문제 14 (Question 14, Q14)
MCP Server 연결 시 FIRST 보안 고려사항은?  
A. 서버 이름  
B. Data/Tool/Credential Scope와 최소 권한  
C. README 색상  
D. Commit 수

## 문제 15 (Question 15, Q15)
Copilot Code Review의 역할을 가장 정확히 설명한 것은?  
A. Human Reviewer 완전 대체  
B. AI Review Signal 제공, 최종 판단은 사람  
C. Test 삭제  
D. 자동 Merge 보장

## 문제 16 (Question 16, Q16)
팀의 Architecture 규칙과 API Convention을 Copilot Context로 묶고 싶다. 관련 기능은?  
A. Spaces  
B. Stash  
C. Release  
D. Fork

## 문제 17 (Question 17, Q17)
자연어 요구사항으로 작은 앱 Prototype을 만들고 발전시키는 기능은?  
A. Spark  
B. Audit Log  
C. Dependabot  
D. Branch Protection

## 문제 18 (Question 18, Q18)
조직 전체의 Copilot 기능 가용성을 중앙 관리하려 한다. 관련 개념은?  
A. Organization Policy  
B. Git Stash  
C. Unit Test  
D. PR Label

## 문제 19 (Question 19, Q19)
Copilot의 개념적 Data Flow 순서로 가장 적절한 것은?  
A. LLM→Context→Prompt→Suggestion  
B. Input/Context→Prompt Building→Filter/Proxy→LLM→Post-processing→Suggestion  
C. Suggestion→Commit→LLM  
D. Repository→자동 학습→정답

## 문제 20 (Question 20, Q20)
사용자가 입력한 문장과 모델에 전달되는 전체 Prompt의 관계는?  
A. 항상 동일  
B. 사용자 입력과 Context를 서비스가 조합할 수 있음  
C. 사용자 입력은 사용 안 함  
D. 모든 Repository가 항상 그대로 전달

## 문제 21 (Question 21, Q21)
Context Window 제한이 있을 때 BEST 원칙은?  
A. 모든 파일 제공  
B. 관련성 높은 Context 선택  
C. Secret 제공  
D. Prompt 제거

## 문제 22 (Question 22, Q22)
Proxy/Filtering 단계의 목적은?  
A. Branch Rename  
B. 정책·안전·Matching 기준에 따른 입력/출력 처리  
C. Repository 삭제  
D. Billing

## 문제 23 (Question 23, Q23)
LLM의 한계로 옳은 것은?  
A. 항상 최신  
B. Hallucination·제한된 Context·오래된 지식 가능  
C. Bias 없음  
D. 모든 계산 정확

## 문제 24 (Question 24, Q24)
좋은 Prompt 구조는?  
A. Goal/Context/Constraints/Output/Verification  
B. `알아서 해`  
C. Secret/Token  
D. File name only

## 문제 25 (Question 25, Q25)
Zero-shot의 설명은?  
A. 여러 예시 포함  
B. 예시 없이 Task 지시  
C. Prompt 없음  
D. Agent만 사용

## 문제 26 (Question 26, Q26)
Few-shot이 유용한 상황은?  
A. 원하는 Output 패턴 예시 제공  
B. Context 제거  
C. Billing  
D. Secret 암호화

## 문제 27 (Question 27, Q27)
Chat History가 잘못된 가정을 포함한다. BEST 행동은?  
A. 계속 사용  
B. 가정을 명시적으로 정정하고 Context 재제공  
C. Test 삭제  
D. Fork

## 문제 28 (Question 28, Q28)
`Public API 유지 + 기존 Test 통과`는 각각 무엇에 가까운가?  
A. Constraint + Verification  
B. Billing + Audit  
C. Exclusion + Space  
D. Agent + MCP

## 문제 29 (Question 29, Q29)
Copilot으로 Refactor한 코드 검증에서 가장 중요한 것은?  
A. 기존 Behavior/Test 유지  
B. 줄 수 감소만 확인  
C. AI가 완료라고 말함  
D. Commit 증가

## 문제 30 (Question 30, Q30)
AI가 만든 README 후 FIRST 행동은?  
A. 실제 코드·명령·버전과 일치 확인  
B. 자동 Publish  
C. Test 삭제  
D. Merge 강제

## 문제 31 (Question 31, Q31)
Unit Test가 Happy Path만 포함한다. 다음 행동은?  
A. Edge/Error Case 추가  
B. 완료  
C. Assertion 제거  
D. Production Data 사용

## 문제 32 (Question 32, Q32)
Integration Test의 주요 목적은?  
A. 작은 함수 하나만 검증  
B. 구성요소 간 상호작용 검증  
C. Prompt 길이 측정  
D. Audit Log 생성

## 문제 33 (Question 33, Q33)
AI가 성능 개선 코드를 제안했다. BEST 검증은?  
A. Benchmark + Correctness Test  
B. 코드 길이  
C. 설명 길이  
D. 변수명

## 문제 34 (Question 34, Q34)
AI가 Security 문제를 못 찾았다고 답했다. 가장 적절한 결론은?  
A. 취약점 없음 확정  
B. Security Tool·Review 등 추가 검증 필요  
C. Secret Scanning 삭제  
D. Test 불필요

## 문제 35 (Question 35, Q35)
Content Exclusion의 목적은?  
A. 특정 콘텐츠의 Copilot Context 사용 제한  
B. 파일 삭제  
C. Secret Rotation  
D. Branch Merge

## 문제 36 (Question 36, Q36)
Content Exclusion이 Secret Management를 대체하는가?  
A. Yes  
B. No  
C. Public Repo에서만 Yes  
D. CLI에서만 Yes

## 문제 37 (Question 37, Q37)
공개 코드와 일치하는 Suggestion을 다루는 보호 설정은?  
A. Suggestions matching public code filtering  
B. Git Rebase  
C. Wiki  
D. Project Board

## 문제 38 (Question 38, Q38)
Copilot Output Ownership 관련 BEST 접근은?  
A. 모든 Output은 자동 Public Domain  
B. 최신 약관과 조직 Policy·법무 기준 확인  
C. AI가 만들었으니 책임 없음  
D. README만 확인

## 문제 39 (Question 39, Q39)
특정 파일에서 Suggestion이 안 보인다. FIRST로 확인할 것은?  
A. Sign-in/활성화/파일 지원/Policy·Exclusion 상태  
B. OS 삭제  
C. Token 공개  
D. Repository Public 전환

## 문제 40 (Question 40, Q40)
Defense in Depth로 가장 적절한 것은?  
A. Policy + Exclusion + Filter + Human Review + Test/Security Check  
B. AI Output 단독  
C. Agent 최대 권한  
D. Test 제거

## 답안 기록

```text
01:   11:   21:   31:
02:   12:   22:   32:
03:   13:   23:   33:
04:   14:   24:   34:
05:   15:   25:   35:
06:   16:   26:   36:
07:   17:   27:   37:
08:   18:   28:   38:
09:   19:   29:   39:
10:   20:   30:   40:
```
