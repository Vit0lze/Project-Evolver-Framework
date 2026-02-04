---
name: project-evolver-mapper
description: Systematic codebase mapping for evolution using an incremental 'Bite and Blow' strategy. Use when the user wants to understand, refactor, or evolve a complex codebase that exceeds context limits, or when requested to map a project for future work.
---

# Project Evolver Mapper

This skill enables systematic mapping of complex codebases to prepare for future evolution. It uses an incremental strategy to digest large projects and produces a high-density global map.

## 1. Proactive Vision Interview (The "Why")

**Goal**: Deduce or extract the 'Project Purpose' before mapping.

1.  **Deduce**: Briefly scan root files (README, package.json, main entry) to guess the project's core purpose.
2.  **Ask**: Present this deduction to the user.
    > "I see this appears to be a [Project Type] aiming to [Goal]. Is this accurate? What is your primary evolution goal (e.g., refactor, feature add, rewrite)?"
3.  **Validate**: Do not proceed to deep mapping until the user confirms the vision.

## 2. Chained Mapping Workflow

Execute this loop to map the codebase.

### Phase A: Scan & Strategy
1.  List all files.
2.  Identify large files (>30k tokens) that need splitting.
3.  Plan the mapping order (typically Core -> Utils -> Features).

### Phase B: Chunk & Draft ("Bite")
For each file (or chunk):
1.  **Split** using `scripts/chunk_reader.py` if the file is too large.
    ```bash
    python scripts/chunk_reader.py path/to/large_file.py --size 30000
    ```
2.  **Analyze** the chunk. Load `references/mapping-patterns.md` for templates.
3.  **Draft** a momentary map in `drafts/`.
    - Create `drafts/MAP_[filename].md`.
    - Extract: Logic Anchors, Dependencies, Breaking Points.

### Phase C: Synthesize ("Blow")
1.  **Combine** all draft maps into a single `GLOBAL_MAP.md` in the root (or `brain/` folder if in agentic mode).
2.  **Format**: strict Markdown.
3.  **Language**: All output MUST be in **English**.

## 3. Output Requirements

- **Drafts**: Temporary, verbose analysis stored in `drafts/`.
- **GLOBAL_MAP.md**: The final deliverable. High density, low fluff.
- **Glossary**: Include a glossary of domain terms found in the code.

## 4. Constraint Checklist

- [ ] "Context Safety First": Never read entire large repos at once.
- [ ] "English Only": Analysis must be in English.
- [ ] "Evolution Ready": Focus on *changeability* (coupling, cohesion), not just description.
