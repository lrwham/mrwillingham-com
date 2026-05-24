# Computer Programming with Scratch — New Year Setup

Use this checklist each time the Scratch course launches for a new school year. It assumes the course infrastructure (description, standards, reference, projects, archetype) is already in place — this is just the work to bring `/scratch/` back online from summer-break mode.

## 1. Plan the schedule

- [ ] Map 9 weeks against the school calendar. Note holidays, planning days, testing windows, early-release days.
- [ ] Decide which units to keep, drop, or reorder. Last year's structure (from [content/archive/2025-26/scratch/](content/archive/2025-26/scratch/_index.md)):
  - Week 1 — **Introduction to Scratch** (interface, sequencing, events, motion, sprite art)
  - Week 2 — **Conditionals & Control Flow** (user input, loops, flow diagrams)
  - Week 3 — **Boolean Operators & Gravity** (and/or/not, velocity, platformer)
  - Week 4 — **Review & Clones**
  - Weeks 5–6 — **Video Game Design Project** (capstone)
  - Week 7 — **Python and the Terminal**
  - Week 8 — **Hackers and AI** (including Teachable Machine ML lesson)
  - Week 9 — **End of Year**
- [ ] For each unit, note standards (MS-CS-FCP.1–6), tools (Scratch, Code.org, Flocabulary, Teachable Machine, etc.), and major assessments.
- [ ] Decide which reusable projects from [content/scratch/projects/](content/scratch/projects/_index.md) to drop in:
  - [ ] [Video Game Design Project](content/scratch/projects/video-game-design/_index.md) — 2 weeks (10 days)
  - [ ] [Platforms & Collision](content/scratch/projects/platformer-collision/index.md) — 1-day lesson (drop into a platformer week)
  - [ ] [Teachable Machine RPS](content/scratch/projects/teachable-machine-rock-paper-scissors/index.md) — 1-day showcase lesson (great fit for an AI unit)

## 2. Carry-over assets to verify

Before writing new lessons, confirm the year-agnostic content is still current:

- [ ] [content/scratch/description.md](content/scratch/description.md) — standards, late-work policy, materials list.
- [ ] [content/scratch/standards.md](content/scratch/standards.md) — MS-CS-FCP standards still match what Georgia is publishing.
- [ ] [content/scratch/reference/](content/scratch/reference/) — unit vocabulary lists still match what you'll teach.
- [ ] [content/scratch/projects/](content/scratch/projects/_index.md) — extracted projects still reflect current Scratch UI, current Teachable Machine URL, etc.

## 3. Create week folders

For each of the 9 weeks:

- [ ] `content/scratch/week-N/_index.md` — weekly landing with `## Unit: …` block + Weekly Schedule table + optional `{{% alert "Graded Assignments" %}}` block.
- [ ] Set `weight:` descending (Week 1 = 100, Week 2 = 90, …). See [AGENTS.md → Weekly Landing Pages](AGENTS.md).
- [ ] Add `cascade.type: docs` so child pages inherit the docs layout.

## 4. Write daily lessons

For each day:

- [ ] Create `content/scratch/week-N/day-N/index.md` using the archetype:
  ```
  hugo new --kind scratch content/scratch/week-1/day-1/index.md
  ```
- [ ] If the lesson uses ```` ```scratch ```` fenced code blocks (block diagrams), set `scratchblocks: true` in front-matter.
- [ ] Confirm `day_number:` is strictly increasing across the entire course (don't reset per week).
- [ ] Confirm `units`, `tags`, `resources` casing matches existing taxonomy values exactly — case-sensitive.
- [ ] Run `hugo --quiet --renderToMemory` after each batch — zero output = success.

## 5. Reactivate the course root landing page

Once `content/scratch/week-1/day-1/index.md` exists and renders:

- [ ] Edit [content/scratch/_index.md](content/scratch/_index.md) — replace the "On Summer Break" card grid with:
  ```markdown
  6th–8th Grade Computer Programming with Scratch

  ## This Week

  {{< this-week >}}
  ```
- [ ] Optionally keep a smaller card row below `{{< this-week >}}` linking to projects, reference, and the most recent archive year — author's preference.

## 6. Update the homepage

- [ ] If you want quarter or semester labeling (e.g., "Q1 - Programming with Scratch"), edit the card title in [content/_index.md](content/_index.md). The default is year-agnostic.
- [ ] When the **previous** school year has been fully archived, add a card to "Past Years & Reference" pointing at the new archive folder (e.g., `archive/2026-27/`).

## 7. During the year

- [ ] Use [weekly-checklist.md](weekly-checklist.md) as a per-week site-audit checklist.
- [ ] Note any standout lessons that should be promoted to the reusable library at end-of-year cleanup.

## 8. End-of-year wrap

When the year is done:

- [ ] `git mv content/scratch/week-* content/archive/<YYYY-YY>/scratch/`
- [ ] Move any year-specific project hubs into the archive too (e.g., a dated `video-game-design-project/` folder).
- [ ] Create a static archive `_index.md` listing the year's weeks. Template: [content/archive/2025-26/scratch/_index.md](content/archive/2025-26/scratch/_index.md).
- [ ] Reset [content/scratch/_index.md](content/scratch/_index.md) to the summer-break card grid.
- [ ] Extract any new standout projects / lessons into [content/scratch/projects/](content/scratch/projects/_index.md). Strip dates, day numbers, year-specific references ("yesterday's project", etc.) — see [AGENTS.md → Archive & Reusable Projects](AGENTS.md).

## References

- [AGENTS.md](AGENTS.md) — full repo conventions.
- [content/archive/2025-26/scratch/](content/archive/2025-26/scratch/_index.md) — last year as a model.
- [content/scratch/projects/](content/scratch/projects/_index.md) — reusable lessons available now.
