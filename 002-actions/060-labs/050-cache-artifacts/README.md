# 실습 (Lab, LAB) 050 — 캐시와 아티팩트 (Cache & Artifacts, CA)

## 목표 (Objective, OBJ)

Cache와 Artifact의 목적을 구분하고 Workflow 성능과 결과 전달 방식을 이해합니다.

## 핵심 차이 (Core Difference, CD)

```text
Cache
→ 다음 실행을 빠르게 하기 위한 재사용 데이터

Artifact
→ 현재 Workflow의 결과 파일을 저장·전달
```

## 실습 주제 (Practice Topics, PT)

- dependency cache
- cache key / restore key
- artifact upload
- artifact download
- retention period

## 검증 (Verify, VER)

- [ ] Cache와 Artifact 차이를 설명한다.
- [ ] Cache miss / hit의 의미를 설명한다.
- [ ] Artifact를 다음 Job에서 사용하는 흐름을 설명한다.

## 도전 과제 (Challenge, CHL)

Test 결과 파일을 Artifact로 저장하고, 별도 Job이 이를 다운로드하는 Workflow를 설계합니다.
