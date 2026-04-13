---
title: "Day 19: Game States & Sound"
date: 2026-04-16
description: "Add start and game-over screens with broadcasts, then add sound effects to complete your falling-objects game."
day_number: 19
units:
  - "Intermediate Scratch"
standards:
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.6
tags:
  - Scratch
  - Broadcasts
  - Sound
  - Events
  - Programming
resources: []
draft: false
toc: true
scratchblocks: true
weight: 4
---

{{< icon "calendar" >}} **Thursday, April 16th, 2026**

{{% objectives %}}

## Objectives

- I can use `broadcast` and `when I receive` to coordinate between sprites.
- I can implement a start screen and game-over screen.
- I can add sound effects to game events.

{{% /objectives %}}

{{% warmup %}}

## Warmup: What's Missing?

Click the green flag on your game. Objects start falling immediately — no title, no instructions. Touch a danger object — the game just freezes. No "Game Over" message, no way to play again without clicking the green flag.

Real games have **states**:
- **Start** — a title screen before the action begins
- **Playing** — the actual gameplay
- **Game Over** — a message when you lose

Today you'll add all three using a tool called **broadcasts**, and then add sound to make your game feel finished.

{{% /warmup %}}

{{% worksession %}}

## Work Session

### Part 1: Broadcasts & Game States

**Broadcasts** let sprites send signals to each other. When one sprite sends a broadcast, every other sprite can hear it and react.

Think of it like a PA announcement at school: one person speaks, everyone hears it, and each person decides how to respond.

```scratch
broadcast [start game v]
```

```scratch
when I receive [start game v]
```

{{% steps %}}

### Create a Start Screen Sprite

Add a new sprite called `Start Screen`. In the costume editor, draw a large filled rectangle that covers most of the stage, then write your game's title and "Click to Start" on top of it.

Add this code:

```scratch
when green flag clicked
go to x: (0) y: (0)
show

when this sprite clicked
broadcast [start game v]
hide
```

When the green flag is clicked, the start screen appears. When the player clicks it, it broadcasts `start game` to every sprite and then hides itself.

### Update the Player

The player should be hidden until the game starts. Update your player sprite's code:

```scratch
when green flag clicked
hide

when I receive [start game v]
set [score v] to (0)
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

{{< callout type="warning" >}}
The player's movement code now starts from `when I receive [start game v]` instead of `when green flag clicked`. The green flag only hides the player — the broadcast tells it when to start.
{{< /callout >}}

### Update the Falling Object Clones

Your clone factories should only start spawning after the game begins. On your **falling object** sprite, change the factory to listen for the broadcast:

```scratch
when green flag clicked
hide

when I receive [start game v]
forever
  wait (pick random (0.5) to (1.5)) seconds
  create clone of [myself v]
end
```

Do the same for your **Danger** sprite — change its factory to start on `when I receive [start game v]` instead of `when green flag clicked`.

### Test the Start Screen

Click the green flag. You should see the start screen. Click it — it disappears, your player shows up, and objects start falling.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Start Screen

- [ ] A start screen appears when the green flag is clicked.
- [ ] Nothing moves until the start screen is clicked.
- [ ] The game begins after clicking the start screen.

{{% /checkpoint %}}

{{% steps %}}

### Create a Game Over Screen

Add a new sprite called `Game Over`. In the costume editor, draw a large filled rectangle and write "Game Over" in big text. You can add "Click green flag to play again" below it.

Add this code:

```scratch
when green flag clicked
hide

when I receive [game over v]
go to x: (0) y: (0)
show
stop [other scripts in sprite v]
```

### Broadcast Game Over from Danger Clones

Update your **Danger** clone code to broadcast `game over` instead of `stop [all v]`:

```scratch
when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-4)
  if <touching [Player v]?> then
    broadcast [game over v]
    delete this clone
  end
end
delete this clone
```

### Stop Everything on Game Over

Each sprite needs to react to the `game over` broadcast. On the **player** sprite, add:

```scratch
when I receive [game over v]
hide
stop [other scripts in sprite v]
```

On both the **falling object** and **Danger** sprites, add:

```scratch
when I receive [game over v]
stop [other scripts in sprite v]
delete this clone
```

This stops the clone factories and removes any remaining clones from the screen.

### Test the Full Flow

Green flag — start screen appears. Click it — game plays. Touch a danger object — game over screen appears. Click the green flag again to restart.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Game Over

- [ ] A game-over screen appears when the player touches a danger object.
- [ ] All falling objects stop and disappear when the game ends.
- [ ] Clicking the green flag resets and restarts the game from the start screen.

{{% /checkpoint %}}

### Part 2: Sound Effects

Sound makes a game feel finished. Scratch has a built-in library with hundreds of effects.

**To add a sound to a sprite:**
1. Click the sprite
2. Click the **Sounds** tab at the top
3. Click the **speaker icon** (bottom-left) to open the library
4. Search for a sound and click it to add

Two blocks for playing sound:

```scratch
start sound [Pop v]
```

```scratch
play sound [Pop v] until done
```

Use `start sound` for short effects — it plays in the background without pausing your code. Use `play sound until done` only when you want the script to wait for the sound to finish.

{{% steps %}}

### Catch Sound

Add a short, positive sound to your **falling object** sprite (search "collect", "coin", or "pop"). Play it when a clone is caught:

```scratch
if <touching [Player v]?> then
  start sound [Collect v]
  change [score v] by (1)
  delete this clone
end
```

### Game Over Sound

Add a dramatic sound to your **Game Over** sprite (search "lose", "wand", or "rattle"):

```scratch
when I receive [game over v]
go to x: (0) y: (0)
show
start sound [Lose v]
stop [other scripts in sprite v]
```

### Background Music (Optional)

If you have time, create a tiny hidden sprite called `Music`. Add a track from the library and loop it:

```scratch
when I receive [start game v]
set volume to (30) %
forever
  play sound [Dance Around v] until done
end

when I receive [game over v]
stop all sounds
```

{{< callout type="tip" >}}
Use `play sound until done` (not `start sound`) inside the `forever` loop. This waits for the track to finish before restarting it. If you use `start sound` in a `forever` loop, Scratch will launch thousands of overlapping sounds instantly.
{{< /callout >}}

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Sound

- [ ] A sound plays when the player catches an object.
- [ ] A sound plays on game over.

{{% /checkpoint %}}

### Part 3: Polish

Use remaining time to make your game as strong as possible for tomorrow's showcase. Bugs first, then features:

| Fix / Feature | Impact |
|---|---|
| Fix bugs (clones not disappearing, score not resetting on restart) | High |
| Add a backdrop that fits your game's theme | Medium |
| Stop the player from going off the edges of the stage | Medium |
| Make objects fall faster as the score increases | Medium |
| Improve the look of your start screen and game-over screen | Low |

{{< callout type="warning" >}}
**Share your project** so it's ready for tomorrow's showcase:
1. Click **Share** in the top-right corner of Scratch
2. Give your project a clear title
3. Add a short description explaining how to play
{{< /callout >}}

{{% checkpoint %}}

### Checkpoint: Polish

- [ ] My game runs from start screen to game over without crashing.
- [ ] My game has at least one sound effect.
- [ ] My project is shared on Scratch with a title and description.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

In four days you built a complete game from nothing: player movement, falling objects, clone spawning, collision detection, scoring, game states, and sound. That's every major Scratch skill you've learned this year working together in one project.

Tomorrow you'll share your game with the class — and get a preview of the group project starting next week.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, debugging, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Implement events and event handlers in a computer program.
