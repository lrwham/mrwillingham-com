---
title: "Boolean Operators Quiz Examples"
draft: false
scratchblocks: true
toc: true
listing: false
---

## Question 1

Will `cast_firebolt` run?

```scratch
when green flag clicked
set [level v] to (4)
set [power v] to (55)
if <<(power) > (50)> and <(level) > (3)>> then
cast_firebolt
end
```

**Answer:** Yes. `power > 50` is true (55 > 50) and `level > 3` is true (4 > 3). Both sides are true, so `and` is true.

---

## Question 2

Will `cast_firebolt` run?

```scratch
when green flag clicked
set [level v] to (2)
set [power v] to (55)
if <<(power) > (50)> and <(level) > (3)>> then
cast_firebolt
end
```

**Answer:** No. `power > 50` is true (55 > 50), but `level > 3` is false (2 > 3). With `and`, both sides must be true.

---

## Question 3

Will `play_sound` run?

```scratch
when green flag clicked
set [health v] to (0)
set [lives v] to (3)
if <<(health) = (0)> or <(lives) = (0)>> then
play_sound
end
```

**Answer:** Yes. `health = 0` is true. With `or`, only one side needs to be true.

---

## Question 4

Will `play_sound` run?

```scratch
when green flag clicked
set [health v] to (50)
set [lives v] to (3)
if <<(health) = (0)> or <(lives) = (0)>> then
play_sound
end
```

**Answer:** No. `health = 0` is false (50 ≠ 0) and `lives = 0` is false (3 ≠ 0). With `or`, at least one side must be true.

---

## Question 5

Will the sprite hide?

```scratch
when green flag clicked
set [visible v] to (1)
if <not <(visible) = (0)>> then
hide
end
```

**Answer:** Yes. `visible = 0` is false (1 ≠ 0). `not` flips it to true, so the sprite hides.

---

## Question 6

Will the sprite hide?

```scratch
when green flag clicked
set [visible v] to (0)
if <not <(visible) = (0)>> then
hide
end
```

**Answer:** No. `visible = 0` is true (0 = 0). `not` flips it to false.

---

## Question 7

Will `game_over` run?

```scratch
when green flag clicked
set [score v] to (100)
set [time v] to (0)
if <<(score) > (50)> and <not <(time) = (0)>>> then
game_over
end
```

**Answer:** No. `score > 50` is true (100 > 50). `time = 0` is true, so `not` flips it to false. `true and false` is false.

---

## Question 8

Will the sprite say "You win!"?

```scratch
when green flag clicked
set [coins v] to (10)
set [keys v] to (0)
if <<(coins) > (9)> or <(keys) > (2)>> then
say [You win!]
end
```

**Answer:** Yes. `coins > 9` is true (10 > 9). With `or`, only one side needs to be true, so it doesn't matter that `keys > 2` is false.

---

## Question 9

Will `reset` run?

```scratch
when green flag clicked
set [speed v] to (10)
set [fuel v] to (0)
if <<(speed) > (5)> and <<(fuel) > (0)> or <(fuel) = (0)>>> then
reset
end
```

**Answer:** Yes. `speed > 5` is true (10 > 5). Inside the inner `or`: `fuel > 0` is false but `fuel = 0` is true, so the `or` is true. `true and true` is true.

---

## Question 10

Will the sprite change color?

```scratch
when green flag clicked
set [level v] to (5)
if <not <<(level) > (10)> or <(level) < (1)>>> then
change [color v] effect by (25)
end
```

**Answer:** Yes. `level > 10` is false (5 > 10) and `level < 1` is false (5 < 1). `false or false` is false. `not false` is true.
