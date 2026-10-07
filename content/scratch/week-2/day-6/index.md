---
title: "Day 6: User Input and Conditionals"
date: 2026-10-19T08:00:00-04:00
description: "Watch an Edpuzzle on user input, add arrow-key controls to your maze, and use if touching color to send the sprite back to the start."
day_number: 6
units:
  - "Intro to Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
tags:
  - Scratch
  - events
  - user input
  - conditionals
resources:
  - Scratch
  - Edpuzzle
draft: false
toc: true
scratchblocks: true
weight: 1
---

{{< icon "calendar" >}} **Monday, October 19th, 2026**

{{% objectives %}}

## Objectives

- I can use user input as events to trigger behavior in my Scratch project.
- I can make my project interactive by responding to keyboard input.
- I can use an `if` block to detect when a sprite is touching a color.

{{% /objectives %}}

{{% warmup %}}

## Warmup: User Input as Events

Watch today's Edpuzzle video. It covers how programs respond to **user input** — key presses, mouse clicks, and other actions — and how Scratch uses event blocks to detect them.

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I watched the Edpuzzle video and answered every question.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Controls and Walls

Open the maze you drew on Friday. If it is lost, remix the starter project on the [Maze Game](/scratch/projects/maze-game/) page and draw a quick maze.

Follow **Project Day 2** on the [Maze Game](/scratch/projects/maze-game/#project-day-2-controls-and-walls) page:

1. **Keyboard controls** — four `when key pressed` blocks, one per arrow key ([Arrow-Key Movement](/scratch/reference/code-patterns/#arrow-key-movement)). Test it. Adjust the step size if the paths are tight.
2. **Wall collision** — a `forever` loop with `if touching color` that sends the sprite back to the start ([Wall Reset](/scratch/reference/code-patterns/#wall-reset)). Use the eyedropper to pick the exact wall color.

A **conditional** is a block that checks whether something is true and responds. `if touching color` is your first one.

**Challenge:** instead of resetting to the start, undo the last move when the sprite hits a wall.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] Four `when key pressed` blocks move my sprite through the maze.
- [ ] A `forever` loop with `if touching color` sends my sprite back to the start.
- [ ] I used the eyedropper to pick my wall color.
- [ ] **Bonus:** the sprite undoes its last move instead of resetting.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Two ideas made your maze a game today:

- **User input events** — `when key pressed` lets the player *do* things.
- **Conditionals** — `if` lets the game *react* to what happens.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including branches (the `if touching color` check).
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including events and conditionals.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (the wall-reset loop).
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program (arrow-key events).
