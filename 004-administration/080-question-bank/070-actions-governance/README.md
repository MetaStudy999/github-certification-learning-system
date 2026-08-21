# 070 Actions Governance — Q061–Q070

## Q061
Enterprise에서 허용 가능한 Actions Source를 제한하는 목적은?

A. Supply-chain 위험 감소  B. README 단축  C. Issue 증가  D. Star 감소

**정답: A** — 신뢰할 수 없는 외부 Action 실행 위험을 줄입니다.

## Q062
외부 Action을 태그 대신 Full Commit SHA로 고정하는 주된 이유는?

A. 변경 불가능한 특정 버전에 고정  B. 실행 속도만 향상  C. Secret 제거  D. Runner 삭제

**정답: A** — 참조 변조·예기치 않은 변경 위험을 줄입니다.

## Q063
`GITHUB_TOKEN` 권한 설정의 권장 원칙은?

A. write-all 기본  B. 필요한 Permission만 명시  C. Admin 부여  D. Token 로그 출력

**정답: B** — Workflow 최소 권한을 적용합니다.

## Q064
Enterprise 전체 Actions 정책과 Organization 정책이 다를 때 먼저 확인할 것은?

A. 상위 Enterprise 제한  B. README  C. Commit author  D. Issue Label

**정답: A** — 하위 Scope는 상위 정책보다 완화할 수 없는 경우가 있습니다.

## Q065
Workflow에서 Production 배포 전에 승인 절차가 필요하다. 가장 관련 깊은 기능은?

A. Environment protection rules  B. Wiki  C. Discussions  D. Sponsors

**정답: A** — Environment 기반 승인·보호 규칙을 사용할 수 있습니다.

## Q066
조직 공통 Workflow 사용을 표준화할 때 관리자가 고려할 것은?

A. Reusable Workflow와 중앙 관리 Repository  B. 개인 Gist만  C. 모든 Repo별 복사  D. Public Token

**정답: A** — 재사용성과 정책 일관성을 높입니다.

## Q067
Actions 사용량 급증을 조사할 때 먼저 볼 지표는?

A. Workflow Run 빈도와 Runner 사용량  B. Star 수  C. README 길이  D. Fork 이름

**정답: A** — 실행량이 비용·Capacity의 직접 신호입니다.

## Q068
관리자가 Workflow 실패를 줄이기 위해 제공할 수 있는 것은?

A. 표준 Template·재사용 Workflow·문서화  B. 권한 전면 확대  C. 모든 Check 제거  D. Secret 공개

**정답: A** — 표준화가 오류와 편차를 줄입니다.

## Q069
Actions 정책 변경 후 일부 Repository만 실패한다. FIRST로 할 일은?

A. 실패 Repo의 Workflow 요구와 새 정책 차이 비교  B. 정책 전체 제거  C. Audit 삭제  D. 모든 Owner 추가

**정답: A** — 영향 Scope를 좁혀 원인을 찾습니다.

## Q070
Actions Governance Evidence로 가장 적절한 것은?

A. Policy 정의·변경 기록·검증 Run  B. Secret 원문  C. 개인 Password  D. Runner SSH Key

**정답: A** — 정책과 실제 동작을 연결해 증명합니다.

---
[← Q051–Q060](../060-security-features-integrations/README.md) · [다음 Q071–Q080 →](../080-runners-network-credentials/README.md)
