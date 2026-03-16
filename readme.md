# Add Content

To make a new page `hugo new content music-technology/dayxx.md`. The archetype includes the front matter..

# Serve Local Development Site

`HUGO_ENV=dev hugo serve --buildFuture --buildDrafts` will serve the site locally and include any content with a future publish date or marked as a draft.

`HUGO_ENV=dev` simply displays a dev banner in the corner of the page to visually remind you that you are viewing the development version of the site. It is used in the Github action that deploys that development server.

# Install GIT Submodules for Themes

`git submodule update --init --recursive`

# Github Actions Setup

Generate keys on the server that will host the website. Then add the username, host IP, and SSH key as secrets in the Github action config.

### Generate New Keys

```bash
ssh-keygen -t ed25519 -f ~/.ssh/deploy_key -N ""
```

### Authorize Keys

```bash
cat ~/.ssh/deploy_key.pub >> ~/.ssh/authorized_keys
```

### Copy & Paste Secret Key

Manually and copy & paste

```bash
cat ~/.ssh/deploy_key
```

# Project Structure

## Content

All lesson content lives in `content/`. Each active class has its own subdirectory:

```
content/
├── _index.md
├── music-technology/    # Music Technology class
│   └── week-1/
│       ├── day-1/
│       ├── day-2/
│       └── ...
├── scratch/             # Scratch programming class
├── sub-plans/           # Substitute teacher plans
├── troubleshooting/     # Troubleshooting guides
└── archive/             # Past classes (preserved, not actively published)
    ├── computer-programming/
    └── music-technology/
```

Each class is organized into weekly folders (`week-1/`, `week-2/`, etc.), with individual day folders containing an `index.md` lesson file. Past classes are moved into `content/archive/` as subdirectories.

## Lesson Front Matter

Day files use these front matter fields:

| Field           | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `title`         | Lesson title, e.g. `"Day 1: Computer Lab Basics"`              |
| `date`          | Publish date (`YYYY-MM-DD`)                                    |
| `description`   | Short summary of the lesson                                    |
| `day_number`    | Numeric day within the week                                    |
| `weight`        | Sort order                                                     |
| `units`         | List of unit names the lesson belongs to                       |
| `tags`          | Topic tags                                                     |
| `resources`     | Tools used (e.g. `Edpuzzle`, `BrainPOP`)                       |
| `scratchblocks` | Set to `true` to enable Scratch block generation from markdown |

# Shortcodes

## Lesson Structure Shortcodes

These paired shortcodes define the sections of a lesson page. They all render a styled section with a header and markdown-rendered inner content.

### `objectives`

Used in every daily lesson.

No parameters. Renders a "Today's Objectives" section. Inner content is typically a bulleted list of "I can..." statements.

```markdown
{{</* objectives */>}}
- I can successfully use loops in GarageBand.
- I can follow class and safety procedures.
{{</* /objectives */>}}
```

### `warmup`

Used in every daily lesson.

Takes a title as a positional parameter. Renders a "Warmup: [Title]" section.

```markdown
{{</* warmup "Edpuzzle Video" */>}}
**Step 1:** Go to Clever and log in...
{{</* /warmup */>}}
```

### `worksession`

Used in every daily lesson. Use multiple sections when the work demands it.

Takes a title as a positional parameter. Renders a "Work Session: [Title]" section.

```markdown
{{</* worksession "Safety and Class Procedures" */>}}
After the warmup, we'll discuss class procedures...
{{</* /worksession */>}}
```

### `checkpoint`

Used in every daily lesson. Place at critical points during the warmup and work session. At least one checkpoint at the end of each warmup and work session.

Takes a title/number as a positional parameter. Renders a "Checkpoint: [Title]" section, typically containing a checklist.

```markdown
{{</* checkpoint "Warmup" */>}}
- [x] I have finished the Edpuzzle video.
{{</* /checkpoint */>}}
```

### `closing`

Used in every daily lesson.

Takes a title as a positional parameter. Renders a "Closing: [Title]" section.

```markdown
{{</* closing "Next Steps" */>}}
Tomorrow we will learn about **layering and timing**.
{{</* /closing */>}}
```

## Utility Shortcodes

### `alert`

Used as needed in daily lessons or elsewhere.

Paired. Takes a title as a positional parameter. Renders a styled alert box.

```markdown
{{</* alert "Important" */>}}
Remember to save your work to OneDrive!
{{</* /alert */>}}
```

### `button`

Used as needed in daily lessons or elsewhere.

Paired. Takes a `text` named parameter for the label. Inner content is the URL. Renders a styled link button that opens in a new tab.

```markdown
{{</* button text="Go to Clever" */>}}https://clever.com/in/ccsd{{</* /button */>}}
```

### `todays-lesson`

Used on the main `_index.md` for a course.

Self-closing, no parameters. Displays a card for today's lesson (matched by date), or a "No Lesson for Today" message.

```markdown
{{</* todays-lesson */>}}
```

### `recent-lessons`

Used on the main `_index.md` for a course.

Self-closing. Optional `count` parameter (defaults to 5). Displays a grid of recent lesson cards from the current section, excluding today.

```markdown
{{</* recent-lessons count=5 */>}}
```
