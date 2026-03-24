---
title: "Day 6: User Input & Conditionals"
date: 2026-03-23
description: "Watch an Edpuzzle on user input, add keyboard controls to your maze, and learn about conditionals by making sprites bounce off walls."
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
  - Programming
  - Events
  - User Input
  - Conditionals
resources:
  - Edpuzzle
draft: false
toc: false
scratchblocks: true
weight: 1
---

{{< icon "calendar" >}} **Monday, March 23rd, 2026**

{{< callout type="important" icon="sparkles" >}}
Read the entire objective, warmup, work session, and closing sections before you start working. This will help you understand the big picture of what we're doing today.
{{< /callout >}}

{{% objectives %}}

## Objectives

- I can use `user input` as events to trigger behavior in my Scratch projects.
- I can make my Scratch projects interactive by responding to keyboard input.
- I can use an `if` block to detect when a sprite is touching a color.

{{% /objectives %}}

{{% warmup %}}

## Warmup: User Input as Events

Watch the video assigned today on Edpuzzle. The video covers how programs respond to **user input** — things like key presses, mouse clicks, and other actions the user takes. Pay attention to how Scratch uses event blocks to detect input.

Login to Clever.com and click on the Edpuzzle icon to access the video.

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [x] I have watched the Edpuzzle video on user input.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Add Controls to Your Maze

Open the maze project you built last Friday. Today you will make it playable by adding keyboard controls.

If you lost your work, [use this project](https://scratch.mit.edu/projects/1293667664).

### Step 1: Add Keyboard Controls

Click on your **player sprite** and add these blocks. You need four `when key pressed` event blocks — one for each arrow key.

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

### Step 2: Play Test

Click the green flag, then press the arrow keys. Your sprite should move around the stage.

- Can you navigate from start to finish?
- If the paths are too narrow or the sprite moves too fast, adjust your maze drawing or change the movement values (try `5` instead of `10`).

{{% checkpoint %}}

### Checkpoint: Controls

- [x] I added four `when key pressed` blocks to my player sprite, one for each arrow key.
- [x] I can navigate through the maze using the keyboard.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session: Bouncing Off Walls

Right now your sprite can walk straight through the walls. Let's fix that using a **conditional** — a block that checks whether something is true and responds.

### The `if touching color` Block

Scratch can detect when a sprite is touching a specific color on the stage. Since you drew all your maze walls in the same color, you can use this to detect wall collisions.

### The `if touching sprite` Block

Scratch can also detect when a sprite is touching another sprite. Since our walls are a sprite, we can use this or the color option.

### Step 1: Add Wall Detection

Add this code to your player sprite. It runs **forever**, constantly checking if the sprite is touching the wall color:

```scratch
when green flag clicked
forever
if <touching color (#000000)?> then
go to x: (-200) y: (150)
end
end
```

**Important:** Click the color swatch in the `touching color` block, then use the **eyedropper tool** to pick the exact color of your maze walls.

Set the `go to` coordinates to your maze's **start position**. To find the right numbers, drag your sprite to the start and look at the x and y values below the stage.

### Step 2: Test It

Click the green flag and navigate the maze. When your sprite touches a wall, it should snap back to the start.

### Challenge

Instead of going back to the start, try making the sprite **undo** its last move when it touches a wall. Hint: you'll need to move the sprite in the opposite direction by the same amount.

{{% checkpoint %}}

### Checkpoint: Conditionals

- [x] I added a `forever` loop with an `if touching color` block.
- [x] I used the eyedropper to pick my wall color.
- [x] When my sprite touches a wall, it goes back to the start.
- [x] **Bonus:** My sprite undoes its last move instead of resetting to start.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: What You Learned Today

Today you learned two powerful new ideas:

- **User input events** — `when key pressed` blocks let your program respond to the player's actions.
- **Conditionals** — `if` blocks let your program make decisions based on what's happening in the project.

These two ideas together make games possible. Events let the player _do_ things, and conditionals let the game _react_ to what happens.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration (loops).
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, user interfaces, programming language, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Develop an event driven program.
