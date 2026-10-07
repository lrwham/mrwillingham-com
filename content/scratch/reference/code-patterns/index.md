---
title: "Scratch Code Patterns"
description: "A cookbook of the Scratch scripts we use again and again: movement, collision, score, gravity, clones, and game states."
weight: 4
toc: true
scratchblocks: true
---

Every game in this class is built from a small set of patterns. Each one below has the code, what it does, and where it shows up. Lesson pages link here instead of repeating the code.

## Arrow-Key Movement

The simplest way to move a sprite. One event block per key.

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

Each press moves the sprite one step. Holding a key repeats the press, but with a short pause first, so movement feels jerky. Good enough for a maze. Used in the [Maze Game](/scratch/projects/maze-game/).

## Smooth Movement

Check the keyboard every frame inside a `forever` loop. Holding a key moves the sprite continuously.

```scratch
when green flag clicked
forever
  if <key [left arrow v] pressed?> then
    change x by (-7)
  end
  if <key [right arrow v] pressed?> then
    change x by (7)
  end
end
```

This is the **game loop** pattern: a loop that never stops, with `if` blocks inside that check what is happening every frame. Almost every game you have played runs on it. Used in the [Falling Objects Game](/scratch/projects/falling-objects-game/) and the [Platformer](/scratch/projects/platformer/).

## Wall Reset

Send the sprite back to the start when it touches a wall color.

```scratch
when green flag clicked
forever
  if <touching color (#000000)?> then
    go to x: (-200) y: (150)
  end
end
```

Click the color swatch and use the **eyedropper** to pick the exact wall color. Set the `go to` coordinates to your start position — drag the sprite there and read the x and y below the stage. If the walls are their own sprite, `touching [Walls v]?` works the same way. Used in the [Maze Game](/scratch/projects/maze-game/).

## Score and Collect

A variable that goes up when the player touches a collectable, which then moves somewhere new.

```scratch
when green flag clicked
set [score v] to (0)
forever
  if <touching [Coin v]?> then
    change [score v] by (1)
    go to [random position v]
  end
end
```

Make the variable with **Variables → Make a Variable**, named `score`, **For all sprites**. `set` replaces the value; `change` adds to it. Put the `set` block right after the green flag so the score resets every game. Used in the [Maze Game](/scratch/projects/maze-game/) and the [Platformer](/scratch/projects/platformer/).

## Falling Object

An object that starts at a random spot along the top, falls, and resets when it reaches the bottom.

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

Replace `-3` with a `speed` variable to make the game get harder over time. Used in the [Falling Objects Game](/scratch/projects/falling-objects-game/).

## Gravity and Velocity

Real objects accelerate as they fall. A `velocity` variable tracks vertical speed and gravity changes it a little every frame.

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

- In the air, `velocity` drops by 1 each frame: -1, -2, -3… so the fall speeds up.
- On the ground, `velocity` resets to 0 so the sprite stops.
- `change y by (velocity)` moves the sprite by the current speed.

Compare this to the fixed-speed version, `change y by (-5)`, which falls at the same speed forever. Used in the [Platformer](/scratch/projects/platformer/).

## Jumping

Set `velocity` to a positive number. Gravity does the rest: the sprite rises, slows, and falls back.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to (10)
end
```

The `if touching ground` check stops the player from jumping in midair. Used in the [Platformer](/scratch/projects/platformer/).

## Landing on Platforms

Treat platforms like the ground with `or`. Move first, then check, and bounce gently on landing so the sprite does not sink into the surface.

```scratch
when green flag clicked
set [gravity v] to (-1)
set [velocity v] to (0)
forever
  change y by (velocity)
  if <not <<touching [ground v]?> or <touching [platform v]?>>> then
    change [velocity v] by (gravity)
  else
    if <(velocity) < (0)> then
      set [velocity v] to ((-0.5) * (velocity))
    else
      set [velocity v] to (0)
    end
  end
end
```

If `velocity` is -8 when the player lands, `-0.5 * -8 = 4`: a small upward bounce that settles the sprite on top of the surface. Used in the [Platformer](/scratch/projects/platformer/).

## Wall Collision

Stop the player from walking through the side of a platform. The trick is the **step-up test**: move sideways, and if you are touching something, step up 5 pixels. If you are still touching, it was a wall, so undo the move.

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

Without the step-up, standing on flat ground would count as a wall hit every frame, because the player is already touching the ground. Used in the [Platformer](/scratch/projects/platformer/).

## Clone Factory

One hidden sprite creates copies of itself. Each clone runs its own script and deletes itself when it is done.

```scratch
when green flag clicked
hide
forever
  wait (pick random (0.5) to (1.5)) seconds
  create clone of [myself v]
end
```

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

- The original sprite is the factory. It stays hidden.
- `when I start as a clone` runs once for each new clone.
- Always end with `delete this clone`, or dead clones pile up and slow the project down.

Tune the `wait` time to spawn more or fewer objects. Used in the [Falling Objects Game](/scratch/projects/falling-objects-game/).

## Broadcasts and Game States

A **broadcast** is a message every sprite can hear. Use it to switch between a start screen, playing, and game over.

Start screen sprite:

```scratch
when green flag clicked
go to x: (0) y: (0)
show

when this sprite clicked
broadcast [start game v]
hide
```

Player sprite — hidden until the game starts:

```scratch
when green flag clicked
hide

when I receive [start game v]
set [score v] to (0)
set [lives v] to (3)
go to x: (0) y: (-140)
show
forever
  if <key [left arrow v] pressed?> then
    change x by (-7)
  end
  if <key [right arrow v] pressed?> then
    change x by (7)
  end
end
```

Game over sprite:

```scratch
when green flag clicked
hide

when I receive [game over v]
go to x: (0) y: (0)
show
stop [other scripts in sprite v]
```

Any sprite can send `broadcast [game over v]` when the player runs out of lives. Every clone factory should start on `when I receive [start game v]` instead of the green flag, and should stop on `when I receive [game over v]`. Used in the [Falling Objects Game](/scratch/projects/falling-objects-game/).

## Sound on Touch

```scratch
when green flag clicked
forever
  if <touching [Star v]?> then
    start sound [Pop v]
    wait (0.5) seconds
  end
end
```

Pick any sound from the **Sounds** tab. The short `wait` stops the sound from retriggering every frame while the sprites overlap. `start sound` keeps the script moving; `play sound until done` pauses the script until the sound finishes.
