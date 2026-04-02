---
title: "Platformer Build-Along"
date: 2026-04-02
build:
  list: never
scratchblocks: true
draft: false
---

This video walks through building a platformer from a blank Scratch project. By the end, you'll have gravity, platforms, and collision detection — everything from Days 12 and 13.

---

## Part 1: Ground & Basic Gravity

We start with a completely blank Scratch project.

### Create the Ground

Create a new sprite and name it `ground`. In the costume editor, draw a filled rectangle across the bottom of the costume. Make it wide enough to span the full stage.

### Make the Player Fall

Select the cat sprite. We want it to fall downward whenever it's not standing on the ground.

```scratch
when green flag clicked
forever
  if <not <touching [ground v]?>> then
    change y by [-5]
  end
end
```

This loop runs every frame. It checks: "Is the player NOT touching the ground?" If true, the player moves down 5 pixels. Once the player reaches the ground, the condition is false and the player stops falling.

> **Vocabulary: Gravity** — A force that pulls objects downward. In our game, we simulate gravity by decreasing the player's y position every frame.

> **Vocabulary: Condition** — A yes-or-no check that controls whether code runs. Here, `not touching ground` is our condition.

> **Edpuzzle Question:** What would happen if you removed the `not` block from this code?

---

## Part 2: Jumping & Movement

### Add Jumping

The player should only jump when they're on the ground — otherwise they could jump mid-air forever.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  change y by [10]
end
```

> **Vocabulary: Boolean** — A value that is either `true` or `false`. The `touching ground?` block is a boolean — it reports true when the player is on the ground, and false when they're in the air.

> **Edpuzzle Question:** Why do we check `touching ground?` before letting the player jump?

### Add Left and Right Movement

Use the arrow keys to move the player sideways.

```scratch
when [left arrow v] key pressed
change x by (-5)
```

```scratch
when [right arrow v] key pressed
change x by (5)
```

At this point you should have a player that falls, lands on the ground, can jump, and can move left and right.

---

## Part 3: Velocity

The basic gravity works, but it doesn't feel realistic. Objects in real life don't fall at a constant speed — they accelerate. We'll use a **variable** to track how fast the player is moving up or down.

### Create the Velocity Variable

Go to the Variables category and create a new variable called `velocity` (for all sprites).

> **Vocabulary: Variable** — A named container that stores a value. The value can change as the program runs.

> **Vocabulary: Velocity** — How fast something is moving in a direction. Positive velocity means moving up; negative means moving down.

### Rewrite the Gravity Code

Replace the old gravity code with this version that uses velocity:

```scratch
when green flag clicked
set [velocity v] to [0]
forever
  if <not <touching [ground v]?>> then
    change [velocity v] by [-1]
  else
    set [velocity v] to [0]
  end
  change y by (velocity)
end
```

Here's what changed:

- Instead of `change y by -5` every frame, we `change velocity by -1`. Each frame, the player falls a little faster — just like real gravity.
- When the player touches the ground, velocity resets to 0.
- At the bottom of the loop, `change y by velocity` moves the player based on their current speed.

> **Vocabulary: Acceleration** — A change in velocity over time. `change velocity by -1` is acceleration — each frame, the falling speed increases by 1.

> **Edpuzzle Question:** What does `change velocity by -1` simulate? (Answer: acceleration due to gravity)

### Update the Jump

Instead of moving the player up directly, set velocity to a positive number. The gravity code handles the rest — the player rises, slows down, and falls back.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to [10]
end
```

Try adjusting the `-1` gravity and `10` jump values. Stronger gravity (like `-2`) makes the player fall faster. A higher jump velocity (like `15`) makes the player jump higher.

---

## Part 4: Redesign the Player

Before we add platforms, the Scratch cat needs to go. It's too big, and its shape causes problems with collision detection.

### Why the Cat Doesn't Work

- Too large to fit on small platforms
- Complex curves make `touching` checks unreliable
- Transparent gaps inside the costume confuse the `touching` block

> **Vocabulary: Collision Detection** — How the game checks whether two sprites are overlapping or touching each other. Scratch uses the visible pixels of a costume for this check.

> **Vocabulary: Hitbox** — The area of a sprite that counts for collision. In Scratch, the hitbox is defined by the non-transparent pixels of the costume.

### Draw a New Character

Create a new costume for your player sprite. Follow these rules:

| Rule | Why |
|------|-----|
| Small (30-40px wide, 40-50px tall) | Must fit on platforms |
| Simple shapes (rectangles, circles) | Complex curves break collision |
| Solid fill, no gaps | Transparent areas confuse `touching` |
| Faces right | Standard for platformers |

Ideas: a small robot, a ball, a stick figure, a blocky animal.

> **Edpuzzle Question:** Why do transparent gaps inside a character cause problems with the `touching` block?

---

## Part 5: Platforms & Landing

