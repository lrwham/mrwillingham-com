# TODO — Promote Computer Programming with Scratch from the 2025-26 archive to a live course

Working plan for bringing `content/archive/2025-26/scratch/` forward as the live `content/scratch/` course for the quarter starting **Mon Oct 12, 2026**. The archive stays untouched throughout. Nothing is committed until Mr. Willingham says so.

Check items off as they land. Delete this file (or move it under an archive note) once the course is live.

---

## 0. Decisions to confirm before building

These change the shape of the work. Recommendations are marked; nothing below is built until confirmed.

- [x] **Day 1 is a Digital Learning Day (Mon 10/12).** Decided: Day 1 is a real at-home lesson page — the archive's Day 2 "Sequencing & Debugging" (BrainPOP *Computer Programming* + Code.org *Programming with Angry Birds*), reframed for a DLD. Tue 10/13 becomes "Computer Lab Basics" (the archive's Day 1).
- [ ] **Conference week early release (Tue 10/13 – Fri 10/16).** Classes are shortened all four days. The archive's Day 1 was also a 30-minute day, so "Computer Lab Basics" is already trimmed. Days 3–5 (Intro to Scratch, Motion & Sequences, Maze Design) will each get a `{{% alert %}}` noting the short period and a "finish tomorrow if needed" line. Confirm the early-release bell schedule is short enough to warrant it.
- [ ] **Week 4 has four days (Tue 11/3 is a student holiday).** The archive's Week 4 (falling-objects game, 5 days) becomes Days 16–19 with the "Quiz & Share Your Game" day sliding to Mon 11/9 (Day 20). The spring-break review warmup on the archive's Day 16 gets cut to a short recap, since there is no break before it this time.
- [x] **Video Game Design Project must finish before Thanksgiving.** Decided: the project runs Days 21–29 (Tue 11/10 – Fri 11/20), nine days. Project Day 8 (Practice & Peer Feedback) and Day 9 (Revisions) merge into one day. Final presentations Fri 11/20.
- [x] **Weeks 8–9 need seven new lessons.** Decided: a **VEXcode VR** mini-unit, scaffolded only (front matter, objectives, standards, section skeletons with TODO stubs — no invented activities). Days 37–42 and 44. See section 5.
- [x] **Reference extraction.** Decided: the full set in section 4 — reference pages plus the maze-game, platformer, falling-objects-game, and python-pokemon-data hubs.
- [ ] **Audience line.** The archive says "6th–8th Grade". Confirm that still holds for this quarter.
- [ ] **Scratch class accounts.** Day 3 tells students to find their Scratch login in a school email. Confirm the accounts (and the email) will exist again, or whether this quarter uses a different login path.
- [ ] **Stale external links.** The archive links specific Scratch studios (`51505776`, `51505777`), starter projects, Microsoft Forms learning checks, Gimkit practice sets, an Edpuzzle, and `cdn.mrwillingham.com/scratch-concepts-slides-rev-a.pdf`. Starter projects and the PDF carry forward as-is. Studios, Forms, Gimkit, and Edpuzzle links are flagged with `<!-- TODO: new link -->` in the copied lessons and listed in section 7 so they can be replaced once the new ones exist.

---

## 1. Calendar and numbering

Source: district calendar, revised 3/11/26.

| Week | Dates | Days | Notes |
| ---- | ----- | ---- | ----- |
| 1 | Mon 10/12 – Fri 10/16 | 1–5 | 10/12 Digital Learning Day; 10/13–16 conference week, early release |
| 2 | Mon 10/19 – Fri 10/23 | 6–10 | |
| 3 | Mon 10/26 – Fri 10/30 | 11–15 | |
| 4 | Mon 11/2, Wed 11/4 – Fri 11/6 | 16–19 | Tue 11/3 student holiday (Election Day) |
| 5 | Mon 11/9 – Fri 11/13 | 20–24 | |
| 6 | Mon 11/16 – Fri 11/20 | 25–29 | Last day before Thanksgiving break |
| — | Mon 11/23 – Fri 11/27 | — | Thanksgiving — school closed |
| 7 | Mon 11/30 – Fri 12/4 | 30–34 | |
| 8 | Mon 12/7 – Fri 12/11 | 35–39 | |
| 9 | Mon 12/14 – Fri 12/18 | 40–44 | Thu 12/17 and Fri 12/18 early release |

