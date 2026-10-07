---
title: "Unit 2 Vocabulary"
description: "Terms from the conditionals, loops, booleans, platformer, and intermediate Scratch lessons."
weight: 12
toc: true
---

## Control Flow

Control Flow
: The order in which a program's instructions run. Conditionals and loops change the flow.

Conditional
: Code that runs only when a condition is true. In Scratch, the `if … then` and `if … then … else` blocks.

Condition
: A yes/no question a program asks, such as `touching [ground v]?` or `(score) = (10)`. It is always either true or false.

Boolean
: A value that is either `true` or `false`.

Boolean Operator
: A block that combines or flips booleans: `and`, `or`, `not`. See [Boolean Operators](/scratch/reference/boolean-operators/).

Loop
: Code that repeats. `forever` repeats until the project stops; `repeat (10)` runs exactly ten times; `repeat until < >` runs until a condition becomes true.

Iteration
: One pass through a loop.

Game Loop
: A `forever` loop with `if` blocks inside it that checks what is happening every frame. Almost every game runs on one.

Flow Diagram
: A picture of a program's steps and decisions, drawn with ovals, rectangles, and diamonds. See [Flow Diagrams](/scratch/reference/flowcharts/).

User Input
: Anything the player does that the program can react to — key presses, mouse clicks, clicking a sprite.

## Variables and Data

Variable
: A named container that holds a value, like `score` or `lives`. The value can change while the program runs.

`set`
: Replaces a variable's value with a new one. Use it to reset.

`change`
: Adds to a variable's current value. Use a negative number to subtract.

Velocity
: How fast something is moving in a direction. In our platformer, a positive `velocity` moves the sprite up and a negative one moves it down.

Gravity
: A constant pull downward. We simulate it by changing `velocity` by a small negative number every frame.

Acceleration
: A change in velocity over time. Falling faster and faster is acceleration.

## Sprites and Collision

Collision Detection
: Checking whether two sprites overlap. Scratch uses the `touching` block and the visible pixels of each costume.

Hitbox
: The part of a sprite that counts for collision. In Scratch it is the non-transparent pixels of the costume.

Platform
: A surface the player can stand on or jump to. Many platforms drawn on one costume still count as one sprite.

Step-Up Test
: A wall-collision technique: after moving sideways and touching something, move up a few pixels and check again. If still touching, it was a wall.

Clone
: A copy of a sprite created while the program runs. Each clone runs the `when I start as a clone` script on its own and should end with `delete this clone`.

Clone Factory
: The original, hidden sprite that creates clones on a timer.

Broadcast
: A message one sprite sends that every sprite can hear with `when I receive`. Used to switch game states.

Game State
: Which part of the game the player is in — start screen, playing, game over, paused.

Remix
: Your own editable copy of someone else's shared Scratch project.

Studio
: A collection of shared projects on Scratch. See [Share to the Class Studio](/scratch/reference/share-to-studio/).
