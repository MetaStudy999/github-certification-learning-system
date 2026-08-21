# Lab 070 — Custom Actions

## Objective

GitHub Action의 세 가지 대표 구현 방식을 구분합니다.

## Types

- JavaScript Action
- Docker Container Action
- Composite Action

## Core Files

일반적으로 `action.yml` 또는 `action.yaml` 메타데이터 파일에서 Action 이름, 입력값, 실행 방식을 정의합니다.

## Compare

| 유형 | 장점 | 고려사항 |
|---|---|---|
| JavaScript | 빠른 실행, GitHub-hosted Runner 친화적 | Node 런타임과 번들 관리 |
| Docker | 실행환경 일관성 | Container 시작 비용, Linux 중심 |
| Composite | 여러 Shell/Action Step 재사용 | 복잡한 로직에는 한계 |

## Verify

- [ ] `action.yml`의 목적을 설명한다.
- [ ] Input / Output 개념을 설명한다.
- [ ] Release Tag와 Version 관리가 필요한 이유를 설명한다.
- [ ] 사용자가 신뢰할 수 있도록 문서화해야 할 항목을 설명한다.
