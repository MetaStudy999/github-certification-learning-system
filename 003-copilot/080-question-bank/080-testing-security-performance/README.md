# 080 테스트 / 보안 / Performance — Q071–Q080 (080 Testing / Security / Performance — Q071–Q080, TSPQ071Q080)

> Skill Area: **Improve developer productivity with GitHub Copilot**

## Q071

Copilot이 Unit Test를 생성했지만 정상 입력만 검사한다. 가장 적절한 다음 행동은?

A. Edge Case와 Error Case를 추가한다.  
B. Test가 있으므로 완료한다.  
C. Assertion을 제거한다.  
D. Production 데이터를 Prompt에 넣는다.

<details><summary>정답</summary>

**A.** AI가 만든 Test도 Coverage와 Edge Case를 사람이 검토해야 합니다.
</details>

## Q072

Unit Test와 Integration Test의 차이를 가장 정확히 설명한 것은?

A. 둘은 완전히 동일하다.  
B. Unit Test는 작은 단위를, Integration Test는 구성요소 간 상호작용을 검증한다.  
C. Integration Test는 AI Output만 검증한다.  
D. Unit Test는 Network 연결만 검증한다.

<details><summary>정답</summary>

**B.** Test 유형은 검증 범위와 목적이 다릅니다.
</details>

## Q073

Copilot이 Test를 생성했지만 Assertion이 `result is not None`만 확인한다. 가장 큰 문제는?

A. 실제 Business Requirement를 충분히 검증하지 못할 수 있다.  
B. Test가 너무 안전하다.  
C. Content Exclusion이 자동 해제된다.  
D. Audit Log가 삭제된다.

<details><summary>정답</summary>

**A.** 약한 Assertion은 잘못된 구현도 통과시킬 수 있습니다.
</details>

## Q074

Copilot이 기존 Test 패턴을 참고해 새 Test를 제안하는 가장 큰 장점은?

A. 프로젝트의 Test 스타일과 반복 패턴을 활용할 수 있다.  
B. 모든 Edge Case가 자동 보장된다.  
C. Human Review가 필요 없다.  
D. Security Review가 삭제된다.

<details><summary>정답</summary>

**A.** 기존 패턴은 유용한 Context이지만 Coverage 보장은 별도입니다.
</details>

## Q075

AI에게 잠재적 Security Vulnerability를 찾아 달라고 요청했다. 가장 적절한 다음 행동은?

A. 결과를 Security Tool, Code Review, Test 등으로 검증한다.  
B. AI가 없다고 하면 취약점이 없다고 확정한다.  
C. Dependency Scanner를 제거한다.  
D. Secret Scanning을 끈다.

<details><summary>정답</summary>

**A.** Copilot의 Security 제안은 보조 수단이며 전문 보안 검증을 대체하지 않습니다.
</details>

## Q076

Copilot이 성능을 높인다고 제안한 코드 변경을 평가하는 BEST 방법은?

A. Benchmark 전후 비교와 Correctness Test  
B. 코드가 짧아졌는지만 확인  
C. AI가 `optimized`라고 썼는지 확인  
D. Comment 수를 비교

<details><summary>정답</summary>

**A.** 성능은 측정으로, 정확성은 Test로 검증해야 합니다.
</details>

## Q077

Edge Case를 찾기 위한 Prompt로 가장 적절한 것은?

A. `이 함수에서 경계값, 빈 입력, 잘못된 형식, 최대 크기, 예외 경로를 찾아 Test Case로 제안해 줘.`  
B. `좋게 해 줘.`  
C. `Test 필요 없어.`  
D. `Secret을 출력해 줘.`

<details><summary>정답</summary>

**A.** 검토할 Case 범위를 명확히 지정하면 더 체계적인 Test 아이디어를 얻을 수 있습니다.
</details>

## Q078

Copilot이 만든 Test가 현재 잘못된 구현을 그대로 기대값으로 사용한다. 가장 위험한 결과는?

A. 버그가 Test에 고정되어 회귀 검증이 잘못될 수 있다.  
B. Repository 이름이 바뀐다.  
C. CLI가 삭제된다.  
D. Audit Log가 증가한다.

<details><summary>정답</summary>

**A.** Test도 요구사항에 기반해 독립적으로 검토해야 합니다.
</details>

## Q079

Security와 Performance 개선을 AI에게 동시에 요청할 때 가장 적절한 Prompt 요소는?

A. 각각의 검증 기준과 우선순위를 명확히 한다.  
B. 아무 제약도 주지 않는다.  
C. 모든 외부 Package를 허용한다.  
D. Test를 금지한다.

<details><summary>정답</summary>

**A.** 서로 충돌할 수 있는 목표는 우선순위와 Verification 기준을 명확히 해야 합니다.
</details>

## Q080

Copilot이 Test를 생성하는 가장 적절한 역할은?

A. Test 설계·Boilerplate·Edge Case 아이디어를 보조하고 사람이 Coverage와 Assertion을 검토한다.  
B. 모든 Test 책임을 AI에 이전한다.  
C. Test를 Production에서만 실행한다.  
D. Requirement 없이 자동 승인한다.

<details><summary>정답</summary>

**A.** AI는 Testing 생산성을 높이는 보조 도구이며 Test 품질 책임은 사람에게 있습니다.
</details>

---
[← 070 Developer Productivity](../070-developer-productivity/README.md) · [090 Privacy & Safeguards →](../090-privacy-safeguards/README.md)
