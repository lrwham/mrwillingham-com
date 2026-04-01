---
title: "Day 13: Platforms & Collision"
date: 2026-04-01
description: "Add solid platforms and use boolean operators to detect landing, wall, and ceiling collisions."
day_number: 13
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - Programming
  - Conditionals
  - Boolean
  - Platformer
resources: []
draft: false
toc: true
scratchblocks: true
weight: 3
---

{{< icon "calendar" >}} **Wednesday, April 1st, 2026**

{{% objectives %}}

## Objectives

- I can redesign my player sprite to be smaller and simpler for a platformer.
- I can use the `or` operator to detect collisions with both the ground and platforms.
- I can implement wall collision using the move-check-step up pattern.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Redesign Your Player

Scratch the cat is too big and awkwardly shaped for a platformer. Before we add platforms, you need a character that fits on them.

Open your gravity project from yesterday and **draw a new costume** for your player sprite.

{{< button text="Starter Project (only if you need to catch up)" >}}https://scratch.mit.edu/projects/1298336874{{< /button >}}

Your character must follow these rules:

| Rule | Why |
|------|-----|
| **Small** — about 30-40 pixels wide, 40-50 pixels tall | Must fit comfortably on a platform |
| **Simple shapes** — rectangles, circles, straight lines | Complex curves make collision detection unreliable |
| **Solid fill** — no transparent gaps inside the character | Transparent areas confuse the `touching` block |
| **Faces right** | Standard direction for a platformer character |

Here is an example character built entirely from rectangles and circles:

<figure>
<img src="example-character.svg" alt="Example platformer character — a simple robot made from rectangles and circles" style="max-width: 8rem;">
</figure>

Notice how it uses only basic shapes — rectangles for the body, head, arms, and legs, with circles for small details. Your character does not need to look like this one. Here are some other ideas:

- A simple ball or cube
- A stick figure with a filled body
- A tiny astronaut or knight (blocky style)
- A small animal (square body, triangle ears)

Use the **costume editor** to draw your character. Keep it blocky — this is not an art contest. A simple design that works is better than a detailed design that breaks.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have drawn a new, smaller player character.
- [ ] My character uses simple shapes with a solid fill.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Platforms with Collision

Right now your player can walk and jump on the ground. But a platformer needs **platforms** — surfaces floating in the air that you can land on, bump your head on, and walk into from the side.

We'll handle all three cases using boolean operators from Day 11 and the velocity system from Day 12.

{{% steps %}}

### Create the Platform Sprite

Create a new sprite called `platform`. In the costume editor, draw a **filled rectangle** — about 100-150 pixels wide and 20 pixels tall. Position it somewhere above the ground on the stage.

You can draw **multiple rectangles** on the same costume to create several platforms at different heights. Since they are all part of one sprite, a single `touching [platform v]?` block detects all of them.

### Land on Platforms

Right now, your gravity code only checks for the ground. We need the player to also land on platforms. This is where the `or` operator comes in — the player should stop falling when touching the ground **or** a platform.

We'll also make two improvements to the code structure:

1. **Move first, then check.** Moving `change y by (velocity)` to the **top** of the loop means the player moves before we check what they're touching. This is important for jumping — without it, the player would jump and immediately be detected as touching the ground again.
2. **Use a `gravity` variable** instead of a hardcoded `-1`. This makes it easy to adjust later.

Create a new variable called `gravity`. Then update your gravity code to match this:

```scratch
when green flag clicked
set [gravity v] to [-1]
set [velocity v] to [0]
forever
  change y by (velocity)
  if <not <<touching [ground v]?> or <touching [platform v]?>>> then
    change [velocity v] by (gravity)
  else
    set [velocity v] to [0]
  end
end
```

The key change from yesterday is wrapping the condition with `or`:

```scratch
<touching [ground v]?> or <touching [platform v]?>
```

This means: "if the player is touching the ground **or** touching a platform, stop falling."

**Test it now.** Click the green flag and walk your player under the platform, then jump. You should land on the platform and stop falling. If the player falls through, double-check that your `or` block has both `touching` checks inside it.

### Add Landing Bounce

Try jumping high and falling onto a platform. At high speeds, the player can sink into a platform because `change y by (velocity)` moves several pixels at once.

To fix this, we add a **bounce** inside the `else` branch. When the player lands while falling, we reverse and halve their velocity. This gently pushes them back out of the surface.

Update the `else` branch:

