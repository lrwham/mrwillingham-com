---
title: "Day 17: Variables Deep Dive"
date: 2026-04-14
description: "Deepen understanding of variables by adding speed and lives to the falling-objects game."
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
  - Variables
  - Programming
resources:
  - Scratch
draft: false
toc: true
scratchblocks: true
weight: 2
---

{{< icon "calendar" >}} **Tuesday, April 14th, 2026**

{{% objectives %}}

## Objectives

- I can explain the difference between `set` and `change` for a variable.
- I can use a variable to control game behavior, not just display a number.
- I can add a `speed` variable and a `lives` variable to my game.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Variables in the Real World

A **variable** is a named container that holds a value — and that value can change while the program runs.

You already know one: `score`. But variables aren't just for points. Think about where values change in the real world:

| Real-World Example | What Changes |
|---|---|
| Scoreboard at a basketball game | The score goes up when a team makes a basket |
| Thermometer | The temperature rises and falls throughout the day |
| Gas gauge in a car | The fuel level drops as you drive |
| Timer on a microwave | The seconds count down toward zero |

Each of these is a container with a name (`temperature`, `fuel`, `time remaining`) that holds a value that changes over time. That's exactly what a variable is in code.

Yesterday you used `score` in your catch game. Today you'll add two more variables that change how the game *plays* — not just what number is on screen.

{{% /warmup %}}

{{% worksession %}}

## Work Session

### `set` vs. `change`

Before we start building, make sure you understand the difference between these two blocks:

```scratch
set [score v] to (0)
```

```scratch
change [score v] by (1)
```

- **`set`** replaces the value entirely. If `score` is 7 and you `set [score v] to (0)`, it's now 0. The old value is gone.
- **`change`** adds to the current value. If `score` is 7 and you `change [score v] by (1)`, it's now 8. You can also change by a negative number — `change [score v] by (-1)` would make it 6.

Think of it this way: **set** is like erasing a whiteboard and writing a new number. **Change** is like adding to what's already there.

### Part 1: Speed Variable

Right now your falling object always falls at the same speed — `change y by (-3)`, every frame, forever. That gets boring fast. What if the game got harder every time you caught something?

A `speed` variable makes that possible. Instead of a fixed number like `-3`, the fall speed comes from a variable that increases over time.

{{% steps %}}

### Create the Variable

Go to the **Variables** category and click **Make a Variable**. Name it `speed`. Make sure "For all sprites" is selected.

### Set the Starting Speed

On the **falling object** sprite, set `speed` to 3 at the start. Add this to the beginning of your green flag code:

```scratch
when green flag clicked
set [speed v] to (3)
go to x: (pick random (-200) to (200)) y: (180)
forever
  change y by ((0) - (speed))
  if <touching [Player v]?> then
    change [score v] by (1)
    change [speed v] by (0.5)
    go to x: (pick random (-200) to (200)) y: (180)
  end
  if <(y position) < (-170)> then
    go to x: (pick random (-200) to (200)) y: (180)
  end
end
```

{{< callout type="tip" >}}
Why `(0) - (speed)` instead of just `-3`? The `speed` variable is a positive number (3, 3.5, 4...) that represents how fast the object falls. Subtracting it from 0 makes it negative, which moves the object downward. As `speed` increases, the object falls faster.
{{< /callout >}}

### Increase Speed on Each Catch

Look at the code above — when the player catches the object, two things happen:
1. `change [score v] by (1)` — the score goes up
2. `change [speed v] by (0.5)` — the object falls a little faster next time

After 4 catches, `speed` is 5. After 10 catches, `speed` is 8. The game ramps up naturally.

### Test It

Click the green flag. Catch a few objects and watch the `speed` variable on the stage. The number should climb, and you should feel the objects fall faster.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 1

- [ ] A `speed` variable appears on the stage.
- [ ] The falling object starts slow and gets faster with each catch.
- [ ] The game feels noticeably harder after 5–6 catches.

{{% /checkpoint %}}

### Part 2: Lives Variable

Right now, if you miss a falling object... nothing happens. It just resets to the top. There's no penalty for missing, which means there's no tension.

A `lives` variable fixes that. The player starts with 3 lives. Every missed object costs one life. Run out of lives — game over.

{{% steps %}}

### Create the Variable

Make a new variable called `lives`.

### Set Lives at the Start

On the **player** sprite, add `set [lives v] to (3)` alongside the score reset:

```scratch
when green flag clicked
set [score v] to (0)
set [lives v] to (3)
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

### Lose a Life When You Miss

On the **falling object** sprite, update the bottom-of-screen check. When the object reaches the bottom without being caught, subtract a life and check if the game is over:

```scratch
if <(y position) < (-170)> then
  change [lives v] by (-1)
  if <(lives) < (1)> then
    stop [all v]
  end
  go to x: (pick random (-200) to (200)) y: (180)
end
```

Walk through this:
1. The object hits the bottom — `change [lives v] by (-1)` takes away one life.
2. The `if` block checks: are lives less than 1 (meaning 0 or below)?
3. If yes — `stop [all v]` ends the game.
4. If no — the object resets to the top and the game continues.

### Test It

Click the green flag. Let three objects fall past you without catching them. The `lives` variable should count down: 3, 2, 1 — then the game stops.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Part 2

- [ ] A `lives` variable appears on the stage and starts at 3.
- [ ] Missing a falling object subtracts one life.
- [ ] The game stops when lives reach 0.

{{% /checkpoint %}}

### Part 3: Keep Building

Your game now has three variables working together: `score`, `speed`, and `lives`. Use remaining time to improve the game. Some ideas:

- **Reset speed on miss** — set `speed` back to 3 when the player loses a life, giving them a breather
- **Bonus life** — if the score reaches 10, add an extra life with `change [lives v] by (1)`
- **Add a backdrop** — paint or choose a background that fits your game
- **Edge limits** — stop the player from sliding off the left and right edges

{{% checkpoint %}}

### Checkpoint: Part 3

- [ ] My game has `score`, `speed`, and `lives` variables all working.
- [ ] I have added at least one extra improvement from the list above.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Yesterday `score` was the only variable in your game. Now you have three — and each one changes how the game plays:

| Variable | What It Does |
|---|---|
| `score` | Tracks points — tells the player how well they're doing |
| `speed` | Controls difficulty — makes the game harder over time |
| `lives` | Creates tension — gives the player a reason to care about every miss |

Variables aren't just for displaying numbers. They control game behavior. Tomorrow you'll learn **clones**, and your game will go from one falling object to a screen full of them.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including variables and data.
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including variables, loops, conditionals, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Create a computer program that utilizes variables and conditional statements.
