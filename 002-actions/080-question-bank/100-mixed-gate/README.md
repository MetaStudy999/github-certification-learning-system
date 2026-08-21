# 100 혼합 통과 기준 — Q091–Q100 (Mixed Gate — Q091–Q100, MGQ091Q100)

## Q091
여러 Repository에서 같은 CI Job 구조를 공유하면서 중앙에서 업데이트하고 싶다. 가장 적절한 것은?

A. Reusable Workflow  B. Artifact  C. Cache  D. Runner Label

<details><summary>정답</summary>**A. Reusable Workflow**</details>

## Q092
Workflow는 실행되지만 Cloud 배포 단계에서 권한 오류가 난다. 가장 먼저 점검할 조합은?

A. `permissions`와 OIDC/Cloud Trust 설정  B. Issue와 Milestone  C. README와 LICENSE  D. Matrix와 Artifact 이름

<details><summary>정답</summary>**A**</details>

## Q093
Python 3.11/3.12 × Ubuntu/Windows Test를 수행하면서 의존성 다운로드 시간을 줄이고 싶다. 적절한 조합은?

A. Matrix + Cache  B. Artifact + Discussion  C. Secret + Label  D. OIDC + Wiki

<details><summary>정답</summary>**A**</details>

## Q094
Build 결과를 Deploy Job으로 전달해야 한다. 가장 적절한 기능은?

A. Artifact  B. Cache만 사용  C. Issue  D. Runner Group

<details><summary>정답</summary>**A**</details>

## Q095
내부망 서버에 배포해야 하고 GitHub-hosted Runner에서 접근할 수 없다. 다음으로 가장 적절한 검토 대상은?

A. 안전하게 관리되는 Self-hosted Runner  B. README 변경  C. Star 증가  D. Discussion 생성

<details><summary>정답</summary>**A**</details>

## Q096
외부 Action의 Tag가 가리키는 코드가 변경될 가능성을 최소화하려면?

A. Full Commit SHA Pinning  B. `latest` 사용  C. Branch Name만 사용  D. Secret으로 Version 저장

<details><summary>정답</summary>**A**</details>

## Q097
PR에서는 Test만, `main` Push에서는 Deploy까지 수행하고 싶다. 가장 적절한 설계는?

A. Event/Branch 조건과 Job `if`를 목적에 맞게 사용  B. Workflow 두 개를 무조건 삭제  C. 모든 Event에서 Deploy  D. Secret을 제거

<details><summary>정답</summary>**A**</details>

## Q098
여러 Workflow에서 반복되는 Setup Step 5개만 재사용하려 한다. 가장 적절한 것은?

A. Composite Action  B. Enterprise Account  C. Runner Group  D. Environment

<details><summary>정답</summary>**A**</details>

## Q099
Self-hosted Runner를 도입했지만 보안 위험을 줄이려 한다. 가장 적절한 조합은?

A. 접근 제한 + 격리 + 패치 + 신뢰할 수 있는 Workflow만 실행  B. 모든 Public Fork 허용  C. Admin Token 상시 저장  D. Log 비활성화

<details><summary>정답</summary>**A**</details>

## Q100
GH-200 시험 준비에서 가장 좋은 최종 학습 방식은?

A. 공식 Domain → Lab → Scenario 문제 → 오답 → Mock 반복  B. YAML 키워드만 암기  C. Brain Dump만 반복  D. 실습 없이 정의만 암기

<details><summary>정답</summary>**A**</details>

## 100-질문 Gate (100-Question Gate, QG)

- [ ] 1회차 80/100 이상
- [ ] 2회차 85/100 이상
- [ ] 오답 재시험 90% 이상
- [ ] 약점 Domain 관련 Lab 재수행

---
[Question Bank 홈](../README.md) · [다음: 090 Final Review →](../../090-final-review/README.md)
