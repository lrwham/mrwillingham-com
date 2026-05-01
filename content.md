# Content Guidelines

Standards and conventions for all lesson content on this site. Follow these rules when creating or updating any page.

---

## Daily Lesson Files (`index.md`)

Each day lives in `content/<course>/week-N/day-N/index.md` (use `_index.md` only if the day has sub-pages).

### Front Matter

```yaml
---
title: "Day N: Lesson Title"
date: YYYY-MM-DDTHH:MM:SS-04:00
description: "One-sentence summary of what students do."
day_number: N
units:
  - "Unit Name"
standards:
  - MSMTC8.CR.1        # music tech
  - CSGPS.K12.CS.1     # scratch
tags:
  - GarageBand
  - MIDI
resources:
  - "GarageBand"
  - "Hooktheory"
draft: false
toc: true
weight: N
---
```

- `title` — "Day N: Title" format, matching the day-N link text used in the week's `_index.md` table exactly.
- `description` — mirrors the one-sentence summary in the weekly schedule table; written in active voice from the student's perspective.
- `weight` — controls sort order within the week; do not change without updating sibling weights.
- `resources` — tools students use (e.g. `"GarageBand"`, `"MuseScore"`, `"Hooktheory"`); used by taxonomy pages.
- `standards` — one or more standard codes that the lesson addresses; must appear in the `## Standards` section at the bottom of the page.

### Page Structure

Every daily lesson must follow this section order:

```
{{< icon "calendar" >}} **Day of week, Month Dayth, Year**

{{% objectives %}}
## Objectives
- I can ...
{{% /objectives %}}

{{% warmup %}}
## Warmup — Title
...
{{% checkpoint %}}
### Checkpoint: Warmup
- [ ] ...
{{% /checkpoint %}}
{{% /warmup %}}

{{% worksession %}}
## Work Session — Title
...
{{% checkpoint %}}
### Checkpoint: Work Session
- [ ] ...
{{% /checkpoint %}}
{{% /worksession %}}

{{% closing %}}
## Closing
...
{{% /closing %}}

## Standards
- [**CODE**](/course/description/#anchor) — Description (parenthetical ties to today's activity).
```

**Rules:**
- Every lesson has exactly one `objectives`, one `warmup`, one `closing`, and at least one `worksession` block.
- Every `warmup` and `worksession` block ends with a `checkpoint` block.
- Use `{{% %}}` delimiters for shortcodes that contain markdown (`objectives`, `warmup`, `worksession`, `checkpoint`, `closing`, `alert`, `steps`).
- Use `{{< >}}` delimiters for shortcodes that do not contain markdown (`callout`, `button`, `icon`, `tabs`, `tab`, `clever`).
- The `## Standards` section is always the last thing in the file, outside all shortcode blocks.

### Key Vocabulary

Include a `### Key Vocabulary` subsection at the top of the `worksession` block when the lesson introduces new terms. Use definition-list syntax:

```markdown
**Term**
: Definition.
```

## Weekly Landing Pages (`_index.md`)

Each week's folder requires an `_index.md` (branch bundle) with the following structure. Do not use `index.md` for week-level pages.

### Front Matter

```yaml
---
title: "Week N: Unit or Topic Name"
draft: false
toc: false
cascade:
  type: docs
weight: N   # descending — later weeks have lower weight
---
```

- The `weight` field should be highest for Week 1 and decrease each week (e.g. Week 1 = 100, Week 2 = 90, etc.) to ensure correct sort order as the week's appear. The oldest week — week 1 — should appear last.
- `toc: false` — the landing page has no in-page table of contents.

### Page Structure

```
## Unit: Unit Name

2–4 sentence paragraph describing what students do and learn this week, written
in plain student-facing language. If the week spans two units, use two
## Unit: blocks, each with its own paragraph.

## Weekly Schedule

| Day | Date     | Topic                          | Summary                              |
| --- | -------- | ------------------------------ | ------------------------------------ |
| N   | Mon M/D  | [Exact Lesson Title](day-N/)   | One active-voice sentence.           |

{{% alert "Graded Assignments" %}}

- **Assignment Name** (due Date) — Description.

Late work will receive a one-time 20 point deduction.

{{% /alert %}}

## Week N+1 Preview        ← week 1 of each course only

One paragraph previewing next week.
```

**Rules:**
- Topic link text must match the lesson's `title:` field exactly (minus the "Day N: " prefix is acceptable, but exact match is preferred).
- Summaries are one sentence, active voice, specific — describe what students *do*, not what the lesson *is about*.
- The `{{% alert "Graded Assignments" %}}` block is included only when real graded items exist. Remove `TBD` placeholders entirely rather than leaving them in.
- `## Week N+1 Preview` appears only in the first week of each course (Music Tech Week 1, Scratch Week 1). Do not add preview sections to any other week.
- No other sections, callouts, or content beyond these elements.