# GH-300 Mock 02 — Questions

**40문항 / 자체 제작 / 응시 Gate용**  
정답은 마지막에 [`answers.md`](./answers.md)에서 확인합니다.

## Q01
한 의료 앱 팀이 AI가 제안한 환자 위험 분류 코드를 사용하려 한다. FIRST로 추가해야 할 검토는?  
A. 변수명 길이  
B. Bias/Fairness, Privacy, Accuracy 검증  
C. Commit 수  
D. Star 수

## Q02
Copilot이 보안 코드를 제안했지만 공식 API와 다르다. BEST 행동은?  
A. 최신 공식 Docs와 실제 실행으로 검증  
B. 설명이 길면 채택  
C. Test 제거  
D. Token 공개

## Q03
AI가 생성한 결과의 잠재적 Harm을 줄이기 위한 BEST 조합은?  
A. Human Review + Test + Security/Privacy Review  
B. Prompt 한 줄  
C. 자동 Merge  
D. 관리자 권한

## Q04
팀원이 `Copilot이 만들었으니 라이선스 책임은 없다`고 말한다. BEST 응답은?  
A. 맞다  
B. 최신 약관·조직 정책·법무 기준을 확인해야 한다  
C. Public Repo면 맞다  
D. CLI에서만 맞다

## Q05
AI가 설명한 알고리즘이 논리적으로 그럴듯하지만 Test에서 실패한다. 무엇을 우선 신뢰해야 하는가?  
A. 설명 문체  
B. 실제 Requirement와 실행/Test Evidence  
C. 답변 길이  
D. 모델 이름

## Q06
AI Output의 Bias를 줄이기 위한 방법으로 가장 적절하지 않은 것은?  
A. 다양한 Case로 평가  
B. 영향 받는 집단별 결과 점검  
C. 검증 없이 첫 Output 사용  
D. Human Review

## Q07
Responsible AI 운영의 핵심으로 가장 적절한 것은?  
A. AI를 사람보다 항상 우선  
B. Risk 이해 + Validation + Accountability  
C. Prompt 비공개  
D. Repository 삭제

## Q08
개발자가 현재 코드 블록을 선택하고 해당 로직의 의미를 질문하려 한다. 가장 자연스러운 기능은?  
A. Chat/Inline Chat  
B. Audit Log  
C. Spark  
D. Billing API

## Q09
여러 파일의 API 이름을 동일한 규칙으로 변경하고 변경안을 검토하려 한다. BEST 기능은?  
A. Edits  
B. Content Exclusion  
C. Audit Log  
D. Space

## Q10
`버그를 찾아 고치고 Test까지 통과시켜`라는 목표를 반복적으로 수행할 기능은?  
A. Agent Mode  
B. Inline Suggestion  
C. PR Summary  
D. Public Code Filter

## Q11
Agent에게 File Write 권한을 부여하기 전 BEST 질문은?  
A. 필요한 최소 경로와 작업 범위가 무엇인가?  
B. 최대 권한을 줄 수 있는가?  
C. Test를 생략할 수 있는가?  
D. Secret을 공유할 수 있는가?

## Q12
Copilot CLI로 생성한 `rm` 명령이 포함된 Script를 받았다. FIRST 행동은?  
A. 관리자 권한으로 실행  
B. 대상 경로와 파괴적 영향 검토  
C. Audit Log 삭제  
D. Repository Public 전환

## Q13
MCP에 대한 옳은 설명은?  
A. Agent 자체  
B. 모델/Agent와 외부 Tool·Data 연결을 표준화하는 Protocol  
C. Git Commit 형식  
D. Copilot Plan 이름

## Q14
Sub-Agent 사용의 적절한 Scenario는?  
A. 큰 Task를 Test/보안/문서 역할로 분리  
B. Secret 저장  
C. Branch 삭제  
D. Billing 변경

## Q15
팀이 PR 변경 내용을 빠르게 이해하고 싶다. 가장 직접적인 기능은?  
A. Pull Request Summary  
B. Content Exclusion  
C. MCP  
D. Unit Test

## Q16
팀의 공통 설계 지식과 코딩 패턴을 Copilot Context로 정리하려 한다. 관련 기능은?  
A. Spaces  
B. Spark  
C. Stash  
D. Rebase

## Q17
Repository에 지속되는 코딩 규칙을 제공하려 한다. BEST 선택은?  
A. Instructions File  
B. 일회성 Prompt만  
C. Content Exclusion  
D. Audit Log

## Q18
반복되는 `보안 Review 절차`를 Prompt로 저장해 재사용하려 한다. BEST 선택은?  
A. Prompt File  
B. Space  
C. Secret  
D. Branch

## Q19
조직에서 Copilot 기능 가용성과 Code Review 정책을 제어하려 한다. 관련 개념은?  
A. Organization Policy  
B. Git Tag  
C. Local Config만  
D. Fork

