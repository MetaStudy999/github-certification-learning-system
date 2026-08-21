#!/usr/bin/env python3
"""Final pass for residual English-only Markdown headings in GCLS.

Run after normalize-language-notation.py. The script only touches Markdown headings
outside fenced code blocks and keeps the original English text in parentheses.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXACT = {
    "Rubric": "평가 기준 (Rubric, RUB)",
    "Scoring": "채점 (Scoring, SCR)",
    "Score": "점수 (Score, SCR)",
    "Final Gate": "최종 통과 기준 (Final Gate, FG)",
    "Gate": "통과 기준 (Gate, GATE)",
    "Queue": "대기열 (Queue, QUE)",
    "HIGH": "높음 (HIGH, H)",
    "MEDIUM": "중간 (MEDIUM, M)",
    "LOW": "낮음 (LOW, L)",
    "Retry Gate": "재도전 통과 기준 (Retry Gate, RG)",
    "GitHub Docs": "GitHub 문서 (GitHub Docs, GHD)",
    "Notes": "메모 (Notes, NTS)",
    "Lab Evidence Template": "실습 증빙 템플릿 (Lab Evidence Template, LET)",
    "Lab Record": "실습 기록 (Lab Record, LR)",
    "GitHub References": "GitHub 참고자료 (GitHub References, GHR)",
    "Preparation Snapshot": "준비 현황 요약 (Preparation Snapshot, PS)",
    "Top-Level Structure": "최상위 구조 (Top-Level Structure, TLS)",
    "CLEAR Evidence": "CLEAR 증빙 (CLEAR Evidence, CE)",
    "Official Baseline": "공식 기준선 (Official Baseline, OB)",
    "5 Domains": "5개 영역 (5 Domains, 5D)",
    "Mock Set": "모의고사 세트 (Mock Set, MS)",
    "Final Evidence": "최종 증빙 (Final Evidence, FE)",
    "Active Queue": "활성 대기열 (Active Queue, AQ)",
    "Retry Result": "재도전 결과 (Retry Result, RR)",
    "Retry Cycle": "재도전 주기 (Retry Cycle, RC)",
    "Priority": "우선순위 (Priority, PRI)",
    "Daily Log": "일일 기록 (Daily Log, DL)",
    "Reflection": "회고 (Reflection, RFL)",
    "Mock Structure": "모의고사 구조 (Mock Structure, MS)",
    "Score Gate": "점수 통과 기준 (Score Gate, SG)",
    "+1 Day Queue": "+1일 대기열 (+1 Day Queue, D1Q)",
    "+7 Day Queue": "+7일 대기열 (+7 Day Queue, D7Q)",
    "Repeated Errors": "반복 오류 (Repeated Errors, RE)",
    "Weekly Summary": "주간 요약 (Weekly Summary, WS)",
    "Result": "결과 (Result, RST)",
    "Trend": "추세 (Trend, TRD)",
    "PASSED": "합격 상태 (PASSED, PS)",
    "CLEAR": "완전 완료 상태 (CLEAR, CLR)",
    "Templates": "템플릿 (Templates, TPL)",
    "Daily Close": "일일 마감 (Daily Close, DC)",
    "Mandatory": "필수 (Mandatory, MND)",
    "Strongly Recommended": "강력 권장 (Strongly Recommended, SR)",
    "Thresholds": "기준값 (Thresholds, THR)",
    "Volume": "규모 (Volume, VOL)",
    "Baseline": "기준선 (Baseline, BL)",
    "Assessment Volume": "평가 규모 (Assessment Volume, AV)",
    "Sets": "세트 (Sets, SET)",
    "Built Set": "구축 세트 (Built Set, BS)",
    "Record Template": "기록 템플릿 (Record Template, RT)",
    "General Evidence Template": "공통 증빙 템플릿 (General Evidence Template, GET)",
    "Score Record": "점수 기록 (Score Record, SR)",
    "Quality Gate": "품질 통과 기준 (Quality Gate, QG)",
    "Common Gate": "공통 통과 기준 (Common Gate, CG)",
    "Supporting Docs": "지원 문서 (Supporting Docs, SD)",
    "Close Gate": "종료 통과 기준 (Close Gate, CG)",
    "Standard Retry Cycle": "표준 재도전 주기 (Standard Retry Cycle, SRC)",
    "Session Log Template": "세션 기록 템플릿 (Session Log Template, SLT)",
    "Minimum Gate": "최소 통과 기준 (Minimum Gate, MG)",
    "Recommended Gate": "권장 통과 기준 (Recommended Gate, RG)",
    "Recommended Structure": "권장 구조 (Recommended Structure, RS)",
    "Evidence Minimum": "최소 증빙 기준 (Evidence Minimum, EM)",
    "Lab PASS": "실습 통과 (Lab PASS, LP)",
    "Lab CLEAR": "실습 완전 완료 (Lab CLEAR, LC)",
    "Session Close Gate": "세션 종료 통과 기준 (Session Close Gate, SCG)",
    "Master Dashboard": "통합 대시보드 (Master Dashboard, MD)",
    "Common Official Entry Points": "공통 공식 진입점 (Common Official Entry Points, COEP)",
    "Result Values": "결과 값 (Result Values, RV)",
    "After Passing": "합격 후 절차 (After Passing, AP)",
    "Portfolio Narrative": "포트폴리오 서사 (Portfolio Narrative, PN)",
    "Portfolio Unit": "포트폴리오 단위 (Portfolio Unit, PU)",
    "Skill Balance": "기술 균형 (Skill Balance, SB)",
    "Personal Accounts": "개인 계정 (Personal Accounts, PA)",
    "Certification Page": "자격증 페이지 (Certification Page, CP)",
    "Daily Tracker": "일일 추적 (Daily Tracker, DT)",
    "Readiness Gate": "준비도 통과 기준 (Readiness Gate, RG)",
    "Score Log": "점수 기록 (Score Log, SL)",
    "Retry Queue": "재도전 대기열 (Retry Queue, RQ)",
    "Reflection Template": "회고 템플릿 (Reflection Template, RT)",
    "Final Reflection Template": "최종 회고 템플릿 (Final Reflection Template, FRT)",
    "Daily Tracker — GH-200": "일일 추적 (Daily Tracker, DT) — GH-200",
    "Readiness Gate — GH-200": "준비도 통과 기준 (Readiness Gate, RG) — GH-200",
    "Score Log — GH-200": "점수 기록 (Score Log, SL) — GH-200",
    "SAML SSO": "SAML 기반 싱글 사인온 (SAML Single Sign-On, SAML SSO)",
    "SCIM": "도메인 간 ID 관리 시스템 (System for Cross-domain Identity Management, SCIM)",
    "2FA": "2단계 인증 (Two-Factor Authentication, 2FA)",
    "MCP": "모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)",
}

TOPICS = {
    "GH-900 Study Guide": "GH-900 학습 가이드",
    "Foundations Labs Completion Gate": "Foundations 실습 완료 통과 기준",
    "Mixed Gate": "혼합 통과 기준",
    "Knowledge": "지식",
    "Hands-on": "실습",
    "Coverage": "범위 충족",
    "Mock": "모의고사",
    "Explainability": "설명 가능성",
    "Retry": "재도전",
    "Final": "최종",
    "Risk Mitigation": "위험 완화",
    "Accept / Modify / Reject": "수락 / 수정 / 거부",
    "Copilot CLI": "Copilot 명령줄 인터페이스",
    "Spaces / Spark": "Spaces / Spark",
    "Proxy / Filtering": "프록시 / 필터링",
    "Post-processing": "후처리",
    "LLM Limitations": "대규모 언어 모델 한계",
    "Chat History": "채팅 기록",
    "Legacy Modernization": "레거시 현대화",
    "Unit Test": "단위 테스트",
    "Assertion Quality": "단언문 품질",
    "Output Ownership": "출력물 소유권",
    "Suggestions Not Showing": "제안이 표시되지 않음",
    "Safeguard Defense in Depth": "다층 방어 안전장치",
    "Requirement": "요구사항",
    "Debug / Refactor": "디버그 / 리팩터",
    "Identities and Access": "식별과 접근",
    "Monitor and Optimize": "모니터링과 최적화",
    "PAT / GitHub App / OAuth App": "PAT / GitHub 앱 / OAuth 앱",
    "Monitor → Optimize": "모니터링 → 최적화",
    "GHES Responsibility": "GHES 책임 범위",
    "License Consumption": "라이선스 사용량",
    "Runners, Network, Credentials": "러너, 네트워크, 자격 증명",
    "Skills Measured": "측정 기술",
    "Skills Measured — July 2026": "측정 기술 — 2026년 7월",
    "2026-08-07 Skills Measured": "2026-08-07 측정 기술",
    "Official Baseline": "공식 기준선",
    "Final Evidence": "최종 증빙",
    "What changed in my understanding?": "내 이해에서 무엇이 달라졌는가?",
    "One-Sentence Summary": "한 문장 요약",
    "CLEAR Reflection Gate": "CLEAR 회고 통과 기준",
    "EXAM-READY Check": "EXAM-READY 점검",
    "Score Record": "점수 기록",
    "Common Official Entry Points": "공통 공식 진입점",
}

WORD = {
    "Study": "학습", "Guide": "가이드", "Foundations": "Foundations", "Labs": "실습",
    "Completion": "완료", "Gate": "통과 기준", "Mixed": "혼합", "Knowledge": "지식",
    "Hands-on": "실습", "Tracker": "추적", "Evidence": "증빙", "Official": "공식",
    "Baseline": "기준선", "Skills": "기술", "Measured": "측정", "Identities": "식별",
    "Access": "접근", "Monitor": "모니터링", "Optimize": "최적화", "Personal": "개인",
    "Accounts": "계정", "Responsibility": "책임", "License": "라이선스", "Consumption": "사용량",
    "Runners": "러너", "Network": "네트워크", "Credentials": "자격 증명", "Risk": "위험",
    "Mitigation": "완화", "Accept": "수락", "Modify": "수정", "Reject": "거부", "Proxy": "프록시",
    "Filtering": "필터링", "Limitations": "한계", "Chat": "채팅", "History": "기록", "Legacy": "레거시",
    "Modernization": "현대화", "Unit": "단위", "Test": "테스트", "Assertion": "단언문", "Quality": "품질",
    "Output": "출력물", "Ownership": "소유권", "Suggestions": "제안", "Showing": "표시", "Safeguard": "안전장치",
    "Defense": "방어", "Depth": "다층", "Requirement": "요구사항", "Debug": "디버그", "Refactor": "리팩터",
    "Final": "최종", "Clear": "완료", "Daily": "일일", "Log": "기록", "Retry": "재도전",
    "Result": "결과", "Cycle": "주기", "Priority": "우선순위", "Reflection": "회고", "Score": "점수",
    "Mock": "모의고사", "Structure": "구조", "Templates": "템플릿", "Mandatory": "필수",
    "Strongly": "강력", "Recommended": "권장", "Thresholds": "기준값", "Volume": "규모",
    "Assessment": "평가", "Sets": "세트", "Built": "구축", "Record": "기록", "Template": "템플릿",
    "General": "공통", "Supporting": "지원", "Docs": "문서", "Close": "종료", "Standard": "표준",
    "Session": "세션", "Minimum": "최소", "Common": "공통", "Entry": "진입", "Points": "지점",
    "Values": "값", "After": "후", "Passing": "합격", "Portfolio": "포트폴리오", "Narrative": "서사",
    "Rubric": "평가 기준", "Scoring": "채점", "Notes": "메모", "References": "참고자료",
    "Preparation": "준비", "Snapshot": "현황 요약", "Top-Level": "최상위", "Page": "페이지",
    "Coverage": "범위 충족", "Explainability": "설명 가능성", "Trend": "추세", "Area": "영역",
    "Areas": "영역", "Day": "일차", "Queue": "대기열", "Active": "활성", "Repeated": "반복",
    "Errors": "오류", "Weekly": "주간", "Summary": "요약", "Check": "점검", "Review": "검토",
    "Requirement": "요구사항", "Lab": "실습", "CLEAR": "CLEAR", "PASS": "통과", "REVIEW": "재검토",
}


def abbr(text: str) -> str:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9-]*", text)
    keep = []
    for token in tokens:
        if token.lower() in {"and", "or", "the", "of", "in", "my", "what", "with", "to"}:
            continue
        if token.isupper() and len(token) <= 8:
            keep.append(token)
        else:
            keep.append(token[0].upper())
    return ("".join(keep) or "TERM")[:12]


def translate(text: str) -> str:
    if text in TOPICS:
        return TOPICS[text]
    parts = re.split(r"(\s+|/|,|&|→|—|–|-)", text)
    changed = False
    out = []
    for part in parts:
        key = part.strip()
        if key in WORD:
            repl = WORD[key]
            out.append(part.replace(key, repl))
            changed = changed or repl != key
        elif key == "&":
            out.append(part.replace("&", "와"))
            changed = True
        else:
            out.append(part)
    result = "".join(out)
    return result if changed else text


def wrap(topic: str) -> str:
    if re.search(r"[가-힣]", topic):
        return topic
    if topic in EXACT:
        return EXACT[topic]
    ko = translate(topic)
    if ko == topic or not re.search(r"[가-힣]", ko):
        return topic
    return f"{ko} ({topic}, {abbr(topic)})"


def normalize_body(body: str) -> str:
    if re.search(r"[가-힣]", body):
        return body
    if body in EXACT:
        return EXACT[body]

    # Mock question identifiers are headings in some files.
    m = re.fullmatch(r"Q(\d{2})", body)
    if m:
        q = m.group(1)
        return f"문제 {q} (Question {q}, Q{q})"

    # Numbered or lettered topic headings.
    m = re.fullmatch(r"((?:\d+|[A-Z])\.\s+)(.+)", body)
    if m:
        idx, topic = m.groups()
        mapped = wrap(topic)
        if mapped != topic:
            return idx + mapped

    # Gate A — Knowledge, etc.
    m = re.fullmatch(r"Gate\s+([A-Z])\s+[—-]\s+(.+)", body)
    if m:
        letter, topic = m.groups()
        return f"통과 기준 (Gate, GATE) {letter} — {wrap(topic)}"

    # Day N — Topic.
    m = re.fullmatch(r"Day\s+(\d+)\s+[—-]\s+(.+)", body)
    if m:
        day, topic = m.groups()
        return f"{day}일차 (Day {day}, D{day}) — {wrap(topic)}"

    # Exercise IDs with residual topics.
    m = re.fullmatch(r"(E\d{3}(?:-\d{2})?)\s+[—-]\s+(.+)", body)
    if m:
        eid, topic = m.groups()
        mapped = wrap(topic)
        if mapped != topic:
            return f"{eid} — {mapped}"

    # Numeric GCLS document ID + title + optional exam code.
    m = re.fullmatch(r"(\d{3})\s+(.+?)(?:\s+[—-]\s+(GH-\d{3}(?:\s+.*)?))?", body)
    if m:
        num, title, exam = m.groups()
        mapped = wrap(title)
        if mapped != title:
            return f"{num} {mapped}" + (f" — {exam}" if exam else "")

    # GH exam-code-prefixed tracker/template headings.
    m = re.fullmatch(r"(GH-\d{3})\s+(.+)", body)
    if m:
        exam, title = m.groups()
        mapped = wrap(title)
        if mapped != title:
            return f"{exam} {mapped}"

    # Score range status headings.
    m = re.fullmatch(r"(\d+[–-]\d+)\s+[—-]\s+(PASS|REVIEW|CLEAR)", body)
    if m:
        score, status = m.groups()
        status_map = {"PASS": "통과 (PASS, P)", "REVIEW": "재검토 (REVIEW, R)", "CLEAR": "완전 완료 (CLEAR, CLR)"}
        return f"{score} — {status_map[status]}"

    # Skills measured with a date suffix.
    m = re.fullmatch(r"Skills Measured\s+[—-]\s+(.+)", body)
    if m:
        tail = m.group(1)
        return f"측정 기술 (Skills Measured, SM) — {tail}"

    mapped = wrap(body)
    return mapped


def process(text: str) -> str:
    out = []
    in_fence = False
    fence = ""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            marker = s[:3]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            out.append(line)
            continue
        if not in_fence:
            m = re.match(r"^(#{1,6}\s+)(.*?)(\s*)$", line)
            if m:
                prefix, body, suffix = m.groups()
                new_body = normalize_body(body)
                line = f"{prefix}{new_body}{suffix}"
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or path.name == "061-language-audit.md":
            continue
        old = path.read_text(encoding="utf-8")
        new = process(old)
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"Finalized Markdown files: {changed}")


if __name__ == "__main__":
    main()
