# GH-100 Final Mock — 질문 (GH-100 Final Mock — Questions, GH-100FMQ)

> 제한시간 권장: 60분 / 40문항. 실제 시험 직전 최종 Gate용입니다.

1. Enterprise가 개인 계정과 업무 Identity를 분리하고 IdP 중심으로 계정을 통제하려 한다. 가장 적절한 모델은?  
A. EMU  B. Public Org  C. Personal Account only  D. Repository Collaborator only

2. SAML SSO가 정상인데 신규 직원 계정이 자동 생성되지 않는다. 가장 관련 깊은 영역은?  
A. SCIM Provisioning  B. Actions Cache  C. Branch Protection  D. Pages

3. 퇴사자 계정이 비활성화되었지만 자동화가 그 사용자의 PAT에 의존한다. 가장 적절한 장기 개선은?  
A. Automation Identity를 사람 Identity에서 분리  B. PAT 공유 확대  C. Owner 권한 부여  D. Audit 제거

4. Organization Owner 권한 검토의 핵심 목적은?  
A. 불필요한 Privilege 제거  B. 모두 Owner 승격  C. SSO 해제  D. Repo Public 전환

5. Team 기반 접근관리가 사용자별 직접 권한보다 일반적으로 나은 이유는?  
A. 일관성과 Lifecycle 관리가 쉬움  B. Secret 저장 가능  C. Audit 불필요  D. Git이 빨라짐

6. Enterprise 전반의 Repository 정책을 일관되게 관리하려면 무엇을 먼저 설계해야 하는가?  
A. Scope와 상위 Policy  B. Issue Label  C. Profile README  D. Star 정책

7. 회사가 서버 운영 부담을 최소화하려 한다. 일반적으로 먼저 검토할 배포 모델은?  
A. GHEC  B. GHES  C. Local Git only  D. Public fork only

8. 규제상 데이터 저장 위치 요구가 있다. 가장 먼저 확인해야 할 것은?  
A. Data Residency 지원과 배포 Architecture  B. PR 제목  C. Wiki  D. Avatar

9. GHES 운영에서 Recovery 요구사항을 충족하려면 반드시 필요한 계획은?  
A. Backup/Restore  B. Sponsors  C. Projects  D. Discussion

10. Enterprise 표준 변경을 전체 적용하기 전 가장 안전한 접근은?  
A. Pilot Scope에서 검증  B. 즉시 전체 적용  C. Audit 중지  D. 모든 Owner 추가

11. 여러 Repo의 기본 Branch에 PR Review를 공통 강제하려면 가장 적절한 제어는?  
A. Ruleset  B. Issue Template  C. Wiki  D. Topic

12. Ruleset 예외가 필요하다. 가장 적절한 예외 설계는?  
A. 승인·기간·Scope·Audit 포함  B. 무기한 예외  C. 익명 예외  D. 문서 없음

13. 비밀키가 Push되기 직전에 차단하려면?  
A. Push Protection  B. Projects  C. Discussions  D. Pages

14. 정적 코드 취약점 분석 결과를 관리하는 기능은?  
A. Code Scanning  B. Milestone  C. Wiki  D. Sponsors

15. 의존성 취약점과 업데이트 자동화를 함께 다루는 대표 기능은?  
A. Dependabot  B. Codespaces  C. Discussions  D. Pages

16. 서비스 통합이 Organization의 일부 Repo만 접근해야 한다. 가장 적절한 방식은?  
A. GitHub App을 제한된 설치 Scope로 사용  B. Enterprise Owner PAT  C. 공용 Password  D. SSH Key 공유

17. GitHub App과 OAuth App 중 선택 기준으로 가장 중요한 것은?  
A. Identity·Permission·Installation 요구  B. Star 수  C. README 길이  D. Issue 수

18. PAT 운영정책에 반드시 포함해야 할 것은?  
A. 최소 Scope·Expiration·Rotation  B. 영구 사용  C. 공개 저장  D. 공용 복사

19. Security Alert를 운영 프로세스에 연결할 때 가장 먼저 정의할 것은?  
A. Ownership과 Escalation  B. Avatar  C. Repository Topic  D. Wiki

20. Secret 노출이 확인됐다. FIRST 조치는?  
A. Credential 회전/폐기  B. Alert 숨김  C. Repo Rename  D. Audit 삭제

