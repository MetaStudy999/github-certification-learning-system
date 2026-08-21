# 050 보안 정책 — Q041–Q050 (050 Security Policies — Q041–Q050, SPQ041Q050)

## Q041
기본 브랜치 직접 Push를 제한하고 PR Review를 강제하려면 가장 적절한 제어는?

A. Ruleset / Branch Protection  B. Issue Label  C. Wiki  D. Star

**정답: A** — Merge 조건과 Push 제한을 정책으로 강제할 수 있습니다.

## Q042
여러 Repository에 동일한 보호정책을 일관되게 적용하려면?

A. 개별 수동 설정만 사용  B. 상위 Scope Ruleset 활용  C. README에만 기록  D. 개인 Git Config

**정답: B** — 중앙 정책으로 편차를 줄입니다.

## Q043
보안 정책의 예외를 허용할 때 가장 중요한 것은?

A. 예외 사유·기간·승인·감사 기록  B. 영구 예외  C. 익명 승인  D. Audit 비활성화

**정답: A** — Exception도 Governance 대상입니다.

## Q044
Secret이 Commit되기 전에 차단하는 데 가장 직접적인 기능은?

A. Push Protection  B. Projects  C. Discussions  D. Codespaces

**정답: A** — Push 단계에서 Secret 노출을 방지합니다.

## Q045
코드 취약점을 정적 분석하는 대표 기능은?

A. Code Scanning  B. Milestone  C. Pages  D. Discussions

**정답: A** — CodeQL 등을 통한 정적 분석 결과를 관리합니다.

## Q046
Dependency 취약성 관리와 가장 관련이 깊은 기능은?

A. Dependabot / Dependency Graph  B. Wiki  C. Profile README  D. Sponsors

**정답: A** — 공급망 의존성 위험을 식별·업데이트합니다.

## Q047
Organization 전체 보안 기능 활성화 전 가장 먼저 고려할 것은?

A. 대상 Scope·License·정책 영향  B. Emoji  C. Star 수  D. Branch 이름

**정답: A** — 비용과 운영 영향을 함께 봐야 합니다.

## Q048
Ruleset 변경 후 Workflow가 실패하기 시작했다. FIRST로 할 일은?

A. 정책 변경 시점과 실패 로그 비교  B. 모든 보호 해제  C. Public 전환  D. Audit 삭제

**정답: A** — Change와 증상을 연결해 원인을 좁힙니다.

## Q049
보안정책을 강제하면서 개발 생산성 저하를 줄이는 방법은?

A. 표준·자동화·명확한 예외 절차 제공  B. 모든 제어 제거  C. Owner 확대  D. Secret 공유

**정답: A** — 안전성과 운영성을 같이 설계합니다.

## Q050
Compliance Evidence로 가장 적절한 것은?

A. Policy 정의 + Audit Log + 검증 결과  B. Token 원문  C. Password 목록  D. 개인 메모만

**정답: A** — 정책과 실제 적용·변경 기록을 연결합니다.

---
[← Q031–Q040](../040-support-licensing-standards/README.md) · [다음 Q051–Q060 →](../060-security-features-integrations/README.md)
