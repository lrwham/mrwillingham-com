---
title: Boolean Operators in Flowcharts
date: 2026-03-30
type: single
toc: false
mermaid: true
---

Imagine you're building a platformer game. Your sprite needs to:

1. **Jump** only when the player presses space **and** the sprite is touching the ground.
2. **Take damage** when the sprite touches lava **or** spikes.
3. **Fall** when the sprite is **not** touching the ground.

## Without Boolean Operators

Without `and`, `or`, and `not`, you have to use **nested `if` blocks** to check each condition separately. The flowchart gets big fast.

```mermaid
flowchart TD
    A([Start]) --> B{Is space\npressed?}

    B -- Yes --> C{Is sprite\ntouching ground?}
    B -- No --> D{Is sprite\ntouching lava?}

    C -- Yes --> J[Jump!]
    C -- No --> D

    J --> D

    D -- Yes --> H[Take damage]
    D -- No --> E{Is sprite\ntouching spikes?}

    E -- Yes --> H
    E -- No --> F{Is sprite\ntouching ground?}

    H --> F

    F -- Yes --> G([Done])
    F -- No --> I[Fall]

    I --> G
```

Notice the problems:

- We have to check **"touching ground?"** in **two different places** — once for jumping and once for falling.
- We have to check **lava** and **spikes** in **separate diamonds**, even though they do the same thing.
- The diagram is large and hard to follow.

## With Boolean Operators

With `and`, `or`, and `not`, each decision combines its conditions into **one diamond**. The flowchart becomes much simpler.

```mermaid
flowchart TD
    A([Start]) --> B{Is space pressed\nAND touching ground?}

    B -- Yes --> C[Jump!]
    B -- No --> D

    C --> D{Is sprite touching\nlava OR spikes?}

    D -- Yes --> E[Take damage]
    D -- No --> F

    E --> F{Is sprite NOT\ntouching ground?}

    F -- Yes --> G[Fall]
    F -- No --> H([Done])

    G --> H
```

Same game logic — but now:

- **`and`** combines the jump conditions into one check.
- **`or`** combines lava and spikes into one check.
- **`not`** flips "touching ground" so we can ask "NOT touching ground?" directly instead of hiding the fall action inside an else branch.

Three operators, half the diagram.
