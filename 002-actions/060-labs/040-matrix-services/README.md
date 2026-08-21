# 실습 (Lab, LAB) 040 — 매트릭스와 서비스 컨테이너 (Matrix & Service Containers, MSC)

## 목표 (Objective, OBJ)

Matrix Strategy로 여러 실행 조합을 만들고 Service Container 개념을 이해합니다.

## 매트릭스 예제 (Matrix Example, MXE)

```yaml
strategy:
  fail-fast: false
  matrix:
    python-version: ['3.11', '3.12']
    os: [ubuntu-latest, windows-latest]

runs-on: ${{ matrix.os }}
```

## 학습 포인트 (Learn, LRN)

- `strategy.matrix`
- `include` / `exclude`
- `fail-fast`
- `max-parallel`
- Service Container의 목적
- DB·Queue 등 의존 서비스의 Port / Health Check 개념

## 검증 (Verify, VER)

- [ ] Matrix가 여러 Job 조합을 생성하는 이유를 설명한다.
- [ ] `include`와 `exclude`의 목적을 설명한다.
- [ ] Service Container가 일반 Step과 어떻게 다른지 설명한다.

## 도전 과제 (Challenge, CHL)

실행 조합 수를 계산하고, 불필요한 조합을 `exclude`하여 비용을 줄입니다.
