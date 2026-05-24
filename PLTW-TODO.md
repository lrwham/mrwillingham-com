# PLTW Design and Modeling — Course Setup Plan

Starting **Fall 2026**. This file tracks everything needed to launch the course — both curriculum research and repo infrastructure. Delete or move into an archive note once the course is live.

## What this course is

PLTW Gateway **Design and Modeling** — a Project Lead The Way middle-school engineering unit. Students apply the engineering design process, build technical sketching and measurement skills, learn 3D modeling software, and prototype solutions to design challenges.

## 1. Curriculum research (do first, before any repo work)

- [ ] Pull the official PLTW Design and Modeling unit list and pacing from the PLTW curriculum portal. Confirm sequence — typical structure is design process → sketching/measurement → 3D modeling → prototyping → signature project.
- [ ] Choose signature project(s). Common PLTW Design and Modeling projects:
  - Puzzle Cube / Soma Cube — design and prototype a 5-piece puzzle.
  - Therapeutic Toy — design a toy for a child with a specific disability.
  - Adaptive Utensil / Grip — assistive device design.
- [ ] Confirm 3D modeling software access with school IT. Options (in order of typical PLTW preference): Autodesk Inventor (official PLTW), Onshape (browser-based, free for education), Tinkercad (simplest, free), SketchUp (free for education).
- [ ] Materials inventory:
  - Isometric/grid paper, rulers, calipers (one set per group)
  - Prototype materials: cardboard, foam board, hot glue, dowels, craft sticks
  - If 3D printing is available, filament + slicer access
- [ ] Decide standards framework — see "Standards setup" below.
- [ ] Decide grade level and course length. PLTW Gateway units are usually 9–10 weeks at ~45 minutes/day. Match what's offered at the school.

## 2. Repo infrastructure (after curriculum research is firm)

Use the existing `content/scratch/` and `content/music-technology/` folders as live templates.

- [ ] Pick the course slug. **Recommendation:** `design-modeling` — short, descriptive, matches the single-word convention of `scratch`. Avoid `pltw` alone (Mr. Willingham may add more PLTW units later) and `pltw-design-modeling` (too long for URLs and sidebar).
- [ ] Create `content/design-modeling/` with:
  - [ ] `_index.md` — course root. Start with the summer-break style card grid (cards linking to `description`, `projects` (empty for now), `reference`) until the first daily lesson is ready. Then swap in `{{< this-week >}}`.
  - [ ] `description.md` — course overview, standards reference, late-work policy, materials list, target grade.
  - [ ] `standards.md` — full standards list with anchors matching the lesson `## Standards` linking pattern (see below).
  - [ ] `reference/_index.md` and at least one starter reference (engineering design process steps, sketching conventions, modeling-software cheatsheet).
  - [ ] `projects/_index.md` — empty hub for now, populated as projects emerge.
- [ ] Create `archetypes/design-modeling/index.md` — copy from `archetypes/scratch/index.md` and adjust front-matter defaults (tags default, no `scratchblocks` field).
- [ ] Add menu entry in `hugo.yaml`:
  ```yaml
  - identifier: design-modeling
    name: Design and Modeling
    pageRef: /design-modeling
    weight: 4   # adjust; renumber siblings if needed
  ```
- [ ] Add a card to `content/_index.md` (homepage) under `### Classes`:
  ```markdown
  {{< card link="design-modeling" title="Design and Modeling" subtitle="PLTW Gateway · 6th–8th Grade" >}}
  ```
- [ ] Update `AGENTS.md`:
  - Repo Map — add a `content/design-modeling/` row mirroring the scratch row.
  - Course Context (Quick Reference) — add a section for the new course.

## 3. Standards setup

PLTW courses align to multiple frameworks. Pick one as the primary anchor for in-lesson `## Standards` blocks and document the rest as a crosswalk in `description.md`.

Options:

- **A. PLTW unit codes** (e.g., `PLTW.DM.1.1`). Matches official PLTW materials and student-facing language. Parents and admin may not recognize them on their own.
- **B. ITEEA STEL codes** (Standards for Technological and Engineering Literacy). Nationally recognized engineering framework.
- **C. Georgia engineering / technology standards.** Required if used for state reporting.

**Recommendation:** Lead with PLTW codes in lesson `## Standards` blocks (students see consistent vocabulary with their curriculum), include a crosswalk table to Georgia / ITEEA in `description.md` for stakeholders.

Anchor pattern (mirrors the scratch convention):

```markdown
[**PLTW.DM.1.1**](/design-modeling/description/#pltw-dm-1) — Description here.
```

Anchor format: `#pltw-dm-N` where `N` is the top-level unit group number, lowercased, no dots.

## 4. Pre-launch lessons

Before Day 1:

- [ ] Plan the full 9-week schedule. Each week's `_index.md` follows the same structure as scratch/music-tech: `## Unit: …` block + Weekly Schedule table + optional Graded Assignments alert. Set `weight:` descending (Week 1 = 100, Week 2 = 90, …).
- [ ] Write Week 1's `_index.md` and the Day 1 lesson in full.
- [ ] Have at least 3 daily lessons drafted ahead of where students are — buffer for sub days and pacing surprises.
- [ ] Run `hugo --quiet --renderToMemory` after each batch of edits. Zero output = success.
- [ ] When `content/design-modeling/week-1/day-1/index.md` is live, swap the course root `_index.md` from the summer-style card grid to `## This Week` + `{{< this-week >}}`.

## 5. References

- [AGENTS.md](AGENTS.md) — repo conventions for daily lessons, shortcodes, standards anchors.
- [content/scratch/](content/scratch/) and [content/music-technology/](content/music-technology/) — live course templates.
- [content/archive/2025-26/](content/archive/2025-26/_index.md) — examples of completed weekly schedules and daily lessons.
- [archetypes/scratch/index.md](archetypes/scratch/index.md) — daily lesson skeleton to copy.