```scratch
when green flag clicked
set [gravity v] to [-1]
set [velocity v] to [0]
forever
  change y by (velocity)
  if <not <<touching [ground v]?> or <touching [platform v]?>>> then
    change [velocity v] by (gravity)
  else
    if <(velocity) < (0)> then
      set [velocity v] to ((-0.5) * (velocity))
    else
      set [velocity v] to [0]
    end
  end
end
```

Here's what the `else` branch does now:

- **If `velocity < 0`** (the player was falling): set velocity to `-0.5 * velocity`. Since velocity is negative, this flips it to a small positive value, bouncing the player gently upward until they settle onto the surface. For example, if velocity is `-8`, then `-0.5 * -8 = 4` — the player bounces up at half the speed they were falling.
- **Otherwise** (the player was moving up or standing still): set velocity to `0`.

**Test it.** Jump from a high platform and land on a lower one. You should see a gentle bounce when you land instead of an instant stop.

### Jump from Platforms

Create a new variable called `jump-velocity` and set it to `10` at the start. Then update your jump code — the player should be able to jump when touching the ground **or** a platform:

```scratch
when green flag clicked
set [jump-velocity v] to [10]
set [gravity v] to [-1]
set [velocity v] to [0]
forever
  change y by (velocity)
  if <not <<touching [ground v]?> or <touching [platform v]?>>> then
    change [velocity v] by (gravity)
  else
    if <(velocity) < (0)> then
      set [velocity v] to ((-0.5) * (velocity))
    else
      set [velocity v] to [0]
    end
  end
end
```

```scratch
when [space v] key pressed
if <<touching [ground v]?> or <touching [platform v]?>> then
  set [velocity v] to (jump-velocity)
end
```

Test it now. You should be able to jump onto the platform and jump again from on top of it. Try changing `jump-velocity` and `gravity` to see how they affect the feel of the game.

### Wall Collision (Move-Check-Step Up)

Try walking into the side of a platform. You'll walk right through it. To fix this, we need to check for walls after every horizontal move.

There's a catch: when you're standing on the ground or a platform, your player is already `touching` it. If we just check `touching` after moving sideways, the game would think you're hitting a wall every time — even when you're just walking on flat ground.

The fix is a **step-up test**:

1. Move the player sideways
2. If touching something, step **up** 5 pixels
3. If **still** touching something, it's a real wall — undo the move
4. Step back down

If stepping up clears the overlap, you were just standing on a surface — no wall. If you're still stuck after stepping up, there's a wall in the way.

We'll switch from arrow keys to **A and D keys** for left/right movement. This keeps the player's hands in one area of the keyboard — A/D for movement and space for jumping — which is easier during gameplay.

Update your left/right movement code:

```scratch
when green flag clicked
forever
  if <key [a v] pressed?> then
    change x by (-5)
    if <<touching [ground v]?> or <touching [platform v]?>> then
      change y by (5)
      if <<touching [ground v]?> or <touching [platform v]?>> then
        change x by (5)
      end
      change y by (-5)
    end
  end
  if <key [d v] pressed?> then
    change x by (5)
    if <<touching [ground v]?> or <touching [platform v]?>> then
      change y by (5)
      if <<touching [ground v]?> or <touching [platform v]?>> then
        change x by (-5)
      end
      change y by (-5)
    end
  end
end
```

Test it — your player should walk normally on flat ground, but stop when they hit the side of a platform.

### Known Bug: Head Bump

Try jumping up into the bottom of a platform. You'll notice the player can get stuck to the ceiling. This happens because when the player moves upward into a platform, velocity is set to `0` — but the player is now inside the platform, and there's nothing to push them back out.

This is a tricky problem to solve cleanly, and we'll fix it in a future lesson. For now, **design your platforms so the player doesn't need to jump directly into the bottom of one.** Space your platforms far enough apart that the player lands on top rather than hitting from below.

### Add More Platforms

To add more platforms, **edit the platform sprite's costume** and draw more rectangles at different positions. Since they are all part of the same sprite, your code works for all of them automatically — no changes needed.

Try creating a layout with 3-4 platforms at different heights that the player can jump between.

**Tip:** Make your platforms at least 20 pixels thick. Thin platforms can cause the player to fall through them at high speeds.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I can land on platforms and jump from them.
- [ ] My player stops when walking into the side of a platform.
- [ ] I have at least 3 platforms at different heights.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you added platforms with three types of collision:

- **Landing** — using `or` to treat platforms like the ground, with a bounce to prevent overlap
- **Wall collision** — using the move-check-step up pattern

We also identified a **head bump bug** where the player can get stuck to the bottom of a platform. We'll tackle that fix in a future lesson.

Tomorrow you'll use everything you've built this week to design a full platformer level.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including Boolean, branches (if...then...else), and iteration.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data or user input.