**44 class days.** Day numbers run 1–44, continuous, one per class day (the DLD counts as Day 1).

**Date front matter.** Full ISO timestamps. The UTC offset flips when daylight saving ends on **Sun Nov 1, 2026**:

- Days 1–15 (Oct 12 – Oct 30): `T08:00:00-04:00`
- Days 16–44 (Nov 2 – Dec 18): `T08:00:00-05:00`

AGENTS.md currently says `-04:00` only; it gets a note about the flip (section 6).

**Week weights.** 100-based scale: Week 1 = 100, Week 2 = 90, … Week 9 = 20. The archive's 10→2 scale is not copied.

---

## 2. Day-by-day mapping (archive → live)

Lesson titles keep the "Day N: " prefix with the new number. Where a lesson's body is "yesterday we…" / "Friday's project", rewrite to match the new sequence.

### Week 1 — Introduction to Scratch (weight 100)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 1 | Mon 10/12 | Day 2 | Sequencing & Debugging (Digital Learning Day) | Reframe the "Mr. Willingham is out" alert as a DLD at-home page. BrainPOP + Code.org via Clever. |
| 2 | Tue 10/13 | Day 1 | Computer Lab Basics | Already a short-day lesson. "Read all the instructions daily" alert moves to the Daily Routine reference page (section 4) and is linked instead. New About Me form link flagged. |
| 3 | Wed 10/14 | Day 3 | Intro to Scratch | Art tools tab block moves to `reference/art-tools/`; lesson links to it. Login paragraph replaced with a link to `reference/scratch-login/`. Short-day alert. |
| 4 | Thu 10/15 | Day 4 | Motion & Sequences | Short-day alert. |
| 5 | Fri 10/16 | Day 5 | Maze Design | Maze worksheet + example SVGs move to `projects/maze-game/`. Short-day alert. |

### Week 2 — Conditionals & Control Flow (weight 90)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 6 | Mon 10/19 | Day 6 | User Input & Conditionals | Keyboard-control and wall-reset code blocks link to `reference/code-patterns/` anchors; lesson keeps the step order and checkpoints. |
| 7 | Tue 10/20 | Day 7 | Flocabulary — Coding: Conditionals | As-is. |
| 8 | Wed 10/21 | Day 8 | Flow Diagrams | Symbol explanations move to `reference/flowcharts/`; worksheet moves with it. Example page stays as a sub-page. |
| 9 | Thu 10/22 | Day 9 | Loops | As-is (Code.org video links carry over). |
| 10 | Fri 10/23 | Day 10 | Loops + Conditionals | As-is. |

### Week 3 — Boolean Operators & Platformer (weight 80)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 11 | Mon 10/26 | Day 11 | Boolean Operators | `flowcharts/`, `learning-check`, `practice-questions` sub-pages move to `reference/boolean-operators/` and `reference/practice/`. |
| 12 | Tue 10/27 | Day 12 | Gravity | Archive has empty `units`, `standards`, `description` and a placeholder standards line — fill them in. Boolean review section links to the reference page. Velocity code links to code-patterns. |
| 13 | Wed 10/28 | Day 13 | Platforms & Collision | Already extracted as `projects/platformer-collision/`; daily page becomes a short pointer to it plus checkpoints. |
| 14 | Thu 10/29 | Day 14 | Platformer Review | `script.md` (406-line build-along) moves to `projects/platformer/build-along/`. |
| 15 | Fri 10/30 | Day 15 | Minecraft Special (Terminal + Minecraft Education) | As-is; terminal commands link to `reference/terminal-vscode/`. |

### Week 4 — Intermediate Scratch (weight 70) — four days

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 16 | Mon 11/2 | Day 16 | New Game: Falling Objects | Spring-break warmup cut to a short recap. Build steps link to `projects/falling-objects-game/` day 1. |
| — | Tue 11/3 | — | *Student holiday* | Listed in the schedule table without a link. |
| 17 | Wed 11/4 | Day 17 | Variables Deep Dive | Links to project day 2. |
| 18 | Thu 11/5 | Day 18 | Clones | Study guide / practice links point at `reference/practice/`. Clone code links to code-patterns. |
| 19 | Fri 11/6 | Day 19 | Game States | Broadcast pattern links to code-patterns. |

