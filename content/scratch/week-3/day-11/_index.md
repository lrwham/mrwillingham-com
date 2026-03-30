---
title: "Day 11: Boolean Operators"
date: 2026-03-30
description: "Learn how to combine conditions using the boolean operators and, or, and not in Scratch."
day_number: 11
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.9
tags:
  - Scratch
  - Programming
  - Conditionals
  - Boolean
resources: []
draft: false
toc: true
scratchblocks: true
mermaid: true
weight: 1
---

{{< icon "calendar" >}} **Monday, March 30th, 2026**

{{% objectives %}}

## Objectives

- I can explain what the `and`, `or`, and `not` operators do.
- I can predict whether a condition is `true` or `false` using boolean operators.
- I can use boolean operators in Scratch to combine multiple conditions.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Review — Conditionals

Last week we used `if` blocks to make decisions in our programs. For example, we checked if a sprite was touching a wall color.

An `if` block checks a single **condition** — something that is either `true` or `false`. But what if you need to check **more than one thing** at the same time?

That's where **boolean operators** come in.

| Operator | What it does |
|----------|-------------|
| `and` | `true` only when **both** conditions are true |
| `or` | `true` when **at least one** condition is true |
| `not` | Flips a condition — `true` becomes `false`, `false` becomes `true` |

### Example

Look at this program:

```scratch
when green flag clicked
set [level v] to (4)
set [power v] to (55)
if <<(power) > (50)> and <(level) > (3)>> then
cast_firebolt
end
```

**Will `cast_firebolt` run?**

- `power > 50` → `55 > 50` → **true**
- `level > 3` → `4 > 3` → **true**
- `true and true` → **true**

Yes — both conditions are true, so the `and` block is true and `cast_firebolt` runs.

**What if `power` was `30`?**

- `power > 50` → `30 > 50` → **false**
- `level > 3` → `4 > 3` → **true**
- `false and true` → **false**

No — with `and`, **both** sides must be true.

{{% checkpoint %}}

### Checkpoint: Warmup

- [x] I can explain what `and`, `or`, and `not` do.
- [x] I can predict the result of a boolean expression.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Boolean Operators in Scratch

{{< callout >}}
See [Boolean Operators in Flowcharts](flowcharts/) for a visual comparison of logic **with** and **without** boolean operators.
{{< /callout >}}

### Where to Find Boolean Operators

In Scratch, the `and`, `or`, and `not` blocks are green and live in the **Operators** category. They are shaped like pointed ovals, which means they fit inside the diamond-shaped slots of `if` blocks.

### Part 1: `and`

The `and` block is true only when **both** conditions are true. Use it when two things must happen at the same time.

```scratch
when green flag clicked
forever
if <<key [space v] pressed?> and <touching [ground v]?>> then
change y by (100)
end
end
```

This code only lets the player jump when they are pressing space **and** touching the ground. Without `and`, the player could jump in midair.

### Part 2: `or`

The `or` block is true when **at least one** condition is true. Use it when either thing should trigger the result.

```scratch
when green flag clicked
forever
if <<touching [lava v]?> or <touching [spikes v]?>> then
go to x: (-200) y: (0)
end
end
```

This resets the player if they touch lava **or** spikes. You don't need two separate `if` blocks.

### Part 3: `not`

The `not` block flips a condition. Use it when you want something to happen only when a condition is **false**.

```scratch
when green flag clicked
forever
if <not <key [space v] pressed?>> then
change y by (-5)
end
end
```

This makes the player fall when they are **not** pressing space. We'll use this idea later this week when we build a gravity system.

### Try It

Open Scratch and build a small project that uses at least **one** boolean operator. Here are some ideas:

- A sprite that only moves when two keys are pressed at the same time (`and`)
- A sprite that changes color when touching one of two different sprites (`or`)
- A sprite that falls when it is `not` touching the ground

{{% checkpoint %}}

### Checkpoint: Work Session

- [x] I built a project that uses at least one boolean operator (`and`, `or`, or `not`).
- [x] I can explain why I chose that operator.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session 2: Learning Check

Complete the **Boolean Operators Learning Check** on CTLS. You will look at Scratch programs and predict whether conditions are `true` or `false`.

Here's [some practice questions](https://www.gimkit.com/practice/69ca6d0b88c5ad63a699673a) while you wait.

{{% checkpoint %}}

### Checkpoint: Learning Check

- [x] I have submitted the Boolean Operators Learning Check on CTLS.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you learned three boolean operators that let you combine conditions:

- **`and`** — both must be true
- **`or`** — at least one must be true
- **`not`** — flips true to false

Later this week, we'll use these operators to build a **gravity system** for a platformer game. The `not` operator will be especially important — we'll use it to make a sprite fall when it is *not* touching the ground.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including Boolean, branches (if...then...else), and iteration.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.9**](/scratch/description/#ms-cs-fcp4) — Develop a program that makes a decision based on data or user input.
