---
title: "Day 9: Loops"
date: 2026-03-26
description: "In this lesson we will introduce using loops in Scratch and Code.org"
day_number: 9
units:
  - None
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - Code.org
  - Programming
  - Loops
resources:
  - None
draft: false
toc: true
scratchblocks: true
weight: 4
---

{{< icon "calendar" >}} **Thursday, March 26th, 2026**

{{% objectives %}}

## Objectives

- I can use `loops` to repeat blocks of code in Scratch.
- I can identify when to use loops to make my code more efficient.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Introduction to Loops

1. Watch this video.

<video controls>
  <source src="https://s3.amazonaws.com/videos.code.org/csf/BB-8_2-5.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

2. Login to Clever and complete levels 1-5 of Lesson 12: Loops with Rey and BB-8 on Code.org.

{{% clever %}}

[Login to Clever first, then this will take you to the lesson.](https://studio.code.org/courses/express-2025/units/1/lessons/12/levels/1)

{{% checkpoint %}}

### Checkpoint: Warmup

- [x] I have watched the video on loops.
- [x] I have completed levels 1-5 of Lesson 12: Loops with Rey and BB-8 on Code.org.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Loops in Scratch

We have already used the `forever` loop in Scratch.

```scratch

forever

```
The `forever` block will repeat the blocks inside forever until the program is stopped. The computer will repeat the code has fast as it can.

This is useful for things that we want to keep checking for.

### Gravity Example

```scratch

when green flag clicked
forever
if <not (onground)> then
change y by (-10)

```

### Loops Make Code More Efficient

Loops can also be used to make code more efficient. Instead of writing the same blocks over and over, we can use a loop to repeat them.

**Which of these is best?**

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

```scratch

when green flag clicked
pen down
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees
move (10) steps
turn cw (90) degrees

```

```scratch

when green flag clicked
pen down
repeat (4)
move (10) steps
turn cw (90) degrees 

```

</div>

#### Try it Yourself

Start with this [Scratch Project](https://scratch.mit.edu/projects/1295926292). It doesn't use loops yet, but it **does** work. Your job is to make the code more efficient by using loops.

{{% checkpoint %}}

### Checkpoint: Work Session

- [x] I have used loops to make code more efficient.
- [x] I can explain why using loops is more efficient than writing the same blocks over and over.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Code.org

For the closing, login to Clever and complete levels 6-10 of Lesson 12: Loops with Rey and BB-8 on Code.org.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration (loops).
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, debugging, user interfaces, usability, variables, lists, loops, conditionals, programming language, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop.
