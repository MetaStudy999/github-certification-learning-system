# 090 Final Review — GH-200 시험 직전 복습

## 빠른 시작 (Quick Start, QS)

시험 직전에는 새로운 기능을 크게 추가하지 않고 **비교 → 보안 → Troubleshooting → 최근 오답** 순서로 압축합니다.

## Final Review Files

| 코드 | 문서 | 목적 |
|---:|---|---|
| 010 | [Final Checklist](./010-final-checklist.md) | Domain별 마지막 확인 |
| 020 | [Confusion Matrix](./020-confusion-matrix.md) | 유사 개념 비교 |
| 030 | [Exam-Day Strategy](./030-exam-day-strategy.md) | 시간·문제 풀이 전략 |

## 핵심 비교

| A | B | 핵심 차이 |
|---|---|---|
| Workflow | Action | 전체 자동화 흐름 vs 재사용 기능 단위 |
| Job | Step | Runner 단위 작업 vs Job 내부 단계 |
| Cache | Artifact | 다음 실행 가속 vs 결과 저장·전달 |
| Reusable Workflow | Composite Action | Job/Workflow 재사용 vs Step 묶음 |
| GitHub-hosted | Self-hosted Runner | GitHub 관리 vs 직접 관리 |
| Variable | Secret | 일반 설정값 vs 민감정보 |
| `GITHUB_TOKEN` | PAT | 실행에 자동 제공되는 Token vs 별도 사용자 Token |
| OIDC | Long-lived Secret | 단기 연합 자격증명 vs 장기 키 |
| `workflow_dispatch` | `workflow_call` | 수동 실행 vs Workflow 재사용 호출 |
| Service Container | Container Job | 보조 서비스 vs Job 자체 실행환경 |

## 최종 Gate

- [ ] 5개 Domain과 비중 확인
- [ ] Event → Workflow → Job → Runner → Step 설명
- [ ] Context와 Expression 설명
- [ ] Matrix / Cache / Artifact 설명
- [ ] Reuse 두 방식 구분
- [ ] Custom Action 3종 구분
- [ ] Runner 두 방식과 Enterprise Governance 설명
- [ ] 최소 권한 / OIDC / Pinning 설명
- [ ] Troubleshooting 순서 설명
- [ ] 최근 Mock 2회 85% 이상
- [ ] 오답 재시험 90% 이상

---

[← 080 Question Bank](../080-question-bank/README.md) · [다음: 100 Projects →](../100-projects/README.md)
