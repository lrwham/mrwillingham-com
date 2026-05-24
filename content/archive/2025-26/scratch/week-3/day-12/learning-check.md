---
title: "Gravity & Velocity Quiz Examples"
draft: false
scratchblocks: true
toc: true
build:
    list: never
---

## Question 1

The cat sprite is in the air and NOT touching the ground. What happens?

```scratch
when green flag clicked
forever
  if <not <touching [ground v]?>> then
    change y by [-5]
  end
```

**Answer:** The cat falls down by 5 each frame. Since the cat is not touching the ground, `touching ground` is false, and `not` flips it to true, so the `change y by -5` runs.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 2

The cat sprite IS touching the ground. What happens?

```scratch
when green flag clicked
forever
  if <not <touching [ground v]?>> then
    change y by [-5]
  end
```

**Answer:** Nothing happens. The cat is touching the ground, so `touching ground` is true. `not true` is false, so the code inside the `if` does not run. The cat stays where it is.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 3

What is the value of `velocity` after 3 frames if the cat is in the air the entire time?

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

**Answer:** Velocity is `-3`. Each frame, velocity decreases by 1: after frame 1 it's -1, after frame 2 it's -2, after frame 3 it's -3. This makes the cat fall faster over time, simulating real gravity.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 4

The cat is touching the ground and `velocity` is currently `-8`. What happens on the next frame?

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

**Answer:** Velocity is reset to `0`. Since the cat is touching the ground, the `else` branch runs and sets velocity to 0. Then `change y by 0` does nothing, so the cat stays on the ground.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 5

The cat is touching the ground and the player presses space. What happens?

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to [10]
end
```

**Answer:** Velocity is set to `10`. Since the cat is touching the ground, the condition is true, so velocity becomes 10. On the next frame, `change y by 10` will move the cat upward — this is the jump.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 6

The cat is in the air (NOT touching the ground) and the player presses space. Will the cat jump?

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to [10]
end
```

**Answer:** No. The cat is not touching the ground, so `touching ground` is false. The code inside the `if` does not run, and velocity is not changed. This prevents the cat from jumping in mid-air.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 7

The cat just jumped and `velocity` is `10`. The cat is now in the air. What is `velocity` after 2 frames?

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

**Answer:** Velocity is `8`. Starting at 10, it decreases by 1 each frame: after frame 1 it's 9, after frame 2 it's 8. The cat is still moving upward but slowing down — just like a real jump.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 8

Why does using a `velocity` variable create smoother gravity than `change y by [-5]`?

The two options are side-by-side here for comparison:

```scratch
change y by [-5]

change [velocity v] by [-1]
change y by (velocity)
```

**Answer:** With fixed gravity, the cat always falls at the same speed (-5 every frame). With velocity, the cat starts falling slowly and gets faster over time (-1, -2, -3, -4...). This simulates acceleration and looks more realistic, like real-world gravity.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 9

What is wrong with this gravity code? What will happen when the cat lands on the ground?

```scratch
when green flag clicked
set [velocity v] to [0]
forever
  if <not <touching [ground v]?>> then
    change [velocity v] by [-1]
  end
  change y by (velocity)
```

**Answer:** The code is missing the `else` block that resets velocity to 0. When the cat lands on the ground, velocity will stay at whatever negative value it reached. The `change y by (velocity)` will keep pushing the cat downward through the ground.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 10

The cat is on the ground and the player presses space. Trace through the code and describe what happens over the next 4 frames. Assume the cat leaves the ground after frame 1.

```scratch
when [space v] key pressed
if <touching [ground v]?> then
  set [velocity v] to [10]
end
```

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

**Answer:** Frame 1: Space sets velocity to 10, cat moves up by 10 and leaves the ground. Frame 2: Cat is in the air, velocity changes to 9, cat moves up by 9. Frame 3: Velocity changes to 8, cat moves up by 8. Frame 4: Velocity changes to 7, cat moves up by 7. The cat rises but slows down each frame, just like a real jump arc.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5, MS-CS-FCP.4.9
