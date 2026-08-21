#!/usr/bin/env python3
"""Normalize GCLS Markdown labels to Korean (English, ABBR) notation.

This script intentionally changes documentation labels only. It does not translate
commands, code, paths, URLs, YAML/JSON keys, or arbitrary prose.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING_MAP = {
    "Quick Start": "빠른 시작 (Quick Start, QS)",
    "Certification Roadmap": "자격증 로드맵 (Certification Roadmap, CR)",
    "System Control Tower": "시스템 통합 관제 (System Control Tower, SCT)",
    "Current Learning Content Scale": "현재 학습 콘텐츠 규모 (Current Learning Content Scale, CLCS)",
    "Status Model": "상태 모델 (Status Model, SM)",
    "Content Status": "콘텐츠 상태 (Content Status, CS)",
    "Learning Status": "학습 상태 (Learning Status, LS)",
    "Learning Architecture": "학습 아키텍처 (Learning Architecture, LA)",
    "Standard Internal Course Structure": "표준 과정 내부 구조 (Standard Internal Course Structure, SICS)",
    "Exam Readiness Gate": "시험 준비도 통과 기준 (Exam Readiness Gate, ERG)",
    "Readiness Gate": "준비도 통과 기준 (Readiness Gate, RG)",
    "Repository Map": "저장소 맵 (Repository Map, RM)",
    "Portfolio Growth Path": "포트폴리오 성장 경로 (Portfolio Growth Path, PGP)",
    "Growth Summary": "성장 요약 (Growth Summary, GS)",
    "Verification": "검증 (Verification, VER)",
    "Current Phase": "현재 단계 (Current Phase, CP)",
    "Overview": "개요 (Overview, OVW)",
    "Terms": "용어 (Terms, TRM)",
    "Concepts": "개념 (Concepts, CPT)",
    "Official Docs": "공식 문서 (Official Docs, ODC)",
    "Official Documentation": "공식 문서 (Official Documentation, ODC)",
    "Official Sources": "공식 출처 (Official Sources, OS)",
    "Official Links": "공식 링크 (Official Links, OL)",
    "Guides": "가이드 (Guides, GDE)",
    "Labs": "실습 (Labs, LAB)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Final Review": "최종 복습 (Final Review, FR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Wrong Answers": "오답 관리 (Wrong Answers, WA)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Evidence": "증빙 (Evidence, EVD)",
    "Exam Snapshot": "시험 개요 (Exam Snapshot, ES)",
    "Content Inventory": "콘텐츠 구성 (Content Inventory, CI)",
    "Core Areas": "핵심 영역 (Core Areas, CA)",
    "Learning Flow": "학습 흐름 (Learning Flow, LF)",
    "Study Plan": "학습 계획 (Study Plan, SP)",
    "Fast Track": "단기 집중 과정 (Fast Track, FT)",
    "Final Checklist": "최종 점검표 (Final Checklist, FC)",
    "Confusion Matrix": "혼동 개념 비교표 (Confusion Matrix, CM)",
    "Exam Day Strategy": "시험 당일 전략 (Exam Day Strategy, EDS)",
    "Project Rubric": "프로젝트 평가 기준 (Project Rubric, PR)",
    "Evidence Checklist": "증빙 점검표 (Evidence Checklist, EC)",
    "Error Log": "오류 기록 (Error Log, EL)",
    "Retry Queue": "재도전 대기열 (Retry Queue, RQ)",
    "Daily Tracker": "일일 추적 (Daily Tracker, DT)",
    "Score Log": "점수 기록 (Score Log, SL)",
    "Study Session": "학습 세션 (Study Session, SS)",
    "Final Capstone": "최종 종합 프로젝트 (Final Capstone, FCAP)",
    "Portfolio Map": "포트폴리오 맵 (Portfolio Map, PM)",
    "Evidence Matrix": "증빙 매트릭스 (Evidence Matrix, EM)",
    "Environment": "환경 (Environment, ENV)",
    "Troubleshooting": "문제 해결 (Troubleshooting, TS)",
}

AREA_LINES = {
    "010 Overview": "010 개요 (Overview, OVW)",
    "020 Terms": "020 용어 (Terms, TRM)",
    "030 Concepts": "030 개념 (Concepts, CPT)",
    "040 Official Docs": "040 공식 문서 (Official Docs, ODC)",
    "050 Guides": "050 가이드 (Guides, GDE)",
    "060 Labs": "060 실습 (Labs, LAB)",
    "070 Exercises": "070 연습문제 (Exercises, EXR)",
    "080 Question Bank": "080 문제은행 (Question Bank, QB)",
    "090 Final Review": "090 최종 복습 (Final Review, FR)",
    "100 Projects": "100 프로젝트 (Projects, PRJ)",
    "110 Mock Exams": "110 모의고사 (Mock Exams, ME)",
    "120 Wrong Answers": "120 오답 관리 (Wrong Answers, WA)",
    "130 Progress": "130 진행 현황 (Progress, PRG)",
    "140 Resources": "140 자료 (Resources, RES)",
    "150 Evidence": "150 증빙 (Evidence, EVD)",
}

TABLE_CELL_MAP = {
    "Content Status": "콘텐츠 상태 (Content Status, CS)",
    "Learning Status": "학습 상태 (Learning Status, LS)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Mock Exam": "모의고사 (Mock Exam, ME)",
    "Final Mock": "최종 모의고사 (Final Mock, FM)",
    "Evidence": "증빙 (Evidence, EVD)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Labs": "실습 (Labs, LAB)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Final Capstone": "최종 종합 프로젝트 (Final Capstone, FCAP)",
}

COURSES = {
    "GitHub Foundations": ("GitHub 기초", "GHF", "GH-900"),
    "GitHub Actions": ("GitHub 액션", "GHACT", "GH-200"),
    "GitHub Copilot": ("GitHub 코파일럿", "GHCOP", "GH-300"),
    "GitHub Administration": ("GitHub 관리", "GHADM", "GH-100"),
    "GitHub Advanced Security": ("GitHub 고급 보안", "GHAS", "GH-500"),
    "GitHub Agentic AI Developer": ("GitHub 에이전틱 AI 개발자", "GHAI", "GH-600"),
}

SUFFIX_MAP = {
    "Overview": "개요 (Overview, OVW)",
    "Terms": "용어 (Terms, TRM)",
    "Concepts": "개념 (Concepts, CPT)",
    "Official Docs": "공식 문서 (Official Docs, ODC)",
    "Guides": "가이드 (Guides, GDE)",
    "Labs": "실습 (Labs, LAB)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Final Review": "최종 복습 (Final Review, FR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Wrong Answers": "오답 관리 (Wrong Answers, WA)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Evidence": "증빙 (Evidence, EVD)",
}

# English-only headings that should remain exact because they are code/product/UI identifiers.
ALLOW_HEADINGS = {
    "README",
    "YAML",
    "JSON",
    "Git",
    "GitHub",
    "CodeQL",
    "Dependabot",
    "SARIF",
    "OIDC",
    "MCP",
    "RBAC",
    "SAML",
    "SCIM",
    "SSO",
    "SBOM",
}


def normalize_heading(line: str) -> str:
    m = re.match(r"^(#{1,6}\s+)(.*?)(\s*)$", line)
    if not m:
        return line
    prefix, body, suffix = m.groups()

    if body in HEADING_MAP:
        return f"{prefix}{HEADING_MAP[body]}{suffix}"

    # Translate official course names while preserving their official English names.
    for english, (korean, abbr, exam) in COURSES.items():
        if english in body and korean not in body:
            body = body.replace(english, f"{korean} ({english}, {abbr} / {exam})")

    # Translate standardized area suffixes used after an em dash or hyphen.
    for english, bilingual in SUFFIX_MAP.items():
        body = re.sub(
            rf"(\s+[—-]\s+){re.escape(english)}$",
            lambda m: f"{m.group(1)}{bilingual}",
            body,
        )

    return f"{prefix}{body}{suffix}"


def normalize_table_cells(line: str) -> str:
    if "|" not in line:
        return line
    parts = line.split("|")
    for i, part in enumerate(parts):
        stripped = part.strip()
        if stripped in TABLE_CELL_MAP:
            left = part[: len(part) - len(part.lstrip())]
            right = part[len(part.rstrip()) :]
            parts[i] = f"{left}{TABLE_CELL_MAP[stripped]}{right}"
        elif stripped in COURSES:
            korean, abbr, exam = COURSES[stripped]
            left = part[: len(part) - len(part.lstrip())]
            right = part[len(part.rstrip()) :]
            parts[i] = f"{left}{korean} ({stripped}, {abbr} / {exam}){right}"
    return "|".join(parts)


def normalize_labels(line: str) -> str:
    # Common bold/plain labels at the start of a line.
    replacements = {
        "Content Status": "콘텐츠 상태 (Content Status, CS)",
        "Learning Status": "학습 상태 (Learning Status, LS)",
        "Quick Start": "빠른 시작 (Quick Start, QS)",
        "Exam Gate": "시험 통과 기준 (Exam Gate, EG)",
        "Final Mock": "최종 모의고사 (Final Mock, FM)",
    }
    for english, bilingual in replacements.items():
        patterns = [
            (rf"^(\s*[-*>]?\s*)\*\*{re.escape(english)}\*\*(\s*[:：])", rf"\1**{bilingual}**\2"),
            (rf"^(\s*[-*>]?\s*){re.escape(english)}(\s*[:：])", rf"\1{bilingual}\2"),
        ]
        for pattern, repl in patterns:
            line = re.sub(pattern, repl, line)
    return line


def normalize_markdown(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        line = normalize_heading(line)
        if line.strip() in AREA_LINES:
            indent = line[: len(line) - len(line.lstrip())]
            line = indent + AREA_LINES[line.strip()]
        line = normalize_table_cells(line)
        line = normalize_labels(line)
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def english_only_headings(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not m:
            continue
        body = re.sub(r"[`*_]", "", m.group(1)).strip()
        if body in ALLOW_HEADINGS:
            continue
        has_hangul = bool(re.search(r"[가-힣]", body))
        has_latin = bool(re.search(r"[A-Za-z]", body))
        if has_latin and not has_hangul:
            findings.append(f"- `{path.relative_to(ROOT)}` L{lineno}: `{body}`")
    return findings


def main() -> None:
    changed: list[Path] = []
    audit: list[str] = []

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name == "061-language-audit.md":
            continue
        original = path.read_text(encoding="utf-8")
        normalized = normalize_markdown(original)
        if normalized != original:
            path.write_text(normalized, encoding="utf-8")
            changed.append(path)
        audit.extend(english_only_headings(path, normalized))

    audit_path = ROOT / "000-start-here" / "061-language-audit.md"
    audit_body = [
        "# 한글·영어·약어 표기 점검 (Korean-English-Abbreviation Audit, KEAA)",
        "",
        "이 문서는 `scripts/normalize-language-notation.py`가 Repository 전체 Markdown 제목을 점검하여 자동 생성합니다.",
        "",
        "## 점검 결과 (Audit Result, AR)",
        "",
    ]
    if audit:
        audit_body.extend([
            f"추가 검토가 필요한 영어 단독 제목: **{len(audit)}개**",
            "",
            "아래 항목은 공식 제품명·코드명인지, 한글·영어·약어 병기가 필요한 학습 제목인지 사람이 최종 확인합니다.",
            "",
            *audit,
        ])
    else:
        audit_body.append("영어만으로 작성된 일반 학습 제목을 발견하지 않았습니다. **PASS**")
    audit_body.extend([
        "",
        "## 적용 기준 (Applied Standard, AS)",
        "",
        "- 기준 문서: `000-start-here/060-language-notation-standard.md`",
        "- 표기 형식: `한글 (English Full Name, ABBR)`",
        "- 명령어·코드·경로·URL·YAML/JSON 키는 번역하지 않음",
        "",
    ])
    new_audit = "\n".join(audit_body)
    old_audit = audit_path.read_text(encoding="utf-8") if audit_path.exists() else ""
    if new_audit != old_audit:
        audit_path.write_text(new_audit, encoding="utf-8")
        changed.append(audit_path)

    print(f"Changed Markdown files: {len(changed)}")
    print(f"Remaining English-only headings: {len(audit)}")
    for path in changed:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