### Week 5 — Quiz, then Video Game Design Project (weight 60)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 20 | Mon 11/9 | Day 20 | Quiz & Share Your Game | Share steps link to `reference/share-to-studio/`. Quiz on CTLS. New studio link flagged. |
| 21 | Tue 11/10 | Day 21 | Brainstorm & Team Formation | Project schedule table rewritten for Days 21–29. Worksheet + exit ticket move under `projects/video-game-design/`. |
| 22 | Wed 11/11 | Day 22 | Game Design Document | As-is; GDD template already in `static/downloads/`. |
| 23 | Thu 11/12 | Day 23 | Box Art | Links to `projects/video-game-design/box-art/`. |
| 24 | Fri 11/13 | Day 24 | Finish Box Art & GDD | As-is. |

### Week 6 — Video Game Design Project — Finish & Present (weight 50)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 25 | Mon 11/16 | Day 25 | Prototype & Presentation — Day 1 | PowerPoint template already in `static/downloads/`. |
| 26 | Tue 11/17 | Day 26 | Prototype & Presentation — Day 2 | |
| 27 | Wed 11/18 | Day 27 | Finish Prototype & Presentation | Both due end of class. |
| 28 | Thu 11/19 | Days 28 + 29 | Peer Feedback & Revisions | Merged (pending decision). Peer feedback worksheet moves under the project hub. The three warmup/work-session `.mp3` files from the archive's Day 28 are dropped unless they are still wanted. |
| 29 | Fri 11/20 | Day 30 | Final Presentations & Share | Last day before break. |

### Week 7 — Python and the Terminal (weight 40)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 30 | Mon 11/30 | Day 31 | Python and VS Code | IDLE / Self Service check and the draft `terminal-setup` page merge into `reference/python-setup/`; lesson links to it. The closing's "tomorrow: turtle" line is fixed — the next day is the guessing game. |
| 31 | Tue 12/1 | Day 32 | Number Guessing Game | As-is. |
| 32 | Wed 12/2 | Day 33 | Pokémon Data with Pandas | Datasets move to `reference/datasets/` (or `static/downloads/`). `pip install` step links to python-setup. |
| 33 | Thu 12/3 | Day 34 | Design Your Own Pokémon | `pokemon-designer.zip` moves with the datasets. |
| 34 | Fri 12/4 | Day 35 | Intro to AI (BrainPOP) | As-is. |

### Week 8 — AI and VEXcode VR (weight 30)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 35 | Mon 12/7 | Day 36 | Hackers (BrainPOP) | Due-date line updated. |
| 36 | Tue 12/8 | Day 40 | Rock, Paper, Scissors with Teachable Machine | Already extracted as `projects/teachable-machine-rock-paper-scissors/`; daily page points to it. |
| 37 | Wed 12/9 | *new* | VEXcode VR — Day 1 | Scaffold. See section 5. |
| 38 | Thu 12/10 | *new* | VEXcode VR — Day 2 | Scaffold. |
| 39 | Fri 12/11 | *new* | VEXcode VR — Day 3 | Scaffold. |

### Week 9 — VEXcode VR and Wrap-Up (weight 20)

| New | Date | Archive | Title | Changes |
| --- | ---- | ------- | ----- | ------- |
| 40 | Mon 12/14 | *new* | VEXcode VR — Day 4 | Scaffold. |
| 41 | Tue 12/15 | *new* | VEXcode VR — Day 5 | Scaffold. |
| 42 | Wed 12/16 | *new* | VEXcode VR — Day 6 | Scaffold. |
| 43 | Thu 12/17 | Day 43 | End-of-Quarter Word Search | Early release. PDF already in `static/downloads/`. |
| 44 | Fri 12/18 | *new* | VEXcode VR — Day 7 | Early release. Scaffold. |

---

## 3. Infrastructure (do first; mechanical)

