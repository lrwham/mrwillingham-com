# AGENTS.md — mrwillingham.com

Operational reference for AI coding agents working in this repository. Human-facing documentation lives in `readme.md`, `content.md`, `technical.md`, `coding-scratch.md`, and `music-tech.md`. This file inlines everything an agent needs for routine work — do not assume a human will read it.

---

## Project Summary

Hugo static site for a middle-school teacher's classes. Live for 2026-27: **Music Technology** (Georgia MSMTC8 standards) and, for Q2 (Oct 12 – Dec 18, 2026), **Computer Programming with Scratch** (Georgia MS-CS-FCP standards). The site uses the [Hextra](https://github.com/imfing/hextra) theme via a Git submodule. Lesson content lives in `content/<course>/week-N/day-NN/index.md`, organized by week. GitHub Actions build Hugo in CI and deploy to S3 + CloudFront on push to `main`. There is no staging server — use local `hugo serve` for previewing drafts.

---

## Repo Map

| Path | What it is | Agent should... |
|------|-----------|-----------------|
| `content/` | All lesson and page content (markdown) | Edit freely; this is the main workspace |
| `content/scratch/` | Computer Programming with Scratch (current quarter) | Edit; daily lessons in `week-N/day-NN/index.md`; date-free project hubs in `projects/`; code patterns, logins, practice, and vocab in `reference/`. Daily pages are short maps that link to `projects/` and `reference/` for the steps — keep it that way. |
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
- `<course>` is `scratch` or `music-technology`.
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
- `date` — Full ISO timestamp with the America/New_York offset: `-04:00` while daylight saving time is in effect, `-05:00` otherwise. DST ends **Sun Nov 1, 2026** and resumes **Sun Mar 14, 2027**, so Scratch Days 1–15 use `-04:00` and Days 16–44 use `-05:00`. Bare `YYYY-MM-DD` works for some existing music-tech files but new lessons should use the full form.
- `description` — One sentence, active voice, student perspective. Mirrors the weekly schedule table's Summary column.
- `day_number` — Integer, continuous across the course. Must strictly exceed the previous lesson's `day_number`.
- `units` — List. Exact spelling must match sibling lessons (see "Taxonomy values" below).
- `standards` — Real standard codes (see Standards section below). Each code listed here must also appear in the `## Standards` section at the bottom of the file.
- `tags` — Topical tags. Scratch lessons always include `- Scratch`. Music Tech lessons typically include the primary DAW tag (`- GarageBand`, `- Soundtrap`, etc.).
- `resources` — Tools students will use. Match existing entries (see "Taxonomy values" below). Printed handouts follow the `"Drum Worksheet Packet (printed)"` pattern — lowercase `printed` in parentheses.
- `weight` — Sort order within the week (1–5 for Mon–Fri). Don't change existing values without recalculating siblings.
- `scratchblocks` — Scratch course only. Set `true` to enable ```scratch fenced code blocks.

### Taxonomy values (`units`, `tags`, `resources`)

What actually creates a duplicate term page is **spelling, not casing.** Hugo normalizes case when keying terms, so `Loops` and `loops` collapse into a single `/tags/loops/` page listing both lessons — only the display title differs, decided by whichever page Hugo reads first. Verified behavior, not theory.

- **Real risk: singular vs. plural and reworded variants.** `Podcast` and `Podcasts` are both live `units` terms today, splitting the same unit across two pages. Check for an existing near-match before inventing a value.
- **Casing convention differs by course.** Music Tech uses TitleCase tags (`Soundtrap`, `Podcast`); Scratch uses lowercase (`loops`, `variables`, `conditionals`). Match the course you're editing so display titles stay consistent.
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
- Page title is the topic/project name ("Platforms and Collision", "Video Game Design Project"), not "Day N: …".
- Otherwise use the same shortcode structure (`objectives` / `warmup` / `worksession` / `checkpoint` / `closing`) as a normal daily lesson when extracting a single-day lesson.
- The `_index.md` of a multi-day project hub doesn't need shortcode blocks — see `content/scratch/projects/video-game-design/_index.md`. Multi-day hubs use `## Project Day N: Title` headings; daily lessons deep-link to them (`/scratch/projects/maze-game/#project-day-2-controls-and-walls`), so don't rename those headings without updating the lessons that link to them. Avoid `+`, `&`, and other punctuation in headings that are link targets — Goldmark drops them and the anchor becomes hard to predict.

To promote an archived lesson into a reusable project: copy it from the archive, strip the front-matter `date:` field and the calendar-icon line, replace year-specific references ("yesterday's project", "this Friday", "next week we'll…") with generic equivalents or a self-contained recap, and add a brief teacher-notes block at the bottom.

### `content/<course>/reference/` — quick-reference pages

Date-free pages for anything lessons would otherwise repeat: login steps, code patterns, tool guides, practice questions, vocabulary. The Scratch course keeps the canonical set — `daily-routine/`, `scratch-login/`, `share-to-studio/`, `code-patterns/` (one `## Pattern Name` heading per Scratch script, deep-linked from lessons), `art-tools/`, `boolean-operators/`, `flowcharts/` (with the printable worksheet as a `type: bare` sub-page), `python-setup/`, `datasets/` (page bundle holding the zips), `practice/` (hub plus one page per practice set), and `unit-N-vocab/`. Printable worksheets are `type: bare` leaf pages (`layouts/bare/single.html`), kept next to the project or reference page that uses them.

