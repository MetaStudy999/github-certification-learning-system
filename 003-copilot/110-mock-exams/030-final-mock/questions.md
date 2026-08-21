# GH-300 Final Mock — Questions

**40문항 / 자체 제작 / 최종 Gate용**  
목표: **90% 이상 권장**. 정답은 마지막에 [`answers.md`](./answers.md)에서 확인합니다.

## Q01
금융 서비스 팀이 Copilot이 제안한 신용 점수 보조 로직을 검토한다. MOST appropriate한 접근은?  
A. 기존 Test만 통과하면 승인  
B. 정확성·Bias/Fairness·Privacy·Security·설명 가능성을 함께 검토  
C. AI가 생성했으므로 책임 면제  
D. 변수명만 Review

## Q02
Copilot이 `이 API는 공식 지원된다`고 설명했지만 근거 링크가 없다. FIRST 행동은?  
A. 최신 공식 문서에서 API와 버전을 확인  
B. 바로 Release  
C. Test 삭제  
D. Prompt를 더 길게 작성

## Q03
AI가 생성한 SQL 코드가 입력 문자열을 직접 Query에 연결한다. BEST 행동은?  
A. 코드를 Reject/수정하고 안전한 Parameterized 방식과 Test를 검토  
B. 그대로 사용  
C. 주석만 추가  
D. Public Code Filter만 켬

## Q04
AI Output을 검증하는 이유로 가장 완전한 설명은?  
A. LLM은 확률적이며 Hallucination·Bias·보안·최신성·Context 한계가 있기 때문  
B. AI는 항상 문법 오류만 내기 때문  
C. Chat에서만 틀리기 때문  
D. GitHub Repository가 없기 때문

## Q05
실제 고객 로그에 PII가 포함되어 있다. Debugging에 Copilot을 사용하려면 BEST 방법은?  
A. PII를 제거·마스킹하고 최소한의 재현 데이터 사용  
B. 로그 전체 업로드  
C. Token과 함께 제공  
D. Public Gist 생성

## Q06
Responsible AI에서 `Mitigation`의 예로 가장 적절한 것은?  
A. Bias 평가·Human Review·Test·Security Check를 적용  
B. 모든 Output 자동 승인  
C. Agent 최대 권한  
D. Audit Log 삭제

## Q07
AI가 제안한 코드의 최종 책임에 대한 BEST 설명은?  
A. AI Vendor가 모든 책임을 자동 부담  
B. 사용 조직과 개발자가 정책·검증·승인 책임을 유지  
C. 책임 개념이 사라짐  
D. Test가 있으면 책임 없음

## Q08
개발자는 함수 본문을 작성 중이고 다음 Pattern을 빠르게 이어 쓰고 싶다. MOST direct 기능은?  
A. Inline Suggestion  
B. Agent Mode  
C. Audit Log  
D. Space

## Q09
개발자는 현재 PR의 복잡한 변경 이유를 대화형으로 질문하고 싶다. 가장 적합한 것은?  
A. Chat  
B. Content Exclusion  
C. Billing API  
D. Spark

## Q10
정해진 Rename을 여러 파일에 적용하고 각 Diff를 검토하려 한다. Agent Mode보다 먼저 고려할 수 있는 기능은?  
A. Edits  
B. Audit Log  
C. Space  
D. Public Code Filter

## Q11
`원인을 조사→파일 수정→Test 실행→실패 시 다시 수정`이 필요한 Task는?  
A. Agent Mode  
B. Inline Suggestion  
C. PR Summary  
D. Content Exclusion

## Q12
Agent Mode를 사용할 때 `Constraints`에 넣기 가장 적절한 것은?  
A. 수정 가능한 디렉터리와 실행 가능한 Tool 범위  
B. 모든 Credential  
C. 관리자 비밀번호  
D. 무제한 네트워크 접근

## Q13
Terminal에서 자연어로 명령을 탐색하면서 연속 세션으로 작업하려 한다. 관련 기능은?  
A. Copilot CLI  
B. Spark  
C. Space  
D. Audit Log

## Q14
MCP Server가 Issue 읽기와 Issue 수정 Tool을 모두 제공한다. 읽기만 필요한 Agent에게 BEST 권한은?  
A. Read-only에 필요한 최소 Scope  
B. Admin Write  
C. 모든 Repository Write  
D. Organization Owner

## Q15
Sub-Agent를 사용하는 BEST 이유는?  
A. 복잡한 Task를 역할별 하위 작업으로 분리하고 Context를 관리  
B. 모든 Context를 무제한 공유  
C. Secret을 저장  
D. Test를 생략

## Q16
Copilot Code Review가 `문제 없음`이라고 했다. BEST 다음 행동은?  
A. Human Reviewer가 Requirement·Security·Test Evidence를 최종 확인  
B. 자동 Merge  
C. Test 삭제  
D. Branch Protection 해제

## Q17
조직이 코드 검토 기준을 일관되게 Copilot에 제공하려 한다. MOST relevant 기능은?  
A. Instructions  
B. Content Exclusion  
C. Git Tag  
D. Billing

## Q18
팀이 동일한 Security Review Prompt를 여러 번 재사용하려 한다. MOST relevant 기능은?  
A. Prompt File  
B. Audit Log  
C. Space  
D. Branch

## Q19
조직의 Copilot Policy 변경 기록을 조사해야 한다. FIRST로 볼 곳은?  
A. Audit Log  
B. Inline Suggestion  
C. Spark  
D. Unit Test

## Q20
Copilot Subscription 관리 자동화와 가장 직접적으로 연결되는 것은?  
A. REST API  
B. Git Merge  
C. Gist  
D. Pages

