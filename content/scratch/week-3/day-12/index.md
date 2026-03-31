---
title: "Day 12: Gravity"
date: 2026-03-31
description: ""
day_number: 12
units:
  - ""
standards: []
tags:
  - Scratch
resources: []
draft: false
toc: true
scratchblocks: true
weight: 2
---

{{< icon "calendar" >}} **Tuesday, March 31st, 2026**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can implement gravity in a Scratch project using basic logic.
- I can use variables to track velocity and implement more accurate gravity effects.

{{% /objectives %}}

{{% warmup %}}

## Warmup

Yesterday we implemented a simple gravity effect by checking if the sprite was touching the ground and changing its y position accordingly. Today, let's review that code and see how we can improve it by using a velocity variable to create smoother movement.

### Yesterday's Gravity Code

Open yesterday's Scratch project and make sure it has all of the following.

Review this code for understanding.

Could you implement all of this yourself?

{{% steps %}}

### Create the Artwork for the Ground

Create a sprite and name it `ground`. Draw a simple rectangle at the bottom of this sprite to represent the ground. Make sure the rectangle is wide enough to cover the stage and is positioned at the bottom.

### Implementing Basic Gravity

Use the following code to make the cat sprite fall when it's not touching the ground.

```scratch
when green flag clicked
forever
  if <not <touching [ground v]?>> then
    change y by [-5]
  end
```

### Jumping

Add jumping to the cat with the following code. This will allow the cat to jump when the space key is pressed.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  change y by [10]
end
```

### Add left and right movement

You should be able to do this unassisted. Add the code so that the cat can move left and right using the left and right arrow keys.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have implemented gravity.
- [ ] I have added jumping to my project.
- [ ] I have added left and right movement to my project.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

### Review Boolean Operators

```scratch
not < >
< > and < >
< > or < >
```

#### Boolean Values

Boolean values are either `true` or `false`. They are often used in conditions to control the flow of a program. For example, you might check if a sprite is touching the ground (true) or not (false) to determine if it should fall.

#### NOT

The `not` operator takes a single boolean value and returns the opposite. For example, if you have a condition that checks if the cat is touching the ground, using `not` would allow you to check if the cat is *not* touching the ground.

#### AND

The `and` operator takes two boolean values and returns true only if both values are true. For example, you could use `and` to check if the cat is touching the ground *and* the space key is pressed before allowing the cat to jump.

#### OR

The `or` operator takes two boolean values and returns true if at least one of the values is true. For example, you could use `or` to check if the cat is touching the ground *or* the space key is pressed to allow for different conditions to trigger a jump.

### Implementing Gravity with Velocity

Using velocity allows for smoother and more realistic movement. Instead of just changing the y position by a fixed amount, we can create a variable called `velocity` that changes over time to simulate acceleration due to gravity.

Velocity is also useful for more realistic affects when walking side-to-side.

{{% steps %}}

### Create a Velocity Variable

Create a variable called `velocity` for all sprites. This variable will be used to track the vertical speed of the cat.

### Set Velocity to 0 at the Start

When the green flag is clicked, set `velocity` to 0. This ensures that the cat starts with no vertical movement.

```scratch
when green flag clicked
set [velocity v] to [0]
```

### Update Velocity for Gravity

In the forever loop, instead of changing the y position by a fixed amount, we will change the `velocity` variable to simulate gravity. For example, you could add a small value to `velocity` each frame to simulate acceleration.

```scratch
when green flag clicked
set [velocity v] to [0]
forever
  if <not <touching [ground v]?>> then
    change [velocity v] by [-1]
  else
    set [velocity v] to [0]
```

### Update Position Based on Velocity

After updating the velocity, you need to change the y position of the cat based on the current velocity.

```scratch
when green flag clicked
set [velocity v] to [0]
forever
  if <not <touching [ground v]?>> then
    change [velocity v] by [-1]
  else
    set [velocity v] to [0]
    end
  change y by (velocity)
```

### Adjust Jumping Code to Use Velocity

When the space key is pressed, instead of changing the y position directly, you can set the `velocity` to a positive value to make the cat jump.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to [10]
end
```

### Adjust the Values for Gravity and Jumping

Both the gravity value of `-1` and the jump velocity of `10` are just examples. You can experiment with these values to find what feels best for your project. Try making the gravity stronger or weaker, or adjusting the jump height to see how it affects the gameplay.

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

#### Stronger Jump {class="no-step-marker"}

```scratch
set [velocity v] to [20]
```

#### Stronger Gravity {class="no-step-marker"}

```scratch
change [velocity v] by [-2]
```

</div>

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I can explain how the `not`, `and`, and `or` boolean operators work.
- [ ] I can use boolean values and operators to control the flow of a Scratch program.
- [ ] I have implemented gravity using a velocity variable.
- [ ] I have adjusted the gravity and jump values to create a fun and playable experience.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Take the learning check on [CTLS](https://studentportal.educationincites.com/cobbssoget).

{{% /closing %}}

## Standards

- [**MS-CS-FCP.X.X**](/scratch/description/#ms-cs-fcpX) — Standard description here.