21. Enterprise가 허용 가능한 Actions Source를 제한해야 하는 이유는?  
A. Supply-chain Risk 감소  B. PR 수 감소  C. README 단축  D. Star 증가

22. Action을 Full Commit SHA로 Pinning하는 이유는?  
A. 참조 변경 위험을 줄이기 위해  B. Secret 제거  C. Runner 삭제  D. Billing 중단

23. Workflow가 `write-all` Token 권한을 사용한다. 가장 적절한 개선은?  
A. 필요한 Permission만 명시  B. Admin PAT 사용  C. Check 제거  D. Public 전환

24. Production 배포 전에 승인자가 필요하다. 가장 적절한 기능은?  
A. Environment Protection  B. Wiki  C. Discussion  D. Sponsor

25. 내부망 Resource에 접근할 필요가 있다. Self-hosted Runner를 도입할 때 가장 중요한 추가 책임은?  
A. Hardening·Network·Patch·Capacity  B. GitHub가 전부 담당  C. Audit 제거  D. Secret 불필요

26. Runner Group의 핵심 목적은?  
A. Runner 사용 Scope를 제한  B. README 관리  C. Billing 제거  D. Star 관리

27. 장기 Cloud Secret 대신 단기 자격증명을 선호한다. 가장 관련 깊은 기술은?  
A. OIDC  B. PAT Classic  C. Password  D. SSH shared key

28. Third-party Vault를 사용하는 이유는?  
A. Secret 중앙관리·회전·접근 통제  B. Secret 공개  C. Runner 제거  D. Audit 중지

29. Self-hosted Runner Queue가 길어지고 대기시간이 늘었다. 가장 가능성 높은 원인은?  
A. Capacity 부족  B. README 오류  C. Star 부족  D. Wiki 증가

30. Actions 비용이 갑자기 증가했다. FIRST로 확인할 것은?  
A. Run 빈도·Runner 사용량·Storage  B. Repo 이름  C. Avatar  D. Issue Label

31. 관리자가 "누가 정책을 바꿨는가"를 확인하려 한다. 가장 적절한 자료는?  
A. Audit Log  B. README  C. Wiki  D. Sponsors

32. Audit 분석에서 Target은 무엇을 의미하는가?  
A. 변경/행위의 대상  B. 비용계정  C. Runner OS  D. 사용자 Bio

33. License 비용과 Actions 비용을 함께 최적화하려면?  
A. Seat 활용률과 Metered Usage를 분리 분석  B. 하나의 숫자로 합쳐 추정  C. Audit 삭제  D. 사용자 전원 삭제

34. API 자동화가 Rate Limit에 걸린다. 가장 적절한 개선은?  
A. 호출 최적화·Backoff·Caching  B. Token 권한 확대  C. Owner 추가  D. SSO 비활성화

35. 월간 Health Review에 포함하기 가장 적절한 조합은?  
A. Identity·Security·Actions·Usage·Cost  B. Password·Private Key  C. Star·Fork only  D. Avatar·Bio

36. 정책 변경 직후 장애가 발생했다. Root Cause 분석에 가장 유용한 조합은?  
A. Audit Change + Operational Logs  B. README + Wiki  C. Star + Fork  D. Profile + Bio

37. Break-glass 절차의 목적은?  
A. 통제된 긴급 예외 제공  B. 영구 Admin 우회  C. Audit 제거  D. 보안기능 해제

38. Enterprise Admin Blueprint에서 Trust Boundary를 문서화해야 하는 이유는?  
A. 책임과 위험 경계를 명확히 하기 위해  B. 디자인 개선  C. Star 증가  D. PR 감소

39. CONTENT-READY와 EXAM-READY의 차이는?  
A. 자료 준비 상태 vs 실제 학습 Gate 통과 상태  B. 같은 의미  C. 둘 다 시험 합격  D. 둘 다 Project 완료

40. 최종 시험 직전 가장 신뢰할 수 있는 준비도 신호는?  
A. 최근 Mock 2회 85%+와 오답 재시험 90%+  B. README 1회 읽기  C. Owner 권한 보유  D. Star 수

---
답안을 확정한 뒤 [`answers.md`](./answers.md)를 확인하세요.
