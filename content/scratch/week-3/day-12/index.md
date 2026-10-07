---
title: "Day 12: Gravity"
date: 2026-10-27T08:00:00-04:00
description: "Implement gravity with a velocity variable so the player accelerates as it falls, then take a learning check."
day_number: 12
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - boolean
  - variables
  - platformer
resources:
  - Scratch
draft: false
toc: true
scratchblocks: true
weight: 2
---

{{< icon "calendar" >}} **Tuesday, October 27th, 2026**

{{% objectives %}}

## Objectives

- I can implement gravity in a Scratch project using `not`.
- I can use a `velocity` variable to make gravity accelerate.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Basic Gravity

Today is Project Day 1 of the [Platformer](/scratch/projects/platformer/). Start a new project and build the **Ground and Basic Gravity** section:

1. A `ground` sprite — a wide rectangle across the bottom.
2. A `forever` loop that moves the player down when it is `not` touching the ground.
3. A space-bar jump that only works from the ground.
4. Left and right movement, on your own.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] My player falls and stops on the ground.
- [ ] My player jumps with space, only from the ground.
- [ ] My player moves left and right.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Gravity With Velocity

Fixed-speed gravity falls at the same rate forever. Real objects speed up. Follow the **Gravity With Velocity** section of [Platformer Project Day 1](/scratch/projects/platformer/#project-day-1-gravity):

1. Make a `velocity` variable (for all sprites).
2. Replace the gravity loop with the [Gravity and Velocity](/scratch/reference/code-patterns/#gravity-and-velocity) pattern.
3. Change the jump to the [Jumping](/scratch/reference/code-patterns/#jumping) pattern, which sets `velocity` instead of moving the sprite directly.
4. Tune the numbers: stronger jump, stronger gravity. Find what feels right.

Trace what happens frame by frame: in the air, `velocity` goes -1, -2, -3… so the fall speeds up. On the ground it resets to 0.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I can explain how `not`, `and`, and `or` work.
- [ ] My gravity uses a `velocity` variable and the fall speeds up.
- [ ] I adjusted the gravity and jump values to make it feel good.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Learning Check

<!-- TODO: new link — Gravity and Velocity learning check -->
Take the learning check on [Microsoft Forms](https://forms.cloud.microsoft/r/GD6W2arjhi). Practice first with [Gravity and Velocity: Quiz Examples](/scratch/reference/practice/gravity-examples/).

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including Boolean and branches (`not touching ground`).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (the velocity loop).
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data (velocity resets when the sprite touches the ground).
