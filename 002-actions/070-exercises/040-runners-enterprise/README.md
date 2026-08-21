# 040 러너와 엔터프라이즈 (Runners & Enterprise, RE) — 연습문제 (Exercises, EXR)

## 목표

GitHub-hosted Runner와 Self-hosted Runner를 운영·보안 관점에서 구분합니다.

### E031
일반적인 공개 인터넷 Build에 GitHub-hosted Runner가 적합한 이유를 설명하세요.

### E032
사내망 Database에 접근해야 하는 Job에서 Self-hosted Runner를 고려하는 이유를 설명하세요.

### E033
Self-hosted Runner 사용 시 GitHub가 대신 책임지지 않는 운영 항목을 세 가지 적으세요.

### E034
Runner Label을 사용해 GPU Runner와 일반 Runner를 구분하는 방식을 설명하세요.

### E035
Runner Group이 Enterprise/Organization 수준에서 어떤 문제를 해결하는지 설명하세요.

### E036
Repository별로 Self-hosted Runner 접근 범위를 제한해야 하는 이유를 최소 권한 원칙과 연결하세요.

### E037
Ephemeral Runner가 장기 실행 Runner보다 격리 측면에서 유리할 수 있는 이유를 설명하세요.

### E038
GitHub-hosted Runner Image가 업데이트될 수 있다는 점을 재현성 관점에서 어떻게 관리할지 설명하세요.

### E039
Actions 사용을 Enterprise Policy로 제한해야 하는 상황을 예로 들어 설명하세요.

### E040
허용된 Action만 사용하도록 정책을 설계할 때 보안성과 개발 생산성 사이의 균형을 어떻게 잡을지 설명하세요.

## 완료 기준

Runner 선택을 비용만으로 결정하지 않고 **네트워크, 격리, 운영 책임, 정책**까지 설명합니다.

관련 Lab: [`080-runners-enterprise`](../../060-labs/080-runners-enterprise/README.md)