**Lesson pages are maps.** A daily lesson states objectives, says what to open and which project day or pattern to follow, carries the checkpoints and the closing, and links out for the actual steps and code. If a work session is pasting in code that already lives on `code-patterns/` or a project hub, link instead. Per-quarter links that change (class studio, Forms, Gimkit) live on one reference page (`share-to-studio/` for the studio) or are flagged `<!-- TODO: new link -->` in the lesson.

### Course root landing pages between school years

When all current-year content has been archived (summer break), the course-root `_index.md` files drop `{{< this-week >}}` and use a static "On Summer Break" headline + card grid pointing to `description/`, `projects/`, `reference/`, and the latest archive. See `content/archive/2025-26/scratch/_index.md` for the archive-side pattern; the live course roots (`content/scratch/_index.md`, `content/music-technology/_index.md`) currently show the in-session form: `## This Week` + `{{< this-week >}}` followed by a `## More` card grid. When a new year's first lesson lands in `content/<course>/week-1/`, swap the static block back to that form.

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

### Computer Programming with Scratch (Q2 2026-27)

- **Audience:** 6th–8th graders, no prior programming experience.
- **Length:** One quarter — 44 class days across 9 weeks, Mon 10/12/2026 – Fri 12/18/2026. Day 1 (Mon 10/12) is a digital learning day with an at-home lesson page. Tue 10/13 – Fri 10/16 are conference-week early-release days. Tue 11/3 is a student holiday (Week 4 has four days). Thanksgiving week (11/23–27) is off. Thu 12/17 and Fri 12/18 are early release.
- **Framework:** Georgia MS-CS-FCP standards (Foundations of Computer Programming).
- **Primary tools:** MIT Scratch (`scratch.mit.edu`, class accounts emailed to students — see `reference/scratch-login/`), Code.org, BrainPOP, Edpuzzle, and Flocabulary via Clever; Python 3 with VS Code (Weeks 7+); Teachable Machine; VEXcode VR (`vr.vex.com`, Weeks 8–9).
- **Promoted from the 2025-26 archive.** Lessons were copied from `content/archive/2025-26/scratch/`, re-dated, renumbered, and slimmed so the steps and code live in `projects/` and `reference/`. The archive stays frozen.
- **Units:**
  - Week 1 — Intro to Scratch (Days 1–5): DLD sequencing/debugging on Code.org, lab basics, Scratch login and art tools, motion and sequences, maze design. Project hub: `projects/maze-game/`.
  - Weeks 2–3 — Conditionals and Control Flow (Days 6–15): keyboard events and `if touching color`, Flocabulary, flow diagrams, loops, the game loop; boolean operators, gravity with velocity, platforms and collision, objective and score; terminal and Minecraft. Hubs: `projects/maze-game/`, `projects/platformer/`.
  - Week 4 — Intermediate Scratch (Days 16–19): falling-objects catch game — variables, clones, broadcasts and game states. Hub: `projects/falling-objects-game/`. Quiz and share on Day 20.
  - Weeks 5–6 — Video Game Design Project (Days 21–29): nine days; Project Days 8 and 9 (peer feedback, revisions) are merged into Day 28. Presentations Fri 11/20. Hub: `projects/video-game-design/`.
  - Week 7 — Python and the Terminal (Days 30–34): VS Code setup, number guessing game, Pokémon data with pandas and matplotlib, Pokémon Designer, BrainPOP AI. Hub: `projects/python-pokemon-data/`; setup on `reference/python-setup/`.
  - Weeks 8–9 — AI and VEXcode VR (Days 35–44): BrainPOP Hackers, Teachable Machine (`projects/teachable-machine-rock-paper-scissors/`), then seven **scaffolded** VEXcode VR days (37–42, 44) with `draft: true` and TODO stubs — the user fills these in. Day 43 is the end-of-quarter word search.
- **Per-quarter links to replace:** class studio (`reference/share-to-studio/`), About Me form (Day 2), learning checks (Days 11, 12), Gimkit (Day 18), VGD forms (Days 25, 28), Pokémon stats form (Day 33), and the Scratch starter projects on the hubs. Each is marked `<!-- TODO: new link -->`.

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
- **Don't rely on stale planning files.** Current schedule lives in each course's week-`N` `_index.md`. Treat any informal notes files as potentially out of date. `TODO-archive-cs-to-live.md` is the promotion checklist for the Scratch course; delete it once the course is fully live.
- **Keep Scratch daily lessons as maps.** Steps and code go on `projects/` hubs and `reference/` pages; a lesson links to them. Don't paste pattern code back into a daily page.

---

## When in Doubt

1. Read the 2–4 most recent daily lessons in the same week to match style and continuity.
2. Read the week's `_index.md` schedule table to confirm the day's planned topic and summary.
3. Read the relevant archetype (`archetypes/music-technology/index.md` or `archetypes/scratch/index.md`) for the canonical skeleton.
4. If no current-year lessons exist yet (e.g., start of school year, summer break), look in `content/archive/<most-recent-YYYY-YY>/<course>/` for how the same topic was taught last year, and in `content/<course>/projects/` for date-free reusable versions of standout lessons.
5. For deeper context that isn't in this AGENTS.md, the human-facing docs in the repo root (`content.md`, `technical.md`, `coding-scratch.md`, `music-tech.md`) are accurate and authoritative. If anything in those docs conflicts with this AGENTS.md, prefer this file for agent operations and surface the discrepancy to the user.
