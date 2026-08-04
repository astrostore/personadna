# PRA-101

# PersonaDNA Layered Architecture

| Field | Value |
|-------|-------|
| Document ID | PRA-101 |
| Category | Architecture |
| Title | Layered Architecture |
| Version | 0.1.0-alpha |
| Status | Evolutionary |
| Milestone | M2 – Architecture |
| Owner | PersonaDNA Architecture |
| Depends On | PRA-100 |
| Last Updated | 2026-08-04 |

---

# 1. Purpose

This document defines the logical layering of the PersonaDNA platform.

The layered architecture separates responsibilities, minimises coupling,
and allows every intelligence engine to evolve independently while
maintaining platform integrity.

---

# 2. Architecture Overview

```
┌──────────────────────────────────────────────┐
│              Layer 7 : Applications          │
├──────────────────────────────────────────────┤
│              Layer 6 : Public APIs           │
├──────────────────────────────────────────────┤
│         Layer 5 : Intelligence Engines       │
├──────────────────────────────────────────────┤
│         Layer 4 : Knowledge Models           │
├──────────────────────────────────────────────┤
│        Layer 3 : Processing Pipeline         │
├──────────────────────────────────────────────┤
│       Layer 2 : Storage & Memory             │
├──────────────────────────────────────────────┤
│     Layer 1 : Core Platform Services         │
└──────────────────────────────────────────────┘
```

---

# 3. Layer Responsibilities

## Layer 1 — Core Platform Services

Provides platform-wide infrastructure.

Responsibilities:

- Configuration
- Logging
- Security
- Metadata
- Version management
- Platform utilities

Owns:

- Platform configuration
- System metadata

Never owns:

- Persona logic
- Knowledge processing

---

## Layer 2 — Storage & Memory

Responsible for persistence.

Stores:

- Personas
- Documents
- Memories
- Knowledge Objects
- Relationships
- Configuration

Never performs reasoning.

---

## Layer 3 — Processing Pipeline

Coordinates information flow.

Responsibilities:

- Input processing
- Validation
- Normalisation
- Routing
- Pipeline orchestration

Acts as the bridge between storage and intelligence.

---

## Layer 4 — Knowledge Models

Defines platform structures.

Contains:

- Persona Model
- Knowledge Object Model
- Relationship Model
- Memory Model
- Growth Model

Contains structure only.

Contains no processing logic.

---

## Layer 5 — Intelligence Engines

Performs cognitive work.

Examples:

- Identity Engine
- OCR Engine
- WritingDNA Engine
- ThinkingDNA Engine
- Meaning Engine
- Persona Engine
- Reflection Engine
- Generation Engine

Every engine owns one capability.

---

## Layer 6 — Public APIs

Provides external access.

Responsibilities:

- REST APIs
- SDK interfaces
- Authentication
- Version compatibility
- Request validation

---

## Layer 7 — Applications

Applications consume PersonaDNA.

Examples:

- SIA
- Shilpkar
- SwingLab
- AptiQuiz

Applications never bypass platform APIs.

---

# 4. Dependency Rules

Layers communicate downward only.

Allowed:

Application
→ API
→ Engine
→ Knowledge Model
→ Storage

Forbidden:

Storage
→ Application

Knowledge Model
→ API

Engine
→ User Interface

---

# 5. Design Principles

Every layer shall:

- Have a single responsibility.
- Minimise dependencies.
- Hide implementation details.
- Expose stable interfaces.
- Remain independently maintainable.

---

# 6. Benefits

This architecture provides:

- Modular development
- Independent testing
- Replaceable engines
- Reusable components
- Easier maintenance
- Long-term scalability

---

# 7. References

- PRA-100 — System Overview

---

# 8. Revision History

| Version | Date | Description |
|----------|------------|------------------------------|
| 0.1.0-alpha | 2026-08-04 | Initial Layered Architecture |
