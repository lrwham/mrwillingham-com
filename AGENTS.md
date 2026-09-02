# AGENTS.md — mrwillingham.com

Operational reference for AI coding agents working in this repository. Human-facing documentation lives in `readme.md`, `content.md`, `technical.md`, `coding-scratch.md`, and `music-tech.md`. This file inlines everything an agent needs for routine work — do not assume a human will read it.

---

## Project Summary

Hugo static site for a middle-school teacher's classes. Live for 2026-27: **PLTW Design and Modeling** (Georgia MS-ENGR-II standards) and **Music Technology** (Georgia MSMTC8 standards). **Computer Programming with Scratch** (Georgia MS-CS-FCP standards) is no longer taught; its `content/scratch/` section stays on disk but is unlinked from the menu and homepage. The site uses the [Hextra](https://github.com/imfing/hextra) theme via a Git submodule. Lesson content lives in `content/<course>/week-N/day-NN/index.md`, organized by week. GitHub Actions build Hugo in CI and deploy to S3 + CloudFront on push to `main`. There is no staging server — use local `hugo serve` for previewing drafts.

---

## Repo Map

| Path | What it is | Agent should... |
|------|-----------|-----------------|
| `content/` | All lesson and page content (markdown) | Edit freely; this is the main workspace |
| `content/design-modeling/` | PLTW Design and Modeling course (current year) | Edit; current-year daily lessons in `week-N/day-NN/index.md`; date-free reusable lessons in `projects/`; vocab and the design-process reference in `reference/` |
| `content/scratch/` | Scratch programming course (no longer taught; unlinked from nav) | Leave alone unless asked; reusable lessons in `projects/`, vocab in `reference/` |
| `content/music-technology/` | Music technology course (current year) | Edit; same structure; reusable lessons in `projects/`; vocab in `reference/` |
| `content/troubleshooting/` | Student self-help guides | Edit when asked |
| `content/archive/` | Frozen snapshots of past school years (`YYYY-YY/<course>/...`) | **Don't edit existing year folders.** They're frozen as taught. Create a new `YYYY-YY/` folder at end of school year to archive that year — see "Archive & Reusable Projects" below. |
| `archetypes/` | Lesson templates used by `hugo new content` | Read for the canonical skeleton; edit only if templates change |
| `layouts/` | Custom Hugo templates and shortcodes | Edit when changing rendering; do NOT touch `themes/hextra/` |
| `layouts/shortcodes/` | Custom shortcode HTML | Read to understand shortcode behavior; rarely edit |
| `assets/css/custom.css` | Color-coded section styling, dark/light vars | Edit when changing visuals |
| `data/icons.yaml` | Inline SVG defs for custom `{{< icon >}}` names | Add icons here; available names: `scratch`, `clever-login`, `edpuzzle-logo`, `remix` (verify by reading the file before referencing) |
| `data/events.yaml` | Calendar event data | Edit when adding events |
| `static/` | Static files (favicon, banner, downloads, etc.) | Add binary assets here |
| `i18n/` | Internationalization strings | Rarely touched |
| `hugo.yaml` | Site configuration | Edit carefully; controls taxonomies, menu, theme params |
| `readme.md`, `content.md`, `technical.md`, `coding-scratch.md`, `music-tech.md`, `weekly-checklist.md` | Human-facing docs | Read for deeper context; agents should rely on this AGENTS.md first |
| `themes/hextra/` | **OFF-LIMITS** — Git submodule | Never edit. If theme behavior needs changing, override via `layouts/` |
| `public/` | **OFF-LIMITS** — Hugo build output | Never edit; never commit; gitignored |
| `.hugo_build.lock` | **OFF-LIMITS** — build lock file | Never edit; gitignored |
| `.venv/`, `.git/`, `.DS_Store` | System files | Ignore |
| `.github/workflows/` | Deploy automation | Edit only when changing CI |
| `.claude/` | Legacy Claude Code config | Ignore |

---

## Build & Verify Commands

Use these to check work after editing content or templates.

| Command | When to use |
|---------|-------------|
| `hugo --quiet --renderToMemory` | **Canonical verify step.** Full build in memory, no disk write. Silent on success; prints errors only. Run after any content or template edit. |
| `hugo --quiet` | Fast syntax/build check that writes to `public/`. Use when you need to inspect generated HTML. |
| `HUGO_ENV=dev hugo serve --buildFuture --buildDrafts` | Local preview at `http://localhost:1313`. `HUGO_ENV=dev` shows the red DEV ribbon. Future-dated and draft lessons are included. |
| `git submodule update --init --recursive` | Required after a fresh clone, before building. |

