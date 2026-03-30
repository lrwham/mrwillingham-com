---
title: "Boolean Operators Quiz Examples"
draft: false
scratchblocks: true
toc: true
build:
    list: never
---

## Question 1

Will `activate_shield` run?

```scratch
when green flag clicked
set [armor v] to (3)
set [energy v] to (40)
if <<(armor) > (0)> and <(energy) > (25)>> then
activate_shield
end
```

**Answer:** Yes. `armor > 0` is true (3 > 0) and `energy > 25` is true (40 > 25). Both sides are true, so `and` is true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 2

Will `turbo_mode` run?

```scratch
when green flag clicked
set [speed v] to (15)
set [boost v] to (1)
if <<(speed) > (20)> and <(boost) = (1)>> then
turbo_mode
end
```

**Answer:** No. `speed > 20` is false (15 > 20). Even though `boost = 1` is true, `and` needs both sides to be true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 3

Will `slip` run?

```scratch
when green flag clicked
set [ground v] to [ice]
if <<(ground) = [water]> or <(ground) = [ice]>> then
slip
end
```

**Answer:** Yes. `ground = water` is false, but `ground = ice` is true. With `or`, only one side needs to be true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 4

Will `reload` run?

```scratch
when green flag clicked
set [ammo v] to (5)
set [energy v] to (20)
if <<(ammo) = (0)> or <(energy) = (0)>> then
reload
end
```

**Answer:** No. `ammo = 0` is false (5 ≠ 0) and `energy = 0` is false (20 ≠ 0). With `or`, at least one side must be true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 5

Will `move_player` run?

```scratch
when green flag clicked
set [paused v] to (0)
if <not <(paused) = (1)>> then
move_player
end
```

**Answer:** Yes. `paused = 1` is false (0 ≠ 1). `not` flips it to true, so `move_player` runs.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 6

Will `start_countdown` run?

```scratch
when green flag clicked
set [timer v] to (30)
if <not <(timer) > (0)>> then
start_countdown
end
```

**Answer:** No. `timer > 0` is true (30 > 0). `not` flips it to false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 7

Will `take_hit` run?

```scratch
when green flag clicked
set [armor v] to (2)
set [invincible v] to (1)
if <<(armor) > (0)> and <not <(invincible) = (1)>>> then
take_hit
end
```

**Answer:** No. `armor > 0` is true (2 > 0). `invincible = 1` is true, so `not` flips it to false. `true and false` is false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5, MS-CS-FCP.4.9

---

## Question 8

Will `unlock_door` run?

```scratch
when green flag clicked
set [gems v] to (2)
set [stars v] to (7)
if <<(gems) > (4)> or <(stars) > (4)>> then
unlock_door
end
```

**Answer:** Yes. `gems > 4` is false (2 > 4), but `stars > 4` is true (7 > 4). With `or`, only one side needs to be true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 9

Will `level_up` run?

```scratch
when green flag clicked
set [xp v] to (150)
set [rank v] to (5)
if <<(xp) > (100)> and <<(rank) = (5)> or <(rank) = (10)>>> then
level_up
end
```

**Answer:** Yes. `xp > 100` is true (150 > 100). Inside the inner `or`: `rank = 5` is true, so the `or` is true. `true and true` is true.

---

## Question 10

Will `game_over` run?

```scratch
when green flag clicked
set [hearts v] to (3)
set [shield v] to (1)
if <not <<(hearts) > (0)> and <(shield) > (0)>>> then
game_over
end
```

**Answer:** No. `hearts > 0` is true (3 > 0) and `shield > 0` is true (1 > 0). `true and true` is true. `not true` is false.