## Q21
개발자의 입력과 Editor Context가 수집된 다음 모델 요청을 구성하는 단계는?  
A. Prompt Building  
B. Git Commit  
C. Billing  
D. Deployment

## Q22
다음 중 Copilot Data Flow를 과도하게 단순화한 잘못된 설명은?  
A. Context가 Prompt 구성에 영향을 줄 수 있다.  
B. 서비스 Filtering/Post-processing이 있을 수 있다.  
C. 모든 Repository 파일이 항상 그대로 모델에 전달되고 영구 학습된다.  
D. LLM Response 후 Suggestion이 표시된다.

## Q23
Context Window가 제한되어 있을 때 가장 좋은 Prompt 전략은?  
A. 필요한 파일·Error·Requirement를 우선 제공  
B. 관련 없는 모든 파일 추가  
C. Secret 추가  
D. Prompt 제거

## Q24
Copilot이 반복적으로 오래된 Syntax를 추천한다. 이것과 가장 관련 있는 LLM 한계는?  
A. 최신성/Source Data의 시점 한계  
B. Audit Log  
C. Billing  
D. Branch Protection

## Q25
Prompt/Response의 Filtering과 Post-processing을 이해할 때 핵심은?  
A. 모델 Output 전후에 서비스 수준의 정책·보호 처리가 있을 수 있음  
B. Human Review가 필요 없음  
C. 모든 Output이 동일  
D. Git History 변경

## Q26
`기존 API 유지, 외부 Package 금지, Python 3.12`는 Prompt에서 주로 무엇인가?  
A. Constraints  
B. Output  
C. Audit  
D. Space

## Q27
`정답은 JSON으로, 각 Finding에 severity와 evidence 포함`은 무엇인가?  
A. Output format  
B. Hallucination  
C. Policy  
D. Billing

## Q28
모델이 원하는 형식 예시를 잘 따르지 못한다. MOST appropriate한 개선은?  
A. 좋은 Few-shot 예시를 제공  
B. Secret 추가  
C. 모든 Context 제거  
D. Test 삭제

## Q29
이전 Chat에서 `Node 18`을 전제로 했지만 현재 프로젝트는 `Node 22`다. BEST 행동은?  
A. 현재 버전을 명시하고 이전 전제를 교정  
B. 그대로 진행  
C. Repository 삭제  
D. Audit Log 삭제

## Q30
Prompt Engineering에서 Verification 기준을 포함하는 이유는?  
A. Output의 성공 여부를 Human/Test가 확인할 기준을 명확히 하기 위해  
B. AI가 무조건 정확해지기 위해  
C. Billing을 줄이기 위해  
D. Branch를 보호하기 위해

## Q31
Copilot이 만든 Refactor가 더 읽기 쉽지만 기존 Error Behavior가 바뀌었다. BEST 판정은?  
A. Requirement 위반 가능성이므로 수정 또는 Reject하고 Test 보완  
B. 읽기 쉬우므로 승인  
C. AI가 만들었으니 승인  
D. Test 삭제

## Q32
AI가 Unit Test 20개를 생성했다. 숫자만으로 품질을 판단할 수 없는 이유는?  
A. Edge Case·Assertion·Requirement Coverage가 중요하기 때문  
B. Test 수는 항상 1개여야 하기 때문  
C. AI Test는 실행되지 않기 때문  
D. Audit Log와 무관하기 때문

## Q33
AI가 `성능 50% 개선`이라고 주장했다. BEST Verification은?  
A. 동일 조건 Benchmark와 Correctness Test  
B. 설명 길이  
C. Comment 수  
D. Commit 메시지

## Q34
Security 취약점 검토를 Copilot에 요청했다. BEST 사용법은?  
A. 추가 Review Signal로 사용하고 Scanner/Threat Analysis/Test와 결합  
B. AI 결과만으로 보안 승인  
C. Secret Scanning 제거  
D. Human Review 제거

## Q35
Content Exclusion의 가장 정확한 한계 설명은?  
A. 특정 Context 사용을 제한하지만 모든 데이터·보안 위험을 제거하지 않는다.  
B. 모든 Secret을 자동 회전한다.  
C. 파일을 Repository에서 삭제한다.  
D. Human Review를 대체한다.

## Q36
Exclusion이 설정됐는데 특정 Editor에서 기대대로 동작하지 않는다. FIRST로 확인할 것은?  
A. 해당 Editor/기능의 지원, 설정 Scope, 경로, Policy 상태  
B. 모든 Credential 공개  
C. Test 삭제  
D. Organization Owner 권한 부여

## Q37
Suggestions matching public code filtering을 사용해도 반드시 별도로 확인할 것은?  
A. 조직의 라이선스·정책·법적 요구사항  
B. 아무것도 없음  
C. Test 삭제  
D. Git History 제거

## Q38
Copilot Suggestion이 갑자기 모든 파일에서 보이지 않는다. FIRST 진단은?  
A. Sign-in/Extension/Feature availability/Policy 상태부터 확인  
B. Repository 삭제  
C. Production Token 공개  
D. 모든 Exclusion 해제

## Q39
Privacy와 Security를 함께 만족시키는 BEST 접근은?  
A. Data 최소화·Exclusion/Policy + Secure Code Review/Test를 함께 적용  
B. Privacy만 보면 Security 불필요  
C. Security만 보면 PII 불필요  
D. Agent 최대 권한

## Q40
최종 Exam-Ready 판정에 가장 적절한 조건은?  
A. 최신 Study Guide 확인 + QBank 85%+ + Mock 2회 85%+ + Final 90% 권장 + 오답 90%+  
B. 기능 이름 암기  
C. Dump 암기  
D. 실습 없음

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
