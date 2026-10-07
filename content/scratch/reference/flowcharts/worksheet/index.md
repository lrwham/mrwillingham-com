---
type: bare
toc: false
title: Flow Diagram Worksheet
draft: false
mermaid: true
---

<style>
  @page { margin: 0.5in; }
  body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0.5in;
    color: #000;
  }
  h1 {
    font-size: 22px;
    margin: 0 0 6px 0;
    text-align: center;
  }
  h2 {
    font-size: 16px;
    margin: 20px 0 6px 0;
    border-bottom: 2px solid #000;
    padding-bottom: 2px;
  }
  h3 {
    font-size: 13px;
    margin: 12px 0 4px 0;
  }
  p, li {
    font-size: 11px;
    line-height: 1.4;
  }
  .name-lines {
    display: flex;
    gap: 40px;
    margin-bottom: 10px;
    font-size: 13px;
  }
  .name-lines span {
    flex: 1;
    border-bottom: 1px solid #000;
    padding-bottom: 2px;
  }
  .shapes-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
    margin-bottom: 10px;
  }
  .shapes-table th, .shapes-table td {
    border: 1px solid #999;
    padding: 4px 8px;
    text-align: left;
  }
  .shapes-table th {
    background: #eee;
  }
  .draw-box {
    border: 2px solid #000;
    border-bottom: 0px;
    min-height: 220px;
    margin: 8px 0 12px 0;
    padding: 8px;
  }
  .draw-box-small {
    border: 2px solid #000;
    min-height: 120px;
    margin: 8px 0 12px 0;
    padding: 8px;
  }
  .answer-lines {
    margin: 6px 0;
  }
  .answer-lines .line {
    border-bottom: 1px solid #999;
    height: 24px;
    margin-bottom: 2px;
  }
  .reference-diagram {
    text-align: center;
    margin: 8px 0;
  }
  .page-break {
    page-break-before: always;
  }
  .mermaid svg {
  height: 700px; /* Or use other units like em, cm, etc. */
  width: auto; /* Preserve aspect ratio */
}
</style>

<div class="name-lines">
  <span><strong>Name:</strong> </span>
  <span><strong>Partner:</strong> </span>
  <span><strong>Period:</strong> </span>
</div>

<table class="shapes-table">
  <tr><th>Shape</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>Oval</strong></td><td>Start or End</td><td>"Start", "Done"</td></tr>
  <tr><td><strong>Rectangle</strong></td><td>Action (do something)</td><td>"Eat breakfast", "Go to school"</td></tr>
  <tr><td><strong>Diamond</strong></td><td>Decision (yes/no question)</td><td>"Is it raining?"</td></tr>
</table>

**Arrows** connect shapes and show which direction the program flows. A diamond always has **two arrows** — one for **Yes** and one for **No**.

**Example**


```mermaid
flowchart TD
    A([START]) --> B[Get out of bed]
    B --> C[Look out the window]
    C --> D{Is it raining?}

    D -- "Yes" --> E{Do you have\nan umbrella?}
    D -- "No" --> F[Put on sunscreen]

    E -- "Yes" --> G[Grab your umbrella]
    E -- "No" --> H[Stay inside and\nplay video games]

    G --> I[Go outside]
    F --> I

    I --> J{Are you\nhaving fun?}
    J -- "Yes" --> K[Keep playing outside]
    J -- "No" --> L[Go back inside]

    K --> M([DONE])
    L --> M
    H --> M
```


<div class="page-break"></div>

## Part 1: Trace the Flow

Look at the maze wall detection diagram on the board/screen. Answer these questions:

### 1. What is the condition in the flow diagram?

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
</div>

### 2. Where are the loops? What is repeated?

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
</div>

## Part 2, Diagram 1: A Real-Life Scenario

> A friend has just messaged you that they've finished their homework and want to hang out.

**Requirements:** At least 3 conditions. At least one merge point (convergence). Bonus: add a loop.

<div class="draw-box"></div>

<div class="page-break"></div>

## Part 2, Diagram 2: A Power-Up in a Game

**Pick one** (or create your own):
- **Speed Boost** — 2x speed, wears off after 10 seconds or if hit
- **Shield** — Blocks next 3 hits, then breaks. Doesn't help with pits
- **Invisibility** — 5 seconds invisible, ends early if you attack

**Requirements:** A condition to activate the power-up. A condition that makes it expire or end.

**Power-up chosen:** _______________________________________________

<div class="draw-box"></div>

<div class="page-break"></div>

## Part 3: Peer Trace

Swap diagrams with another pair. Pick a starting input and trace through each diagram.

### Diagram 1 Feedback

**Starting input I chose:** _________________________________________

**Path I followed:**

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
  <div class="line"></div>
</div>

**Feedback:** Did you reach an ending? Was anything confusing or broken?

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
</div>

### Diagram 2 Feedback

**Starting input I chose:** _________________________________________

**Path I followed:**

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
  <div class="line"></div>
</div>

**Feedback:** Did you reach an ending? Was anything confusing or broken?

<div class="answer-lines">
  <div class="line"></div>
  <div class="line"></div>
</div>

<div class="page-break"></div>

## Mini-Challenge: Translate to Scratch

Look at this flow diagram. Write the Scratch blocks that match this logic. Pseudocode is fine.

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

**Try it in Scratch if you finished early**
