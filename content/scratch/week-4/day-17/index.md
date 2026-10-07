---
title: "Day 17: Variables Deep Dive"
date: 2026-11-04T08:00:00-05:00
description: "Add speed and lives variables so the game gets harder with each catch and ends when lives run out."
day_number: 17
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - variables
resources:
  - Scratch
draft: false
toc: true
scratchblocks: true
weight: 3
---

{{< icon "calendar" >}} **Wednesday, November 4th, 2026**

{{% objectives %}}

## Objectives

- I can explain the difference between `set` and `change` for a variable.
- I can use a variable to control game behavior, not just display a number.
- I can add `speed` and `lives` variables to my game.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Variables in the Real World

A **variable** is a named container that holds a value that can change while the program runs. You know `score`. Where else do values change?

| Real-world example | What changes |
| --- | --- |
| Scoreboard at a basketball game | The score goes up with each basket |
| Thermometer | The temperature rises and falls |
| Gas gauge | The fuel level drops as you drive |
| Microwave timer | The seconds count down |

Two blocks change a variable:

```scratch
set [score v] to (0)
change [score v] by (1)
```

**`set`** replaces the value — like erasing a whiteboard and writing a new number. **`change`** adds to it — a negative number subtracts.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I can explain the difference between `set` and `change`.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Speed and Lives

Follow **Project Day 2** on the [Falling Objects Game](/scratch/projects/falling-objects-game/#project-day-2-speed-and-lives) page:

1. **Speed** — a `speed` variable replaces the fixed `-3`, and each catch changes it by `-0.5` so the next fall is faster.
2. **Lives** — a `lives` variable starts at 3; a miss subtracts one; at zero the game stops.
3. **Keep building** — reset speed on a miss, a bonus life at 10 points, a backdrop, edge limits.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] The object falls faster after each catch.
- [ ] `lives` starts at 3, drops on a miss, and the game stops at 0.
- [ ] I added at least one extra improvement.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

| Variable | What it does |
| --- | --- |
| `score` | Tells the player how well they are doing |
| `speed` | Makes the game harder over time |
| `lives` | Gives the player a reason to care about every miss |

Variables control behavior, not just numbers on screen. Tomorrow: clones.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including variables and data.
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including variables, loops, and conditionals.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data (the game ends when `lives` drops below 1).
