# GH-100 Mock 시험 01 — 질문 (GH-100 Mock Exam 01 — Questions, GH-100MEQ)

> 제한시간 권장: 60분 / 40문항

1. Enterprise가 IdP로 사용자 계정 Lifecycle까지 관리하려면 가장 적절한 조합은?  
A. SAML only  B. SAML + SCIM  C. SSH + PAT  D. Actions + OIDC

2. 로그인한 사용자가 Repository를 수정할 수 있는지 결정하는 개념은?  
A. Authentication  B. Authorization  C. Provisioning  D. Auditing

3. 퇴사자 접근이 남아 있다. FIRST로 확인할 것은?  
A. SCIM Deprovisioning  B. README  C. Cache  D. Branch name

4. 고권한 Role의 권장 원칙은?  
A. 모두에게 부여  B. 최소 인원  C. 외부 협력사 기본 부여  D. 공용 계정

5. Team Sync의 주요 목적은?  
A. IdP Group과 Team Membership 동기화  B. Secret 저장  C. Billing 삭제  D. Repo Archive

6. 외부 협력사가 특정 Repo 하나만 접근해야 한다. 가장 적절한 방식은?  
A. Enterprise Owner  B. Org Owner  C. 해당 Repo 최소 권한  D. 모든 Private Repo Read

7. Enterprise 계층에서 여러 Org에 공통 정책을 적용하려면?  
A. 상위 Enterprise Scope에서 설계  B. 개인 Git Config  C. Issue Label  D. README

8. GHEC와 GHES 차이로 가장 적절한 것은?  
A. 둘 다 고객 운영  B. Cloud SaaS vs 고객 운영 Server  C. 둘 다 On-prem  D. 둘 다 Public only

9. Data Residency 요구가 있는 경우 먼저 검토할 것은?  
A. 저장 위치와 배포 모델  B. Star 수  C. Fork 수  D. README 길이

10. GHES Upgrade 전 FIRST로 확인할 것은?  
A. 지원 Upgrade Path와 Release Notes  B. Team 이름  C. Issue 수  D. Wiki

11. Enterprise Support 요청 전 가장 적절한 준비는?  
A. 재현 절차와 영향 범위, 로그  B. Password 목록  C. 모든 권한 확대  D. Audit 삭제

12. Branch 직접 Push를 제한하고 PR Review를 강제하려면?  
A. Ruleset/Branch Protection  B. Projects  C. Wiki  D. Sponsors

13. 여러 Repo에 동일한 보호 정책을 일관되게 적용하려면?  
A. 상위 Scope Ruleset  B. 각 개발자 로컬 설정  C. README만  D. Issue Template

14. Secret이 Commit되기 전에 차단하는 기능은?  
A. Push Protection  B. Discussions  C. Pages  D. Projects

15. 정적 코드 취약점 분석과 가장 관련 깊은 기능은?  
A. Code Scanning  B. Milestones  C. Wiki  D. Pages

16. Dependency 취약성 관리와 가장 관련 깊은 것은?  
A. Dependabot/Dependency Graph  B. Discussions  C. Sponsors  D. Profile

17. 자동화 통합이 여러 Repo에 최소 권한으로 접근해야 한다. 가장 적절한 선택은?  
A. 공유 Classic PAT  B. GitHub App  C. 개인 Password  D. 공용 Owner 계정

18. PAT를 사용해야 할 때 가장 안전한 운영은?  
A. 최소 Scope·짧은 만료·안전한 저장  B. 영구 Token  C. README에 저장  D. 팀 공용 복사

19. 보안 Alert가 대량 발생했다. FIRST로 정해야 할 것은?  
A. 책임 Owner와 우선순위 기준  B. Avatar  C. Repo Topic  D. Star

20. Secret Scanning Alert 대응의 FIRST 조치는?  
A. Credential 폐기/회전  B. Alert 삭제  C. Repo Rename  D. Branch 삭제

21. Ruleset 변경 후 Workflow 실패가 시작됐다. FIRST 조치는?  
A. 변경 시점과 실패 로그 비교  B. 보호 전체 해제  C. 모든 Owner 추가  D. Audit 제거

22. Compliance Evidence로 가장 적절한 것은?  
A. 정책 + Audit Log + 검증 결과  B. Token 원문  C. Password 목록  D. SSH Private Key

23. Enterprise Actions에서 허용 Source를 제한하는 주된 이유는?  
A. Supply-chain 위험 감소  B. README 단축  C. Star 증가  D. Issue 감소

24. 외부 Action을 Full Commit SHA로 고정하는 이유는?  
A. 특정 불변 버전에 고정  B. Secret 제거  C. Runner 삭제  D. Billing 중지

25. `GITHUB_TOKEN` 권한의 권장 원칙은?  
A. write-all  B. 필요한 Permission만  C. Admin  D. Token 로그 출력

26. Production 배포 전 승인 절차가 필요하다. 관련 기능은?  
A. Environment protection rules  B. Wiki  C. Discussions  D. Sponsors

27. 내부망 DB에 접근해야 하는 Workflow의 Runner 후보는?  
A. 보호된 Self-hosted Runner  B. 항상 Public Runner  C. 개인 노트북  D. Anonymous runner

28. Self-hosted Runner의 추가 책임은?  
A. OS·Network·Hardening·Capacity 관리  B. GitHub가 전부 관리  C. Secret 불필요  D. Audit 불필요

29. Runner Group의 주요 목적은?  
A. Runner 접근 Scope 제어  B. README 생성  C. Issue 삭제  D. License 제거

30. 장기 Cloud Key 대신 권장할 수 있는 방식은?  
A. OIDC Federation  B. Shared PAT  C. Password  D. Public Secret

31. Third-party Vault 연동의 주요 목적은?  
A. Secret 중앙관리·회전  B. Secret 공개  C. Audit 삭제  D. Runner 제거

32. Self-hosted Runner가 잡을 받지 못한다. FIRST로 확인할 것은?  
A. Online 상태·Label·Group Scope  B. README  C. PR 제목  D. Wiki

33. Actions 비용 급증 분석의 FIRST 신호는?  
A. Workflow Run 빈도와 Runner 사용량  B. Star 수  C. Fork 수  D. README 길이

34. "누가 설정을 변경했는가"를 조사하는 핵심 자료는?  
A. Audit Log  B. Wiki  C. Profile  D. Sponsors

35. License 활용률을 계산하려면?  
A. 할당 사용자 vs 실제 활성 사용자  B. Star vs Fork  C. PR vs Issue  D. Branch vs Tag

36. API 사용량 급증 시 FIRST로 볼 것은?  
A. 호출 주체·Endpoint·빈도·Rate Limit  B. README  C. Topic  D. Avatar

37. 비용 최적화의 올바른 순서는?  
A. 측정→원인→조치→재측정  B. 기능 전체 중지  C. 사용자 전체 삭제  D. 로그 삭제

38. 정책 변경 후 Workflow 실패율이 증가했다. 결합해야 할 자료는?  
A. Audit Log + Workflow Run Trend  B. README + Wiki  C. Star + Fork  D. Bio + Avatar

39. Break-glass 예외를 설계할 때 필요한 것은?  
A. 승인·기간·Scope·Audit  B. 영구 예외  C. 익명 사용  D. Audit 비활성화

40. GH-100에서 가장 적절한 관리자 판단 방식은?  
A. Scope·상위정책·최소권한·감사 가능성을 함께 검토  B. 항상 Owner 권한 확대  C. 보안기능 해제  D. 수동 설정만 사용

---
답안을 확정한 후 [`answers.md`](./answers.md)를 확인하세요.
