# 020 IDE & CLI Features — Q011–Q020

> Skill Area: **Use GitHub Copilot features**

## Q011

코드를 작성하는 도중 다음 줄의 구현을 빠르게 제안받고 싶다. 가장 직접적인 기능은?

A. Audit Log  
B. Inline Suggestion  
C. Content Exclusion  
D. Space

<details><summary>정답</summary>

**B.** Inline Suggestion은 코드 작성 흐름 안에서 다음 코드 제안을 제공합니다.
</details>

## Q012

현재 함수가 왜 오류를 발생시키는지 대화형으로 질문하고 설명을 이어가고 싶다. 가장 적합한 기능은?

A. Copilot Chat  
B. Subscription REST API  
C. Public Code Filter  
D. CODEOWNERS

<details><summary>정답</summary>

**A.** 설명·추가 질문·디버깅 탐색에는 Chat이 적합합니다.
</details>

## Q013

Terminal에서 자연어로 Shell 명령을 탐색하고 Script 초안을 만들고 싶다. 가장 관련 있는 기능은?

A. Copilot CLI  
B. Copilot Space  
C. Pull Request Summary  
D. Content Exclusion

<details><summary>정답</summary>

**A.** Copilot CLI는 Terminal 중심 상호작용과 Script·File 작업에 사용됩니다.
</details>

## Q014

Copilot CLI가 생성한 Shell Script를 실행하기 전에 가장 중요한 행동은?

A. Prompt를 삭제한다.  
B. 파일·권한·명령의 영향을 검토한다.  
C. 무조건 관리자 권한으로 실행한다.  
D. Extension을 재설치한다.

<details><summary>정답</summary>

**B.** 생성 Script도 AI Output이므로 파괴적 명령, 경로, 권한, Secret 노출 여부를 검토해야 합니다.
</details>

## Q015

여러 파일에 걸친 변경을 AI의 제안 형태로 편집하고 검토하면서 적용하려 한다. 가장 직접적으로 고려할 기능은?

A. Copilot Edits  
B. Audit Log  
C. Billing  
D. Public Code Matching Filter

<details><summary>정답</summary>

**A.** Edits는 다중 파일 변경을 편집·검토하는 작업에 적합합니다.
</details>

## Q016

다음 중 Chat보다 Inline Suggestion을 우선 고려하기 좋은 상황은?

A. Architecture 대안을 장시간 토론  
B. 현재 함수의 반복적인 다음 코드를 작성  
C. 조직 정책을 감사  
D. MCP Server 권한을 설계

<details><summary>정답</summary>

**B.** 작성 중인 코드의 다음 부분을 빠르게 완성하는 상황에 Inline Suggestion이 자연스럽습니다.
</details>

## Q017

Copilot Chat의 Output에 가장 적절한 태도는?

A. IDE에 표시되므로 공식 문서와 동일하게 본다.  
B. 대화형 제안으로 보고 실행·문서·Test로 검증한다.  
C. Code Review 없이 자동 승인한다.  
D. 답변이 길수록 정확하다고 본다.

<details><summary>정답</summary>

**B.** Chat 응답 역시 확률적 AI Output이므로 검증이 필요합니다.
</details>

## Q018

IDE에서 Copilot Suggestion이 전혀 보이지 않는다. FIRST로 확인하기 가장 적절한 것은?

A. 무조건 OS를 재설치한다.  
B. Copilot 활성화·Sign-in·Extension/IDE 상태와 해당 파일 지원 여부를 확인한다.  
C. 모든 Content Exclusion을 삭제한다.  
D. Repository를 Public으로 변경한다.

<details><summary>정답</summary>

**B.** 기본 활성화·인증·환경 상태부터 단계적으로 Troubleshoot하는 것이 적절합니다.
</details>

## Q019

CLI Session을 사용하는 이점으로 가장 적절한 것은?

A. 모든 Shell 명령을 안전하다고 자동 승인한다.  
B. Terminal Workflow 안에서 Context를 이어가며 상호작용할 수 있다.  
C. Repository 권한을 자동 상승시킨다.  
D. Content Exclusion을 무효화한다.

<details><summary>정답</summary>

**B.** Session은 CLI 상호작용의 연속성을 제공할 수 있지만 권한·안전 검토를 대체하지 않습니다.
</details>

## Q020

IDE와 CLI 중 어느 인터페이스를 선택할지 결정할 때 가장 중요한 기준은?

A. 항상 최신 기능이 많은 쪽  
B. 현재 작업 흐름과 필요한 상호작용 방식  
C. 답변 글자 수  
D. Repository Star 수

<details><summary>정답</summary>

**B.** 시험에서도 Scenario의 목적과 Workflow에 맞는 기능 선택이 핵심입니다.
</details>

---
[← 010 Responsible AI](../010-responsible-ai/README.md) · [030 Agent & Advanced Features →](../030-agent-advanced-features/README.md)
