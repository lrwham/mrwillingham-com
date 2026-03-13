---
title: "Day 36 - Finish Pong"
scratchblocks: true
date: 2026-03-06
day_number: 36
tags:
  - Scratch
units:
  - game-design
standards:
resources:
  - Scratch
draft: false
toc: false
---
# Friday, March 6, 2026

{{< objectives >}}

- I can create artwork in Scratch using primitive tools like lines, circles, and rectangles.
- I can write code in Scratch to allow a player to move.
- I can write code in Scratch to allow objects to move on their own.
  {{< /objectives >}}

{{< warmup "Check your work from yesterday" >}}
There are two checkpoints in today's warmup. **Complete both.**

If you need your Scratch account details, see Mr. Willingham.

Yesterday, we created the following artwork. Check yours... Use the `Paint a Sprite` tool to make them if needed...

![Paint a Sprite](paint-sprite.png)

1. A perfectly round ball. Hold down the shift key while drawing a circle.
1. A vertical rectangle for player 1's paddle.
1. A vertical rectangle for player 2's paddle.

| The Ball | Player 1's Paddle | Player 2's Paddle |
| --- | --- | --- |
| ![The Ball](ball.svg) | ![Player 1's Paddle](player1.svg) | ![Player 2's Paddle](player2.svg) |

{{< checkpoint "1. Artwork" >}}

1. I have confirmed all of the artwork is correct.
1. optional - I have created a background for the game.
{{< /checkpoint >}}

The code for the ball is the following.

```scratch
when green flag clicked
go to x: (0) y: (0)
point in direction (pick random(0)  to (360))
forever
  move (10) steps
  if on edge, bounce
```

The code for one of the paddles is the following.

```scratch
when [w v] key pressed
change y by (10)

when [s v] key pressed
change y by (-10)
```

The code for the second paddle is the same, but with different keys.

```scratch
when [up arrow v] key pressed
change y by (10)

when [down arrow v] key pressed
change y by (-10)
```

{{< checkpoint "2. Code" >}}

1. I have confirmed all of the code is correct.
{{< /checkpoint >}}

{{< /warmup >}}

{{< worksession "Bounce off Paddles and Scoring" >}}

We'll work together to add the following features to our game:

- The ball bounces off the paddles.
- A player scores a point when the ball goes past the opponent's paddle.

{{< checkpoint "Work Session" >}}

1. I have added code to make the ball bounce off the paddles.
1. I have added code to keep track of the score for each player.
{{< /checkpoint >}}
{{< /worksession >}}

{{< closing "Discuss the Group Project" >}}
On Monday, you will pick your groups.
We'll discuss some of the project now, but we'll have more time to discuss it on Monday.
{{< /closing >}}
