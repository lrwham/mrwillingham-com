## Technical Overview

### Framework and Theme
- **Static site generator:** [Hugo](https://gohugo.io/)
- **Theme:** [Hextra](https://github.com/imfing/hextra) (installed as a git submodule) — provides built-in search, dark/light theme toggle, responsive sidebar navigation, and card-based layouts. Dark theme is the default.
- **Config:** [hugo.yaml](hugo.yaml) with `enableGitInfo: true` (uses Git commit metadata for last-modified dates), timezone `America/New_York`, Goldmark renderer with unsafe HTML enabled, and taxonomies for tags, units, standards, and resources.

### Content Organization
```
content/
├── _index.md                  # Homepage
├── music-technology/          # Music Tech course (by week/day)
├── scratch/                   # Programming course (by week/day)
├── troubleshooting/           # Student self-help guides
└── sub-plans/                 # Substitute teacher plans
```
Each lesson follows a **Course → Week → Day** hierarchy, with archetypes in [archetypes/](archetypes/) providing templates for new lessons.

### Custom Shortcodes
Custom shortcodes in [layouts/shortcodes/](layouts/shortcodes/) provide consistent lesson structure and styling:

**Lesson structure (color-coded sections):**
- `{{% objectives %}}` — "Today's Objectives" section (purple) containing "I can…" statements.
- `{{% warmup %}}` — Warmup section (amber/orange); title set by `## Warmup:` header inside.
- `{{% worksession %}}` — Work session block (blue); can be used multiple times per lesson; title set by `## Work Session:` header inside.
- `{{% checkpoint %}}` — Checkpoint / checklist section (red); title set by `### Checkpoint:` header inside; nestable inside warmup/worksession.
- `{{% closing %}}` — Lesson wrap-up section (green); title set by `## Closing:` header inside.

**Utility shortcodes:**
- `{{% alert "Title" %}}` — Styled alert box for announcements; takes title as a positional parameter.
- `{{< button text="..." >}}URL{{< /button >}}` — Styled link button opening in a new tab.
- `{{< callout type="..." >}}` — Styled callout box; types: `default`, `info`, `warning`, `error`, `important`, `tip`; optional `icon` parameter.
- `{{< icon "name" >}}` — Inline icon; takes icon name as a positional parameter.
- `{{< tabs >}}` / `{{< tab name="..." >}}` — Tabbed content for multi-step instructions.
- `{{< clever >}}` — "Login with Clever" SSO button.
- `{{< todays-lesson >}}` — Displays a card for today's lesson (matched by current date) or a "No Lesson for Today" message.
- `{{< recent-lessons count="5" >}}` — Grid of recent lesson cards from the current section.

### Custom Layouts, Partials, and Assets
- [layouts/partials/custom/head-end.html](layouts/partials/custom/head-end.html) — Injects `scratchblocks.js` (v3.6.4) to render ` ```scratch ` fenced code blocks as visual Scratch blocks when `scratchblocks: true` is set in front matter; adds a sidebar collapse toggle with `localStorage` persistence; shows a red **DEV** ribbon when `HUGO_ENV=dev`.
- [layouts/_default/_markup/render-codeblock-scratch.html](layouts/_default/_markup/render-codeblock-scratch.html) — Custom markdown renderer for Scratch code blocks.
- [layouts/bare/single.html](layouts/bare/single.html) — Print-friendly bare layout with page-break styling for printing lessons.
- [assets/css/custom.css](assets/css/custom.css) — Color-coded lesson section styling, card hover effects, sidebar toggle styling, dark/light mode variables.
- [data/icons.yaml](data/icons.yaml) — Custom SVG icon definitions for Scratch, Code.org, and others.
- Static assets in [static/](static/) include the favicon, horizontal logo, Clever login button, Code.org logo, Scratch remix button, and site banner.

### Build and Deployment
Two GitHub Actions workflows in [.github/workflows/](.github/workflows/) deploy to an EC2 instance via SSH (`appleboy/ssh-action`):
- **[deploy.yml](.github/workflows/deploy.yml)** — Production deploy on push to `main`, builds to `/var/www/mrwillingham.com` with `hugo --minify --cleanDestinationDir`.
- **[deploy-dev.yml](.github/workflows/deploy-dev.yml)** — Dev deploy on push to `dev`, builds to `/var/www/dev.mrwillingham.com` with `HUGO_ENV=dev` set so the DEV ribbon appears.

Both workflows `git fetch`, reset hard to the target branch, update submodules, and rebuild with Hugo.