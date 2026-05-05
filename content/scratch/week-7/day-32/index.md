---
title: "Day 32"
date: 2026-05-05T11:19:21-04:00
description: ""
day_number: 1
units:
  - ""
standards: []
tags:
  - Scratch
resources: []
draft: false
toc: true
scratchblocks: false
weight: 1
---

{{< icon "calendar" >}} **Tuesday, May 5nd, 2026**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can
- I can
- I can

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

<!-- Add warmup instructions here -->

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ]
- [ ]

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

- [ ]
- [ ]

{{% /checkpoint %}}

{{% /worksession %}}


{{% closing %}}

## Closing

<!-- Add closing/wrap-up instructions here -->

{{% /closing %}}

## Standards

- [**MS-CS-FCP.X.X**](/scratch/description/#ms-cs-fcpX) — Standard description here.
