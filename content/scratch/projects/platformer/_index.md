---
title: "Platformer"
description: "A three-day project: gravity with a velocity variable, platforms with landing and wall collision, then a collectable objective with score and respawn."
draft: false
toc: true
cascade:
  type: docs
scratchblocks: true
---

Build a platformer from a blank project. Day 1 is gravity and jumping, Day 2 is platforms and collision, Day 3 adds an objective and score. Boolean operators do the heavy lifting, so read [Boolean Operators](/scratch/reference/boolean-operators/) first if `and`, `or`, and `not` are new.

## Schedule

| Project Day | Plan |
| ----------- | ---- |
| 1 | **Gravity** — ground sprite, basic gravity with `not`, jumping, then smoother gravity with a `velocity` variable |
| 2 | **Platforms and Collision** — redesign the player, land on platforms with `or`, landing bounce, wall collision with the step-up test |
| 3 | **Objective and Score** — a collectable placed on a platform, a `score` variable, player reset, and respawn |

## Project Day 1: Gravity

### Ground and Basic Gravity

1. Create a sprite named `ground`. Draw a filled rectangle across the bottom of the costume, wide enough to span the stage.
2. On the player sprite, make it fall whenever it is not touching the ground:

```scratch
when green flag clicked
forever
  if <not <touching [ground v]?>> then
    change y by (-5)
  end
end
```

3. Add a jump that only works from the ground:

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  change y by (10)
end
```

4. Add left and right movement on your own. Either [movement pattern](/scratch/reference/code-patterns/#arrow-key-movement) works.

### Gravity With Velocity

Fixed-speed gravity falls at the same rate forever. Real objects accelerate. Create a variable called `velocity` (for all sprites) and switch to the [Gravity and Velocity](/scratch/reference/code-patterns/#gravity-and-velocity) pattern:

```scratch
when green flag clicked
set [velocity v] to (0)
forever
  if <not <touching [ground v]?>> then
    change [velocity v] by (-1)
  else
    set [velocity v] to (0)
  end
  change y by (velocity)
end
```

Then change the jump to set velocity instead of moving the sprite directly — the [Jumping](/scratch/reference/code-patterns/#jumping) pattern:

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to (10)
end
```

Experiment. A stronger jump is `set [velocity v] to (20)`; stronger gravity is `change [velocity v] by (-2)`. Find values that feel good.

Practice tracing this code frame by frame: [Gravity and Velocity: Quiz Examples](/scratch/reference/practice/gravity-examples/).

## Project Day 2: Platforms and Collision

Full steps on the [Platforms and Collision](platforms-and-collision/) page. In short:

1. **Redesign the player.** Small (30–40 px wide), simple shapes, solid fill, facing right. Scratch the cat is too big and has transparent gaps that confuse `touching`.
2. **Platforms.** One sprite named `platform` with several filled rectangles on one costume. One `touching [platform v]?` block covers all of them.
3. **Land on platforms** with `or`, move before you check, and bounce gently on landing — [Landing on Platforms](/scratch/reference/code-patterns/#landing-on-platforms).
4. **Jump from platforms** by adding `or touching platform` to the jump's condition.
5. **Wall collision** with the step-up test — [Wall Collision](/scratch/reference/code-patterns/#wall-collision). Switch movement to the A and D keys so one hand handles movement and the other handles space.

Known bug: jumping into the underside of a platform can stick the player to it. Space platforms so the player lands on top instead of hitting from below.

## Project Day 3: Objective and Score

<!-- TODO: new link — confirm the platformer starter project is still shared -->
Use the [starter project](https://scratch.mit.edu/projects/1298622870) only if your own code is not working.

1. **Create an objective sprite** — a coin, star, gem, or key, about 20–30 pixels so it fits on a platform.
2. **Place it on a platform** the player has to work to reach.
3. **Make a `score` variable** (for all sprites) and set it to 0 when the green flag is clicked.
4. **Detect collection** on the objective sprite: when touching the player, hide, and `change [score v] by (1)`.
5. **Reset the player** to the starting position after a collection, for example `go to x: (-200) y: (-100)`, so the player has to cross the platforms again.
6. **Respawn** the objective after a short wait, in the same or a new position, so the loop continues.

```scratch
when green flag clicked
set [score v] to (0)
show
forever
  if <touching [Player v]?> then
    change [score v] by (1)
    hide
    wait (2) seconds
    go to [random position v]
    show
  end
end
```

Share with a partner and play each other's games. What do you like? What would you change?

## Resources

- [Platforms and Collision](platforms-and-collision/) — the full Day 2 lesson with every code block.
- [Platformer Build-Along](build-along/) — a start-to-finish script, from a blank project through wall collision, with vocabulary.
- [Scratch Code Patterns](/scratch/reference/code-patterns/) — gravity, jumping, landing, and wall collision in one place.

## Checkpoints

**Day 1**

- [ ] The player falls and stops on the ground.
- [ ] The player jumps with space, only from the ground.
- [ ] Gravity uses a `velocity` variable and the fall speeds up.

**Day 2**

- [ ] I drew a new, smaller player with simple shapes and a solid fill.
- [ ] The player lands on platforms and jumps from them.
- [ ] The player stops when walking into the side of a platform.
- [ ] There are at least three platforms at different heights.

**Day 3**

- [ ] An objective sits on a platform.
- [ ] Touching it adds 1 to `score`, hides it, and resets the player.
- [ ] The objective reappears so it can be collected again.

## Teacher Notes

- Day 1 works best as a review warmup (rebuild basic gravity) followed by the velocity upgrade as the work session.
- Day 2 is the densest day. Students who get stuck on wall collision can skip it and still have a playable game.
- The head-bump bug is real and students will find it. Acknowledging it up front beats pretending it does not exist.
- A Code.org nested-loops lesson makes a good warmup for Day 3 while you check Day 2 projects.
