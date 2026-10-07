---
title: "Day 19: Game States"
date: 2026-11-06T08:00:00-05:00
description: "Use broadcasts to add a start screen and game-over screen so the game has a clear beginning and end."
day_number: 19
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
tags:
  - Scratch
  - broadcasts
  - events
resources:
  - Scratch
  - Edpuzzle
draft: false
toc: true
scratchblocks: true
weight: 5
---

{{< icon "calendar" >}} **Friday, November 6th, 2026**

{{< callout type="warning" >}}
The group Video Game Design Project starts Tuesday. You will need colored pencils or markers for the design days. Groups are at most three students.
{{< /callout >}}

{{% objectives %}}

## Objectives

- I can use `broadcast` and `when I receive` to coordinate between sprites.
- I can implement a start screen and a game-over screen.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Quiz Prep

Watch today's Edpuzzle video through Clever, then review [Quiz Practice](/scratch/reference/practice/).

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I watched the Edpuzzle video.
- [ ] I reviewed the study guide and tried the sample questions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Game States

Click the green flag on your game: objects fall instantly, no title. Lose: it just freezes. **Game states** — start screen, playing, game over — give the game structure, and **broadcasts** let sprites switch between them:

```scratch
broadcast [start game v]
when I receive [start game v]
```

A broadcast is like a PA announcement: one sprite sends it, every sprite hears it, and each decides how to respond.

Follow **Project Day 4** on the [Falling Objects Game](/scratch/projects/falling-objects-game/#project-day-4-game-states) page (remix its starter project only if your game is lost):

1. **Start screen** — a sprite that shows on the green flag and broadcasts `start game` when clicked. The player and both clone factories wait for that broadcast.
2. **Game over screen** — the danger clones subtract a life and broadcast `game over` at zero; every sprite stops and clears on that message.
3. **Polish** — sounds, more object types, a backdrop, a high score.

The full code is on [Broadcasts and Game States](/scratch/reference/code-patterns/#broadcasts-and-game-states).

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] A start screen appears and nothing moves until it is clicked.
- [ ] A game-over screen appears when `lives` reaches 0 and all objects stop.
- [ ] The green flag restarts from the start screen.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

In four days you built a complete game from nothing: movement, falling objects, clones, collision, scoring, lives, and game states. Monday is the quiz, then you share the game with the class.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including events (broadcasts).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program (sprites that react to `start game` and `game over`).
