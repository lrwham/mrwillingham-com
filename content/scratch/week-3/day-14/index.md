---
title: "Day 14: Platformer Review"
date: 2026-10-29T08:00:00-04:00
description: "Add a collectible objective sprite with a score variable and respawn loop to complete the platformer."
day_number: 14
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.4.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - platformer
  - variables
  - Code.org
resources:
  - Scratch
  - Code.org
draft: false
toc: true
scratchblocks: false
weight: 4
---

{{< icon "calendar" >}} **Thursday, October 29th, 2026**

{{% objectives %}}

## Objectives

- I can complete a platformer game in Scratch.
- I can use loops, conditionals, and variables to create a game mechanic.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Code.org Nested Loops

Log in to Clever, open Code.org, and start **Lesson 14: Nested Loops**.

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I started Lesson 14: Nested Loops.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Objective and Score

Follow **Project Day 3** on the [Platformer](/scratch/projects/platformer/#project-day-3-objective-and-score) page. Use its starter project only if your own code is not working.

1. Create an objective sprite (coin, star, gem, key) about 20–30 pixels.
2. Place it on a platform the player has to work to reach.
3. Make a `score` variable and set it to 0 on the green flag.
4. When the player touches the objective: hide it and add 1 to `score`.
5. Reset the player to the start so they have to cross the platforms again.
6. Respawn the objective after a short wait.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] An objective sits on a platform.
- [ ] Touching it adds 1 to `score` and hides it.
- [ ] The player is sent back to the start.
- [ ] The objective reappears so it can be collected again.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Play Each Other's Games

Share your game with a partner and play theirs. What do you like? What would you change?

<!-- TODO: new link — class studio links; see /scratch/reference/share-to-studio/ -->
Mr. Willingham may add a few to the class studio: [Share to the Class Studio](/scratch/reference/share-to-studio/).

{{% /closing %}}

## Standards

- [**MS-CS-FCP.4.2**](/scratch/description/#ms-cs-fcp4) — Utilize the design process to brainstorm, implement, test, and revise an idea (placing and testing the objective).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (collect, reset, respawn).
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data or user input (the touching check and score).
