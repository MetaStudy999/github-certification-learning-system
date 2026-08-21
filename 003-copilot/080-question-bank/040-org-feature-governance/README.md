# 040 Organization & Feature Governance — Q031–Q040

> Skill Area: **Use GitHub Copilot features**

## Q031

조직 전체에서 특정 Copilot 기능의 사용 가능 여부를 중앙 관리하려 한다. 가장 관련 있는 개념은?

A. Organization-wide Policy  
B. Git Stash  
C. Fork  
D. Release Tag

<details><summary>정답</summary>

**A.** Organization Policy는 조직 차원에서 Copilot 기능과 사용 범위를 관리하는 데 사용됩니다.
</details>

## Q032

관리자가 Copilot 관련 설정 변경 이벤트를 추적하려 한다. 가장 적절한 기능은?

A. Audit Log  
B. Inline Suggestion  
C. Spark  
D. Unit Test

<details><summary>정답</summary>

**A.** Audit Log는 조직의 관리 이벤트 추적에 사용됩니다.
</details>

## Q033

Copilot Subscription 관리를 자동화하는 관리 Scenario와 가장 관련 있는 것은?

A. REST API  
B. Markdown Preview  
C. Git Merge  
D. Codespaces Port Forwarding

<details><summary>정답</summary>

**A.** 최신 GH-300 범위에는 Subscription 관리에 REST API를 사용하는 개념이 포함됩니다.
</details>

## Q034

Repository 전반에서 `Python 3.12, type hints, pytest` 규칙을 Copilot에 지속적으로 전달하려 한다. 가장 적절한 것은?

A. Instructions File  
B. 일회성 Chat Prompt만 사용  
C. Audit Log  
D. Branch Protection

<details><summary>정답</summary>

**A.** 반복 적용되는 Repository 수준 지침은 Instructions File이 적합한 후보입니다.
</details>

## Q035

매번 PR을 검토할 때 동일한 분석 절차를 재사용하려 한다. 가장 적절한 방식은?

A. Prompt File  
B. Content Exclusion  
C. Git Tag  
D. Secret Scanning

<details><summary>정답</summary>

**A.** 반복 가능한 Task Prompt를 파일로 저장해 재사용하는 방식이 적합합니다.
</details>

## Q036

Instructions File과 Prompt File의 차이를 가장 정확하게 설명한 것은?

A. 둘은 완전히 같은 기능이다.  
B. Instructions는 지속적인 지침, Prompt File은 반복 Task Prompt 재사용에 가깝다.  
C. Instructions는 Secret 저장용이다.  
D. Prompt File은 Audit Log다.

<details><summary>정답</summary>

**B.** 적용 목적과 지속성 관점에서 구분합니다.
</details>

## Q037

조직에서 Code Review 정책을 켰다고 해서 가장 잘못된 결론은?

A. Review Workflow를 일관되게 관리할 수 있다.  
B. AI Review 결과를 사람이 다시 확인해야 한다.  
C. 모든 Human Reviewer를 즉시 제거해도 된다.  
D. 기능 가용성을 Policy로 관리할 수 있다.

<details><summary>정답</summary>

**C.** AI Review는 보조 기능이며 Human Accountability를 대체하지 않습니다.
</details>

## Q038

Audit Log의 목적과 가장 거리가 먼 것은?

A. 관리 변경 추적  
B. 관련 이벤트 조사  
C. 조직 운영 가시성 향상  
D. AI Output의 정확성을 자동 보장

<details><summary>정답</summary>

**D.** Audit Log는 운영 이벤트 추적 도구이지 AI Output 검증 도구가 아닙니다.
</details>

## Q039

조직 Policy를 설계할 때 고려할 항목으로 가장 적절하지 않은 것은?

A. Security / Compliance  
B. Feature availability  
C. Data governance  
D. 모든 사용자에게 무조건 최대 권한 부여

<details><summary>정답</summary>

**D.** 최소 권한과 조직 요구사항에 맞는 통제가 기본 원칙입니다.
</details>

## Q040

Copilot Code Review의 Review Standard를 Instructions로 정의하는 가장 큰 목적은?

A. 검토 기준의 일관성을 높이기 위해  
B. 모든 Test를 삭제하기 위해  
C. Repository를 Private으로 바꾸기 위해  
D. CLI를 비활성화하기 위해

<details><summary>정답</summary>

**A.** 일관된 검토 관점을 제공하는 데 도움이 됩니다.
</details>

---
[← 030 Agent Features](../030-agent-advanced-features/README.md) · [050 Data & Architecture →](../050-data-architecture/README.md)
