# 080 Security — Q071–Q080

## Q071
Workflow의 `GITHUB_TOKEN` 권한은 어떻게 설계하는 것이 가장 바람직한가?

A. 필요한 최소 권한만 부여  B. 항상 `write-all`  C. Token 사용 금지  D. 모든 Job에 Admin 권한

<details><summary>정답</summary>**A** — 최소 권한 원칙을 적용합니다.</details>

## Q072
Cloud Provider에 장기 Access Key를 저장하지 않고 단기 자격증명을 얻는 방식과 가장 관련 있는 것은?

A. OIDC  B. Cache  C. Artifact  D. Matrix

<details><summary>정답</summary>**A. OIDC**</details>

## Q073
OIDC의 주요 보안 장점은?

A. 장기 Cloud Secret 의존을 줄일 수 있다.  B. Runner가 필요 없다.  C. Workflow를 암호화한다.  D. 모든 권한을 자동 부여한다.

<details><summary>정답</summary>**A**</details>

## Q074
Third-party Action을 Full Commit SHA로 고정하는 가장 직접적인 목적은?

A. 참조 대상 코드의 예기치 않은 변경 위험 감소  B. Job 개수 증가  C. Secret 암호화  D. Runner 생성

<details><summary>정답</summary>**A**</details>

## Q075
Fork에서 온 PR Workflow에 민감 Secret을 무조건 제공하면 위험한 이유는?

A. 외부 기여자가 수정한 코드가 Secret을 탈취할 수 있기 때문  B. Artifact 생성이 불가능해서  C. Matrix가 느려져서  D. Git이 손상돼서

<details><summary>정답</summary>**A**</details>

## Q076
Secret을 디버깅하기 위해 Log에 직접 출력하는 방법은?

A. 피해야 한다.  B. 권장된다.  C. OIDC 필수 단계다.  D. Artifact 업로드 전에 반드시 필요하다.

<details><summary>정답</summary>**A**</details>

## Q077
`permissions`를 Workflow 전체보다 Job 수준에서 더 좁게 지정하는 장점은?

A. Job별 필요한 권한만 부여 가능  B. Runner 수 증가  C. Artifact 자동 삭제  D. Secret 공개

<details><summary>정답</summary>**A**</details>

## Q078
Self-hosted Runner 보안에서 특히 중요한 것은?

A. 신뢰할 수 없는 Workflow와 내부 자원의 경계를 관리  B. README 색상  C. Issue Milestone  D. Star 수

<details><summary>정답</summary>**A**</details>

## Q079
Artifact에 민감 파일이 포함되는 것을 방지하는 가장 좋은 방법은?

A. Upload Path와 생성 파일을 명시적으로 검토  B. Artifact 이름만 변경  C. Matrix 제거  D. Runner Group 삭제

<details><summary>정답</summary>**A**</details>

## Q080
GitHub Actions 공급망 보안의 일부로 보기 어려운 것은?

A. Action Pinning  B. 최소 Token 권한  C. Trusted Runner  D. Repository Star 수

<details><summary>정답</summary>**D**</details>

---
관련 Lab: [`090-security-oidc`](../../060-labs/090-security-oidc/README.md)
