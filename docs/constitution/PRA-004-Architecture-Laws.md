# PRA-004

# PersonaDNA Architecture Laws

| Field | Value |
|-------|-------|
| Document ID | PRA-004 |
| Category | Constitution |
| Title | Architecture Laws |
| Version | 0.1.0-alpha |
| Status | Immutable |
| Milestone | M1 – Reference Architecture |
| Owner | PersonaDNA Architecture |
| Depends On | PRA-000, PRA-001, PRA-002, PRA-003 |
| Last Updated | 2026-08-03 |

---

# 1. Purpose

This document establishes the mandatory architectural laws governing the
design, implementation and evolution of the PersonaDNA platform.

These laws apply to every engine, module, API, knowledge model and future
application built upon PersonaDNA.

---

# Law 1 — Understand Before Generate

No engine shall generate personalized output before sufficient understanding
has been established.

Generation is always the final stage of the intelligence pipeline.

---

# Law 2 — Single Responsibility

Each engine owns one primary responsibility.

Responsibilities shall never overlap without explicit architectural approval.

---

# Law 3 — Modular Independence

Every engine shall remain independently maintainable, testable and
replaceable.

Internal implementation shall not affect external behaviour.

---

# Law 4 — Defined Interfaces

Communication between engines shall occur only through defined interfaces.

Hidden dependencies are prohibited.

---

# Law 5 — Evidence Preservation

Meaningful observations shall retain their supporting evidence.

Evidence must remain distinguishable from interpretation.

---

# Law 6 — Explainable Intelligence

Whenever practical, PersonaDNA shall preserve sufficient information to
explain how important conclusions were reached.

---

# Law 7 — Version Compatibility

Architecture shall evolve without unnecessarily breaking existing engines,
knowledge models or applications.

Breaking changes require a major version.

---

# Law 8 — Platform Before Application

Reusable intelligence belongs inside PersonaDNA.

Application-specific behaviour belongs inside consuming applications.

---

# Law 9 — Knowledge Before Memory

Knowledge represents understanding.

Memory represents storage.

Memory shall never replace understanding.

---

# Law 10 — Identity Is Evolutionary

Persona models shall evolve over time.

Historical understanding shall be preserved whenever practical.

---

# Law 11 — Relationships Matter

Knowledge objects should remain connected whenever meaningful relationships
exist.

Disconnected knowledge reduces intelligence.

---

# Law 12 — No Circular Ownership

No engine may own another engine.

Engines collaborate.

Ownership remains independent.

---

# Law 13 — Separation of Concerns

Architecture documents define structure.

Source code implements structure.

Applications consume structure.

These responsibilities shall remain separate.

---

# Law 14 — Immutable Constitution

Documents within the Constitution define permanent architectural direction.

Changes require formal review and version updates.

---

# Law 15 — Evolution Through Versioning

Evolutionary documents improve through controlled versioning.

Historical revisions shall remain traceable.

---

# Law 16 — Human Authority

Human decisions always override automated conclusions.

PersonaDNA provides recommendations, not unquestionable truth.

---

# Law 17 — Privacy First

Personal knowledge shall remain under the ownership of the individual.

Access must be intentional and controlled.

---

# Law 18 — Long-Term Maintainability

Architectural decisions shall prioritise maintainability over short-term
implementation convenience.

---

# Law 19 — Architectural Compliance

Every new engine, API, schema and application shall comply with these
Architecture Laws.

Non-compliance requires explicit architectural approval.

---

# References

- PRA-000 — Reference Architecture Index
- PRA-001 — PersonaDNA Vision
- PRA-002 — PersonaDNA Constitution
- PRA-003 — Core Principles

---

# Revision History

| Version | Date | Description |
|----------|------------|------------------------------|
| 0.1.0-alpha | 2026-08-03 | Initial Architecture Laws |