After editing a lesson, always run `hugo --quiet --renderToMemory` and confirm zero output before considering the task done. Never commit `public/` or `.hugo_build.lock`.

### Future-dated lessons are invisible in production

Neither `hugo.yaml` nor `.github/workflows/deploy.yml` sets `buildFuture`, so **Hugo's default applies: a lesson dated later than the build time is not rendered at all.** Consequences an agent must not misread as bugs:

- Scaffolding a full week ahead of time is normal, but only the days whose `date:` has already passed appear in `public/` or on the live site. The rest 404 until their date arrives, at which point the next deploy publishes them.
- A weekly schedule table therefore contains links that are legitimately dead in prod. **Do not "fix" these by deleting rows or rewriting links.** Verify with `hugo serve --buildFuture` instead.
- `{{< this-week >}}` anchors on the most recent lesson whose `date` is in the past (falling back from an exact today match), then renders that lesson's `.Parent` week. So a newly scaffolded week does not surface on the course root until at least one of its days has arrived.
- This is the mechanism that reveals lessons to students day by day. It is intentional — leave it alone.

---

## Daily Lesson Files

### Path Rules

- A daily lesson is `content/<course>/week-N/day-NN/index.md` (use `index.md` — singular `_index.md` is reserved for branch bundles).
- `_index.md` is used for week landing pages and for daily lessons that have their own sub-pages.
- `<course>` is `design-modeling` or `music-technology` (`scratch` exists but is no longer taught).
- Day folder is `day-N` (no zero-padding, matching existing convention).
- Past-year lessons live at `content/archive/<YYYY-YY>/<course>/week-N/day-NN/index.md` with the same structure — don't edit them.
- Date-free reusable lesson templates live at `content/<course>/projects/<slug>/index.md` — see "Archive & Reusable Projects" below.

### Required Front Matter

```yaml
---
title: "Day N: Short Lesson Title"
date: 2026-05-15T08:00:00-04:00
description: "One-sentence student-facing summary; mirrors weekly schedule table."
day_number: 40
units:
  - "Unit Name"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.2
tags:
  - Scratch
  - variables
resources:
  - "Scratch"
  - "Teachable Machine"
draft: false
toc: true
scratchblocks: false   # Scratch lessons only; set true to render ```scratch fenced blocks
weight: 5
---
```

**Field rules:**

- `title` — `"Day N: Title"` format. Must match the link text in the week's `_index.md` schedule table exactly.
- `date` — Full ISO timestamp with `-04:00` offset (America/New_York). Bare `YYYY-MM-DD` works for some existing music-tech files but new lessons should use the full form.
- `description` — One sentence, active voice, student perspective. Mirrors the weekly schedule table's Summary column.
- `day_number` — Integer, continuous across the course. Must strictly exceed the previous lesson's `day_number`.
- `units` — List. Exact spelling must match sibling lessons (see "Taxonomy values" below).
- `standards` — Real standard codes (see Standards section below). Each code listed here must also appear in the `## Standards` section at the bottom of the file.
- `tags` — Topical tags. Scratch lessons always include `- Scratch`. Music Tech lessons typically include the primary DAW tag (`- GarageBand`, `- Soundtrap`, etc.). Design and Modeling lessons use TitleCase topic tags (`- Sketching`, `- Multiview`, `- Dimensioning`, `- Statistics`, `- Tinkercad`, `- Quiz Review`).
- `resources` — Tools students will use. Match existing entries (see "Taxonomy values" below). Printed handouts follow the `"Drum Worksheet Packet (printed)"` pattern — lowercase `printed` in parentheses.
- `weight` — Sort order within the week (1–5 for Mon–Fri). Don't change existing values without recalculating siblings.
- `scratchblocks` — Scratch course only. Set `true` to enable ```scratch fenced code blocks.

### Taxonomy values (`units`, `tags`, `resources`)

What actually creates a duplicate term page is **spelling, not casing.** Hugo normalizes case when keying terms, so `Loops` and `loops` collapse into a single `/tags/loops/` page listing both lessons — only the display title differs, decided by whichever page Hugo reads first. Verified behavior, not theory.

- **Real risk: singular vs. plural and reworded variants.** `Podcast` and `Podcasts` are both live `units` terms today, splitting the same unit across two pages. Check for an existing near-match before inventing a value.
- **Casing convention differs by course.** Music Tech and Design and Modeling use TitleCase tags (`Soundtrap`, `Podcast`, `Sketching`, `Dimensioning`); Scratch uses lowercase (`loops`, `variables`, `conditionals`). Match the course you're editing so display titles stay consistent.
- **Design and Modeling `units` values** are the PLTW lesson names: `"Introduction to Design"` (Lesson 1), `"Modeling"` (Lesson 2), `"Design Challenge"` (Lesson 3). Common `resources` values: `"Engineering Notebook"`, `"Linking Cubes"`, `"Dial Caliper"`, `"Ruler"`, `"Tinkercad"`, `"myPLTW"`, `"Excel"`, `"BrainPOP"`.
- **The front-matter key is `units`, plural.** Two files use singular `unit:`, which Hugo ignores entirely — those pages are missing from the taxonomy. Don't copy that pattern.
- To see every existing term, run `hugo --quiet` and list `public/units/`, `public/tags/`, and `public/resources/`.
- An ampersand slugifies to a double dash: `"Loops & Layering"` → `/units/loops--layering/`. Prefer `and` in new term values.

### Required Page Structure

Every daily lesson follows this exact section order:

```markdown
{{< icon "calendar" >}} **Friday, May 15th, 2026**