- [ ] `hugo.yaml` — add a `scratch` menu entry (`name: Computer Programming`, `pageRef: /scratch`, `weight: 3`, filling the slot the Design and Modeling entry left).
- [ ] `content/_index.md` — add a `{{< card link="/scratch/" title="Computer Programming with Scratch" subtitle="6th–8th Grade" >}}` under Classes. Absolute path, per house style.
- [ ] `content/scratch/_index.md` — replace the "On Summer Break" block with `## This Week` + `{{< this-week >}}` and a `## More` card grid (description, projects, reference, 2025-26 archive), matching `content/music-technology/_index.md`. Drop the stale `lastmod: "2026-05-24"`.
- [ ] `content/scratch/description.md` — confirm the course description and late-work policy still apply; no structural change.
- [ ] `content/scratch/standards.md` — currently `draft: true` and duplicates `description.md`. Delete it or leave as draft; recommend delete.
- [ ] `content/scratch/reference/_index.md` — give it a real title/intro and a card grid once the reference pages in section 4 exist.
- [ ] `archetypes/scratch/index.md` — already correct. No change.
- [ ] `AGENTS.md` — section 6.

---

## 4. Reference pages (date-free, linked from lessons)

The archive repeats the same instructions and code across many days. Pulling them into standalone pages lets each daily lesson become a short map — objectives, "open X, do Y, link to the pattern", checkpoints — instead of re-explaining. Each entry lists which archive days currently carry the content.

### `content/scratch/reference/` — new pages

| Page | What it holds | Pulled from | Linked by |
| ---- | ------------- | ----------- | --------- |
| `daily-routine/` | How to use this site: read everything first, objectives → warmup → work session → closing, Clever login, what to do when finished early, lost-work policy | Day 1 alert, Day 6 callout, Day 21 callout | Course root, Days 2, 6, 21 |
| `scratch-login/` | Where the class Scratch account comes from, finding it in school email via Office 365, what to do if Scratch logs you out, when to use the starter project link | Days 3, 6, 18 | Days 3–20 |
| `art-tools/` | Scratch paint editor: color sliders, primitive shapes, brush/fill/select/text/reshape/eraser, with the existing screenshots and the art challenges | Day 3 tabs block + 5 PNGs | Days 3, 5, 23 |
| `code-patterns/` | **Scratch Code Patterns** cookbook — one anchor per pattern, each with a `scratch` block and a two-line explanation: arrow-key movement (event blocks), smooth movement (forever + if key pressed), wall collision reset, touching-sprite collision, score variable, falling object with random reset, velocity gravity + jump, platform landing (move-check-step-up), clone factory + clone script, broadcast game states, play sound on touch | Days 6, 10, 12, 13, 16, 17, 18, 19 | Nearly every Scratch build day |
| `boolean-operators/` | `not` / `and` / `or` with Scratch blocks and the flowchart versions | Day 11 `flowcharts/` sub-page, Day 12 review section | Days 11, 12, 13 |
| `flowcharts/` | Flow diagram symbols (oval, rectangle, diamond), how to read and trace one, and the printable Flow Diagram Worksheet as a sub-page | Day 8 body + `flow-diagram-worksheet/`, Day 11 `flowcharts/` | Days 8, 11 |
| `share-to-studio/` | Share button → Add to Studio, with the current class studio link in one place (change it once per quarter instead of per lesson) | Days 20, 30 | Days 20, 29, 42 |
| `practice/` | Quiz practice hub: study guide PDF link, Boolean Operators examples + practice questions, Gravity & Velocity examples, Code-Focused examples, Concept-Focused examples (each archive sub-page becomes a child page) | Day 11 `learning-check.md`, `practice-questions.md`; Day 12 `learning-check.md`; Day 18 `learning-check-code.md`, `learning-check-concepts.md` | Days 11, 12, 18, 20, 42 |
| `python-setup/` | Is Python installed (IDLE / Self Service), opening VS Code, making the `python-class` folder, integrated terminal, basic commands table, running a script, `pip install`, troubleshooting | Day 31 warmup + `terminal-setup/` (currently `draft: true`), Day 33 install step, Day 15 terminal commands | Days 15, 30–33, 40 |
| `datasets/` | Download page for `pokemon.csv.zip`, `players_info.csv.zip`, `pokemon-designer.zip`, with a one-line description of each and column notes | Days 33, 34 page bundles | Days 32, 33 |
| `unit-2-vocab/` | Finish the existing draft (Control Flow, Booleans, Variables, Clones, Broadcasts) and un-draft it | `unit-1-vocab` pattern; terms scattered across Days 6–19 | Days 7, 11, 18, 42 |
| `unit-3-vocab/` | Python, terminal, data, AI terms | Days 31–35, 40 | Days 30–37 |

