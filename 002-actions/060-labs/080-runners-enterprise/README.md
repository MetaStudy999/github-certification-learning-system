# Lab 080 — Runners & Enterprise

## Objective

GitHub-hosted Runner와 Self-hosted Runner의 차이와 Enterprise 운영 관점을 이해합니다.

## Compare

| 항목 | GitHub-hosted | Self-hosted |
|---|---|---|
| 관리 | GitHub | 사용자/조직 |
| 환경 준비 | 표준 이미지 제공 | 직접 설치·패치 |
| 격리 | 실행 단위로 관리 | 구성에 따라 다름 |
| 네트워크 | 표준 Cloud 환경 | 내부망 연계 가능 |
| 책임 | 상대적으로 적음 | 보안·업데이트 책임 증가 |

## Enterprise Topics

- Runner Group
- Repository / Organization 접근 범위
- Action allow/deny policy
- Workflow usage policy
- Runner Label
- Scale set / autoscaling 개념

## Verify

- [ ] Self-hosted Runner를 선택해야 하는 대표 이유를 설명한다.
- [ ] Self-hosted Runner의 보안 책임을 설명한다.
- [ ] Runner Group과 Label의 역할을 구분한다.
- [ ] Enterprise에서 허용 Action을 제한하는 이유를 설명한다.
