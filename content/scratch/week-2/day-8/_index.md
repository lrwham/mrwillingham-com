---
title: "Day 8: Flow Diagrams"
date: 2026-03-25
description: "Complete an offline flow diagram activity to map out conditional logic using yes/no decisions on paper."
day_number: 8
units:
  - "Conditionals"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.3.4
  - MS-CS-FCP.4.1
tags:
  - conditionals
  - flow-diagrams
  - unplugged
  - offline
resources:
  - Flow Diagram Worksheet
draft: false
toc: true
scratchblocks: true
mermaid: true
weight: 3
---

{{< icon "calendar" >}} **Wednesday, March 25th, 2026**

{{< callout type="important" icon="sparkles" >}}
Read the entire objective, warmup, work session, and closing sections before you start working. This will help you understand the big picture of what we're doing today.
{{< /callout >}}

{{% objectives %}}

## Objectives

- I can read a flow diagram and predict its outcome.
- I can draw a flow diagram that represents a conditional (if/else) decision.
- I can connect flow diagrams to `if` blocks in Scratch.

{{% /objectives %}}

{{% warmup %}}

## Warmup: What is a Flow Diagram?

Yesterday you learned the vocabulary of conditionals — `if`, `else if`, `else`, and how programs use conditions to decide what to do. Today we're going to **draw** that logic on paper using **flow diagrams**.

A flow diagram is a picture that shows the steps a program follows and the decisions it makes along the way. There are three shapes you need to know:

| Shape         | Meaning                       | Example                         |
| ------------- | ----------------------------- | ------------------------------- |
| **Oval**      | Start or End                  | "Start", "Done"                 |
| **Rectangle** | Action (do something)         | "Eat breakfast", "Go to school" |
| **Diamond**   | Decision (yes or no question) | "Is it raining?"                |

**Arrows** connect the shapes and show which direction the program flows. A diamond always has **two arrows** coming out — one for **Yes** and one for **No**.

Mr. Willingham will walk through an example on the board:

> **"Is it raining?"** → Yes: Bring an umbrella → Go to school / No: Go to school

```mermaid
flowchart TD
    A([Start]) --> B{Is it raining?}
    B -- Yes --> C[Bring an umbrella]
    B -- No --> D[Go to school]
    C --> D
    D --> E([Done])
```

Notice how the diamond is the **condition** — the same thing that goes inside an `if` block in Scratch. The two paths (Yes and No) are like the code inside `if` and `else`.

{{% checkpoint %}}

### Checkpoint: Warmup

- [x] I understand the three flow diagram shapes (oval, rectangle, diamond).
- [x] I understand that a diamond is a yes/no decision — just like a condition in an `if` block.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

### Part 1 — Trace the Flow

In this example, identify the condition and find loops. Loops are when the flow goes back to an earlier point in the diagram. This indicates code that will repeat.

1. What is the condition in this flow diagram?
1. Where are there loops? What is repeated?

```mermaid
flowchart TD
    A([Start]) --> B{Is the sprite touching the wall color?}
    B -- Yes --> C[Go back to start position]
    B -- No --> D[Keep moving]
    C --> B
    D --> B
```

{{% checkpoint %}}

#### Checkpoint: Part 1

- [x] I can identify the condition in a flow diagram.
- [x] I can identify loops in a flow diagram.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

### Part 2 — Draw Your Own

#### Diagram 1: A real-life scenario

With a partner, create a flow diagram with at least three conditions based on the following scenario:

> A friend has just messaged you that they've finished their homework and want to hang out.

1. What yes/no conditions will impact whether, when, and where you can hang out with your friend?
2. BONUS: Add a loop to your flow diagram — a condition that gets checked over and over, like "Is my homework done yet?" where `No` loops back to the same question and `Yes` moves forward.

#### Diagram 2: A power-up in a game

With a partner, pick one of these power-up ideas (or create your own) and draw a flow diagram showing how it works:

- **Speed Boost** — Player picks up a speed item. They move 2x faster, but it wears off after 10 seconds or if they get hit.
- **Shield** — Player activates a shield. It blocks the next 3 hits, then breaks. If the player falls in a pit, the shield does not help.
- **Invisibility** — Player turns invisible for 5 seconds. Enemies can't see them, but the effect ends early if they attack.

Your flow diagram should include:
1. A condition that must be met to **activate** the power-up
2. A condition that causes the power-up to **expire** or end

{{% checkpoint %}}

#### Checkpoint: Part 2

- [x] I can draw a flow diagram that represents a conditional (if/else) decision.
- [x] I can include at least three conditions in my flow diagram.
- [x] BONUS: I can include a loop in my flow diagram.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

### Part 3 — Trace Your Partner's Diagram

Swap your diagrams (both Diagram 1 and Diagram 2) with another partner pair.

For **each** diagram you receive:
1. Pick a starting input (for example: "It's 8pm and you haven't eaten dinner yet" for Diagram 1, or "Player has 0 mana" for Diagram 2).
2. Trace through the diagram step by step, following the arrows. Write down each step you take and the path you follow.
3. Did you reach an ending? Did anything confuse you or seem broken? Write one piece of feedback for the other pair.

Give the diagrams back with your feedback.

{{% checkpoint %}}

#### Checkpoint: Part 3

- [x] I traced through another pair's diagrams with sample inputs.
- [x] I gave one piece of feedback on each diagram.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Why?

Here's a side-by-side comparison of a flow diagram and the Scratch code it represents. Find the matching conditions in the flow diagram and the `if` blocks in the Scratch code. Notice how the flow diagram is a visual way to plan out the logic before writing any code.

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

<div>

```mermaid
flowchart TD
    A([Start]) --> B
    B[Player Presses E Key] --> H[Say Player Attempts Cast Spell]
    H --> C
    C{mana > 20}
    D{distance < 10}
    C -- "Yes" --> D
    C -- "No" --> E([Fail: Not enough mana])
    D -- "Yes" --> F([Cast success])
    D -- "No" --> G([Fail: Too far])
```

</div>
<div>

```scratch
when [e v] key pressed
say [Player Attempts Cast Spell]
if <(mana) > (20)> then
    if <(cast distance) < (10)> then
        say [Cast success!]
    else
        say [Fail: Too far]
    end
else
    say [Fail: Not enough mana]
end
```
</div>
</div>

### Discuss: Why?

How could planning with a flow diagram be useful? It seems like a lot of work, but what for?

### Mini-Challenge: Translate to Scratch

Look at this flow diagram. On paper (or on the back of your worksheet), write the Scratch blocks that would match this logic. Pseudocode is fine — you don't need exact Scratch syntax.

```mermaid
flowchart TD
    A([Start]) --> B{Is the sprite touching a coin?}
    B -- Yes --> C[Add 1 to score]
    C --> D{Is score = 10?}
    D -- Yes --> E[Say You win!]
    D -- No --> B
    B -- No --> B
    E --> F([Done])
```

{{< callout type="info" >}}
Think about which parts are `if` blocks, which parts repeat (loops), and what order the blocks go in.
{{< /callout >}}

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration (loops).
- [**MS-CS-FCP.3.4**](/scratch/description/#ms-cs-fcp3) — Develop an algorithm to decompose a problem of a daily task.
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including flowcharting and/or storyboarding, coding, debugging, user interfaces, usability, variables, lists, loops, conditionals, programming language, and events.
