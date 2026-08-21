# 100 Projects — GitHub 액션 (GitHub Actions, GHACT / GH-200) 통합 프로젝트

## 프로젝트 001 — CI/CD 자동화 프로젝트 (Project 001 — CI/CD Automation Project, PCICDAP)

### 목표

Python 애플리케이션을 대상으로 다음 흐름을 구축합니다.

```text
Push / Pull Request
      ↓
CI Workflow
      ↓
Lint / Test
      ↓
Matrix
      ↓
Artifact
      ↓
Security controls
      ↓
Optional deployment gate
```

## 단계 (Phase, PH) 1 — CI

- [ ] `push` / `pull_request` Trigger
- [ ] Checkout
- [ ] Python Setup
- [ ] Dependency Install
- [ ] Test

## 단계 (Phase, PH) 2 — 매트릭스 / 아티팩트 (Matrix / Artifact, MA)

- [ ] Python 버전 Matrix
- [ ] 필요 시 OS Matrix
- [ ] Test 결과 Artifact 저장

## 단계 (Phase, PH) 3 — 재사용 (Reuse, R)

- [ ] 공통 Step 또는 Workflow 재사용
- [ ] Reusable Workflow와 Composite Action 중 선택 이유 기록

## 단계 (Phase, PH) 4 — 보안 (Security, S)

- [ ] 최소 `permissions`
- [ ] Secret을 Log에 출력하지 않음
- [ ] 외부 Action 버전 정책 확인
- [ ] OIDC 배포 구조를 설명

## 단계 (Phase, PH) 5 — 문제 해결 (Troubleshooting, T)

- [ ] 의도적 실패 1회 생성
- [ ] Log에서 원인 확인
- [ ] 수정 후 성공 Evidence 저장

## 평가 기준

| 영역 | 배점 |
|---|---:|
| Workflow 구조 | 20 |
| Test / Matrix | 20 |
| Artifact / Reuse | 20 |
| Security | 20 |
| Troubleshooting / 설명 | 20 |

**80점 이상:** PASS  
**90점 이상 + Evidence:** CLEAR 후보
