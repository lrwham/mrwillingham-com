---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
description: ""
day_number: 1
units:
  - ""
standards: []
tags:
  - Scratch
resources: []
draft: false
toc: true
scratchblocks: false
weight: 1
---

{{< icon "calendar" >}} **{{ dateFormat "Monday, January 2nd, 2006" .Date }}**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can
- I can
- I can

{{% /objectives %}}

{{% warmup %}}

## Warmup

{{< clever >}}

<!-- Add warmup instructions here -->

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ]
- [ ]

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

<!-- Add work session instructions here -->

<!-- OPTIONAL: Use buttons for project/worksheet links
{{< button text="Open Project" >}}https://scratch.mit.edu{{< /button >}}
-->

<!-- OPTIONAL: Scratch code blocks — set scratchblocks: true in frontmatter
```scratch
when green flag clicked
move (10) steps
```
-->

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ]
- [ ]

{{% /checkpoint %}}

{{% /worksession %}}

<!-- OPTIONAL: Second work session block
{{% worksession %}}

## Work Session 2

{{% checkpoint %}}

### Checkpoint: Work Session 2

- [ ]

{{% /checkpoint %}}

{{% /worksession %}}
-->

{{% closing %}}

## Closing

<!-- Add closing/wrap-up instructions here -->

{{% /closing %}}

## Standards

- [**MS-CS-FCP.X.X**](/scratch/description/#ms-cs-fcpX) — Standard description here.
