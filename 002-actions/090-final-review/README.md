# 090 Final Review — GH-200 시험 직전 복습

## 핵심 비교

| A | B | 핵심 차이 |
|---|---|---|
| Workflow | Action | 전체 자동화 흐름 vs 재사용 기능 단위 |
| Job | Step | Runner 단위 작업 vs Job 내부 단계 |
| Cache | Artifact | 다음 실행 가속 vs 결과 저장·전달 |
| Reusable Workflow | Composite Action | Job/Workflow 재사용 vs Step 묶음 |
| GitHub-hosted | Self-hosted Runner | GitHub 관리 vs 직접 관리 |
| Variable | Secret | 일반 설정값 vs 민감정보 |
| `GITHUB_TOKEN` | PAT | 실행에 자동 제공 vs 별도 사용자 토큰 |
| OIDC | Long-lived secret | 단기 연합 자격증명 vs 장기 키 |

## 시험 직전 확인

- [ ] 5개 Domain과 비중 확인
- [ ] Event → Workflow → Job → Runner → Step 설명
- [ ] Context와 Expression 설명
- [ ] Matrix / Cache / Artifact 설명
- [ ] Reuse 두 방식 구분
- [ ] Runner 두 방식 구분
- [ ] 최소 권한 / OIDC / Pinning 설명
- [ ] Troubleshooting 순서 설명
- [ ] 최근 Mock 2회 85% 이상
- [ ] 오답 재시험 90% 이상
