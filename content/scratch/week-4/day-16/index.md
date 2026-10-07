---
title: "Day 16: New Game: Falling Objects"
date: 2026-11-02T08:00:00-05:00
description: "Build a playable falling-objects game from a blank project using motion, loops, conditionals, and a score variable."
day_number: 16
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - review
  - loops
  - conditionals
  - variables
resources:
  - Scratch
draft: false
toc: true
scratchblocks: false
weight: 1
---

{{< icon "calendar" >}} **Monday, November 2nd, 2026**

{{% objectives %}}

## Objectives

- I can use key presses and motion blocks to move a sprite.
- I can use a `forever` loop with `if` blocks to create game behavior.
- I can use a variable to track score.

{{% /objectives %}}

{{% warmup %}}

## Warmup: What Do You Remember?

Answer in your head, then check with a neighbor:

| Question | Hint |
| --- | --- |
| What block makes code run over and over? | Control category, gold |
| What block makes code run *only when* something is true? | Also gold, shaped like a mouth |
| What category holds `change x by` and `change y by`? | Blue |
| What is a **variable**? | Think of `score` |
| What does `when green flag clicked` do? | The starting point |

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I can name the loop block, the conditional block, and the motion category.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: A New Game

We are starting fresh. Objects fall from the sky; you move a character at the bottom to catch them; every catch earns a point. By Friday it is a complete game.

Follow **Project Day 1** on the [Falling Objects Game](/scratch/projects/falling-objects-game/#project-day-1-player-object-score) page:

1. **The player** — a sprite about 50–60 pixels wide with [Smooth Movement](/scratch/reference/code-patterns/#smooth-movement) left and right.
2. **The falling object** — a small sprite using the [Falling Object](/scratch/reference/code-patterns/#falling-object) pattern.
3. **Scoring** — a `score` variable that goes up when the object touches the player.

Finished? Try the extensions on the project page: faster falls, a backdrop, edge limits, a penalty for misses.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] My player slides left and right with the arrow keys.
- [ ] One object falls from a random spot and resets at the bottom.
- [ ] Catching it adds 1 to `score`, and the object resets to the top.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

You used every major skill from the first three weeks — events, motion, `forever`, `if`, variables — and built a playable game in one period. Right now one object falls at a time. Later this week, **clones** turn that into a screen full of them.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (fall, reset, catch).
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program (key presses checked every frame).
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop (the game loop on both sprites).
