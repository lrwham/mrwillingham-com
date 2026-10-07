---
title: "Day 18: Clones"
date: 2026-11-05T08:00:00-05:00
description: "Replace the single falling object with a clone factory that spawns many independent objects at once."
day_number: 18
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - clones
resources:
  - Scratch
draft: false
toc: true
scratchblocks: true
weight: 4
---

{{< icon "calendar" >}} **Thursday, November 5th, 2026**

{{% objectives %}}

## Objectives

- I can explain why clones are useful.
- I can use `create clone of [myself]` to make copies of a sprite.
- I can write code that runs on each clone with `when I start as a clone`.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Quiz Is Monday

The unit quiz is Monday. Spend the warmup on [Quiz Practice](/scratch/reference/practice/): skim the study guide, then try a few [code-focused](/scratch/reference/practice/code-examples/) and [concept-focused](/scratch/reference/practice/concept-examples/) questions.

<!-- TODO: new link — Gimkit practice set for the unit quiz -->

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I looked at the study guide.
- [ ] I tried at least five practice questions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Clones

Click the green flag on your game. One object falls. You catch it. Another falls. Think about Tetris, Space Invaders, Fruit Ninja — dozens of objects at once. Those programmers built **one** and let the program copy it. In Scratch that is **clones**:

```scratch
create clone of [myself v]
when I start as a clone
delete this clone
```

Follow **Project Day 3** on the [Falling Objects Game](/scratch/projects/falling-objects-game/#project-day-3-clones) page (remix its starter project only if your game is lost):

1. **Convert to clones** — delete the falling object's old code and replace it with the [Clone Factory](/scratch/reference/code-patterns/#clone-factory) pattern: a hidden original that spawns a clone every 0.5–1.5 seconds, and a clone script that falls, scores, and deletes itself.
2. **A danger object** — a second sprite with the same factory pattern that spawns less often, falls faster, and (for now) stops the game on touch.
3. **Tune the difficulty** with the table on the project page.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] My original falling sprite is hidden and spawns clones.
- [ ] Several objects fall at once; catching one removes only that one.
- [ ] Clones that reach the bottom disappear.
- [ ] A danger object falls too, and touching it ends the game.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

One sprite, unlimited copies. The same pattern is behind bullets, enemies, particles, and coins in every game with lots of moving objects. Tomorrow: a start screen, a game-over screen, and sounds.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including abstraction (one script, many clones).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (the clone script).
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop (`repeat until` in each clone).