### `content/scratch/projects/` — new hubs

| Hub | Project days | Pulled from | Notes |
| --- | ------------ | ----------- | ----- |
| `maze-game/` | 1 Maze Design (worksheet, example SVGs) · 2 Keyboard Controls & Wall Collision · 3 Loops + Conditionals collectable | Days 5, 6, 10 | Maze worksheet and four SVGs move here. |
| `platformer/` | 1 Gravity (velocity) · 2 Platforms & Collision (fold in existing `platformer-collision/`) · 3 Objective, score, respawn (build-along script) | Days 12, 13, 14 + `script.md` | Replaces the lone `platformer-collision/` page; keep its URL with an `aliases:` entry. |
| `falling-objects-game/` | 1 Player + falling object + score · 2 Speed and lives · 3 Clones and danger · 4 Game states, sounds, polish | Days 16–19 | The heaviest lessons in the archive (248–316 lines each); the daily pages shrink to pointers. |
| `python-pokemon-data/` | 1 Pandas stats + plots · 2 Design Your Own Pokémon | Days 33, 34 | Datasets live in `reference/datasets/`. |
| `video-game-design/` (exists) | — | Days 21–30 worksheets | Move `brainstorm-worksheet/`, `exit-ticket/`, `peer-feedback-worksheet/` under this hub (date-free versions). |

Existing `teachable-machine-rock-paper-scissors/` stays; `projects/_index.md` card grid gets the new hubs.

Rule for every extracted page: no `date:`, `day_number:`, or week `weight:`; no calendar line; "yesterday"/"Friday" language replaced with "Project Day N" or a self-contained recap; a short teacher-notes block at the bottom of project hubs.

---

## 5. Gap lessons — VEXcode VR scaffold (Days 37–42 and 44)

Seven scaffolded daily pages for a **VEXcode VR** mini-unit (`vr.vex.com`, block-based robot programming in a browser — no hardware). Scaffold only: complete front matter, a one-line description, placeholder objectives, the full section skeleton with `<!-- TODO -->` stubs, and standards drawn from MS-CS-FCP.5 (embedded computing, sensors, hardware I/O) plus 4.5/4.8/4.9. No invented activities; Mr. Willingham fills the work sessions.

- [ ] Day 37 — VEXcode VR — Day 1 (`units: ["VEXcode VR"]`, `resources: ["VEXcode VR"]`, `tags: [vex, robotics, Scratch]`)
- [ ] Day 38 — Day 2
- [ ] Day 39 — Day 3
- [ ] Day 40 — Day 4
- [ ] Day 41 — Day 5
- [ ] Day 42 — Day 6
- [ ] Day 44 — Day 7 (early release)

Day 43 is the archive's word search, carried over.

---

## 6. AGENTS.md updates

- [ ] Project Summary — Scratch is live again: "Live for Q2 2026-27: **Computer Programming with Scratch** (Oct 12 – Dec 18) and **Music Technology**." Remove "no longer taught / unlinked from nav".
- [ ] Repo Map — `content/scratch/` row: "Edit; current-year lessons in `week-N/day-NN/`; reusable projects in `projects/`; reference pages in `reference/`".
- [ ] Path Rules — `<course>` is `scratch` or `music-technology`.
- [ ] Required Front Matter — note the `-04:00` → `-05:00` offset flip on Nov 1, 2026 (and the matching flip back in March).
- [ ] Course Context — rewrite the Scratch block: audience, 44 days across 9 weeks starting Mon 10/12/2026, Day 1 is a DLD, Tue 11/3 off, Thanksgiving week off, early release 12/17–18; unit list per section 2; the `reference/` and `projects/` pages per section 4; the "lesson page is a map, reference pages hold the steps" pattern.
- [ ] Archive section — the 2025-26 Scratch archive is the source the live course was promoted from; still frozen.

---

## 7. Links to replace once the new ones exist

Flagged in copied lessons with `<!-- TODO: new link -->`.

