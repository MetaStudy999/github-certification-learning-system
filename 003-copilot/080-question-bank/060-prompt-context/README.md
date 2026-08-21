# 060 프롬프트 와 컨텍스트 — Q051–Q060 (060 Prompt & Context — Q051–Q060, PCQ051Q060)

> Skill Area: **Apply prompt engineering and context crafting**

## Q051

다음 중 좋은 Prompt의 구성으로 가장 적절한 것은?

A. Goal + Context + Constraints + Output + Verification  
B. 파일 이름만 입력  
C. `알아서 해` 한 문장  
D. Secret + Password + Token

<details><summary>정답</summary>

**A.** 목표, 관련 Context, 제약, 원하는 Output, 검증 기준을 명확히 할수록 유용한 결과를 얻기 쉽습니다.
</details>

## Q052

Zero-shot Prompting의 설명으로 가장 적절한 것은?

A. 여러 예시를 제공한다.  
B. 예시 없이 지시와 Context를 제공한다.  
C. Prompt를 전혀 제공하지 않는다.  
D. 항상 Agent Mode를 사용한다.

<details><summary>정답</summary>

**B.** Zero-shot은 별도의 예시 없이 Task를 지시합니다.
</details>

## Q053

Few-shot Prompting이 특히 도움이 될 수 있는 상황은?

A. 원하는 Output 형식과 패턴을 예시로 보여 주고 싶을 때  
B. Context를 완전히 제거하고 싶을 때  
C. Audit Log를 검색할 때만  
D. Secret을 암호화할 때

<details><summary>정답</summary>

**A.** 몇 개의 좋은 예시는 원하는 패턴과 형식을 모델에 보여 줄 수 있습니다.
</details>

## Q054

Few-shot Prompt에서 잘못된 예시를 제공했을 때 가장 큰 위험은?

A. 모델이 그 잘못된 패턴을 따라갈 수 있다.  
B. Repository가 자동 삭제된다.  
C. Git History가 사라진다.  
D. Audit Log가 중지된다.

<details><summary>정답</summary>

**A.** 예시 자체가 Context이므로 부정확한 예시는 Output 품질을 낮출 수 있습니다.
</details>

## Q055

버그 분석 Prompt에 가장 유용한 Context 조합은?

A. 관련 함수 + 실패 Test + Stack Trace + Library Version  
B. 무관한 Repository 100개의 README  
C. 사용자 Password  
D. 아무 Context도 제공하지 않음

<details><summary>정답</summary>

**A.** 문제와 직접 관련된 코드·실패 정보·환경 정보가 우선입니다.
</details>

## Q056

Chat History에 이전의 잘못된 가정이 남아 있다. 가장 적절한 행동은?

A. 계속 같은 가정을 사용한다.  
B. 잘못된 가정을 명시적으로 정정하고 필요한 Context를 다시 제공한다.  
C. 모든 Test를 삭제한다.  
D. Repository를 Fork한다.

<details><summary>정답</summary>

**B.** Chat History도 Context가 될 수 있으므로 잘못된 가정을 교정해야 합니다.
</details>

## Q057

Prompt Engineering과 Prompt Crafting을 구분한 설명으로 가장 적절한 것은?

A. 둘은 반드시 완전히 다른 제품이다.  
B. Crafting은 개별 Prompt 작성, Engineering은 반복 가능한 Prompt 전략과 성능 개선까지 포함하는 관점으로 볼 수 있다.  
C. Prompt Engineering은 Git Merge다.  
D. Prompt Crafting은 Secret 저장이다.

<details><summary>정답</summary>

**B.** 시험에서는 Prompt 구성 원칙과 더 넓은 Engineering Process 모두를 이해해야 합니다.
</details>

## Q058

`기존 API를 유지하면서 Refactor하고 모든 기존 Test를 통과해야 한다`는 내용은 Prompt의 어떤 요소에 가장 가깝나?

A. Constraints / Verification  
B. Audit Event  
C. Billing  
D. Content Exclusion

<details><summary>정답</summary>

**A.** API 유지가 Constraint이고 Test 통과가 Verification 기준입니다.
</details>

## Q059

Prompt에 `코드만 작성해` 대신 `변경 이유와 Test도 함께 제공해`라고 명시하는 가장 큰 장점은?

A. 검토 가능한 Output 구조를 얻는 데 도움이 된다.  
B. AI가 항상 정확해진다.  
C. Privacy가 자동 보장된다.  
D. 모든 보안 취약점이 사라진다.

<details><summary>정답</summary>

**A.** Output 형식과 Verification 요구를 명확히 하면 Human Review가 쉬워집니다.
</details>

## Q060

Context Crafting에서 가장 중요한 원칙은?

A. 가능한 모든 정보를 무조건 넣는다.  
B. 문제 해결에 필요한 관련성 높은 Context를 선택한다.  
C. Secret을 많이 제공한다.  
D. Prompt를 항상 한 단어로 작성한다.

<details><summary>정답</summary>

**B.** 관련성과 명확성이 Context 품질의 핵심입니다.
</details>

---
[← 050 Data & Architecture](../050-data-architecture/README.md) · [070 Developer Productivity →](../070-developer-productivity/README.md)
