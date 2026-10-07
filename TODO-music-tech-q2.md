# TODO — Move Music Technology to Q2 (Oct 12 – Dec 18, 2026)

Working plan for re-dating the live `content/music-technology/` course from Q1 (Aug 3 – Oct 9) to Q2, filling the days that never got pages, and pulling repeated material into `projects/` and `reference/`. The 2025-26 archive is untouched; it is consulted only as source material for the podcast unit. Nothing is committed until Mr. Willingham says so.

Companion to `TODO-archive-cs-to-live.md`; same calendar, same conventions.

---

## 0. Decisions to confirm before building

- [x] **Keep a record of Q1?** Decided: edit in place. Git history keeps every Q1 page as taught; no snapshot folder.
- [x] **Day mapping.** Q1 and Q2 both have 44 slots, a digital learning day, and one four-day week, but in different places. Recommendation: drop Q1's Day 11 (the DLD placeholder — its only content is "Complete the lesson on CTLS") and give the DLD slot to Q2 Day 1. Q1 Days 1–10 shift to Q2 Days 2–11; Q1 Days 12–44 keep their numbers. No lesson is compressed or cut. The cost is that Weeks 2 and 3 each straddle two units (section 2).
- [x] **Day 1 (DLD, Mon 10/12) content.** Decided: an at-home page — read the syllabus, complete About Me in CTLS, and do the BrainPOP *Sound Waves* lesson (from the 2025-26 archive's independent-work day).
- [x] **Pages that never existed in Q1** — Day 25 (quiz), Day 29 (finish the scene), and the podcast unit, Days 37–44. Decided: write all ten as full lessons, the podcast days adapted from the archive (2025-26 Days 4–11) to Soundtrap, following the Q1 week tables.
- [ ] **Conference-week early release (Tue 10/13 – Fri 10/16).** Q2 Days 2–5 are shortened periods. Q1 Days 1–4 (welcome, scavenger hunt, finish the hunt, layering) were full periods except Day 3. The plan adds a short-class alert to each and a "finish tomorrow if needed" line; the scavenger hunt due date moves to Day 5. Confirm, or say which content to trim.
- [x] **Unit names.** Decided: `Loops and Layering`, `Beat Making` (unchanged), `Music Reading` (unchanged), `Melody and Form` (absorbing Day 23's `Harmony & Form`), `Sound for Screen`, `Podcasts`. Term-page URLs change; nothing else does.
- [ ] **Q1-specific text to remove.** The Day 16 "Friday's technical problems" alert, BEACON short-period notes (Days 12, 13, 15 closings), the fall-break language (Days 34, 35, Week 7 and 8 indexes), the Labor Day four-day Week 6, and the magnet-presentation short class on Day 29. All replaced with Q2 equivalents or dropped.
- [ ] **Per-quarter links.** Three Microsoft Forms (MIDI controller scavenger hunt, Mystery Transcription guess form, Computer Check-in) and every "today's CTLS post" reference carry over as-is, flagged `<!-- TODO: new link -->` where a new form will be needed. Day 9 also carries an existing `<!-- TODO: list the exact keys -->` for the assigned drum keys.

---

## 1. Calendar and numbering

Same calendar as the Scratch plan (district calendar revised 3/11/26).

| Week | Dates | Days | Notes |
| ---- | ----- | ---- | ----- |
| 1 | Mon 10/12 – Fri 10/16 | 1–5 | 10/12 Digital Learning Day; 10/13–16 early release |
| 2 | Mon 10/19 – Fri 10/23 | 6–10 | |
| 3 | Mon 10/26 – Fri 10/30 | 11–15 | |
| 4 | Mon 11/2, Wed 11/4 – Fri 11/6 | 16–19 | Tue 11/3 student holiday |
| 5 | Mon 11/9 – Fri 11/13 | 20–24 | |
| 6 | Mon 11/16 – Fri 11/20 | 25–29 | Last day before Thanksgiving |
| — | Mon 11/23 – Fri 11/27 | — | Thanksgiving |
| 7 | Mon 11/30 – Fri 12/4 | 30–34 | |
| 8 | Mon 12/7 – Fri 12/11 | 35–39 | |
| 9 | Mon 12/14 – Fri 12/18 | 40–44 | Thu 12/17 and Fri 12/18 early release |

**Dates.** All lessons get `T08:00:00` (Q1 used `06:00` on Days 12–17). Offset `-04:00` for Days 1–15 (through Oct 30), `-05:00` for Days 16–44 (DST ends Nov 1).

**Week weights** stay 100 → 20. Day `weight` is the weekday position (Mon 1 … Fri 5); Week 4 uses 1, 3, 4, 5.

---

## 2. Day-by-day mapping (Q1 → Q2)

Titles keep "Day N:" with the new number. "Tomorrow", "Friday", "Monday after break" language is rewritten to match the new sequence.

### Week 1 — Loops and Layering (weight 100)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 1 | Mon 10/12 | *new* | Digital Learning Day: Syllabus, About Me, and Sound Waves | At-home page per section 0. Links `reference/daily-routine/`. |
| 2 | Tue 10/13 | Day 1 | Welcome to Music Technology | Short-class alert. "Read all instructions" alert and log-off procedure move to `reference/daily-routine/`; Soundtrap login and vocab move to `reference/soundtrap-basics/`. About Me already done on Day 1 — that work session becomes a quick CTLS check. |
| 3 | Wed 10/14 | Day 2 | Soundtrap Loop Scavenger Hunt | Short-class alert. Sound-library tabs and vocab link to `soundtrap-basics/`; the five-set table lives on the `projects/loops-and-layering/` hub. Due date → Friday 10/16. |
| 4 | Thu 10/15 | Day 3 | Finish the Scavenger Hunt | Already a 20-minute lesson; fits early release as written. Set table replaced with a hub link. |
| 5 | Fri 10/16 | Day 4 | Layering and Dynamics | Short-class alert. Layering/dynamics explanation and vocab move to `reference/arranging-loops/`; the "Apply It" steps stay. Export video link moves to `reference/turning-in-work/`. |

### Week 2 — Loops to Beats (weight 90)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 6 | Mon 10/19 | Day 5 | Choosing Loops by Category and Genre | Loop-role table and genre-first steps move to `reference/arranging-loops/`. |
| 7 | Tue 10/20 | Day 6 | Introduction to Drums | Parts-of-the-kit list moves to `reference/beat-making/`. |
| 8 | Wed 10/21 | Day 7 | MIDI and the Beat Grid | Patterns Beatmaker setup (with the screenshot) and the rock-beat grid move to `reference/beat-making/`; lesson links the grid. |
| 9 | Thu 10/22 | Day 8 | Writing a Drum Beat | Rock-beat grid repeated from Day 7 and both fill grids move to `reference/beat-making/`. MP3 export steps → `turning-in-work/`. Rock Beat due Thu 10/22. |
| 10 | Fri 10/23 | Day 9 | Four on the Floor and Quantization | Live-recording tabs and the quantization explanation move to `reference/beat-making/`. MIDI controller form flagged. Existing key-list TODO stays flagged. |

### Week 3 — Beats to Music Reading (weight 80)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 11 | Mon 10/26 | Day 10 | Loop Song and Two Beats | Loop Song requirements move to the `projects/loops-and-layering/` hub (Project Day 5); quantization review links `beat-making/`. |
| 12 | Tue 10/27 | Day 12 | Music Reading 101 | Staff, clef, grand staff, keyboard, whole/half steps move to `reference/music-reading-101/`; practice links to `reference/note-reading-practice/`. BEACON note dropped. |
| 13 | Wed 10/28 | Day 13 | Rhythm Primer and Meet MuseScore | Note values, rests, time signature → `music-reading-101/`; MuseScore first-launch steps → `reference/musescore-basics/`. Short-period line dropped. |
| 14 | Thu 10/29 | Day 14 | Ode to Joy Transcription | Score-setup steps, "when it sounds wrong" table, and PDF export → `musescore-basics/` and `turning-in-work/`. Melody table moves to `projects/mystery-transcription/` (Project Day 1). |
| 15 | Fri 10/30 | Day 15 | Mystery Transcription | Melody table → hub (Project Day 2). Closing's BEACON/"Monday short period" line dropped. |

### Week 4 — Music Reading (weight 70) — four days

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 16 | Mon 11/2 | Day 16 | Mystery Transcription: Nine Melodies | "You do not need to finish Ode to Joy" alert dropped. Video and guess form stay; form flagged. Hub Project Day 3. |
| — | Tue 11/3 | — | *Student holiday* | Unlinked row. |
| 17 | Wed 11/4 | Day 17 | Mystery Transcription Reveal | `all-mysteries.mp3` stays in the day bundle. C major scale and first melody → `reference/melody-and-form/`. |
| 18 | Thu 11/5 | Day 18 | A Minor and the Tonic | "How we turn work in" → `turning-in-work/` (the lesson keeps the "check yesterday's submission" callout). A minor scale table and tonic vocab → `melody-and-form/`. |
| 19 | Fri 11/6 | Day 19 | Form: Binary and Ternary | Form table and vocab → `melody-and-form/`; the copy-paste-vary recipe (duplicated on Days 19 and 20) → `musescore-basics/`. |

### Week 5 — Melody and Form (weight 60)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 20 | Mon 11/9 | Day 20 | Tonic, Dominant, and Cadence | Scale-numbering and tonic/dominant/cadence tables → `melody-and-form/`. "Monday you add a repeat sign" → "tomorrow". |
| 21 | Tue 11/10 | Day 21 | One Piece, One Period: Binary or Ternary | Requirements, `title-subtitle-name.png`, and advice move to the `projects/melody-project/` hub. "Quiz this Friday, September 4th" → "quiz Monday, November 16th" (Days 21–24). |
| 22 | Wed 11/11 | Day 22 | Music Reading and the Listening Party | Practice buttons → `note-reading-practice/`. |
| 23 | Thu 11/12 | Day 23 | Chords and Harmony: Building ABA in Soundtrap | Chord-picker guide and the three progressions move to `projects/aba-chords/`. Unit → Melody and Form. |
| 24 | Fri 11/13 | Day 24 | Review Day: Note Reading, Form, Tonic and Dominant | Quiz is Monday. |

### Week 6 — Quiz, then Sound for Screen (weight 50)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 25 | Mon 11/16 | *new* | Quiz: Music Reading and Form | Short page: note-reading warmup, quiz on CTLS, early finisher = open Soundtrap or MuseScore. `standards: []`? No — RE.2 fits. |
| 26 | Tue 11/17 | Day 26 | Sound for Screen: Intro and Ambience | Sync point / ambience / diegetic vocab and the approved-sources rule → `reference/sound-design/`. Hub `projects/urban-runner/` Project Day 1. |
| 27 | Wed 11/18 | Day 27 | Volume Automation: Approaching Vehicles | Inverse-square and Doppler explanation + `automation-curve.png` → `sound-design/` (the image is currently duplicated in Days 28 and 34). |
| 28 | Thu 11/19 | Day 28 | Footsteps, Jumps, and Foley | Footstep-pack table and chop/sync steps → hub; six required elements → hub (they are only in this closing today). "Friday is a short class" → "Friday is the last day before break; finish today." |
| 29 | Fri 11/20 | *new* | Finish the Scene | Written from the Q1 Week 6 table row: check the six required elements, finish, save. Upload is after break. |

### Week 7 — Sound for Screen (weight 40)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 30 | Mon 11/30 | Day 30 | Upload and Vote | Upload + watch-and-vote procedure → `reference/peer-voting/` (duplicated on Day 36). "Required Elements list on the assignment" → hub link. |
| 31 | Tue 12/1 | Day 31 | Recording Day | Mic setup / test / teardown steps → `reference/recording-setup/` (duplicated on Day 32). BrainPOP warmup stays. Found Sound homework due Thu 12/3. |
| 32 | Wed 12/2 | Day 32 | Take Out the Trash | Gain/headroom vocab → `recording-setup/`. Check-in form flagged. |
| 33 | Thu 12/3 | Day 33 | Effects Practice | Effects vocab → `sound-design/` (duplicated on Day 34). |
| 34 | Fri 12/4 | Day 34 | Sound Design Project | Requirements, clip images, effects list, and rubric move to `projects/sound-design-project/`. "Due Monday after fall break" → "due Monday 12/7". |

### Week 8 — Sound Design Wrap-Up and Podcasts (weight 30)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 35 | Mon 12/7 | Day 35 | Sound Design Project: Finish and Submit | Rubric link `../../week-7/day-34/#rubric` → hub. Early-finisher brainstorm table → `projects/podcast/`. |
| 36 | Tue 12/8 | Day 36 | Sound Design Project: Share and Vote | Procedure → `peer-voting/`. |
| 37 | Wed 12/9 | *new* | Podcast Brainstorm | From the Q1 table + archive Day 4: four categories, two intros. Hub Project Day 1. |
| 38 | Thu 12/10 | *new* | Record Your Intros and Choose a Topic | Archive Day 5, in Soundtrap: record both intros, trim and split, pick the topic. |
| 39 | Fri 12/11 | *new* | Write Your Script | Archive Day 6: script expectations (intro, main content, conclusion, audio notes) in Word Online. Script due Tue 12/15. |

### Week 9 — Podcasts (weight 20)

| Q2 | Date | Q1 | Title | Changes |
| -- | ---- | -- | ----- | ------- |
| 40 | Mon 12/14 | *new* | Intro Music | Archive Day 7: 2–4 loops, 10–20 seconds that builds, exported MP3. Links `arranging-loops/`. |
| 41 | Tue 12/15 | *new* | Peer Feedback and Final Script | Archive Day 8: read two scripts, specific feedback, revise, submit. |
| 42 | Wed 12/16 | *new* | Record Your Podcast | Archive Day 9: mic setup via `recording-setup/`, record one section at a time. |
| 43 | Thu 12/17 | *new* | Edit Your Podcast | Early release. Archive Day 10: re-record weak sections, cut mistakes, balance, add music and SFX. |
| 44 | Fri 12/18 | *new* | Finish and Share | Early release. Export MP3, upload to CTLS, listen and comment. Podcast due today. |

Both Week 9 early-release days land on the edit/finish days. Flagged in section 0; if that is too tight, Day 41's revision time can absorb the first edit pass.

---

## 3. Infrastructure

- [ ] `content/music-technology/_index.md` — swap the "Podcast Vocabulary" card for a "Reference" card and update the Project Library subtitle. Drop stale `lastmod`.
- [ ] `content/music-technology/reference/_index.md` — card grid for the new pages.
- [ ] `content/music-technology/projects/_index.md` — card grid including the new hubs; keep Film Scoring and Classical Remix.
- [ ] `content/_index.md` and `hugo.yaml` — no change (Music Tech is already linked).
- [ ] Delete `.DS_Store` files under `content/music-technology/` (four of them) and add nothing new.

---

## 4. Reference pages (`content/music-technology/reference/`)

| Page | Holds | Pulled from | Linked by |
| ---- | ----- | ----------- | --------- |
| `daily-routine/` | Read everything first, objectives → warmup → work session → closing, where CTLS and Synergy live, what to bring, absences, the log-off procedure (save, close tabs, log off, headphones back) | Day 1 alerts and closing; every "save and log off" closing | Course root, Days 1, 2 |
| `soundtrap-basics/` | Login (student email + lunch number, do not guess), Enter Studio, headphone volume check, Sound library (set key and tempo, filter, preview, add), saving, core vocab (DAW, project, track, loop, tempo, scale type) | Days 1, 2 | Days 2–11, 23, 26 |
| `turning-in-work/` | The three rules (original title, two exports, both attached), MuseScore MP3 + PDF export, Soundtrap MP3 export, Soundtrap video export and the CTLS discussion upload, the export-and-upload video | Days 8, 10, 14, 15, 18, 21, 22, 30, 35 | Every graded day |
| `arranging-loops/` | Layering over time (the measures table), dynamics and balance, loop roles table, genre-first order, vocab (layering, measure, dynamics, balance, texture, cohesive, genre, arrangement) | Days 4, 5 | Days 5, 6, 11, 40 |
| `beat-making/` | Parts of the kit, Patterns Beatmaker setup (with screenshot), the rock-beat grid, both fill grids, four-on-the-floor, recording a live drum track, quantization as rounding + grid choice + how-to, MIDI definition | Days 6–10, 13 | Days 7–11, 23 |
| `music-reading-101/` | Staff, clefs, grand staff, middle C, keyboard landmarks (D E F B), octaves, whole/half steps, note values, rests, dots, time signature, counting; link to the slides PDF | Days 12, 13 | Days 12, 13, 24, 25 |
| `note-reading-practice/` | The musictheory.net links (treble, bass, mixed, keyboard, keyboard reverse) with the "perfect score twice" targets, and what the quiz covers | Days 12, 13, 21, 22, 24 | Days 12–25 |
| `musescore-basics/` | New-score setup, the N key, durations first, Cmd+Z, playback, "when it sounds wrong" table, tempo marking, title via Score Properties, insert measures, copy-paste-vary recipe, lyric numbering (Cmd+L) | Days 13, 14, 17–21 | Days 13–22 |
| `melody-and-form/` | C major and A minor scale tables, scale numbering, tonic / dominant / cadence (tables and the comma-period idea), the ending formula, form (binary, ternary, letters), the B-section "change two things" list, A minor pentatonic | Days 17–23 | Days 17–25, 40 |
| `sound-design/` | Sync point, ambience, diegetic/non-diegetic, approved sound sources, the automation curve (image, inverse square law, Doppler), Foley basics (chop, sync, vary, jumps are two sounds), effects vocab (reverb, delay, EQ, distortion, modulation, pitch shift) | Days 26–28, 33, 34 | Days 26–36, 43 |
| `recording-setup/` | Analog vs digital notes, clean-take rules, mic setup / test / tear down steps, gain and headroom, the "quiet, recording" take protocol | Days 31, 32 | Days 31, 32, 38, 42 |
| `peer-voting/` | Assignment chart, watch your six, rank, one form once, points, "vote for the work not the person" | Days 30, 36 | Days 30, 36, 44 |
| `podcast-vocab/` (exists) | Unchanged; add a card. | — | Days 37–44 |

### Project hubs (`content/music-technology/projects/`)

| Hub | Project days | Pulled from |
| --- | ------------ | ----------- |
| `loops-and-layering/` | 1 Scavenger hunt (five-set table, naming themes) · 2 Finish and pick one · 3 Share out and rebuild as an arrangement · 4 Genre-first build · 5 Loop Song (requirements, export) | Days 2–5, 10 |
| `mystery-transcription/` | 1 Ode to Joy (melody table) · 2 Mystery melody (table, two rules) · 3 Nine melodies and the guess form · 4 Reveal and diagnosis | Days 14–17 |
| `melody-project/` | 1 A minor melody that ends on the tonic · 2 Binary and ternary from one A section · 3 Tonic-dominant binary piece · 4 One Piece, One Period (requirements, header image, advice) · 5 Listening party | Days 18–22 |
| `aba-chords/` | One day: Soundtrap Chords tool, the three progressions, beat, pentatonic improvisation | Day 23 |
| `urban-runner/` | 1 Coin and ambience · 2 Vehicles and automation · 3 Footsteps and Foley (pack table) · 4 Finish · 5 Upload and vote; the six required elements as the rubric | Days 26–30 |
| `sound-design-project/` | Clip choice (images), requirements, effects to try, automation, rubric, finish checklist, share and vote | Days 34–36 |
| `podcast/` | 1 Brainstorm (categories table) · 2 Intros and topic · 3 Script (expectations) · 4 Intro music · 5 Peer feedback and final script · 6 Record · 7 Edit · 8 Finish and share | Day 35 early-finisher block + archive Days 4–11 |
| `film-scoring/`, `classical-remix/` (exist) | Unchanged. | — |

Rules as before: no `date:`, `day_number:`, or week `weight:` on any of these; "Project Day N"; a short teacher-notes block on each hub; daily pages become maps that link out.

---

## 5. AGENTS.md updates

- [ ] Project Summary — both courses live for Q2.
- [ ] Repo Map — `content/music-technology/` row gains the same "lessons are maps" note as Scratch.
- [ ] Course Context (Music Technology) — rewrite: 44 days Oct 12 – Dec 18, Day 1 DLD, early-release and holiday notes, unit list per section 2 with hub and reference paths, the quiz on Day 25, Thanksgiving between Days 29 and 30, podcast due Day 44.
- [ ] Taxonomy note — record the renamed unit values if section 0 approves them.

---

## 6. Links to replace or confirm

| Where | What |
| ----- | ---- |
| Day 10 | MIDI Controller Scavenger Hunt form (embedded iframe + backup link) |
| Day 16 | Mystery Transcription guess form |
| Day 32 | Computer Check-in form |
| Days 28, 33 | Footstep Sound Pack and Ryze-Realm-Warp.zip — posted on CTLS, no site change |
| Days 30, 36, 44 | Assignment charts and voting forms on CTLS posts |
| Days 1, 2 | About Me activity and syllabus in CTLS; `static/downloads/music-tech-syllabus.docx` carries over |
| Day 10 | `<!-- TODO: list the exact keys -->` for the assigned drum keys (pre-existing) |

---

## Status (end of build pass)

Done on disk, nothing committed:

- [x] Sections 3 and 4 — course root, reference index, project index; all 12 new reference pages; the seven hubs plus `podcast/sample-script/`. Images moved to the pages that own them (Patterns Beatmaker screenshot → `reference/beat-making/`, automation curve → `reference/sound-design/`, score header → `projects/melody-project/`, the three clip stills → `projects/sound-design-project/`, the Soundtrap export screenshot → `reference/turning-in-work/`). `.DS_Store` files removed.
- [x] Section 2 — folders restructured (Q1 Days 1–10 → Q2 Days 2–11, Q1 Day 11 deleted, Q1 Day 20 moved to Week 5), every lesson and week page rewritten, all 44 days present. `all-mysteries.mp3` stays in `week-4/day-17/`.
- [x] The ten new lessons — Day 1 (DLD), Day 25 (quiz), Day 29 (finish the scene), Days 37–44 (podcast).
- [x] Unit values renamed per section 0.
- [x] Section 5 — AGENTS.md updated.
- [ ] Section 6 links — flagged `<!-- TODO: new link -->` on Days 10, 16, 32; the drum-keys TODO on Day 10 is still open.
- [ ] **Verification.** The automated link/anchor/standards check could not be run (the Claude Code sandbox classifier was failing on every shell call at the end of the build). Every deep-link anchor used in the lessons and hubs was checked by hand against its target heading and resolves. The script is saved at the session scratchpad as `verify_mt.py` and is reproduced in section 9 below; run it, then `hugo --quiet --renderToMemory` once Hugo is installed, then `HUGO_ENV=dev hugo serve --buildFuture`.

## 9. Verification script

Save as `verify_mt.py` anywhere and run `python3 verify_mt.py` from the repo root. It checks every internal link, image, download, and heading anchor under `content/music-technology/`, confirms each lesson's front-matter `standards` match its `## Standards` section, prints the day number, date, unit, and title of all 44 days in order, greps for leftover Q1 language (September, August, fall break, BEACON, magnet), and lists the remaining `TODO` markers.

```python
import re, os, glob
from collections import Counter

files = glob.glob('content/music-technology/**/*.md', recursive=True)

def url_for(path):
    p = path[len('content'):]
    p = re.sub(r'/(_?index)\.md$', '/', p)
    return re.sub(r'\.md$', '/', p)

urls = {url_for(f): f for f in glob.glob('content/**/*.md', recursive=True)}
for f in glob.glob('content/**/*.md', recursive=True):
    m = re.search(r'^aliases:\n((?:  - .*\n)+)', open(f).read(), re.M)
    if m:
        for a in re.findall(r'  - (.*)', m.group(1)):
            urls[a.strip()] = f
for f in glob.glob('content/music-technology/**/*', recursive=True):
    if os.path.isfile(f) and not f.endswith('.md'):
        urls[f[len('content'):]] = f
for f in glob.glob('static/**/*', recursive=True):
    if os.path.isfile(f):
        urls[f[len('static'):]] = f

def anchors(f):
    out = set()
    for h in re.findall(r'^#{1,6} (.*)$', open(f).read(), re.M):
        h = re.sub(r'`', '', h).strip().lower()
        h = re.sub(r'[^\w\s-]', '', h)
        out.add(re.sub(r'\s+', '-', h))
    return out

bad = []
for f in files:
    s = open(f).read()
    links = (re.findall(r'\]\(([^)\s]+)\)', s)
             + re.findall(r'\{\{< button[^>]*>\}\}([^{]+)\{\{< /button >\}\}', s)
             + re.findall(r'link="([^"]+)"', s)
             + re.findall(r'src="([^"]+)"', s))
    for l in links:
        l = l.strip()
        if l.startswith(('http', 'mailto')):
            continue
        frag = None
        if '#' in l:
            l, frag = l.split('#', 1)
        if l == '':
            target = url_for(f)
        elif l.startswith('/'):
            target = l
        else:
            target = os.path.normpath(os.path.join(url_for(f), l))
            if l.endswith('/') and not target.endswith('/'):
                target += '/'
        tf = urls.get(target) or urls.get(target.rstrip('/') + '/') or urls.get(target.rstrip('/'))
        if not tf:
            bad.append((f, l, 'MISSING')); continue
        if frag and not frag.startswith('msmtc8') and tf.endswith('.md') and frag not in anchors(tf):
            bad.append((f, l + '#' + frag, 'NO ANCHOR in ' + tf))
for b in bad:
    print(b)
print('links: checked', len(files), 'files;', len(bad), 'problems')

print('--- days')
for f in sorted(glob.glob('content/music-technology/week-*/day-*/index.md'),
                key=lambda x: int(re.search(r'day-(\d+)', x).group(1))):
    s = open(f).read(); fm = s.split('---')[1]; body = s.split('---', 2)[2]
    std = re.findall(r'  - (MSMTC8\.[A-Z]+\.\d)', fm)
    std2 = re.findall(r'\[\*\*(MSMTC8\.[A-Z]+\.\d)\*\*\]', body)
    if sorted(std) != sorted(std2):
        print('STANDARDS MISMATCH', f, std, std2)
    print(re.search(r'day_number: (\d+)', fm).group(1), re.search(r'date: (\S+)', fm).group(1),
          re.search(r'units:\n  - "([^"]+)"', fm).group(1), '|', re.search(r'title: "(.*)"', fm).group(1))

print('--- leftover Q1 language')
pat = re.compile(r'september|august|fall break|BEACON|magnet|technical problems', re.I)
for f in files:
    for i, line in enumerate(open(f), 1):
        if pat.search(line):
            print(f, i, line.strip()[:100])

print('--- TODOs')
for f in files:
    for i, line in enumerate(open(f), 1):
        if 'TODO' in line:
            print(f, i, line.strip()[:100])
```

## 7. Order of work

1. Confirm section 0.
2. Section 4 reference pages and hubs first, so lessons link to real URLs.
3. Section 2, week by week: re-date, renumber (Days 1–10 shift), re-weight, strip what the reference pages hold, rewrite sequence language, drop Q1-specific alerts.
4. The ten new lessons (Days 1, 25, 29, 37–44).
5. Section 3 landing pages, section 5 AGENTS.md.
6. Verify: link and anchor script, standards consistency, then `hugo --quiet --renderToMemory` once Hugo is installed, then `HUGO_ENV=dev hugo serve --buildFuture` and click through every week.

---

## 8. Out of scope

- `content/archive/2025-26/` — read-only source for the podcast unit.
- `content/scratch/` — done under its own plan.
- Quiz content and answer keys — never on the site.
