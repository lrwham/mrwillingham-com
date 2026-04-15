---
title: "Example Learning Check"
draft: false
scratchblocks: true
toc: true
---

Each question shows a small piece of Scratch code. Read carefully and try to answer before checking.

---

## Question 1

When will this script start running?

```scratch
when I start as a clone
show
```

**Answer:** As soon as a new clone of this sprite is created by a `create clone of [myself v]` block. It does not run for the original sprite.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 2

What does the last block do?

```scratch
when I start as a clone
show
wait (2) seconds
delete this clone
```

**Answer:** `delete this clone` removes *this specific clone* from the stage. Other clones and the original sprite are not affected.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 3

Why is `hide` used here, and what is the role of the original sprite?

```scratch
when green flag clicked
hide
forever
  wait (1) seconds
  create clone of [myself v]
end
```

**Answer:** The original sprite is acting as a clone factory — it is never meant to be seen. `hide` keeps it invisible while the forever loop makes new visible clones every second.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5, MS-CS-FCP.4.8

---

## Question 4

About how many clones will exist 10 seconds after the green flag is clicked?

```scratch
when green flag clicked
forever
  wait (pick random (0.5) to (1.5)) seconds
  create clone of [myself v]
end
```

**Answer:** About 10 clones. The average wait is 1 second (halfway between 0.5 and 1.5), so in 10 seconds we expect roughly 10 clones — sometimes a few more, sometimes a few less.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 5

Each time this block runs, what does it produce?

```scratch
pick random (1) to (10)
```

**Answer:** A whole number between 1 and 10 (including both 1 and 10), chosen randomly. Running it again usually gives a different number.

**Standards:** MS-CS-FCP.3.2

---

## Question 6

When does this loop stop?

```scratch
repeat until <(y position) < (-170)>
  change y by (-3)
end
```

**Answer:** It stops as soon as the sprite's `y position` becomes less than -170. Each pass through the loop moves the sprite 3 pixels down, so eventually the condition becomes true and the loop ends.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 7

Under what condition does the `change y by (-5)` block actually run?

```scratch
if <not <touching [ground v]?>> then
  change y by (-5)
end
```

**Answer:** Only when the sprite is *not* touching the ground. `touching ground` is false in the air, and `not false` is true, so the `if` runs and the sprite falls by 5.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 8

A clone is falling and touches the Player. What happens?

```scratch
when I start as a clone
show
repeat until <(y position) < (-170)>
  change y by (-3)
  if <touching [Player v]?> then
    change [score v] by (1)
    delete this clone
  end
end
delete this clone
```

**Answer:** The score goes up by 1 and *this one clone* is deleted. Other falling clones continue on their own.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5, MS-CS-FCP.4.8

---

## Question 9

These two scripts are on different sprites. What does the first one cause the second one to do?

Sprite A:

```scratch
when green flag clicked
broadcast [start game v]
```

Sprite B:

```scratch
when I receive [start game v]
show
go to x: (0) y: (-100)
```

**Answer:** When the green flag is clicked, Sprite A broadcasts "start game". Sprite B hears the broadcast, shows itself, and moves to x 0, y -100.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 10

A clone of an enemy sprite touches the Player. What happens?

```scratch
if <touching [Player v]?> then
  stop [all v]
end
```

**Answer:** Every script in the whole project stops immediately. This is a quick way to end the game — we'll replace it with a proper game-over screen tomorrow.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 11

What is the value of `health` after this script finishes?

```scratch
when green flag clicked
set [health v] to (5)
change [health v] by (-1)
change [health v] by (-1)
change [health v] by (-1)
```

**Answer:** 2. The variable starts at 5, then decreases by 1 three times: 5 → 4 → 3 → 2.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 12

When does `say [Level up!]` run?

```scratch
if <<(score) > (10)> or <key [space v] pressed?>> then
  say [Level up!]
end
```

**Answer:** Whenever *at least one* of the two conditions is true — either the score is greater than 10, or the space key is pressed (or both). `or` is true as long as one side is true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 13

When does this script run?

```scratch
when [space v] key pressed
change y by (20)
```

**Answer:** Every time the user presses the space key. It does *not* need the green flag to run.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 14

After this script runs, which costume is the sprite showing? Assume the sprite has costumes `costume1`, `costume2`, `costume3`, and `costume4` in that order.

```scratch
when green flag clicked
switch costume to [costume1 v]
repeat (3)
  next costume
end
```

**Answer:** `costume4`. The sprite starts at costume1, then `next costume` runs 3 times: costume1 → costume2 → costume3 → costume4.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 15

How is this block different from `go to x: (100) y: (0)`?

```scratch
glide (2) secs to x: (100) y: (0)
```

**Answer:** `glide` moves the sprite *smoothly* to the target over 2 seconds. `go to` would teleport it there instantly.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 16

Is the sprite visible after this script finishes?

```scratch
when green flag clicked
show
hide
show
hide
```

**Answer:** No. The last block is `hide`, so the sprite ends up hidden. Only the *final* state matters — the earlier `show`/`hide` blocks flash by so fast you won't see them.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 17

What does this block do to the sprite?

```scratch
set size to (50) %
```

**Answer:** Shrinks the sprite to half of its normal size. 100% is the original size, 50% is half as big, 200% would be twice as big.

**Standards:** MS-CS-FCP.3.2

---

## Question 18

What does this loop let the player do?

```scratch
when green flag clicked
forever
  if <key [right arrow v] pressed?> then
    change x by (5)
  end
  if <key [left arrow v] pressed?> then
    change x by (-5)
  end
end
```

**Answer:** Move the sprite left and right with the arrow keys. Holding an arrow key keeps the sprite moving because the `forever` loop keeps checking.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8, MS-CS-FCP.4.9

---

## Question 19

This clone generating code creates clones that try to catch and hurt the player. What will the clones need to do when they are created by this script?

```scratch
when green flag clicked
hide
forever
  wait (pick random (1) to (3)) seconds
  create clone of [myself v]
end
```

**Answer:** They will need to show themselves and start moving towards the player.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 20

What is the problem with this clone code?

```scratch
when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-3)
end
```

**Answer:** There is no `delete this clone` at the end. Once a clone falls past y = -170 and the `repeat until` ends, the clone just sits there forever. Over time, hidden clones pile up and slow the project down. Always clean up clones when you're done with them.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5
