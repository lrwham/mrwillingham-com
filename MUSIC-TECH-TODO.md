# Music Technology — New Year Setup

Use this checklist each time the Music Technology course launches for a new school year. It assumes the course infrastructure (description, standards, reference, projects, archetype) is already in place — this is just the work to bring `/music-technology/` back online from summer-break mode.

## 1. Plan the schedule

- [ ] Map 9 weeks against the school calendar. Note holidays, planning days, testing windows, early-release days.
- [ ] Decide which units to keep, drop, or reorder. Last year's structure (from [content/archive/2025-26/music-technology/](content/archive/2025-26/music-technology/_index.md)):
  - Weeks 1–3 — **Podcasts** (wave science, mic setup, scripting, recording, editing, distribution)
  - Week 4 — **Beat Making**
  - Week 5 — **Music Reading**
  - Week 6 — **Musical Form & Melody Writing**
  - Week 7 — **Remixing**
  - Weeks 7–8 — **Film Scoring**
  - Week 9 — **End of Year**
- [ ] For each unit, note standards (MSMTC8.CR / PR / RE / CN), tools (GarageBand, Soundtrap, MIDI controllers, etc.), and major assessments.
- [ ] Decide which reusable projects from [content/music-technology/projects/](content/music-technology/projects/_index.md) to drop in:
  - [ ] [Classical Remix](content/music-technology/projects/classical-remix/_index.md) — 3-day project
  - [ ] [Film Scoring](content/music-technology/projects/film-scoring/_index.md) — 5–7-day capstone

## 2. Carry-over assets to verify

Before writing new lessons, confirm the year-agnostic content is still current:

- [ ] [content/music-technology/description.md](content/music-technology/description.md) — standards, late-work policy, materials list.
- [ ] [content/music-technology/reference/podcast-vocab.md](content/music-technology/reference/podcast-vocab.md) — vocabulary still matches what you'll teach.
- [ ] [content/music-technology/projects/](content/music-technology/projects/_index.md) — extracted project guides still reflect current tools (e.g., GarageBand version still right).

## 3. Create week folders

For each of the 9 weeks:

- [ ] `content/music-technology/week-N/_index.md` — weekly landing with `## Unit: …` block + Weekly Schedule table + optional `{{% alert "Graded Assignments" %}}` block.
- [ ] Set `weight:` descending (Week 1 = 100, Week 2 = 90, …). See [AGENTS.md → Weekly Landing Pages](AGENTS.md).
- [ ] Add `cascade.type: docs` so child pages inherit the docs layout.

## 4. Write daily lessons

For each day:

- [ ] Create `content/music-technology/week-N/day-N/index.md` using the archetype:
  ```
  hugo new --kind music-technology content/music-technology/week-1/day-1/index.md
  ```
- [ ] Confirm `day_number:` is strictly increasing across the entire course (don't reset per week).
- [ ] Confirm `units`, `tags`, `resources` casing matches existing taxonomy values exactly — these are case-sensitive and a typo creates an orphan term page.
- [ ] Run `hugo --quiet --renderToMemory` after each batch — zero output = success.

## 5. Reactivate the course root landing page

Once `content/music-technology/week-1/day-1/index.md` exists and renders:

- [ ] Edit [content/music-technology/_index.md](content/music-technology/_index.md) — replace the "On Summer Break" card grid with:
  ```markdown
  6th–8th Grade Music Technology

  ## This Week

  {{< this-week >}}
  ```
- [ ] Optionally keep a smaller card row below `{{< this-week >}}` linking to projects, reference, and the most recent archive year — author's preference.

## 6. Update the homepage

- [ ] If you want quarter or semester labeling (e.g., "Q1 - Music Technology"), edit the card title in [content/_index.md](content/_index.md). The default is year-agnostic.
- [ ] When the **previous** school year has been fully archived, add a card to "Past Years & Reference" pointing at the new archive folder (e.g., `archive/2026-27/`).

## 7. During the year

- [ ] Use [weekly-checklist.md](weekly-checklist.md) as a per-week site-audit checklist.
- [ ] Note any standout lessons or projects that should be promoted to the reusable library at end-of-year cleanup.

## 8. End-of-year wrap

When the year is done:

- [ ] `git mv content/music-technology/week-* content/archive/<YYYY-YY>/music-technology/`
- [ ] Move any year-specific project hubs and sub-plans into the archive too.
- [ ] Create a static archive `_index.md` listing the year's weeks. Template: [content/archive/2025-26/music-technology/_index.md](content/archive/2025-26/music-technology/_index.md).
- [ ] Reset [content/music-technology/_index.md](content/music-technology/_index.md) to the summer-break card grid.
- [ ] Extract any new standout projects / lessons into [content/music-technology/projects/](content/music-technology/projects/_index.md). Strip dates, day numbers, and year-specific references — see [AGENTS.md → Archive & Reusable Projects](AGENTS.md).

## References

- [AGENTS.md](AGENTS.md) — full repo conventions.
- [content/archive/2025-26/music-technology/](content/archive/2025-26/music-technology/_index.md) — last year as a model.
- [content/music-technology/projects/](content/music-technology/projects/_index.md) — reusable lessons available now.
