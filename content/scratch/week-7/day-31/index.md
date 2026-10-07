---
title: "Day 31: Number Guessing Game"
date: 2026-12-01T08:00:00-05:00
description: "Build a guessing game with variables, random numbers, input(), conditionals, and a loop."
day_number: 31
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
resources:
  - Python
  - VS Code
  - Edpuzzle
draft: false
toc: true
scratchblocks: false
weight: 2
---

{{< icon "calendar" >}} **Tuesday, December 1st, 2026**

{{% objectives %}}

## Objectives

- I can run a Python script in VS Code without errors.
- I can build a number guessing game with variables, random numbers, `input()`, and `if`/`elif`/`else`.
- I can use a `while` loop so the player keeps guessing until they are right.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Turtle Control

Watch the Edpuzzle review of setting up a project in VS Code (through Clever).

{{< clever >}}

Then make a new file in `python-class`, paste this in, and run it. Click the turtle window and use the arrow keys.

```python
import turtle

screen = turtle.Screen()
screen.title("Turtle Keyboard Control")
t = turtle.Turtle()

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

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

turtle.mainloop()
```

Notice: four functions, four key events. The same idea as four `when key pressed` blocks in Scratch.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] A turtle window opened.
- [ ] The arrow keys move the turtle in all four directions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Number Guessing Game

Follow along with Mr. Willingham. We build the game together, adding one feature at a time:

1. **Variables** — a secret number and a guess.
2. **Random numbers** — `import random` and `random.randint(1, 100)`.
3. **User input** — `input()` to ask for a guess, `int()` to turn it into a number.
4. **Conditionals** — `if` / `elif` / `else` for too high, too low, correct.
5. **A loop** — `while` so the player keeps guessing.

If there is time: cheat codes. What could a player type to get an advantage?

Stuck on an error? [Troubleshooting](/scratch/reference/python-setup/#troubleshooting).

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] My game picks a random number and accepts a guess with `input()`.
- [ ] It says too high, too low, or correct with `if`/`elif`/`else`.
- [ ] A loop lets the player keep guessing until they get it.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Five concepts — variables, random numbers, input, conditionals, loops — and you have a playable game in text. Those are the same building blocks as every Scratch game you built, in a different language. Tomorrow: real data.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including variables, branches, and iteration.
- [**MS-CS-FCP.4.7**](/scratch/description/#ms-cs-fcp4) — Create a program that accepts user input and stores it in a variable (`input()` on every turn).
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop (the `while` loop).
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on user input (comparing the guess to the secret number).
