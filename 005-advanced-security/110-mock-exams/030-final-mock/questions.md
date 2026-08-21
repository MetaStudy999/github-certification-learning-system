# GH-500 Final Mock — 질문 (GH-500 Final Mock — Questions, GH-500FMQ)

> 자체 제작 40문항. 목표 점수 **90%+**.

1. 여러 저장소의 보안 상태를 중앙에서 비교하려 한다. A Projects B Security Overview C Pages D Actions Cache
2. Push 단계에서 자격증명 노출을 막는 기능은? A SBOM B CodeQL C Push Protection D Security Campaign
3. 특정 취약점 유형을 여러 저장소에서 기간 내 줄이려 한다. A Security Campaign B Release C Wiki D Fork
4. Secret Protection과 Code Security의 차이는? A 저장소 vs 조직 B 자격증명 노출 vs 코드 취약점 C PR vs Issue D Git vs GitHub
5. Alert Dismissal에서 가장 중요한 것은? A 빠른 종료 B 근거·책임·추적성 C Star 수 D Repository 크기
6. 조직 고유 민감정보 패턴을 탐지하려면? A SARIF B SBOM C Custom Pattern D Dependency Review
7. 발견된 자격증명의 현재 유효성을 판단하는 데 도움되는 것은? A Validity Check B Code Owners C Projects D Actions
8. Bypass 예외의 적절한 운영은? A 누구나 무기한 B 제한된 권한·사유·기간·감사 C 기록 없음 D 정책 비활성화
9. Secret 노출 사고의 완료 대응은? A Alert 닫기 B 영향 파악 후 무효화/교체 및 검증 C Repository 삭제 D Branch 변경
10. 여러 저장소에 보안 정책을 확장할 때 가장 적절한 관점은? A 각자 임의 설정 B 상위 Scope 표준화 C 로그 제거 D 예외 무제한
11. PR에서 새 의존성의 위험을 검토하는 기능은? A Dependency Review B Secret Protection C CodeQL D SAML
12. 기존 알려진 취약 의존성 경고는? A Dependabot Alerts B Push Protection C Security Campaign D SARIF
13. 의존성 관계를 파악하는 기반 기능은? A Dependency Graph B SBOM만 C CodeQL D Copilot
14. 표준화된 소프트웨어 구성요소 명세는? A SARIF B SBOM C SAML D SCIM
15. Transitive Dependency는? A 직접 선언 B 간접 포함 C Secret 유형 D 분석 결과 형식
16. 자동 의존성 업데이트 PR에 대한 적절한 태도는? A 무조건 Merge B 테스트·호환성 검증 C 모두 닫기 D 모두 무시
17. 빠르고 단순한 CodeQL 도입 방식은? A Advanced Setup B Default Setup C Manual only D Disabled
18. 세밀한 빌드·분석 제어가 필요하면? A Default Setup B Security Overview C Advanced Setup D Push Protection
19. 정적 분석 결과 표준 교환 형식은? A SBOM B SARIF C SAML D SCIM
20. CodeQL Alert가 많을 때 적절한 대응은? A 모두 Dismiss B 위험·영향·신뢰도 기반 우선순위화 C 분석 중단 D 저장소 삭제
21. PR 기반 Code Security의 장점은? A Merge 전 조기 발견 B 모든 취약점 100% 보장 C Secret 저장 D 사용자 인증
22. False Positive 의심 Alert에 적절한 조치는? A 근거 검토 후 상태 처리 B 즉시 삭제 C 분석 중단 D 기록 제거
23. CodeQL이 모든 보안 문제를 찾는다고 보는 것은? A 적절 B 부적절, 다른 통제와 검증 필요 C Secret에만 해당 D 의존성에만 해당
24. Code Security 운영 흐름은? A Detect → Prioritize → Remediate → Verify B Ignore → Delete C Fork → Star D Clone → Tag
25. 다수 Repository 위험을 우선순위화하는 데 유용한 기능은? A Security Overview B Wiki C Pages D Discussions
26. Security Campaign의 필수 설계 요소는? A 목표 위험·대상·기한·책임자 B Star 수 C README 길이 D Branch 수
27. Campaign 성공 증거는? A Campaign 생성 B 대상 위험의 실제 감소와 검증 C Issue 증가 D Alert 숨김
28. 반복 문제를 줄이는 가장 좋은 방법은? A 원인 분석과 예방 통제 개선 B 매번 Dismiss C 로그 제거 D 분석 비활성화
29. Severity만으로 우선순위를 정하면 부족한 이유는? A 실제 노출·영향·맥락도 중요 B Severity가 무의미 C UI 문제 D 비용 문제
30. MTTR은 무엇을 보는 지표인가? A Remediation 속도 B Branch 수 C 사용자 수 D Repository 크기
31. 보안 Role 설계의 기본 원칙은? A 최소 권한 B 최대 권한 C 공용 관리자 D 익명 변경
32. Default Configuration의 장점은? A 여러 저장소에 표준 설정 확장 B 모든 Alert 삭제 C 사용자 인증 D Branch 생성
33. 정책 예외의 적절한 조건은? A 사유·기한·승인·감사 B 누구나 영구 허용 C 기록 금지 D 자동 전체 승인
34. 관리 API/자동화에서 필요한 것은? A 최소 권한·변경 추적·검증 B 공용 관리자 Token C 감사 제거 D 무기한 자격증명
35. 정책 Rollout 후 가장 먼저 검증할 것은? A 실제 적용 상태와 예외 B README 제목 C Star 수 D Fork 수
36. Public Repository와 Enterprise 환경 비교에서 중요한 것은? A 기능 가용성과 운영 책임 B Markdown 문법 C Git 명령 차이 D Commit 길이
37. Prevention-first와 Gate-based 전략의 관계는? A 상호 보완 가능 B 하나만 항상 정답 C 완전히 동일 D 무관
38. GH-500에서 실제 시험 준비에 가장 중요한 것은? A 기능 이름만 암기 B Scenario에서 기능 선택·대응 판단 C 메뉴 색상 암기 D 유출문제 수집
39. CONTENT-READY와 EXAM-READY의 차이는? A 저장소 자료 준비 vs 실제 학습 기준 통과 B 동일 C 시험 합격 vs 자격 만료 D Public vs Private
40. 시험 직전 최종 판단으로 가장 적절한 것은? A 날짜가 왔으니 무조건 응시 B 최신 Study Guide 확인 + 최근 Mock/오답 Gate 통과 C 실습 생략 D 약점 Domain 무시
