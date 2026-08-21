# GH-600 시험-Day 전략 (GH-600 Exam-Day Strategy, GH-600ES)

## 문제 읽기 순서

1. Agent의 Goal과 현재 단계가 Planning인지 Execution인지 확인합니다.
2. Scope / Permission / Environment 조건을 찾습니다.
3. State / Evaluation / Guardrail 요구를 찾습니다.
4. `BEST`, `FIRST`, `MOST appropriate` 조건을 표시합니다.

## 선택지 제거 기준

- 필요한 것보다 과도한 권한을 요구함
- 계획 검토 없이 바로 고위험 실행
- Evaluation 없이 성공으로 간주
- 실패를 무한 Retry
- Multi-Agent가 불필요한데 복잡성만 증가
- Human Oversight / Accountability를 제거

## 시간 관리

- 1차: 정의·비교 문제
- 2차: Scenario 기반 설계 문제
- 3차: 긴 Multi-Agent / Guardrail 문제
- 마지막: 미응답·Review 표시 문제 확인

## 시험 직전

공식 Study Guide, Confusion Matrix, 최근 오답만 압축 복습합니다.
