---
title: "Day 10: ..."
date: 2026-03-27
description: ""
day_number: 10
units:
  - None
standards:
  - None
tags:
  - None
resources:
  - None
draft: true
toc: true
scratchblocks: false
weight: 5
---

{{< icon "calendar" >}} **Friday, March 27th, 2026**

{{% alert "Code.org Homework Due" %}}
The Code.org `Programming with Angry Birds` lesson from Tuesday is due today.
{{% /alert %}}

{{% objectives %}}

## Objectives

- I can explain what a `loop` is and why it is useful.
- I can use the `forever` block to make code repeat continuously.
- I can use the `repeat` block to make code repeat a specific number of times.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Week 1 Review

Think about what you've learned this week. Be ready to answer these questions out loud when called on:

1. What is a **sequence**?
2. What is an **event**? Give an example of an event block in Scratch.
3. What happens if your blocks are in the wrong order?

{{% checkpoint %}}

### Checkpoint: Warmup

- [x] I am ready to answer the review questions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Part 1: What is a Loop?

A **loop** is a way to make the computer repeat instructions. Instead of copying and pasting the same blocks over and over, you wrap them in a loop block and let Scratch do the repeating for you.

Scratch has two main loop blocks:

```scratch
forever
end
```

The `forever` block repeats the blocks inside it **non-stop** until you press the stop button.

```scratch
repeat (10)
end
```

The `repeat` block repeats the blocks inside it a **specific number of times**, then stops.

### Try It: Without a Loop

Build this program. Click the green flag to run it.

```scratch
when green flag clicked
move (10) steps
wait (0.5) seconds
move (10) steps
wait (0.5) seconds
move (10) steps
wait (0.5) seconds
move (10) steps
wait (0.5) seconds
```

That's a lot of repeated blocks just to move four times. Now let's use a loop.

### Try It: With a Loop

Replace all of that with this:

```scratch
when green flag clicked
repeat (4)
move (10) steps
wait (0.5) seconds
end
```

Same result, way less code. That's the power of loops.

{{% checkpoint %}}

### Checkpoint: Part 1

- [x] I built the program without a loop and ran it.
- [x] I rebuilt it using a `repeat` block and got the same result.
- [x] I can explain in my own words why loops are useful.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session: Part 2: Animation with Loops

Loops are the key to animation in Scratch. By combining loops with `next costume` and motion blocks, you can make a sprite look like it's walking, flying, or doing anything you want.

### Your Task

1. Choose a sprite from the library that has **multiple costumes** (most animal and character sprites do). Click on the "Costumes" tab to check.
2. Build a program that animates the sprite walking across the stage using a loop:

```scratch
when green flag clicked
repeat (20)
move (5) steps
next costume
wait (0.1) seconds
end
```

3. Try changing the values. What happens if you increase the repeat count? Speed up the wait time? Change the step size?

### Challenge

Make your sprite walk to one side of the stage, then walk back to where it started. You'll need two loops — one for each direction. Use a negative number in `move` to go left.

```scratch
when green flag clicked
repeat (20)
move (5) steps
next costume
wait (0.1) seconds
end
repeat (20)
move (-5) steps
next costume
wait (0.1) seconds
end
```

{{% checkpoint %}}

### Checkpoint: Part 2

- [x] I chose a sprite with multiple costumes.
- [x] My sprite animates across the stage using a loop with `next costume`.
- [x] **Bonus**: My sprite walks to one side and then walks back.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Week 1 Complete

This week you learned:

- How to use the Scratch editor and art tools
- **Sequences** — code runs in order, top to bottom
- **Events** — blocks that start code when something happens (green flag, key press)
- **Loops** — blocks that repeat code automatically

Next week, we'll learn about **conditionals** — how to make your programs make decisions.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration (loops).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop.
