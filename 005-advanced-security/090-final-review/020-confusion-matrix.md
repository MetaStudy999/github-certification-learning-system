# GH-500 Confusion 매트릭스 (GH-500 Confusion Matrix, GH-500CM)

| A | B | 핵심 차이 |
|---|---|---|
| Secret Protection | Code Security | 자격증명 노출 vs 코드 취약점 |
| Push Protection | Secret Alert | 사전 차단 vs 사후 탐지·대응 |
| Validity Check | Custom Pattern | 유효성 판단 보조 vs 조직 고유 패턴 탐지 |
| Dependency Graph | SBOM | GitHub 의존성 관계 vs 표준화된 구성요소 명세 |
| Dependabot Alert | Dependency Review | 알려진 취약 의존성 경고 vs PR 변경 검토 |
| Direct Dependency | Transitive Dependency | 직접 선언 vs 간접 포함 |
| CodeQL | SARIF | 분석 엔진/쿼리 vs 결과 교환 형식 |
| Default Setup | Advanced Setup | 빠른 표준 구성 vs 세밀한 분석 제어 |
| Security Overview | Security Campaign | 상태 가시성 vs 목표형 위험 감소 활동 |
| Dismissal | Remediation | 근거 기반 상태 처리 vs 실제 위험 수정 |
| Prevention-first | Gate-based | 위험 유입 전 예방 vs 특정 단계 통과 통제 |
| Repository Setting | Organization/Enterprise Policy | 개별 저장소 범위 vs 다수 저장소 표준화 |

시험 전 각 행을 **예시 Scenario 하나씩** 만들어 설명합니다.
