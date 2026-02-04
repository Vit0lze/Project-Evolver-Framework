---
name: project-field-explorer
description: Unrestricted deep-dive research into codebase flaws identified in a Global Map. Use when the user wants to investigate 'Breaking Points', plan complex refactors, or prepare a fail-proof execution plan (Connective Handshake) for a future Injector skill.
---

# Project Field Explorer

This skill performs a constant, deep-dive research into every structural flaw identifying in `GLOBAL_MAP.md`. It prepares a fail-proof execution plan for future injection.

## 1. Trigger & Setup

**Trigger**: "Use the project-field-explorer skill to investigate the Breaking Points identified in the Global Map."

**Data Retrieval**:
1.  Autonomously locate `GLOBAL_MAP.md` in the workspace root or `brain/` folder.
2.  Read the **Vision** section of the map.
3.  **Vision Alignment**: Ensure all research prioritizes the stated Project Purpose and Evolution Goal.

## 2. Deep-Dive Execution Logic

For **EACH** Breaking Point identified in the Map, perform the following unrestricted analysis:

1.  **Inspect Code**: Read the actual source code around the reported `BREAK` point.
2.  **Extract Golden Rules**: Identify the hidden business logic that *must* remain invariant.
    > "What business value is this messy code actually providing?"
3.  **Blast Radius**: Trace references to determine exactly which files will break if this changes.
4.  **Architectural Fit**: Consult `references/architectural-solutions.md` to select the best pattern (SOLID, Design Patterns) for the fix.

## 3. Connective Handshake

For every breaking point, generate a **Connective Handshake**:

1.  **Solution ID**: Assign a unique ID (e.g., `SOL-AUTH-01`).
2.  **External Dependencies**: Explicitly check and list if new libraries (npm, pip) are needed.
3.  **Target Manifest**: List every file path that the future 'Injector' skill will need to modify.

## 4. Output

Generate a report using `assets/templates/FIELD_RESEARCH_REPORT.md` for each major issue (or consolidated for related issues).

**Constraint Checklist**:
- [ ] **No Limits**: Deep dive until clarity is absolute.
- [ ] **Explicit Deps**: Never assume libraries exist. Check them.
- [ ] **English Only**: All reports must be in English.
