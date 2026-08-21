# 070 Developer Productivity — Q061–Q070

> Skill Area: **Improve developer productivity with GitHub Copilot**

## Q061

다음 중 Copilot을 Developer Productivity에 활용하는 예로 가장 적절한 것은?

A. 코드 생성·설명·Refactoring·Documentation 보조  
B. 모든 Production Deployment를 무검증 자동 승인  
C. Secret을 Prompt에 저장  
D. Git History를 제거

<details><summary>정답</summary>

**A.** Copilot은 반복 작업·코드 이해·작성·문서화 등 다양한 개발 Workflow를 보조할 수 있습니다.
</details>

## Q062

익숙하지 않은 Programming Language를 Copilot으로 학습할 때 가장 적절한 행동은?

A. AI 설명을 최신 공식 문서와 교차 확인한다.  
B. AI 답변을 언어 사양으로 간주한다.  
C. 실행하지 않는다.  
D. Compiler Error를 무시한다.

<details><summary>정답</summary>

**A.** 학습 가속에는 유용하지만 최신성과 정확성은 공식 자료·실행으로 확인해야 합니다.
</details>

## Q063

Refactoring Prompt에서 가장 중요한 Verification은?

A. 기존 Behavior와 Test가 유지되는지 확인  
B. 코드 줄 수가 반드시 절반인지 확인  
C. AI가 `완료`라고 말했는지 확인  
D. Commit 수가 증가했는지 확인

<details><summary>정답</summary>

**A.** Refactoring은 외부 동작을 보존하면서 구조를 개선하는 것이므로 기존 Test와 요구사항 검증이 중요합니다.
</details>

## Q064

Copilot으로 README 초안을 만들었다. 가장 적절한 다음 행동은?

A. 실제 CLI, 설정, API와 문서 내용이 일치하는지 검증한다.  
B. 자동 Publish한다.  
C. Code Review를 생략한다.  
D. 오래된 버전 정보를 그대로 둔다.

<details><summary>정답</summary>

**A.** Documentation도 Hallucination과 최신성 문제를 가질 수 있습니다.
</details>

## Q065

Legacy Application을 현대화할 때 Copilot의 역할로 가장 적절한 것은?

A. 변경 후보·새 API·Refactor 아이디어를 제안하고 사람이 호환성·Test를 검증한다.  
B. 모든 Legacy Code를 삭제한다.  
C. Migration Test를 생략한다.  
D. Dependency Version을 무조건 최신으로 올린다.

<details><summary>정답</summary>

**A.** Modernization은 호환성·Deprecation·Behavior 검증이 필수입니다.
</details>

## Q066

Copilot을 Context Switching 감소에 활용하는 예로 가장 적절한 것은?

A. 현재 코드 주변에서 설명·문서·관련 구현 아이디어를 얻는다.  
B. 모든 개발 도구를 제거한다.  
C. Repository를 한 파일로 합친다.  
D. Test Framework를 삭제한다.

<details><summary>정답</summary>

**A.** IDE/Repository Context 안에서 필요한 도움을 받아 외부 검색 전환을 줄일 수 있습니다.
</details>

## Q067

Sample Data를 AI로 생성할 때 가장 중요한 주의점은?

A. 실제 고객 PII를 그대로 복제하지 않고 요구사항에 맞는 합성 데이터인지 확인한다.  
B. Production DB를 Prompt에 넣는다.  
C. Sample은 Test할 필요가 없다.  
D. AI가 만든 값은 항상 통계적으로 완벽하다.

<details><summary>정답</summary>

**A.** Privacy와 데이터 품질을 모두 검토해야 합니다.
</details>

## Q068

Debugging에서 Copilot을 가장 잘 사용하는 방식은?

A. Error Message·관련 코드·재현 조건을 제공하고 가설을 받은 뒤 실제로 검증한다.  
B. `고쳐`라고만 하고 결과를 바로 Deploy한다.  
C. Stack Trace를 무시한다.  
D. Test를 삭제한다.

<details><summary>정답</summary>

**A.** Debugging은 관련 Context와 재현·검증 과정이 중요합니다.
</details>

## Q069

Copilot이 성능 최적화 코드를 제안했다. 가장 적절한 검증은?

A. Benchmark + Correctness Test  
B. 코드가 더 복잡하면 빠르다고 가정  
C. AI 설명만 확인  
D. 변수 이름만 비교

<details><summary>정답</summary>

**A.** 성능 개선은 측정하고, 최적화 과정에서 정확성이 깨지지 않았는지 확인해야 합니다.
</details>

## Q070

AI를 SDLC 전체에서 사용할 때 가장 적절한 원칙은?

A. 각 단계에서 AI를 보조 도구로 사용하고 인간의 책임과 자동화된 검증을 유지한다.  
B. AI가 있으면 Requirement와 Test가 필요 없다.  
C. Human Review를 제거한다.  
D. Security Tool을 모두 대체한다.

<details><summary>정답</summary>

**A.** Copilot은 SDLC 생산성을 높일 수 있지만 기존 Engineering Control과 책임을 대체하지 않습니다.
</details>

---
[← 060 Prompt & Context](../060-prompt-context/README.md) · [080 Testing / Security / Performance →](../080-testing-security-performance/README.md)
