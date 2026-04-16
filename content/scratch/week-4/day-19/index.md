---
title: "Day 19: Game States"
date: 2026-04-16
description: "Add start and game-over screens with broadcasts, then polish your game."
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

{{% /objectives %}}

{{% warmup %}}

## Warmup: Prepare for Quiz

Understanding our game code so far is a great way to prepare for the quiz tomorrow.

Login to Clever and open the Edpuzzle video for today.

After the video, review the study guide and sample questions.

[Study Guide](https://cdn.mrwillingham.com/scratch-concepts-slides-rev-a.pdf)

[Sample Code Focused Questions](../day-18/learning-check-code/)

[Sample Conceptual Questions](../day-18/learning-check-concepts/)

{{< clever >}}

{{% checkpoint %}}

#### Checkpoint: Quiz Preparation

- [ ] I have watched the Edpuzzle video for today.
- [ ] I have reviewed the study guide.
- [ ] I have attempted the sample questions.

{{% /checkpoint %}}

{{% /warmup %}}


{{% worksession %}}

## What's Missing?

Open your game **or** open this [starter code](https://scratch.mit.edu/projects/1307458321) if your game is lost or incomplete.

Click the green flag on your game. Objects start falling immediately — no title, no instructions. Touch a dangerous falling object — the game just freezes. No "Game Over" message, no way to play again without clicking the green flag.

In other words, your game is difficult to enjoy. We need to add some structure to give the game more polish.

Game state describes what part of the game the player is in and what the values of different variables are. 

Games have **states** like:
- **Start** — a title screen before the action begins
- **Playing** — the actual gameplay
- **Game Over** — a message when you lose

More advanced games may have other states like "Paused", "Level Complete", "Loading", "Main Menu", "Store", "Cutscene", etc.

Today you'll add `start screen`, `playing`, and `game-over` states using a tool called **broadcasts**.

Using these states means it is easy to go back to `start screen` for example if the player wants to play again.

This also makes it easier to add additional features like `pause game` in the future.

{{% /worksession %}}

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

#### Create a Start Screen Sprite

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

{{< callout type="info" >}}
That name `start game` is important. It is a label for the broadcast signal. Every sprite in the game will listen for that signal to know the game has started.
{{< /callout >}}


#### Update the Player

The player should be hidden until the game starts. Update your player sprite's code so that it listens for the `start game` broadcast before showing and allowing movement. The player should be hidden when the green flag is clicked, and only show and move after receiving the `start game` broadcast:

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

{{< callout type="info" >}}
The player's movement code now starts from `when I receive [start game v]` instead of `when green flag clicked`. The green flag only hides the player — the broadcast tells it when to start.
{{< /callout >}}

#### Update the Falling Object Clones

Your clone factories should only start spawning after the game begins. Remember, the game now begins when the broadcast message `start game` is received. On your **falling object** sprite, change the factory to listen for the broadcast:

```scratch
when green flag clicked
hide

when I receive [start game v]
forever
  wait (pick random (0.5) to (1.5)) seconds
  create clone of [myself v]
end
```

#### Danger Clones

The dangerous falling objects should also only start after the game begins. Change the clone factory to start on `when I receive [start game v]` instead of `when green flag clicked`.

#### Test the Start Screen

Click the green flag. You should see the start screen. Click it — it disappears, your player shows up, and objects start falling.

{{% /steps %}}

{{% checkpoint %}}

#### Checkpoint: Start Screen

- [ ] A start screen appears when the green flag is clicked.
- [ ] Nothing moves until the start screen is clicked.
- [ ] The game begins after clicking the start screen.

{{% /checkpoint %}}

### Game Over Screen

{{% steps %}}

#### Create a Game Over Screen

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

#### Broadcast Game Over from Danger Clones

Update your **Danger** clone code so that touching the player costs one life, and the game ends only when `lives` runs out. Replace the old `stop [all v]` check with this:

```scratch
when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-4)
  if <touching [Player v]?> then
    change [lives v] by (-1)
    if <(lives) < (1)> then
      broadcast [game over v]
    end
    delete this clone
  end
end
delete this clone
```

{{< callout type="info" >}}
The player still has 3 lives from Day 17. Each danger hit subtracts one. Only the hit that takes `lives` below 1 broadcasts `game over` — that's when the game-over screen appears.
{{< /callout >}}

#### Stop Everything on Game Over

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

#### Test the Full Flow

Green flag — start screen appears. Click it — game plays. Take hits from danger objects until `lives` drops to 0 — game over screen appears. Click the green flag again to restart.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Game Over

- [ ] A game-over screen appears when `lives` drops to 0.
- [ ] All falling objects stop and disappear when the game ends.
- [ ] Clicking the green flag resets and restarts the game from the start screen.

{{% /checkpoint %}}


### Finished Early? Polish Your Game!

Use remaining time to make your game as strong as possible for tomorrow's showcase.

- add sounds
- add more variety to your falling objects
- add a background costume
- add a score display
- add a high score display
- etc...


{{% /worksession %}}

{{% closing %}}

## Closing

In four days you built a complete game from nothing: player movement, falling objects, clone spawning, collision detection, scoring, game states, and more. That's every major Scratch skill you've learned this year working together in one project.

Tomorrow you'll share your game with the class — and get a preview of the group project starting next week.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, debugging, and events.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.6**](/scratch/description/#ms-cs-fcp4) — Implement events and event handlers in a computer program.
