# 090 개인정보 보호 와 Safeguards — Q081–Q090 (090 Privacy & Safeguards — Q081–Q090, PSQ081Q090)

> Skill Area: **Configure privacy, content exclusions, and safeguards**

## Q081

Content Exclusion의 목적을 가장 정확하게 설명한 것은?

A. 특정 콘텐츠가 Copilot Context로 사용되지 않도록 구성하는 것  
B. 원본 파일을 Repository에서 삭제하는 것  
C. 모든 Secret을 자동 회전하는 것  
D. Branch를 Merge하는 것

<details><summary>정답</summary>

**A.** Content Exclusion은 Context 사용 제어 기능이며 파일 삭제나 Secret Management 자체가 아닙니다.
</details>

## Q082

Content Exclusion을 설정했으므로 실제 Secret을 코드에 저장해도 안전하다는 주장은?

A. 맞다.  
B. 틀리다. Secret Management와 Exclusion은 별개의 보호 계층이다.  
C. Public Repository에서만 맞다.  
D. CLI에서만 맞다.

<details><summary>정답</summary>

**B.** Exclusion은 Secret 저장·회전·권한 관리 기능을 대체하지 않습니다.
</details>

## Q083

특정 파일이 제외되어야 하는데 Copilot이 관련 내용을 사용하는 것처럼 보인다. FIRST로 할 일은?

A. 적용 범위·경로·정책·Editor 지원과 설정 상태를 확인한다.  
B. Repository를 삭제한다.  
C. 모든 Policy를 비활성화한다.  
D. Production Token을 Prompt에 넣는다.

<details><summary>정답</summary>

**A.** Exclusion Troubleshooting은 설정 범위와 적용 상태부터 단계적으로 확인합니다.
</details>

## Q084

Suggestions matching public code filtering의 목적과 가장 가까운 것은?

A. 공개 코드와 일치하는 제안을 다루는 보호 설정  
B. Git Commit을 자동 삭제  
C. Subscription 비용 계산  
D. Unit Test 생성

<details><summary>정답</summary>

**A.** 공개 코드 일치 제안을 관리하는 Safeguard입니다.
</details>

## Q085

Public Code Matching Filter를 켰으므로 라이선스·법적 검토가 항상 필요 없다는 설명은?

A. 맞다.  
B. 틀리다. Filter는 보호 계층 중 하나이며 조직의 정책·법적 검토를 대체하지 않는다.  
C. Enterprise에서만 맞다.  
D. CLI에서만 맞다.

<details><summary>정답</summary>

**B.** 기술적 Filter와 법적·정책적 책임은 동일하지 않습니다.
</details>

## Q086

Copilot Output Ownership을 다룰 때 가장 적절한 접근은?

A. 현재 GitHub 약관과 조직 정책·법무 기준을 확인한다.  
B. 모든 Output은 자동으로 Public Domain이라고 가정한다.  
C. AI가 생성했으므로 누구도 책임지지 않는다.  
D. README만 확인한다.

<details><summary>정답</summary>

**A.** Output 사용·소유 관련 사항은 최신 약관과 조직 정책을 기준으로 확인해야 합니다.
</details>

## Q087

Copilot Suggestion이 특정 파일에서 보이지 않는다. 가장 적절한 Troubleshooting 순서는?

A. Sign-in/활성화 → 파일/언어 → Policy/Exclusion → 환경/서비스/로그  
B. OS 삭제 → Repository 삭제 → Token 공개  
C. Test 삭제 → Merge → Deploy  
D. Audit Log만 확인하고 종료

<details><summary>정답</summary>

**A.** 기본 환경부터 정책·Exclusion과 서비스 상태까지 점진적으로 확인합니다.
</details>

## Q088

Privacy와 Security를 가장 잘 구분한 것은?

A. Privacy는 데이터 처리·보호, Security는 시스템·코드·접근 위험 방어에 초점을 둔다.  
B. 둘은 항상 완전히 같은 용어다.  
C. Privacy는 Git Branch 이름이다.  
D. Security는 Prompt Style이다.

<details><summary>정답</summary>

**A.** 서로 연관되지만 보호 대상과 관점이 다릅니다.
</details>

## Q089

조직 Copilot Policy를 구성하는 이유로 가장 적절한 것은?

A. 기능 사용 범위를 Security·Compliance·Data Governance 요구에 맞게 관리  
B. 모든 사람에게 최대 권한 부여  
C. Human Review 제거  
D. 모든 Repository를 Public으로 변경

<details><summary>정답</summary>

**A.** 조직 Policy는 기능 가용성과 위험을 중앙 관리하는 수단입니다.
</details>

## Q090

Defense in Depth 관점에서 가장 적절한 조합은?

A. Policy + Exclusion + Public Code Filter + Human Review + Test/Security Check  
B. AI Output 단독  
C. Chat History만 저장  
D. Test를 제거하고 Agent 권한 확대

<details><summary>정답</summary>

**A.** 하나의 보호장치가 모든 위험을 해결하지 않으므로 여러 계층을 결합합니다.
</details>

---
[← 080 Testing / Security / Performance](../080-testing-security-performance/README.md) · [100 Mixed Exam Gate →](../100-mixed-gate/README.md)
