# 010 책임 있는 AI — Q001–Q010 (010 Responsible AI — Q001–Q010, RAIQ001Q010)

> Skill Area: **Use GitHub Copilot responsibly**

## Q001

Copilot이 생성한 코드가 문법적으로 올바르고 읽기 쉽다. Production 반영 전에 가장 적절한 행동은?

A. AI가 생성했으므로 바로 Merge한다.  
B. 사람이 요구사항·보안·Test 결과를 검토한다.  
C. 코드 길이만 확인한다.  
D. 다른 AI에게 한 번 더 물어본 뒤 자동 Merge한다.

<details><summary>정답</summary>

**B.** AI Output은 제안이며 정확성·보안·요구사항 충족 여부를 사람이 검증해야 합니다.
</details>

## Q002

Copilot이 실제로 존재하지 않는 Library API를 제안했다. 가장 관련 있는 개념은?

A. Content Exclusion  
B. Hallucination  
C. Audit Log  
D. Sub-Agent

<details><summary>정답</summary>

**B.** 그럴듯하지만 사실이 아닌 Output은 Hallucination의 대표 사례입니다.
</details>

## Q003

AI가 생성한 사용자 평가 로직이 특정 집단에 불리한 결과를 지속적으로 낸다. 가장 먼저 검토할 위험은?

A. Bias / Fairness  
B. Cache Miss  
C. Git Branch  
D. CLI Session

<details><summary>정답</summary>

**A.** 데이터와 패턴의 편향이 불공정한 결과로 이어질 수 있습니다.
</details>

## Q004

보안상 민감한 Production Token을 Prompt에 넣어 오류를 분석하려 한다. 가장 적절한 조치는?

A. Token 전체를 넣되 Chat History를 지운다.  
B. Token을 마스킹하고 민감정보 없이 재현 가능한 예제를 만든다.  
C. Token을 Base64로 변환해 넣는다.  
D. Token이 짧으면 그대로 넣는다.

<details><summary>정답</summary>

**B.** 민감정보를 최소화하고 재현 가능한 비민감 예제를 사용하는 것이 적절합니다. Encoding은 비밀 보호가 아닙니다.
</details>

## Q005

Copilot이 제안한 코드가 Test를 모두 통과했다. 그래도 추가 Human Review가 필요한 가장 좋은 이유는?

A. Test가 모든 요구사항·보안·정책을 완전히 보장하지 않기 때문이다.  
B. AI 코드는 항상 틀리기 때문이다.  
C. Test는 AI 코드에서 실행되지 않기 때문이다.  
D. Human Review는 코드 길이를 줄이기 위해서만 필요하다.

<details><summary>정답</summary>

**A.** Test Coverage 자체가 불완전할 수 있고 보안·정책·비즈니스 요구사항은 별도 검토가 필요합니다.
</details>

## Q006

Responsible AI 관점에서 가장 부적절한 태도는?

A. Output을 검증한다.  
B. 잠재적 Bias를 검토한다.  
C. AI가 추천했으므로 결과 책임도 AI에게 있다고 본다.  
D. Privacy 영향을 확인한다.

<details><summary>정답</summary>

**C.** AI 사용 결과에 대한 최종 판단과 책임은 인간과 조직의 거버넌스에 남습니다.
</details>

## Q007

Copilot이 오래된 Framework 사용법을 제안할 가능성에 대응하는 가장 적절한 방법은?

A. AI 설명만 신뢰한다.  
B. 최신 공식 문서와 버전을 교차 확인한다.  
C. 코드가 길면 최신이라고 판단한다.  
D. Prompt를 영어로 바꾸면 자동 해결된다.

<details><summary>정답</summary>

**B.** 모델과 서비스는 최신성을 완전히 보장하지 않으므로 공식 문서 검증이 필요합니다.
</details>

## Q008

다음 중 AI Output의 잠재적 Harm을 줄이는 방법으로 가장 적절한 것은?

A. 검토 없이 자동 배포  
B. Human Review, Test, Security Check를 결합  
C. 모든 Prompt를 매우 짧게 작성  
D. Output을 항상 첫 번째 제안으로 고정

<details><summary>정답</summary>

**B.** 여러 검증 계층을 결합하는 것이 위험 완화에 효과적입니다.
</details>

## Q009

Copilot에게 생성 결과의 이유를 설명하게 하는 것의 장점과 한계를 가장 정확하게 설명한 것은?

A. 설명이 있으면 실행 검증은 필요 없다.  
B. 설명은 Review에 도움되지만 사실 여부와 코드 정확성은 별도로 검증해야 한다.  
C. 설명은 Privacy를 자동 보장한다.  
D. 설명은 모든 Bias를 제거한다.

<details><summary>정답</summary>

**B.** Explanation은 이해를 돕지만 Verification을 대체하지 않습니다.
</details>

## Q010

Copilot 제안을 `Reject`하는 것이 가장 적절한 상황은?

A. 요구사항을 위반하고 보안 취약점을 만든다.  
B. 변수 이름이 본인 취향과 조금 다르다.  
C. 주석이 한 줄 부족하다.  
D. 코드가 두 줄 더 길다.

<details><summary>정답</summary>

**A.** 요구사항 또는 보안을 심각하게 위반하는 제안은 거절하고 안전한 대안을 선택해야 합니다.
</details>

## Score

- 9–10: 다음 Set 진행
- 8: 오답 확인 후 진행
- 7 이하: Responsible AI Exercise와 Lab 090 재학습

---
[← Question Bank](../README.md) · [020 IDE & CLI →](../020-ide-cli-features/README.md)