## Q20
조직 관리 이벤트를 조사하는 기능은?  
A. Audit Log  
B. Inline Suggestion  
C. Spark  
D. Unit Test

## Q21
Context Gathering 이후 일반적으로 이어질 단계는?  
A. Prompt Building  
B. Git Merge  
C. Billing  
D. Branch Delete

## Q22
사용자 Prompt와 Editor Context가 결합되는 이유는?  
A. 더 관련성 있는 요청을 모델에 구성하기 위해  
B. Repository를 자동 공개하기 위해  
C. Test 삭제를 위해  
D. Secret 회전을 위해

## Q23
Copilot의 Response가 서비스의 후처리를 거칠 수 있음을 나타내는 개념은?  
A. Post-processing  
B. Git Stash  
C. Milestone  
D. Release

## Q24
다음 중 LLM/Copilot 한계가 아닌 것은?  
A. 제한된 Context  
B. Hallucination 가능성  
C. 오래된 정보 가능성  
D. 모든 Output의 100% 정확성

## Q25
관련 없는 대형 Context가 많을 때 발생할 수 있는 문제는?  
A. 혼동·관련성 저하  
B. 항상 정확성 증가  
C. Secret 자동 암호화  
D. Audit Log 감소

## Q26
Prompt에서 `Python 3.12만 사용하고 외부 Package 금지`는 무엇인가?  
A. Constraint  
B. Audit  
C. Exclusion  
D. Space

## Q27
`결과를 JSON 형식으로 반환`은 Prompt의 어떤 요소인가?  
A. Output format  
B. Hallucination  
C. Policy  
D. MCP

## Q28
Few-shot을 사용할 BEST 이유는?  
A. 원하는 패턴/형식을 예시로 보여 주기 위해  
B. Secret 보호  
C. Billing  
D. Audit

## Q29
Chat History가 오래되어 현재 요구와 충돌한다. BEST 행동은?  
A. 필요한 Context를 다시 명시하고 잘못된 전제를 제거  
B. 계속 사용  
C. Test 삭제  
D. Branch 보호 해제

## Q30
Refactoring 성공 기준으로 가장 적절한 것은?  
A. 기존 외부 Behavior 유지 + Test 통과 + 구조 개선  
B. 코드 줄 수 감소  
C. AI 승인  
D. Commit 증가

## Q31
Legacy Code 현대화 시 FIRST로 명확히 해야 할 것은?  
A. 목표 Version·호환성·Test 기준  
B. Prompt 색상  
C. Star 수  
D. PR Label

## Q32
AI가 생성한 Test가 구현 코드를 그대로 복제해 같은 버그를 재현한다. 문제는?  
A. Test 독립성과 요구사항 검증이 약함  
B. Audit 문제  
C. Billing 문제  
D. Context Exclusion 문제

## Q33
Integration Test를 Copilot에 요청할 때 유용한 Context는?  
A. 구성요소 관계·API Contract·환경 설정  
B. 무관한 README  
C. Password  
D. 아무 정보 없음

## Q34
Security 개선 제안을 받아들이기 전 BEST 행동은?  
A. Threat/Scanner/Test/Code Review로 검증  
B. 무조건 적용  
C. Test 제거  
D. Secret 공개

## Q35
Content Exclusion이 기대대로 적용되지 않는 것 같을 때 FIRST 점검은?  
A. 설정 범위·경로·지원 Editor/Policy  
B. Repository 삭제  
C. 모든 Secret 공개  
D. Merge 강제

## Q36
Content Exclusion과 Public Code Matching Filter의 차이는?  
A. Context 사용 제한 vs 공개 코드 일치 제안 처리  
B. 둘 다 Branch 기능  
C. 둘 다 Billing  
D. 완전히 동일

## Q37
Suggestion이 특정 파일에서 안 보일 때 가장 부적절한 행동은?  
A. Extension/Sign-in 확인  
B. 파일·언어 지원 확인  
C. Policy/Exclusion 확인  
D. Production Secret을 Prompt에 넣기

## Q38
Output Ownership 관련 정보를 확인해야 할 BEST 출처는?  
A. 최신 공식 Terms/Docs + 조직 정책  
B. 오래된 임의 블로그 하나  
C. 시험 Dump  
D. AI 답변만

## Q39
Public Code Matching Filter가 켜져 있어도 필요한 것은?  
A. 조직의 라이선스·정책 검토  
B. 아무 검토도 불필요  
C. Human Review 제거  
D. Test 삭제

## Q40
시험 준비 Gate로 가장 적절한 것은?  
A. QBank/Mock 반복 점수 + 오답 재학습 + 최신 Study Guide 확인  
B. 기능 이름만 암기  
C. Dump 암기  
D. 실습 없이 응시

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