| Where | What |
| ----- | ---- |
| Day 2 | About Me Microsoft Form (`forms.office.com/r/KUY3wCsirJ` carried over) |
| Days 1, 6, 7, 19, 31, 34, 35 | Edpuzzle / Flocabulary / BrainPOP assignments — reassign in those tools (links are via Clever, so no URL change) |
| Day 11 | Boolean Operators learning check on CTLS; Gimkit practice set |
| Day 12 | Gravity and Velocity learning check (`forms.cloud.microsoft/r/GD6W2arjhi` carried over) |
| Day 18 | Gimkit practice set for the unit quiz |
| `reference/share-to-studio/` | Class Scratch studio link(s) — the one place Days 10, 14, 20, 27, 29 point to |
| Day 25 | Pre-presentation form |
| Day 28 | Game summary form for studio descriptions |
| Day 33 | Pokémon stats submission (currently says "submit on CTLS") |
| Hubs | Scratch starter projects on `maze-game/` (1293617748), `platformer/` (1298622870) and `platforms-and-collision/` (1298336874), `falling-objects-game/` (1307434289, 1307458321), Day 9 loops refactor (1295926292) — confirm they are still shared from the class account |
| Archive only | OneDrive box-art folder and the Day 28 audio clips were not carried forward |

---

## Status (end of first build pass)

Done on disk, nothing committed:

- [x] Section 3 infrastructure — menu entry, homepage card, course root with `{{< this-week >}}`, `standards.md` deleted, `reference/_index.md` and `projects/_index.md` card grids.
- [x] Section 4 — all 12 reference pages (plus `practice/` children, `flowcharts/worksheet/` and `flowcharts/example/`), and the `maze-game/`, `platformer/` (with `platforms-and-collision/` moved in under an alias and `build-along/`), `falling-objects-game/`, and `python-pokemon-data/` hubs. VGD worksheets moved under `projects/video-game-design/`.
- [x] Section 2 — all 44 daily lessons and nine week pages. Dates, day numbers, weights, and the DST offset flip verified by script. Front-matter `standards` match each `## Standards` list.
- [x] Section 5 — VEXcode VR Days 37–42 and 44 scaffolded with `draft: true` so TODO pages cannot reach production. Flip `draft: false` when each is filled in. The Week 8 and 9 schedule tables carry "TBD" summaries for those rows until then.
- [x] Section 6 — AGENTS.md updated.
- [ ] Section 7 — links still flagged `<!-- TODO: new link -->` (see list below). Replace as the new forms, studios, and Gimkit sets exist.
- [ ] **Step 7 verification not run.** Neither Hugo nor Homebrew is installed on this Mac, so `hugo --quiet --renderToMemory` could not be executed. A script-level check confirmed every internal link and heading anchor resolves and every standards list matches, but shortcode rendering is unverified until Hugo runs. Install Hugo (`brew install hugo`, or the binary from gohugo.io), then run the verify step and `HUGO_ENV=dev hugo serve --buildFuture --buildDrafts`.

## 8. Order of work

1. Confirm section 0.
2. Section 3 infrastructure (menu, homepage, course root).
3. Section 4 reference pages and project hubs — build these **before** the daily lessons so the lessons can link to real URLs.
4. Section 2 daily lessons, week by week: copy from the archive, re-date, renumber, re-weight, strip what the reference pages now hold, fix "yesterday/next week" language, fill in missing front matter (archive Day 12 has empty `units`/`standards`/`description`).
5. Section 5 gap lessons.
6. Section 6 AGENTS.md.
7. Verify: `hugo --quiet --renderToMemory` (zero output), then `HUGO_ENV=dev hugo serve --buildFuture` and click through every week's schedule table, every reference card, and every project hub. Check `public/units/`, `public/tags/`, `public/resources/` for singular/plural duplicates introduced by the new pages.

**Blocker:** Hugo is not installed on this Mac and git is blocked until the Xcode license is accepted (`sudo xcodebuild -license`). Install Hugo (`brew install hugo`) before step 7.

---

## 9. Out of scope (not touching)

- `content/archive/2025-26/` — frozen.
- `content/music-technology/` — untouched.
- Quiz content, answer keys, CTLS material — never on the site.
- Theme files under `themes/hextra/`.
