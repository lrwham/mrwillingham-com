---
title: "Day 4: User Input as Events"
date: 2026-03-19
description: "Use keyboard input events to control a sprite and build an interactive maze game."
day_number: 4
units:
  - "Intro to Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
tags:
  - Scratch
  - Programming
  - Motion
  - Sequences
  - Events
  - User Input
resources: []
draft: false
toc: false
scratchblocks: true
weight: 4
---

# Thursday, March 19th, 2026

{{< objectives >}}

- I can use `user input` as events to trigger behavior in my Scratch projects.
- I can make my Scratch projects interactive by responding to keyboard input.

{{< /objectives >}}

{{< warmup "User Input as Events" >}}

Watch the video assigned today on Edpuzzle. The video covers how programs respond to **user input** — things like key presses, mouse clicks, and other actions the user takes. Pay attention to how Scratch uses event blocks to detect input.

Login to [Clever.com](https://clever.com/) and click on the Edpuzzle icon to access the video.

{{< checkpoint "Warmup" >}}

- [x] I have watched the Edpuzzle video on user input.

{{< /checkpoint >}}

{{< /warmup >}}

{{< worksession "Navigate a Maze" >}}

You will create a maze game in Scratch where the player controls a sprite using the keyboard. The goal is to navigate through the maze without touching the walls.

### Step 1: Set Up the Maze

1. Start a new Scratch project.
2. Create a new sprite to serve as the maze walls. Use the **line tool** and **rectangle tool** to draw your maze layout. Make sure the paths are wide enough for a small sprite to fit through.
3. Choose a small sprite from the library to be the player (or draw your own).
4. Position the player sprite at the start of the maze.

### Step 2: Add Keyboard Controls

Use `when key pressed` event blocks to make the player move. You need four of them — one for each arrow key.

```scratch
when [up arrow v] key pressed
change y by (10)

when [down arrow v] key pressed
change y by (-10)

when [left arrow v] key pressed
change x by (-10)

when [right arrow v] key pressed
change x by (10)
```

Test your controls. Click the green flag, then press the arrow keys. Your sprite should move around the stage.

### Step 3: Play Test

Try navigating your maze. If the paths are too narrow or the sprite moves too fast, adjust your maze drawing or change the movement values (try `5` instead of `10`).

{{< checkpoint "Work Session" >}}

- [x] I have created a maze sprite using the drawing tools.
- [x] I have added a player sprite.
- [x] I have used `when key pressed` event blocks to make the player move with the arrow keys.
- [x] I can navigate through my maze using the keyboard.
- [x] **Bonus**: I have added a second player character with separate keyboard controls (e.g., WASD) for a two-player maze game.

{{< /checkpoint >}}

{{< /worksession >}}

{{< closing "Next Steps" >}}

Tomorrow we will learn about **loops** — a way to make code repeat automatically. Loops are one of the most powerful tools in programming. Instead of writing the same blocks over and over, you can tell Scratch to repeat them for you.

{{< /closing >}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences and algorithms.
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, user interfaces, programming language, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program.
