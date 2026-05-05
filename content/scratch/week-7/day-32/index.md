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

{{< clever >}}

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

<!-- Add work session instructions here -->

<!-- OPTIONAL: Use buttons for project/worksheet links
{{< button text="Open Project" >}}https://scratch.mit.edu{{< /button >}}
-->

<!-- OPTIONAL: Scratch code blocks — set scratchblocks: true in frontmatter
```scratch
when green flag clicked
move (10) steps
```
-->

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ]
- [ ]

{{% /checkpoint %}}

{{% /worksession %}}

<!-- OPTIONAL: Second work session block
{{% worksession %}}

## Work Session 2

{{% checkpoint %}}

### Checkpoint: Work Session 2

- [ ]

{{% /checkpoint %}}

{{% /worksession %}}
-->

{{% closing %}}

## Closing

<!-- Add closing/wrap-up instructions here -->

{{% /closing %}}

## Standards

- [**MS-CS-FCP.X.X**](/scratch/description/#ms-cs-fcpX) — Standard description here.
