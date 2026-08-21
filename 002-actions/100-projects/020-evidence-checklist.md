# 020 Evidence 점검표 — CI/CD 자동화 프로젝트 (020 Evidence Checklist — CI/CD Automation Project, ECCICDAP)

## 저장소 Evidence (Repository Evidence, RE)

- [ ] Project Repository URL
- [ ] `.github/workflows/` 구조
- [ ] README의 Workflow 설명

## 워크플로 Evidence (Workflow Evidence, WE)

- [ ] Push 실행 성공 URL
- [ ] Pull Request 실행 성공 URL
- [ ] Matrix 실행 화면 또는 Run URL
- [ ] Artifact 생성 확인
- [ ] Cache Hit/Miss 관찰 기록

## 재사용 Evidence (Reuse Evidence, RE)

- [ ] Reusable Workflow 또는 Composite Action 사용 위치
- [ ] 선택 이유
- [ ] Input/Output 또는 Secret 전달 방식 설명

## 보안 Evidence (Security Evidence, SE)

- [ ] `permissions` 설정 확인
- [ ] Secret 평문 저장 없음
- [ ] 외부 Action Version/Pinning 정책 기록
- [ ] OIDC 구조 설명 또는 설계도
- [ ] Self-hosted Runner 사용 시 접근 범위 설명

## 문제 해결 Evidence (Troubleshooting Evidence, TE)

```text
Failure scenario:
Run URL:
Failed job/step:
Root cause:
Fix:
Successful run URL:
What I learned:
```

## Final Evidence

- [ ] Project Rubric 80점 이상
- [ ] 핵심 Workflow Run 성공
- [ ] 실패 → 수정 과정 기록
- [ ] 보안 Checklist 완료
- [ ] 5분 이내로 아키텍처 설명 가능
