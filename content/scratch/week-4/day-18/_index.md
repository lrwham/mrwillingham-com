---
title: "Day 18: Clones"
date: 2026-04-15
description: "Use clones to spawn many falling objects from a single sprite."
day_number: 18
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - Clones
  - Programming
resources: []
draft: false
toc: true
scratchblocks: true
weight: 3
---

{{< icon "calendar" >}} **Wednesday, April 15th, 2026**

{{% objectives %}}

## Objectives

- I can explain why clones are useful in Scratch.
- I can use `create clone of [myself]` to generate multiple copies of a sprite.
- I can write code that runs on each clone using `when I start as a clone`.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Learning Check Friday

Check out this outline of what we have learned so far: [Study Guide](https://cdn.mrwillingham.com/scratch-concepts-slides-rev-a.pdf).

Here are some practice questions to test your understanding: [Learning Check Practice](https://www.gimkit.com/practice/69de3ed0d781918e7228264f).

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have reviewed the study guide.
- [ ] I have completed the learning check practice questions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session 1: Review

We'll review the study guide together and take questions or discuss any concepts that are still unclear. This is your chance to ask about anything we've covered so far.

### Learning Check Friday

Here is an [example learning check](learning-check-code/) that focuses on code questions.

You can also try these short-answer [concept practice questions](learning-check-concepts/) to review vocabulary, booleans, and the big ideas behind what we've built.

{{% /worksession %}}

{{% worksession %}}

## Work Session 2: Clones

### The Problem

Open your catch game from Monday or use [this starter project](https://scratch.mit.edu/projects/1307434289). I know some of you experience issues with Scratch logging you out. Use the starter project if you lost some work, didn't finish, etc...

Click the green flag.

One object falls. You catch it. Another falls. You catch it. Over and over — one at a time.

That works, but think about a game like Tetris, Space Invaders, or Fruit Ninja — dozens of objects on screen at once. How did those programmers make all of those without building each one by hand?

They didn't. They built **one**, and the program copied it.

In Scratch, that tool is called **clones**. Today you'll transform your catch game from one falling object to as many as you want.

### The Solution: Clones

Clones use three special blocks:

```scratch
create clone of [myself v]
```

```scratch
when I start as a clone
```

```scratch
delete this clone
```

Here's how they work together:

- The **original** sprite is a factory. It creates clones, then hides itself — it's never visible.
- Each **clone** is an independent copy. It runs its own code starting from `when I start as a clone`.
- When a clone is done — caught, off screen, used up — it removes itself with `delete this clone`.

### Part 1: Convert to Clones

Right now your falling object sprite has a `forever` loop that makes one object fall and reset. We're going to replace that with a clone system.

{{% steps %}}

### Hide the Original and Create a Clone Factory

The original sprite shouldn't be visible — it just makes clones. **Delete all the existing code** on your falling object sprite and replace it with this:

```scratch
when green flag clicked
hide
forever
  wait (pick random (0.5) to (1.5)) seconds
  create clone of [myself v]
end
```

This creates a new clone every 0.5 to 1.5 seconds. The original stays hidden the whole time.

### Write the Clone Code

Add a **second script** on the same sprite. This code runs on each clone when it's created:

```scratch
when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-3)
  if <touching [Player v]?> then
    change [score v] by (1)
    delete this clone
  end
end
delete this clone
```

Walk through this in your head:

1. The clone appears at a random x position near the top of the stage.
2. It falls 3 pixels per frame.
3. If it touches the player — score goes up, clone is deleted.
4. If it reaches the bottom without being caught — clone is also deleted.

### Test It

Click the green flag. You should see multiple objects falling at the same time, each at its own random position. Catch them — the score should increase.

{{< callout type="tip" >}}
You wrote code for **one** sprite, but many copies are running at once. Each clone is independent — catching one doesn't affect the others.
{{< /callout >}}

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 1

- [ ] My original sprite is hidden.
- [ ] New clones spawn every 0.5–1.5 seconds.
- [ ] Multiple objects fall at the same time.
- [ ] Catching a clone increases the score and removes that clone.
- [ ] Clones that reach the bottom disappear.

{{% /checkpoint %}}

### Part 2: Dodge Objects

A catch game is more interesting when there's something to **avoid**. Add a second type of falling object — something the player must dodge.

{{% steps %}}

### Create a Danger Sprite

Create a new sprite called `Danger`. Draw something the player should avoid — a rock, a bomb, a red X, a spiky ball. Keep it about 30x30 pixels.

### Set Up the Clone Factory

Add the same factory pattern to the Danger sprite:

```scratch
when green flag clicked
hide
forever
  wait (pick random (1) to (3)) seconds
  create clone of [myself v]
end
```

{{< callout type="tip" >}}
The danger objects spawn less often (1–3 seconds instead of 0.5–1.5) so the player isn't overwhelmed. You can adjust these numbers later to change the difficulty.
{{< /callout >}}

### Write the Danger Clone Code

The danger clones fall the same way, but instead of increasing the score, they end the game:

```scratch
when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-4)
  if <touching [Player v]?> then
    stop [all v]
  end
end
delete this clone
```

For now, touching a danger clone just stops everything with `stop [all v]`. Tomorrow you'll replace this with a proper game-over screen.

### Test It

Click the green flag. Both types of objects should fall — catch the good ones, dodge the bad ones. Touching a danger object should stop the game.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 2

- [ ] A second type of object falls that the player must dodge.
- [ ] Touching a danger object ends the game.
- [ ] Both catch and dodge objects fall at the same time.

{{% /checkpoint %}}

### Extension: Tune the Difficulty

If you finish early, experiment with these values to find settings that feel challenging but fair:

| What to Change | Where | Effect |
|---|---|---|
| Clone spawn rate | `wait` time in the factory loop | Lower = more objects, harder |
| Fall speed | `change y by` in clone code | Higher number = faster, harder |
| Danger frequency | `wait` time in the Danger factory | Lower = more danger, harder |
| Danger speed | `change y by` in Danger clone code | Faster danger = harder to dodge |

{{% /worksession %}}

{{% closing %}}

## Closing

Your game went from one falling object to a screen full of them — and you only built two sprites. That's the power of clones: one sprite can create as many independent copies as it needs.

This is the same pattern used in any game with many moving objects: bullets, enemies, particles, coins. One sprite, unlimited copies.

Tomorrow you'll add a start screen and game-over screen, plus sound effects to make the game feel complete.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including abstraction and decomposition.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop.
