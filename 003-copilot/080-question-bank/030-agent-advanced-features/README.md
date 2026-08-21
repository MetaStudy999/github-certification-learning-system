# 030 에이전트 와 고급 기능 — Q021–Q030 (030 Agent & Advanced Features — Q021–Q030, AAFQ021Q030)

> Skill Area: **Use GitHub Copilot features**

## Q021

여러 파일을 조사하고 수정한 뒤 Test를 실행하고 실패하면 다시 수정하는 작업에 가장 적합한 기능은?

A. Inline Suggestion  
B. Agent Mode  
C. Audit Log  
D. Content Exclusion

<details><summary>정답</summary>

**B.** Agent Mode는 목표를 받아 여러 단계의 작업과 Tool 사용을 반복할 수 있는 Scenario에 적합합니다.
</details>

## Q022

Agent Mode를 사용할 때 가장 중요한 안전 원칙은?

A. 가능한 모든 File과 Tool에 관리자 권한을 준다.  
B. 필요한 범위의 최소 권한과 명확한 Constraints를 제공한다.  
C. Test를 생략해 시간을 줄인다.  
D. Agent가 수정한 내용은 자동 Merge한다.

<details><summary>정답</summary>

**B.** Agent가 행동할 수 있으므로 Tool·Data·Credential 범위를 최소화하고 검증 조건을 명확히 해야 합니다.
</details>

## Q023

MCP(Model Context Protocol)의 역할을 가장 정확하게 설명한 것은?

A. Git Branch를 병합하는 프로토콜  
B. AI/Agent와 외부 Tool·Data Source의 연결을 표준화하는 프로토콜  
C. Copilot 구독 결제 방식  
D. 공개 코드 필터의 다른 이름

<details><summary>정답</summary>

**B.** MCP는 모델/Agent가 외부 Context와 Tool을 표준화된 방식으로 사용할 수 있게 하는 연결 계층입니다.
</details>

## Q024

MCP Server를 Agent에 연결할 때 FIRST로 고려할 보안 사항은?

A. Server 이름 길이  
B. Agent가 접근할 Data와 Tool 권한 범위  
C. README 색상  
D. Commit Message 형식

<details><summary>정답</summary>

**B.** Trust Boundary와 최소 권한이 핵심입니다.
</details>

## Q025

Sub-Agent를 사용하는 목적에 가장 가까운 것은?

A. 모든 작업을 한 Context에 무조건 합친다.  
B. 특정 하위 작업을 분리·위임해 역할과 Context를 관리한다.  
C. Repository를 Fork한다.  
D. Content Exclusion을 해제한다.

<details><summary>정답</summary>

**B.** Sub-Agent는 복잡한 작업을 역할별로 분리하고 Context 사용을 최적화하는 데 활용될 수 있습니다.
</details>

## Q026

Copilot Code Review에 대한 설명으로 가장 적절한 것은?

A. Human Reviewer가 더 이상 필요 없다.  
B. AI가 PR의 변경을 검토하고 개선 제안을 제공할 수 있지만 최종 판단은 사람이 해야 한다.  
C. Merge 권한을 항상 자동 부여한다.  
D. Unit Test를 삭제한다.

<details><summary>정답</summary>

**B.** AI Review는 보조 수단이며 Accountability와 최종 승인 책임을 대체하지 않습니다.
</details>

## Q027

Pull Request Summary의 주된 목적은?

A. PR 변경내용을 이해하기 쉽게 요약하도록 지원  
B. Repository를 자동 삭제  
C. Secret을 암호화  
D. Branch Protection을 해제

<details><summary>정답</summary>

**A.** PR Summary는 변경 이해와 Review 준비를 돕는 기능입니다.
</details>

## Q028

팀의 Architecture 규칙, API Convention, Design Pattern을 Copilot이 참고할 수 있는 지식 Context로 묶고 싶다. 가장 관련 있는 기능은?

A. Spaces  
B. Git Stash  
C. Dependabot  
D. Pages

<details><summary>정답</summary>

**A.** Spaces는 관련 지식과 Context를 묶어 Copilot 활용에 제공하는 용도로 이해할 수 있습니다.
</details>

## Q029

자연어 요구사항을 기반으로 작은 애플리케이션 Prototype을 빠르게 만들고 발전시키려 한다. 가장 관련 있는 기능은?

A. GitHub Spark  
B. Audit Log  
C. Content Exclusion  
D. Git Tag

<details><summary>정답</summary>

**A.** Spark는 자연어 중심의 앱 생성·개발 Scenario에 해당합니다.
</details>

## Q030

Agent Mode가 Chat보다 항상 더 좋은 선택이 아닌 이유는?

A. Agent Mode는 코드를 볼 수 없기 때문이다.  
B. 단순 질문에는 불필요한 Tool 권한·작업 범위·복잡성을 늘릴 수 있기 때문이다.  
C. Chat은 모든 Tool을 자동 실행하기 때문이다.  
D. Agent Mode는 Prompt를 사용하지 않기 때문이다.

<details><summary>정답</summary>

**B.** 작업 목적에 맞는 최소한의 기능을 선택해야 안전성과 효율성이 높습니다.
</details>

---
[← 020 IDE & CLI](../020-ide-cli-features/README.md) · [040 Organization & Governance →](../040-org-feature-governance/README.md)
