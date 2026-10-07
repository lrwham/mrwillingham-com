---
title: "Day 9: Loops"
date: 2026-10-22T08:00:00-04:00
description: "Watch an introduction to loops, complete Code.org Lesson 12 levels 1–10, and refactor a Scratch project with repeat loops."
day_number: 9
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - Code.org
  - loops
resources:
  - Scratch
  - Code.org
draft: false
toc: true
scratchblocks: true
weight: 4
---

{{< icon "calendar" >}} **Thursday, October 22nd, 2026**

{{% objectives %}}

## Objectives

- I can use loops to repeat blocks of code in Scratch.
- I can identify when a loop makes code more efficient.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Introduction to Loops

1. Watch the first Code.org video on loops.

<video controls>
  <source src="https://s3.amazonaws.com/videos.code.org/csf/BB-8_2-5.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

2. Log in to Clever, open Code.org, and complete **levels 1–5** of **Lesson 12: Loops with Rey and BB-8**.

{{< clever >}}

The videos inside the lesson are hosted on YouTube, which is blocked at school. Use [this alternate link for the second video](https://s3.amazonaws.com/videos.code.org/csf/BB-8_repeat.mp4).

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I watched the loops video.
- [ ] I completed levels 1–5 of Lesson 12.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Loops in Scratch

You have already used one loop: `forever`. It repeats the blocks inside as fast as it can until the program stops, which is why it is perfect for things you want to keep checking, like your maze's wall collision.

Loops also make code **shorter**. Which of these is better?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

```scratch
when green flag clicked
pen down
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees
```

```scratch
when green flag clicked
pen down
repeat (4)
move (10) steps
turn cw (90) degrees
end
```

</div>

### Try It

<!-- TODO: new link — confirm the loops refactor project is still shared -->
Remix [this Scratch project](https://scratch.mit.edu/projects/1295926292). It works, but it does not use loops. Make the code shorter by replacing repeated blocks with `repeat` loops. The project should behave exactly the same when you are done.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I replaced repeated blocks with loops.
- [ ] I can explain why a loop is more efficient than copying the same blocks.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Code.org

Back in Clever, complete **levels 6–10** of Lesson 12: Loops with Rey and BB-8.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including iteration (loops).
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including loops.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (the Code.org levels).
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop (the refactored project).
