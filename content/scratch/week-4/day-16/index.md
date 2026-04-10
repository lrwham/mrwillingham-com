---
title: "Day 16: Welcome Back — New Game"
date: 2026-04-13
description: "Review motion, loops, conditionals, and variables by starting a brand new falling-objects game."
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
  - Review
  - Events
  - Loops
  - Conditionals
  - Variables
  - Programming
resources: []
draft: false
toc: true
scratchblocks: true
weight: 1
---

{{< icon "calendar" >}} **Monday, April 13th, 2026**

{{% objectives %}}

## Objectives

- I can use arrow key events and motion blocks to move a sprite.
- I can use a `forever` loop with `if` blocks to create game behavior.
- I can use a variable to track score.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Spring Break Review

Welcome back! It's been a while since you opened Scratch. Let's see what you remember.

Answer these out loud when called on:

| Question | Hint |
|---|---|
| What block makes code run over and over? | It's in the Control category and it's gold |
| What block makes code run *only when* something is true? | Also gold, shaped like a mouth |
| What category holds `change x by` and `change y by`? | It's blue |
| What is a **variable**? | Think of `score` |
| What does `when green flag clicked` do? | It's the starting point |

You've used all of these before. Today you'll use them again — in a brand new project.

{{% /warmup %}}

{{% worksession %}}

## Work Session: A New Game

We're starting fresh. No old projects. Open Scratch and create a **new project**.

The game: objects fall from the sky. You move a character at the bottom of the screen to catch them. Every catch earns a point.

### Part 1: The Player

{{% steps %}}

### Choose or Draw a Player Sprite

Delete the default cat sprite. Add or draw a player sprite — a bowl, a character, a basket — whatever you want. Keep it simple and about 50–60 pixels wide.

### Add Arrow Key Movement

Make the player move left and right with the arrow keys. Add this code to the player sprite:

```scratch
when green flag clicked
go to x: (0) y: (-140)
forever
  if <key [left arrow v] pressed?> then
    change x by (-7)
  end
  if <key [right arrow v] pressed?> then
    change x by (7)
  end
end
```

Click the green flag and test it. Your player should slide left and right smoothly.

{{< callout type="tip" >}}
This uses a pattern you learned in Week 2: a `forever` loop with `if` blocks inside. The loop checks the keyboard every frame so the player can move at any time.
{{< /callout >}}

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 1

- [ ] I have a player sprite near the bottom of the stage.
- [ ] The player moves left and right with the arrow keys.

{{% /checkpoint %}}

### Part 2: The Falling Object

{{% steps %}}

### Create a Falling Sprite

Add or draw a second sprite — a star, apple, coin, or anything your player would want to catch. Keep it small (about 30x30 pixels).

### Make It Fall

Add this code to the falling sprite:

```scratch
when green flag clicked
go to x: (pick random (-200) to (200)) y: (180)
forever
  change y by (-3)
  if <(y position) < (-170)> then
    go to x: (pick random (-200) to (200)) y: (180)
  end
end
```

Click the green flag. The object should appear at a random spot near the top, fall down, and reset to a new random position when it reaches the bottom.

### Understand What's Happening

Walk through this code in your head:

1. The object starts at a random x position, y = 180 (top of the stage).
2. The `forever` loop moves it down 3 pixels every frame.
3. When it passes y = -170 (bottom of the stage), the `if` block resets it to a new random spot at the top.

This is the same loop-with-conditionals pattern from Week 2 — just applied to a falling object instead of a moving player.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 2

- [ ] A sprite falls from a random position at the top of the stage.
- [ ] When it reaches the bottom, it resets to a new random position at the top.

{{% /checkpoint %}}

### Part 3: Scoring

{{% steps %}}

### Create a Score Variable

Go to the **Variables** category and click **Make a Variable**. Name it `score`. Make sure "For all sprites" is selected.

On the **player** sprite, add `set [score v] to (0)` right after the green flag:

```scratch
when green flag clicked
set [score v] to (0)
go to x: (0) y: (-140)
forever
  if <key [left arrow v] pressed?> then
    change x by (-7)
  end
  if <key [right arrow v] pressed?> then
    change x by (7)
  end
end
```

### Detect When the Player Catches the Object

On the **falling object** sprite, add a check inside the `forever` loop for touching the player. Put it **before** the bottom-of-screen check:

```scratch
when green flag clicked
go to x: (pick random (-200) to (200)) y: (180)
forever
  change y by (-3)
  if <touching [Player v]?> then
    change [score v] by (1)
    go to x: (pick random (-200) to (200)) y: (180)
  end
  if <(y position) < (-170)> then
    go to x: (pick random (-200) to (200)) y: (180)
  end
end
```

Now when the falling object touches the player, the score goes up by 1 and the object resets to the top.

### Test It

Click the green flag. Catch the falling object a few times. Watch the score increase.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 3

- [ ] A `score` variable appears on the stage and starts at 0.
- [ ] Catching the falling object adds 1 to the score.
- [ ] After being caught, the object resets to a new position at the top.

{{% /checkpoint %}}

### Extension: Make It Your Own

If you finish early, try any of these:

- **Speed it up** — change `-3` to `-5` for a faster fall
- **Add a backdrop** — paint or choose a background for your game
- **Edge limits** — stop the player from sliding off the edges of the stage
- **Missed penalty** — subtract 1 from the score when the object reaches the bottom without being caught

{{% /worksession %}}

{{% closing %}}

## Closing

Today you used every major skill from the first three weeks — events, motion, `forever` loops, `if` blocks, and variables — and built a playable game in one class period.

Right now, only one object falls at a time. Later this week you'll learn a tool called **clones** that lets you create dozens of falling objects from a single sprite. That's when this game gets interesting.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration (loops).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Implement events and event handlers in a computer program.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop.