Now we add platforms the player can land on.

### Create the Platform Sprite

Create a new sprite called `platform`. Draw a filled rectangle — about 100-150 pixels wide and 20 pixels tall. Position it above the ground on the stage.

You can draw multiple rectangles on the same costume to create several platforms. One sprite, many surfaces.

> **Vocabulary: Platform** — A surface the player can stand on, jump to, or interact with. In Scratch, all platforms drawn on one costume count as a single sprite.

### Introduce the Gravity Variable

Create a variable called `gravity` so we can easily tune the fall speed later. Replace the hardcoded `-1`.

### Update the Gravity Code

Two important changes:

1. **Move first, then check.** `change y by velocity` moves to the **top** of the loop. This way the player moves before we check what they're touching — important for jumping to work correctly.
2. **Use `or`** to detect both the ground and platforms.

> **Vocabulary: `or` Operator** — A boolean operator that returns true if **either** condition is true. We use it to treat the ground and platforms the same way.

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

The key line:

```scratch
<touching [ground v]?> or <touching [platform v]?>
```

This means: "Is the player touching the ground OR touching a platform?" If either is true, stop falling.

> **Edpuzzle Question:** What does the `or` block let us do that a single `touching` block can't?

---

## Part 6: Landing Bounce & Jump Velocity

### The Problem

When the player falls fast, `change y by velocity` can move them several pixels into a platform in one frame. The player sinks in before the code detects the collision.

### Add a Landing Bounce

Inside the `else` branch (when the player IS touching ground or platform), check if velocity is negative (falling). If so, reverse it and cut it in half. This gently pushes the player back out.

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

Example: if velocity is `-8`, then `-0.5 * -8 = 4`. The player bounces up gently and settles onto the surface.

> **Vocabulary: Nested Conditional** — An `if` block inside another `if` block. Here, we nest a velocity check inside the landing check.

> **Edpuzzle Question:** If velocity is `-8` when the player lands, what does it become after the bounce formula `(-0.5) * velocity`?

### Create the Jump-Velocity Variable

Create a variable called `jump-velocity` and set it to `10` at the start. Update the jump code to also use `or` — the player should jump from platforms too:

```scratch
when [space v] key pressed
if <<touching [ground v]?> or <touching [platform v]?>> then
  set [velocity v] to (jump-velocity)
end
```

Now the player can jump from any surface, and you can tune jump height by changing one variable.

---

## Part 7: Wall Collision & Final Polish

### The Problem

Walk into the side of a platform. The player passes right through it. We need wall collision.

### Why It's Tricky

When the player stands on the ground, they're already `touching` it. If we just check `touching` after moving sideways, the game would think every step is a wall collision — even on flat ground.

### The Move-Check-Step Up Pattern

> **Vocabulary: Step-Up Test** — A collision technique where, after detecting an overlap, the player is temporarily moved up to see if the overlap clears. If it clears, they were standing on a surface. If not, they hit a wall.

The pattern:

1. Move the player sideways
2. If touching something, step **up** 5 pixels
3. If **still** touching, it's a real wall — undo the sideways move
4. Step back down

We also switch to **A/D keys** for movement, keeping the player's hands in one area of the keyboard (A/D + space).

> **Vocabulary: Wall Collision** — Detecting when the player walks into the side of a solid object and preventing them from passing through.

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

> **Edpuzzle Question:** In the step-up test, why do we move the player up 5 pixels before checking for a wall again?

### Known Bug: Head Bump

If the player jumps into the bottom of a platform, they can get stuck. Velocity is set to 0 while they're inside the platform, with nothing to push them out. For now, design your platforms with enough space so players land on top rather than bumping from below. We'll fix this properly in a later lesson.

### Add More Platforms

Edit the platform sprite's costume and draw more rectangles at different heights. Since they're all one sprite, no code changes needed.

Aim for 3-4 platforms at different heights that the player can jump between. Keep platforms at least 20 pixels thick so the player can't fall through at high speeds.

---

## Final Code Summary

At the end of this build, you should have three scripts on your player sprite:

**Gravity & Landing:**

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

**Jumping:**

```scratch
when [space v] key pressed
if <<touching [ground v]?> or <touching [platform v]?>> then
  set [velocity v] to (jump-velocity)
end
```

**Movement with Wall Collision:**

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

### Variables

| Variable | Starting Value | Purpose |
|----------|---------------|---------|
| `velocity` | `0` | Tracks vertical speed |
| `gravity` | `-1` | How fast the player accelerates downward |
| `jump-velocity` | `10` | How fast the player moves upward when jumping |

### Sprites

| Sprite | Description |
|--------|-------------|
| Player | Small, simple character (30-40 x 40-50px, solid fill) |
| `ground` | Filled rectangle spanning the bottom of the stage |
| `platform` | One sprite with multiple filled rectangles at different heights |