{{% objectives %}}

## Objectives

- I can describe what training data is.
- I can collect images and train a classifier.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Title Here

Warmup content...

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I did the warmup.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Title Here

Work session content...

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I completed the work session.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Closing content...

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Description here (parenthetical ties to today's activity).
```

**Rules:**

- Exactly one `objectives`, one `warmup`, one `closing`, at least one `worksession`.
- Every `warmup` and `worksession` ends with a `checkpoint` block.
- Calendar-icon line at the top uses long-form date: `Friday, May 15th, 2026`.
- `## Standards` is always the final section, outside all shortcode blocks.
- Place an optional `{{% alert "message" %}}` block at the top (above `{{% objectives %}}`) for announcements, sub plans, or schedule changes.

### Key Vocabulary

When introducing terms in the `worksession`, add a `### Key Vocabulary` subsection using definition-list syntax:

```markdown
### Key Vocabulary

Training Data
: The collection of examples used to teach a machine learning model.

Confidence Score
: A percentage that tells you how sure the model is about its prediction.
```

The blank line between the term and `:` definition matters — Goldmark requires it.

---

## Weekly Landing Pages (`_index.md`)

Each week folder has `_index.md` (branch bundle). Do not use `index.md` for week-level pages.

### Required Front Matter

```yaml
---
title: "Week N: Unit or Topic Name"
draft: false
toc: false
cascade:
  type: docs
weight: 100   # descending — Week 1 has highest weight, later weeks lower
---
```

- `weight` decreases as week number increases (Week 1 = 100, Week 2 = 90, etc.). This makes Week 1 appear last in sidebar ordering, with the newest week first.
- **The 100-based scale above is authoritative for new content.** Past years used a smaller scale (2025-26 Music Tech ran 12→4, Scratch 10→2). Only the *relative order* matters to Hugo, so both work — but don't copy the old numbers when starting a new year, and don't renumber a frozen archive to match.
- `toc: false` because the landing page has no in-page TOC.
- `cascade.type: docs` propagates the docs layout to all child pages.

### Required Page Structure

```markdown
## Unit: Unit Name

Two to four sentence paragraph describing what students do and learn this week,
written in plain student-facing language. If the week spans two units, use two
separate `## Unit:` blocks, each with its own paragraph.

## Weekly Schedule

| Day | Date     | Topic                                | Summary                              |
| --- | -------- | ------------------------------------ | ------------------------------------ |
| 1   | Mon 5/11 | [Exact Lesson Title](day-36/)        | One active-voice sentence summary.   |
| 2   | Tue 5/12 | [Exact Lesson Title](day-37/)        | One active-voice sentence summary.   |

{{% alert "Graded Assignments" %}}

- **Assignment Name** (due Date) — Description.

Late work will receive a one-time 20 point deduction.

{{% /alert %}}

## Week N+1 Preview

One paragraph previewing next week.   ← Week 1 of each course only.
```

**Rules:**

- Topic link text must match the lesson's `title:` field (the "Day N: " prefix may be stripped, but exact match is preferred).
- Summaries are one sentence, active voice, specific — describe what students *do*.
- The `{{% alert "Graded Assignments" %}}` block is included only when real graded items exist. Remove `TBD` placeholders entirely.
- The `## Week N+1 Preview` section appears only in Week 1 of each course.
- No other sections beyond these elements.

---

## Shortcode Reference

All custom shortcodes in `layouts/shortcodes/`. Two delimiter styles exist; use the right one or the markdown inside will not render.

| Shortcode | Delimiter | Paired | Parameters | Purpose |
|-----------|-----------|--------|------------|---------|
| `objectives` | `{{% %}}` | yes | none | "Today's Objectives" section (purple). Inner `## Objectives` header + "I can…" bullets. |
| `warmup` | `{{% %}}` | yes | none | Warmup section (amber). Inner `## Warmup: Title` sets the heading. |
| `worksession` | `{{% %}}` | yes | none | Work session (blue). Inner `## Work Session: Title` sets the heading. May appear multiple times. |
| `checkpoint` | `{{% %}}` | yes | none | Checklist block (red). Inner `### Checkpoint: Title`. Nest inside `warmup` or `worksession`. |
| `closing` | `{{% %}}` | yes | none | Closing wrap-up (green). Inner `## Closing` or `## Closing: Title`. |
| `alert` | `{{% %}}` | yes | title (positional) | Styled alert box. `{{% alert "Graded Assignments" %}}` |
| `callout` | `{{< >}}` | yes | `type=`, `icon=` | Inline callout. Types: `default`, `info`, `warning`, `error`, `important`, `tip`. |
| `button` | `{{< >}}` | yes | `text=` | Styled link button (opens in new tab). Inner content is the URL. `{{< button text="Open Project" >}}https://scratch.mit.edu{{< /button >}}` |
| `icon` | `{{< >}}` | no | name (positional) | Inline icon. `{{< icon "calendar" >}}` Custom names live in `data/icons.yaml`. |
| `tabs` / `tab` | `{{< >}}` | yes | `tab` takes `name=` | Tabbed multi-step instructions. Wrap `tab` blocks inside `tabs`. |
| `clever` | `{{< >}}` | no | none | "Login with Clever" SSO button image. |
| `todays-lesson` | `{{< >}}` | no | none | Card for today's lesson (matches by date). Used on course `_index.md`. |
| `recent-lessons` | `{{< >}}` | no | `count=` (default 5) | Grid of recent lesson cards. |
| `this-week` | `{{< >}}` | no | check the file | Used on course landing pages. Read `layouts/shortcodes/this-week.html` if needed. |

**`this-week` link-rewriting behavior:** `{{< this-week >}}` (used on `content/scratch/_index.md` and `content/music-technology/_index.md`) embeds the most recent week's `_index.md` content into the course root page. Because relative links like `[Title](day-40/)` would otherwise resolve incorrectly when embedded on `/scratch/` instead of `/scratch/week-8/`, the shortcode rewrites `href="day-N/"` patterns to absolute paths at render time. Authors should keep writing relative `day-N/` links in weekly schedule tables — the shortcode handles the rest. **Caveat:** the rewrite only matches `href="day-N/"`. If you add other relative links inside a weekly `_index.md` (e.g., to a project page in `../../video-game-design-project/`), use absolute paths from the start, or they will appear broken when embedded on the course root.

**Delimiter rule of thumb:** Use `{{% %}}` for shortcodes that wrap markdown content (`objectives`, `warmup`, `worksession`, `checkpoint`, `closing`, `alert`). Use `{{< >}}` for shortcodes that emit HTML directly or whose content does not need markdown rendering (`callout`, `button`, `icon`, `tabs`, `tab`, `clever`, `todays-lesson`, `recent-lessons`). Mixing these breaks rendering.

---

## Archive & Reusable Projects

Beyond the current year's weekly lessons, the repo carries two parallel content trees.

### `content/archive/<YYYY-YY>/<course>/...` — past-year snapshots

Verbatim snapshots of past school years. Every daily lesson keeps its original `date:`, `day_number:`, `weight:`, and content — including dated assignment notes and "today we'll…" language. Lives in a separate top-level Hugo section (`archive`), so the `{{< this-week >}}` / `{{< recent-lessons >}}` / `{{< todays-lesson >}}` shortcodes on the live course landing pages can't surface archived lessons (they filter by `.Section`).

- **Don't edit existing year folders.** They are frozen.
- At end of school year, archive the year with `git mv content/<course>/week-* content/archive/<YYYY-YY>/<course>/` (also move dated project hubs and sub-plans). Add a static `_index.md` listing each week — use `content/archive/2025-26/scratch/_index.md` as the template.
- Archived lessons' standards anchors (e.g., `/scratch/description/#ms-cs-fcp3`) still resolve to the live current-year description page. Leave them as-is.

### `content/<course>/projects/<slug>/` — reusable lesson templates

Date-free, generalized lesson and project guides. Future cohorts pull from here.

Conventions:

- **No `date:`, `day_number:`, or week-positional `weight:`** — these aren't tied to a school day.
- **No calendar-icon long-form date line** at the top.
- Schedules key off "Project Day 1 … Project Day N", not specific dates.
- Page title is the topic/project name ("Platforms & Collision", "Video Game Design Project"), not "Day N: …".
- Otherwise use the same shortcode structure (`objectives` / `warmup` / `worksession` / `checkpoint` / `closing`) as a normal daily lesson when extracting a single-day lesson.
- The `_index.md` of a multi-day project hub doesn't need shortcode blocks — see `content/scratch/projects/video-game-design/_index.md`.

To promote an archived lesson into a reusable project: copy it from the archive, strip the front-matter `date:` field and the calendar-icon line, replace year-specific references ("yesterday's project", "this Friday", "next week we'll…") with generic equivalents or a self-contained recap, and add a brief teacher-notes block at the bottom.

### Course root landing pages between school years

When all current-year content has been archived (summer break), the course-root `_index.md` files drop `{{< this-week >}}` and use a static "On Summer Break" headline + card grid pointing to `description/`, `projects/`, `reference/`, and the latest archive. See current `content/scratch/_index.md` and `content/music-technology/_index.md`. When the new year's first lesson lands in `content/<course>/week-1/`, swap the static block back to `## This Week` + `{{< this-week >}}`.

### Callout Examples

```markdown
{{< callout type="warning" >}}
Save your project before closing GarageBand.
{{< /callout >}}

{{< callout type="important" icon="sparkles" >}}
You must submit by end of class.
{{< /callout >}}
```

### Tabs Example

```markdown
{{< tabs >}}
{{< tab name="Step 1" >}}
Click the **Share** button.
{{< /tab >}}
{{< tab name="Step 2" >}}
Click **Copy Link**.
{{< /tab >}}
{{< /tabs >}}
```

---

## Standards

### Design and Modeling (MS-ENGR-II)

Full list with descriptions: `content/design-modeling/description.md`. The framework is Georgia's Middle School Engineering and Technology course 21.02200, *Invention and Innovation — Grade 7*. Anchor pattern:

```markdown
[**MS-ENGR-II-4.5**](/design-modeling/description/#ms-engr-ii-4) — Description here (parenthetical ties to today's activity).
```

The anchor is `#ms-engr-ii-N` where N is the top-level standard (1–6), not the sub-number. So `MS-ENGR-II-5.4` links to `#ms-engr-ii-5`. Cite sub-elements (`MS-ENGR-II-4.5`) in front matter and in the `## Standards` list; the description page lists every sub-element under its parent heading.

Standard groups:

- **MS-ENGR-II-1** — Employability skills (1.1 communicate, 1.5 teamwork are the ones lessons use most)
- **MS-ENGR-II-2** — Lab safety and tool usage (2.4 select the right tool, 2.5 safe use)
- **MS-ENGR-II-3** — Inventions, innovations, and their impact (career connections)
- **MS-ENGR-II-4** — The Engineering Design Process (4.1 the steps, 4.2 construct a system, 4.3 explain it, 4.4 reverse engineer, 4.5 the notebook)
- **MS-ENGR-II-5** — Invent/innovate for a societal need (5.1 research, 5.2 EDP evidence in the notebook, 5.3 prototype, 5.4 mathematical and scientific reasoning — measurement, statistics, dimensioning, CAD)
- **MS-ENGR-II-6** — Technology Student Association

### Scratch (MS-CS-FCP)

Full list with descriptions: `content/scratch/description.md`. Anchor pattern for links from a lesson's `## Standards` section:

```markdown
[**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Description here.
```

The anchor is `#ms-cs-fcpN` where N is the top-level standard group (1–6), not the sub-number. So `MS-CS-FCP.3.4` links to `#ms-cs-fcp3`.

Standard groups:

- **MS-CS-FCP.1** — Career, communication, professionalism
- **MS-CS-FCP.2** — Computer components and processing
- **MS-CS-FCP.3** — Computational thinking, problem-solving, algorithms
- **MS-CS-FCP.4** — Programming concepts and practice (variables, loops, events, debugging)
- **MS-CS-FCP.5** — Embedded computing, hardware, sensors
- **MS-CS-FCP.6** — Ethics, collaboration, creative expression

### Music Tech (MSMTC8)

Full list with descriptions: `content/music-technology/description.md`. Anchor pattern:

```markdown
[**MSMTC8.CR.1**](/music-technology/description/#msmtc8cr1) — Description here.
```

Anchor format is `#msmtc8<domain>N` (lowercased, no dots). Domains: `cr` (Creating), `pr` (Performing), `re` (Responding), `cn` (Connecting).

### Rules

- Every code in the front-matter `standards:` list must appear in the `## Standards` section at the bottom of the file.
- Every code in the `## Standards` section should be in the front-matter `standards:` list.
- The parenthetical or trailing clause in each standard entry should tie the standard to the specific activity in *this* lesson, not just paraphrase the standard.
- Pure procedural/logistics days (e.g., lab setup) may legitimately have `standards: []` and no `## Standards` section.

---

## House Style

- **No emojis** unless the user explicitly requests them.
- **Voice:** Active, student-facing ("You will…", "Open Scratch and…", "Click **Share**").
- **Em dashes** (`—`, U+2014) for parenthetical asides — not double hyphens.
- **Bold UI elements:** Button names and menu items in bold (`Click **Share**`, `Open the **File** menu`).
- **Code/keys:** Backticks for code, keyboard shortcuts, and file paths (`` `cmd + S` ``, `` `content/scratch/` ``).
- **Objectives** use the `- I can…` pattern, one bullet per objective.
- **Vocabulary** uses Markdown definition lists with a blank line between term and `:` line.
- **Checkboxes** use `- [ ]` (unchecked) and `- [x]` (checked, for examples only).
- **Headings:** `## Warmup: Title`, `## Work Session: Title`, `### Checkpoint: Title` — the colon-space-title format is mandatory.
- **Links:** Prefer descriptive link text (`[Teachable Machine](https://teachablemachine.withgoogle.com/train/image)`) over raw URLs. Use direct/deep links when they reduce clicks for students. **Always use absolute paths for `{{< card >}}` links on course root `_index.md` files** (e.g. `link="/scratch/projects"`, not `link="projects"`) — CloudFront + S3 resolves bare relative links from the site root, not the page's directory, causing broken URLs in production.
- **Numbers:** Spell out one through nine in prose; use digits for 10+ and for all measurements, counts, and step numbers.
- **Lesson length:** Daily lessons are typically 100–250 lines. Going much longer usually means the work session is too dense for one class period.

---

## Converting a Teacher Lesson Plan into a Lesson Page

The user often supplies a teacher-facing lesson plan (timed agenda, materials list, teacher notes) and asks for a lesson page. **Site pages are student-facing.** Convert, don't transcribe.

**Drop entirely:**

- Timed agendas (`| 5 min | Welcome, attendance |`). Students don't need minute budgets, and they go stale the first time a period runs long.
- Teacher notes about classroom management, prep, staffing, seating charts, or which students to watch.
- Materials lists — these are the teacher's setup checklist. Student-needed tools belong in front-matter `resources:` instead.
- Anything naming individual students.

**Promote into student content:**

- Teacher notes that are really instructions in disguise. "Set the tempo expectation up front" becomes a step in the walkthrough; "circulate for headphone volume" becomes a `{{< callout type="warning" >}}`.
- Pacing reassurance the student benefits from ("most people will finish Sets 1–3 today") — as a `{{< callout type="info" >}}`.
- Grading criteria and due dates. Students should know what "finished" means.

**Rewrite:**

- Objectives from "Students will…" to the `- I can…` pattern.
- Agenda blocks into the required section order — the agenda's warmup/mini-lesson/work-time/share-out maps cleanly onto `warmup` → `worksession` → `closing`. A long work block often splits into two `worksession` blocks (instruction, then application).

**Supply what the plan omits:**

- **Standards.** Teacher plans usually list none. Choose real codes from the course `description.md`, tie each to a specific activity in *this* lesson, and mirror them in front matter. Verify anchors resolve.
- Front matter generally — `units`, `tags`, `resources`, `description`, `day_number`, `weight`.

**Reconcile before writing.** Plans drift from the site: check grade level, unit names, and dates against `description.md` and the week's `_index.md`, and surface conflicts rather than silently picking one. If a plan links a handout at a path that doesn't exist on this site, ask where it should live or whether it's print-only — don't invent a URL.

---

## Known Issues

- **The 2025-26 Music Tech archive is incomplete.** `week-8/_index.md` links `day-37/`–`day-40/` and `week-9/_index.md` links `day-43/`, but those folders were never committed. 37 lessons exist, while `content/archive/2025-26/_index.md` advertises "Days 1–42." Those schedule links are dead. **Don't try to repair them** — archives are frozen, and fixing the count requires the user's explicit OK. Scratch's archive (days 1–43) is complete.

---

## Course Context (Quick Reference)

### Design and Modeling (PLTW Gateway)

- **Audience:** Grade 7, no prior experience.
- **Length:** One quarter — 45 days across 9 weeks, 50-minute periods. Started Mon 8/3/2026.
- **Framework:** Georgia MS-ENGR-II standards (Invention and Innovation — Grade 7). PLTW's own unit structure is Lesson 1 Introduction to Design → Lesson 2 Modeling → Lesson 3 Design Challenge.
- **Primary tools:** Engineering Notebook (composition book), linking cubes, rulers, dial calipers, isometric and square graph paper, myPLTW (`my.pltw.org`, via Clever), Tinkercad (class join links in the Day 22 lesson), Excel, BrainPOP.
- **Day numbering:** Mon 8/17 (digital learning day) counts as Day 11 and has no lesson page; the Week 3 schedule table lists it without a link.
- **Units to date:**
  - Lesson 1 — Introduction to Design (Days 1–21): Activity 1.1 Foot Orthosis Instant Design Challenge; 1.2 A Picture Is Worth a Thousand Words (thumbnail, isometric, multiview); 1.3 Measuring Matters (rulers, paper skimmer build and launch); 1.4 Skimmer Statistics (mean/median/mode/range, quartiles, box plots — class data measured in **feet**); 1.5 Dialed In (dial caliper, dimensioning conventions). Project 1.6 (mechanical dissection) has not been taught yet.
  - Lesson 2 — Modeling (Day 22 on): Activity 2.1 Taking Modeling to Another Dimension (Tinkercad). Next: 2.2 For Good Measure, 2.3 It's for the Birds, Project 2.4 Puzzle Cube.
- **Assessment:** Unit 1 Quiz Fri 9/4 (Day 25), paper only. **Quiz content, answer keys, and study-guide practice objects never go on the site** — that material stays in CTLS and the teacher's folder. Warmup answer checks for in-class practice items are fine.
- **Recurring lesson pattern:** headed notebook page (name/period · date · title), a warmup that doubles as quiz review (ruler reading with the "zero trap," quartiles by hand), a work session that often lives on myPLTW (say so and give the navigation path — the site page is a map, not the steps), a partner check, a closing sentence.

### Computer Programming with Scratch (no longer taught)

- **Audience:** 6th–8th graders, no prior programming experience.
- **Length:** 45 days across 9 weeks.
- **Framework:** Georgia MS-CS-FCP standards (Foundations of Computer Programming).
- **Primary tool:** MIT Scratch (`scratch.mit.edu`).
- **Units to date:**
  - Unit 1: Introduction to Scratch (interface, sequencing, events, motion, sprite art, maze design)
  - Unit 2: Conditionals & Control Flow (keyboard events, `if`, collision, flow diagrams, loops, efficiency)
  - Unit 3: Boolean Operators & Platformer (and/or/not, velocity, gravity, platform/wall collision, variables, game state, CLI/Minecraft intro)
  - Additional units in weeks 4–8 covering animation, data, and AI/machine learning (see `content/scratch/week-*/` for current scope).
- **Major projects:** Maze Game, Platformer Game, Video Game Design Project (see `content/scratch/video-game-design-project/`), Box Art Project.

### Music Technology

- **Audience:** Grade 8.
- **Length:** 45 days across 9 weeks.
- **Framework:** Georgia MSMTC8 standards (Creating, Performing, Responding, Connecting).
- **Primary tools:** GarageBand (primary DAW), Soundtrap (podcast recording), Musescore, Hooktheory, musictheory.net, Edpuzzle, Flocabulary, BrainPop.
- **Hardware:** Mac computers, XLR microphones, audio interfaces, portable audio recorders.
- **Units to date:**
  - Unit 1: Podcasts (Days 1–11) — wave science, mic setup, scripting, intro music, recording, editing, distribution
  - Unit 2: Sound Design (Days 12–15) — effects (Pitch Shift, Reverb, EQ, Distortion, Delay, Chorus, Tremolo), automation, layering with video
  - Additional units in weeks 4–8 covering MIDI, music reading, beat making, remixing (see `content/music-technology/week-*/` for current scope).

When in doubt about course content beyond what's in this AGENTS.md, read the relevant week's `_index.md` and the most recent 2–3 daily lessons in that week.

---

## Git & Deployment

- **Branches:**
  - `main` — production. Push triggers `.github/workflows/deploy.yml` → builds Hugo in CI, syncs to S3, invalidates CloudFront (`mrwillingham.com`).
  - No staging branch or server. Use `hugo serve` locally for previewing drafts.
- **Submodules:** `themes/hextra` is a Git submodule. Fresh clones need `git submodule update --init --recursive` before building.
- **Build pipeline:** GitHub Actions runner checks out the repo, installs Hugo Extended (pinned version — see `.github/workflows/deploy.yml`), runs `hugo --minify --cleanDestinationDir`, syncs `public/` to S3 with `aws s3 sync --delete`, then invalidates the CloudFront distribution.
- **Hugo version:** Pinned in `.github/workflows/deploy.yml`. Must be ≥ 0.156.0 — the `hugo.Data` function used in `layouts/calendar/list.html` was introduced in that release. Local Hugo version should match or exceed the pinned CI version.
- **Never commit** unless the user explicitly asks. The user controls when changes ship to prod.

---

## Guardrails

- **Never edit** `themes/hextra/` — it's a Git submodule. Override theme behavior via files in `layouts/` instead.
- **Never edit or commit** `public/` or `.hugo_build.lock` — they are build artifacts (gitignored).
- **Never edit** `.env*` files (denied at the permission layer).
- **Don't invent** assignments, due dates, project scope, or activities the user didn't ask for. Ask a focused clarifying question instead.
- **Don't change `weight` values** on existing lessons without recalculating siblings — it silently reorders the sidebar.
- **Don't add `date:` or `day_number:`** to pages under `content/<course>/projects/` — they are intentionally date-free templates.
- **Don't edit `content/archive/`** existing year folders — they're frozen snapshots of past years.
- **Don't commit** unless explicitly asked.
- **Use the Edit tool**, not `sed` or `awk`, for file edits.
- **Use the Write tool**, not bash heredocs or `echo` redirection, for new files.
- **Verify with `hugo --quiet --renderToMemory`** after any edit before declaring done. Zero output = success.
- **Check for an existing near-match** before inventing a `units`, `tags`, or `resources` value — singular/plural and reworded variants split a term across two pages. See "Taxonomy values" above; casing alone does not split a term.
- **Don't delete or rewrite weekly schedule links that 404 in prod.** Future-dated lessons are excluded from production builds by design — see "Future-dated lessons are invisible in production."
- **Don't rely on stale planning files.** Current schedule lives in each course's week-`N` `_index.md`. Treat any informal notes files as potentially out of date.

---

## When in Doubt

1. Read the 2–4 most recent daily lessons in the same week to match style and continuity.
2. Read the week's `_index.md` schedule table to confirm the day's planned topic and summary.
3. Read the relevant archetype (`archetypes/design-modeling/index.md`, `archetypes/music-technology/index.md`, or `archetypes/scratch/index.md`) for the canonical skeleton.
4. If no current-year lessons exist yet (e.g., start of school year, summer break), look in `content/archive/<most-recent-YYYY-YY>/<course>/` for how the same topic was taught last year, and in `content/<course>/projects/` for date-free reusable versions of standout lessons.
5. For deeper context that isn't in this AGENTS.md, the human-facing docs in the repo root (`content.md`, `technical.md`, `coding-scratch.md`, `music-tech.md`) are accurate and authoritative. If anything in those docs conflicts with this AGENTS.md, prefer this file for agent operations and surface the discrepancy to the user.
