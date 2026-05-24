---
title: "Day 32: Number Guessing Game"
date: 2026-05-05T11:19:21-04:00
description: "Build a number guessing game in Python using variables, random numbers, user input, conditional statements, and loops."
day_number: 32
units:
  - "Python and the Terminal"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.7
  - MS-CS-FCP.4.8
  - MS-CS-FCP.4.9
tags:
  - python
  - variables
  - loops
  - conditionals
  - input
resources: []
draft: false
toc: true
scratchblocks: false
weight: 2
---

{{< icon "calendar" >}} **Tuesday, May 5th, 2026**

{{% objectives %}}

## Objectives

- I can run a Python script in Visual Studio Code without errors.
- I can build a number guessing game that uses variables, random numbers, `input()`, and `if/elif/else` statements.
- I can use a `while` loop to let a player keep guessing until they find the right answer.

{{% /objectives %}}

{{% warmup %}}

## Warmup

Watch the Edpuzzle video that reviews how to setup a project in Visual Studio Code. Login to Clever to find Edpuzzle.

{{< clever >}}

### After the Video

Start a new project in Visual Studio Code and copy the code below. This code will allow you to control a turtle using the arrow keys on your keyboard.

```python
import turtle

# Setup
screen = turtle.Screen()
screen.title("Turtle Keyboard Control")

t = turtle.Turtle()

# Movement functions
def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

# Bind keys
screen.listen()  # Required — tells the screen to accept keyboard input
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

turtle.mainloop()
```

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I ran the code in VS Code and a turtle window opened on screen.
- [ ] I clicked the turtle window and used the arrow keys to move the turtle in all four directions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

Follow along with Mr. Willingham. We'll work on a number guessing game together. We'll add features gradually and focus on the following skills.

1. Variables
2. Random numbers
3. User input
4. Conditional statements
5. Loops

### Cheat Codes

If things go well, we'll have time to add some cheat codes to our game. These will allow the player to gain an advantage. What ideas can you come up with for cheat codes?

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] My number guessing game generates a random number and accepts a guess from the player using `input()`.
- [ ] My game tells the player whether their guess is too high, too low, or correct using `if/elif/else`.
- [ ] My game uses a loop so the player can keep guessing until they get it right.

{{% /checkpoint %}}

{{% /worksession %}}


{{% closing %}}

## Closing

Today you built a complete, playable game from scratch using five core programming concepts: variables, random numbers, user input, conditionals, and loops. These are the same building blocks used in almost every real program ever written. Tomorrow we'll use loops again to create beautiful patterns with the `turtle` module — and you'll see how a few lines of code can produce surprisingly complex results.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including variables, branches, and iteration — students apply all three concepts directly while building the guessing game's core logic.
- [**MS-CS-FCP.4.7**](/scratch/description/#ms-cs-fcp4) — Create a program that accepts user input and stores the result in a variable — students use `input()` to collect a guess and store it in a variable on every turn.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop — students write a `while` loop that keeps the game running until the player guesses correctly.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data or user input — students use `if/elif/else` to compare the player's guess to the secret number and respond with a hint.
