---
title: "Day 15: Terminal and Minecraft"
date: 2026-10-30T08:00:00-04:00
description: "Learn basic Terminal commands (ls, cd, touch, mkdir) and use /tp and /fill in Minecraft Education Edition."
day_number: 15
units:
  - "Python and the Terminal"
standards:
  - MS-CS-FCP.2.3
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - terminal
  - command line
  - Minecraft
resources:
  - Terminal
  - Minecraft Education Edition
  - Code.org
draft: false
toc: true
scratchblocks: false
weight: 5
---

{{< icon "calendar" >}} **Friday, October 30th, 2026**

{{% objectives %}}

## Objectives

- I can use a command line interface (CLI) to navigate folders and create files.
- I can use commands in Minecraft Education Edition to modify my world.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Finish Nested Loops

Log in to Clever and check your progress on **Code.org Lesson 14: Nested Loops**. Finish it now if you have not.

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I completed Lesson 14: Nested Loops.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: The Command Line

A **command line interface (CLI)** controls a computer with typed text instead of clicks. Before windows and icons existed, it was the only way to use a computer — Unix (1971) and MS-DOS (1981) were built around it. The Mac (1984) and Windows (1985) made the **graphical user interface (GUI)** popular, but developers still use the CLI every day: it is faster for many tasks, it can be automated, and it gives you more control.

### Terminal Walkthrough

Open the **Terminal** app and follow along with Mr. Willingham. The command table on [Python and VS Code Setup](/scratch/reference/python-setup/#basic-terminal-commands) is the reference. Today's commands:

| Command | What it does |
| ------- | ------------ |
| `ls` | List what is here (try `ls Desktop`) |
| `pwd` | Print where you are |
| `cd Desktop` / `cd ..` | Move into a folder / back up one |
| `touch hello.txt` | Create an empty file |
| `nano hello.txt` | Edit a file in the terminal (`ctrl + X` to exit and save) |
| `mkdir my-project` | Make a folder |

### Minecraft's Command Line

Minecraft has a CLI built in. Press **/** or **T** to open chat; every command starts with `/`.

**`/tp` — teleport.** Coordinates are x (east/west), y (up/down), z (north/south). `~` means "relative to where I am."

```
/tp @s 0 80 0
/tp @s ~ ~50 ~
```

**`/fill` — fill a region with blocks.** Hundreds of blocks at once.

```
/fill ~0 ~0 ~0 ~10 ~10 ~10 glass
/fill ~0 ~-1 ~0 ~20 ~-1 ~20 gold_block
/fill ~0 ~0 ~0 ~5 ~3 ~5 air
```

Open **Minecraft Education Edition**, create a world, and experiment.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I followed the Terminal walkthrough.
- [ ] I created a Minecraft world.
- [ ] I used `/tp` or `/fill`.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

If time allows, we join a multiplayer server. On Monday we start a brand-new Scratch game.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.2.3**](/scratch/description/#ms-cs-fcp2) — Demonstrate an understanding of how computers process programming commands (typed commands executed one at a time).
- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences and algorithms (a sequence of terminal commands).
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including user interfaces (CLI versus GUI).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (`/fill` to build structures).
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop (Code.org nested loops).
