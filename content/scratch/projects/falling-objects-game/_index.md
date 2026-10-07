---
title: "Falling Objects Game"
description: "A four-day project: a catch game that grows from one falling object into a complete game with speed, lives, clones, danger objects, and start and game-over screens."
draft: false
toc: true
cascade:
  type: docs
scratchblocks: true
---

Objects fall from the top of the stage. You move a character at the bottom to catch them. Every catch earns a point. Over four days the game gains difficulty, lives, dozens of simultaneous objects, and proper game states. Every skill from the first three weeks shows up here.

## Schedule

| Project Day | Plan |
| ----------- | ---- |
| 1 | **Player, Object, Score** — smooth arrow-key movement, one falling object, a `score` variable |
| 2 | **Speed and Lives** — `speed` makes the game harder with every catch; `lives` ends it after three misses |
| 3 | **Clones** — replace the single object with a clone factory, then add a danger object to dodge |
| 4 | **Game States** — start screen and game-over screen with broadcasts, then polish and sounds |

The code for each pattern lives on [Scratch Code Patterns](/scratch/reference/code-patterns/). The steps below say what to build and link to the pattern.

## Project Day 1: Player, Object, Score

Start a **new** project. Delete the cat.

### The Player

1. Add or draw a player sprite — a bowl, a basket, a character — about 50–60 pixels wide.
2. Use the [Smooth Movement](/scratch/reference/code-patterns/#smooth-movement) pattern so the player slides left and right with the arrow keys. Start the player at `go to x: (0) y: (-140)`.

### The Falling Object

1. Add or draw a second sprite — a star, apple, or coin, about 30 × 30 pixels.
2. Use the [Falling Object](/scratch/reference/code-patterns/#falling-object) pattern. The object starts at a random x along the top, falls 3 pixels per frame, and resets when it passes the bottom.

### Scoring

1. **Variables → Make a Variable**, name it `score`, **For all sprites**.
2. On the player, add `set [score v] to (0)` right after the green flag.
3. On the falling object, inside the `forever` loop and **before** the bottom-of-screen check, add:

```scratch
if <touching [Player v]?> then
  change [score v] by (1)
  go to x: (pick random (-200) to (200)) y: (180)
end
```

Extensions: speed it up (`-5`), paint a backdrop, stop the player at the stage edges, subtract a point for a miss.

## Project Day 2: Speed and Lives

`set` replaces a variable's value; `change` adds to it. Today both matter.

### Speed

1. Make a variable called `speed`.
2. On the falling object, `set [speed v] to (-3)` at the start and replace `change y by (-3)` with `change y by (speed)`.
3. Inside the catch check, add `change [speed v] by (-0.5)`. Each catch makes the next fall a little faster.

```scratch
when green flag clicked
set [speed v] to (-3)
go to x: (pick random (-200) to (200)) y: (180)
forever
  change y by (speed)
  if <touching [Player v]?> then
    change [score v] by (1)
    change [speed v] by (-0.5)
    go to x: (pick random (-200) to (200)) y: (180)
  end
  if <(y position) < (-170)> then
    go to x: (pick random (-200) to (200)) y: (180)
  end
end
```

### Lives

1. Make a variable called `lives`. On the player, `set [lives v] to (3)` next to the score reset.
2. On the falling object, change the bottom-of-screen check so a miss costs a life and the game stops at zero:

```scratch
if <(y position) < (-170)> then
  change [lives v] by (-1)
  if <(lives) < (1)> then
    stop [all v]
  end
  go to x: (pick random (-200) to (200)) y: (180)
end
```

Extensions: reset `speed` to -3 when a life is lost; award a bonus life at 10 points; add a backdrop; stop the player at the edges.

## Project Day 3: Clones

<!-- TODO: new link — confirm the catch-game starter project is still shared -->
Open your game, or remix the [starter project](https://scratch.mit.edu/projects/1307434289) if yours is lost.

One object at a time is dull. Games like Tetris, Space Invaders, and Fruit Ninja put dozens of objects on screen by building **one** and letting the program copy it. In Scratch that is **clones**.

### Convert to Clones

1. On the falling object, **delete all the existing code** and replace it with the [Clone Factory](/scratch/reference/code-patterns/#clone-factory) pattern: a hidden original that creates a clone every 0.5–1.5 seconds, plus a `when I start as a clone` script that falls, scores on touching the player, and deletes itself.
2. Test. Several objects should fall at once, each at its own random x.

### A Danger Object

1. Create a new sprite called `Danger` — a rock, a bomb, a red X, about 30 × 30 pixels.
2. Give it the same factory pattern, but spawn less often: `wait (pick random (1) to (3)) seconds`.
3. Its clone script falls a little faster (`change y by (-4)`) and, for now, ends the game on touch:

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

### Tune the Difficulty

| What to change | Where | Effect |
| -------------- | ----- | ------ |
| Spawn rate | `wait` in the factory loop | Lower = more objects, harder |
| Fall speed | `change y by` in the clone script | Bigger number = faster, harder |
| Danger frequency | `wait` in the Danger factory | Lower = more danger |
| Danger speed | `change y by` in the Danger clone script | Faster = harder to dodge |

## Project Day 4: Game States

<!-- TODO: new link — confirm the clones starter project is still shared -->
Open your game, or remix the [starter project](https://scratch.mit.edu/projects/1307458321) if yours is lost.

Right now the game starts the instant the green flag is clicked and freezes when you lose. **Game states** — start screen, playing, game over — fix that, using the [Broadcasts and Game States](/scratch/reference/code-patterns/#broadcasts-and-game-states) pattern.

### Start Screen

1. Add a `Start Screen` sprite: a large filled rectangle with your title and "Click to Start". It shows on the green flag; when clicked, it broadcasts `start game` and hides.
2. The **player** hides on the green flag and does everything else — set score and lives, go to the start position, show, movement loop — under `when I receive [start game v]`.
3. Both **clone factories** start on `when I receive [start game v]` instead of the green flag.

### Game Over Screen

1. Add a `Game Over` sprite: a large rectangle that says "Game Over — click the green flag to play again". It hides on the green flag and shows on `when I receive [game over v]`.
2. In the **Danger** clone script, replace `stop [all v]` with a life check:

```scratch
if <touching [Player v]?> then
  change [lives v] by (-1)
  if <(lives) < (1)> then
    broadcast [game over v]
  end
  delete this clone
end
```

3. Every sprite reacts to `game over`. Player: hide and `stop [other scripts in sprite v]`. Both clone sprites: `stop [other scripts in sprite v]` then `delete this clone`.

Test the whole flow: green flag → start screen → click → play → lose three lives → game over → green flag restarts.

### Polish

Add sounds ([Sound on Touch](/scratch/reference/code-patterns/#sound-on-touch)), more object varieties, a backdrop, a high score. Then share it: [Share to the Class Studio](/scratch/reference/share-to-studio/).

## Checkpoints

**Day 1**

- [ ] The player slides left and right with the arrow keys.
- [ ] One object falls from a random spot and resets at the bottom.
- [ ] Catching it adds 1 to `score`.

**Day 2**

- [ ] The object falls faster after each catch.
- [ ] `lives` starts at 3, drops on a miss, and the game stops at 0.

**Day 3**

- [ ] The original falling sprite is hidden and spawns clones.
- [ ] Several objects fall at once; catching one removes only that one.
- [ ] A danger object falls too, and touching it ends the game.

**Day 4**

- [ ] A start screen appears and nothing moves until it is clicked.
- [ ] A game-over screen appears when `lives` reaches 0 and all objects stop.
- [ ] The green flag restarts from the start screen.

## Teacher Notes

- Day 1 doubles as a review of everything from the first three weeks. If there was a break right before it, add a short "what do you remember" warmup.
- Day 3 is the conceptual leap. The clone factory idea (one hidden original, many copies) is worth drawing on the board.
- Day 4 is also the natural quiz-review day: [Quiz Practice](/scratch/reference/practice/) has code-focused and concept-focused example questions built from this game.
- A fifth day for a quiz plus polish-and-share works well; see the archive for how that was run.
