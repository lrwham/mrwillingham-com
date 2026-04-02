---
title: "Day 14: Platformer Review"
date: 2026-04-02
description: ""
day_number: 14
units:
  - ""
standards:
  - MS-CS-FCP.4.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
  - MS-CS-FCP.4.9
tags:
  - Scratch
resources: []
draft: false
toc: true
scratchblocks: false
weight: 4
---

{{< icon "calendar" >}} **Thursday, April 2nd, 2026**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can implement a platformer game in Scratch.
- I can use loops, conditionals, and variables to create game mechanics.

{{% /objectives %}}

{{% warmup %}}

## Warmup

Login to Clever, go to Code.org, start Lesson 14: Nested Loops. 

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have started lesson 14: Nested Loops on Code.org

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

Use [this starter code](https://scratch.mit.edu/projects/1298622870) only if your code is not working.

{{% steps %}}

### Create an Objective Sprite

An objective is something the player collects for points — a coin, star, gem, key, etc. Create a new sprite and draw your collectible. Keep it small (about 20-30 pixels) so it fits on a platform.

### Place the Objective on a Platform

Position your objective sprite on a platform that the player will need to work to reach. It shouldn't be easy — make the player jump across platforms to get there.

### Add a Score Variable

Create a variable called `score` (for all sprites). Set it to `0` when the green flag is clicked.

### Detect Collection

On the **objective sprite**, add code to detect when the player touches it. When collected, the objective should hide, and the score should increase by 1.

### Reset the Player

After collecting the objective, teleport the player back to a starting position (e.g., `go to x: -200 y: -100`). This forces the player to navigate the platforms again.

### Respawn the Objective

After a short wait, show the objective again in a new (or the same) position. The loop continues — collect, reset, collect again.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I have an objective sprite placed on a platform.
- [ ] When the player touches the objective, the score increases by 1.
- [ ] The objective disappears when collected.
- [ ] The player is teleported back to the starting position.
- [ ] The objective reappears so the player can collect again.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Share your game with a partner and play each other's games. What do you like about your partner's game? What would you change about it?

{{% /closing %}}

## Standards

- [**MS-CS-FCP.4.2**](/scratch/description/#ms-cs-fcp4) — Utilize the design process to brainstorm, implement, test, and revise an idea.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data or user input.
