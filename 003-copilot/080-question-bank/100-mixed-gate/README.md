# 100 Mixed Exam Gate — Q091–Q100

> 전 범위 Scenario Gate. 각 문제에서 **목적·제약·검증 책임**을 먼저 찾습니다.

## Q091

팀이 여러 Repository에서 동일한 Python 코딩 규칙을 Copilot에 지속적으로 적용하고 싶다. 가장 적절한 접근은?

A. 매 질문마다 규칙을 수동으로 다시 입력한다.  
B. Instructions를 사용해 지속 지침을 제공한다.  
C. Content Exclusion을 모두 해제한다.  
D. Audit Log를 삭제한다.

<details><summary>정답</summary>

**B.** 반복되는 공통 지침은 Instructions 활용 Scenario와 맞습니다.
</details>

## Q092

Agent가 외부 Issue 시스템을 조회하고 파일을 수정해야 한다. 가장 중요한 설계 원칙은?

A. 모든 Tool에 관리자 권한을 부여한다.  
B. MCP/Tool 연결의 Data·Write·Credential Scope를 최소화하고 실행 결과를 검증한다.  
C. Test를 제거한다.  
D. Prompt에 Production Secret을 넣는다.

<details><summary>정답</summary>

**B.** Agentic Workflow에서는 Tool Trust Boundary와 최소 권한이 핵심입니다.
</details>

## Q093

Copilot이 생성한 Migration 코드가 기존 Test를 통과하지만 새 Database Version에서만 실패한다. 가장 적절한 교훈은?

A. 기존 Test 통과만으로 충분하지 않다. 목표 환경의 Integration/Compatibility Test가 필요하다.  
B. AI 코드는 Test할 필요가 없다.  
C. Content Exclusion 문제다.  
D. Audit Log를 끄면 해결된다.

<details><summary>정답</summary>

**A.** Verification은 실제 Requirement와 Target Environment를 포함해야 합니다.
</details>

## Q094

조직에서 Copilot Code Review를 활성화했다. 어떤 운영 방식이 가장 적절한가?

A. AI Review가 있으면 모든 Human Approval을 제거한다.  
B. AI Review를 추가 신호로 사용하고 사람 Reviewer가 요구사항·보안·Risk를 최종 판단한다.  
C. 모든 PR을 자동 Merge한다.  
D. Test 실패도 무시한다.

<details><summary>정답</summary>

**B.** Copilot Code Review는 Human Review를 강화하는 보조 수단입니다.
</details>

## Q095

Copilot 답변이 오래된 API를 사용한다. 가장 적절한 FIRST 행동은?

A. 최신 공식 Documentation과 현재 Version을 확인한다.  
B. 답변이 길면 그대로 사용한다.  
C. Repository를 Public으로 바꾼다.  
D. Secret을 더 제공한다.

<details><summary>정답</summary>

**A.** 최신성 한계를 공식 자료로 검증해야 합니다.
</details>

## Q096

`입력 검증 함수를 개선해 줘`라는 Prompt가 원하는 결과를 자주 내지 못한다. 가장 좋은 개선은?

A. Input/Expected behavior/Error policy/Constraints/Test criteria를 Context와 함께 명확히 제공한다.  
B. Prompt를 더 짧게 만든다.  
C. Verification을 제거한다.  
D. 실제 Password를 추가한다.

<details><summary>정답</summary>

**A.** 명확한 Prompt Structure와 관련 Context가 필요합니다.
</details>

## Q097

특정 Source 파일을 Content Exclusion에 추가했다. 가장 정확한 기대는?

A. 해당 파일이 Repository에서 삭제된다.  
B. 설정 범위에서 Copilot Context 사용을 제한하는 데 도움되지만 별도의 Secret/Access 관리가 계속 필요하다.  
C. 모든 AI 위험이 사라진다.  
D. Human Review가 필요 없어졌다.

<details><summary>정답</summary>

**B.** Content Exclusion은 하나의 Privacy/Context Control입니다.
</details>

## Q098

새 기능을 빠르게 Prototype하고 싶은 개발자가 자연어로 앱을 만들고 반복 개선하려 한다. 현재 시험 범위에서 가장 관련 있는 기능은?

A. Spark  
B. Audit Log  
C. Git Tag  
D. Content Exclusion

<details><summary>정답</summary>

**A.** GitHub Spark는 자연어 중심 앱 생성·개발 Scenario와 연결됩니다.
</details>

## Q099

Copilot의 Suggestion이 공개 코드와 일치할 가능성을 관리하고 싶다. 가장 관련 있는 Safeguard는?

A. Suggestions matching public code filtering  
B. Branch Rename  
C. Git Rebase  
D. Issue Label

<details><summary>정답</summary>

**A.** 공개 코드 Matching을 다루는 필터 설정이 관련됩니다.
</details>

## Q100

GH-300 준비가 가장 잘 되었다고 볼 수 있는 상태는?

A. 기능 이름만 100개 암기했다.  
B. 6개 Skill Area를 설명하고 IDE/CLI/Agent/MCP를 실습했으며 QBank·Mock에서 반복적으로 목표 점수를 넘고 오답을 재검증했다.  
C. 실제 시험 Dump만 외웠다.  
D. Copilot Output을 한 번도 검증하지 않았다.

<details><summary>정답</summary>

**B.** 최신 시험 범위 이해 + 실습 + 문제풀이 + 검증 가능한 점수와 오답 학습이 함께 필요합니다.
</details>

## 100문제 Gate

- [ ] 1회차 **80/100 이상**
- [ ] 2회차 **85/100 이상**
- [ ] 오답 재시험 **90% 이상**
- [ ] 약점 Skill Area의 관련 Lab 재수행

다음 단계: [`110 Mock Exams`](../../110-mock-exams/README.md)

---
[← 090 Privacy & Safeguards](../090-privacy-safeguards/README.md) · [Question Bank 홈](../README.md)
