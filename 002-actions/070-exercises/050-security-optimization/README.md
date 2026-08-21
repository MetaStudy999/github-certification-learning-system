# 050 보안 와 최적화 (Security & Optimization, SO) — 연습문제 (Exercises, EXR)

## 목표

Actions 보안을 최소 권한, 자격증명 수명, 공급망 신뢰, 실행 효율 관점에서 판단합니다.

### E041
Workflow가 Repository 내용을 읽기만 할 때 `GITHUB_TOKEN`에 Write 권한을 주지 않아야 하는 이유를 설명하세요.

### E042
Cloud 배포에서 장기 Access Key 대신 OIDC를 사용할 때 얻는 보안 이점을 설명하세요.

### E043
Secret을 `echo`로 출력하는 디버깅 방식이 위험한 이유와 안전한 대안을 설명하세요.

### E044
Third-party Action을 Full Commit SHA로 Pinning하는 이유를 공급망 보안과 연결하세요.

### E045
PR from Fork에서 Secret 노출을 특히 주의해야 하는 이유를 설명하세요.

### E046
Cache Poisoning 위험을 줄이기 위해 Cache Key와 사용 범위를 어떻게 설계할지 설명하세요.

### E047
Artifact에 Secret이나 불필요한 민감 파일이 포함되지 않도록 검증하는 절차를 제안하세요.

### E048
Dependency 설치 시간을 줄이는 데 Cache가 적합하고 Build 결과 전달에는 Artifact가 적합한 이유를 설명하세요.

### E049
중복 실행을 줄이기 위해 `concurrency`와 Job 조건을 적용할 수 있는 상황을 설명하세요.

### E050
Workflow 보안 검토 시 `permissions`, Secrets, OIDC, Action Pinning, Runner Trust를 어떤 순서로 확인할지 자신의 Checklist를 작성하세요.

## 완료 기준

보안을 단순 Secret 관리가 아니라 **Token 권한 + 공급망 + Runner + Cloud 인증 + Artifact/Cache** 전체로 설명합니다.

관련 Lab: [`050-cache-artifacts`](../../060-labs/050-cache-artifacts/README.md), [`090-security-oidc`](../../060-labs/090-security-oidc/README.md)
