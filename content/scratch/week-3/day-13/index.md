---
title: "Day 13: Platforms and Collision"
date: 2026-10-28T08:00:00-04:00
description: "Add floating platforms and use or to detect landing, jumping, and wall collisions with the move-check-step-up pattern."
day_number: 13
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - boolean
  - platformer
  - collision
resources:
  - Scratch
draft: false
toc: true
scratchblocks: false
weight: 3
---

{{< icon "calendar" >}} **Wednesday, October 28th, 2026**

{{% objectives %}}

## Objectives

- I can redesign my player sprite to be smaller and simpler for a platformer.
- I can use `or` to detect collisions with both the ground and platforms.
- I can implement wall collision with the move-check-step-up pattern.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Redesign Your Player

Scratch the cat is too big and oddly shaped for a platformer. Open yesterday's gravity project and draw a new costume for your player following the rules in the **Warmup** of [Platforms and Collision](/scratch/projects/platformer/platforms-and-collision/): small, simple shapes, solid fill, facing right.

Only remix the starter project on that page if your gravity project is lost.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I drew a new, smaller player character.
- [ ] It uses simple shapes with a solid fill.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Platforms With Collision

Follow the **Work Session** steps on [Platforms and Collision](/scratch/projects/platformer/platforms-and-collision/), in order:

1. Create the `platform` sprite.
2. Land on platforms using `or`, with `change y by (velocity)` moved to the top of the loop and a `gravity` variable.
3. Add the landing bounce.
4. Jump from platforms with a `jump-velocity` variable.
5. Wall collision with the step-up test, switching movement to the A and D keys.
6. Add more platforms.

Test after every step. The same code, in one place, is on [Scratch Code Patterns](/scratch/reference/code-patterns/#landing-on-platforms).

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I can land on platforms and jump from them.
- [ ] My player stops when walking into the side of a platform.
- [ ] I have at least three platforms at different heights.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you added **landing** (treating platforms like the ground with `or`, plus a bounce) and **wall collision** (the step-up test). You also met the head-bump bug, where jumping into the underside of a platform can stick the player. Design around it for now.

Tomorrow: an objective to collect and a score.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including Boolean and branches (`or` in the landing and wall checks).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (the step-up test).
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data (velocity and touching checks).
