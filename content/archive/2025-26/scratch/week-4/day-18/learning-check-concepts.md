---
title: "Example Questions: Concept Focused"
draft: false
scratchblocks: true
toc: true
---

These questions focus on the vocabulary and ideas behind Scratch, not just how a specific script behaves. A few use short code snippets where they help — especially the true/false boolean questions.

---

## Question 1

What is a **sprite** in Scratch?

**Answer:** A sprite is a character or object in a Scratch project. Each sprite has its own costumes, sounds, and scripts. You program sprites to make them do things.

**Standards:** MS-CS-FCP.3.2

---

## Question 2

What is the **stage**, and how is it different from a sprite?

**Answer:** The stage is the background area where everything happens. Sprites appear and move on top of the stage. The stage itself can have **backdrops** (its own images) and can even run scripts — but it cannot move around like a sprite can.

**Standards:** MS-CS-FCP.3.2

---

## Question 3

What is the difference between a **costume** and a **backdrop**?

**Answer:** A costume belongs to a sprite and changes how that sprite looks. A backdrop belongs to the stage and changes what the background looks like. Both can be switched during a project to animate or change scenes.

**Standards:** MS-CS-FCP.3.2

---

## Question 4

What is an **algorithm**?

**Answer:** A step-by-step set of instructions for solving a problem. Every Scratch script is an algorithm — the blocks tell the computer exactly what to do, in order.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 5

What does it mean to **debug** a program?

**Answer:** Debugging means finding and fixing mistakes ("bugs") in your code so the program behaves the way you want it to. Reading your code, testing it, and making small changes until it works is all part of debugging.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 6

Scratch is an **event-driven** programming language. What does that mean, and what is an example of an **event**?

**Answer:** Event-driven means scripts wait for something to happen ("an event") before they run. Examples of events include clicking the green flag, pressing a key, clicking a sprite, or receiving a broadcast. The "hat" blocks at the top of each stack mark which event starts that script.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 7

Why do programmers use **loops** like `forever` and `repeat`? What would programs look like without them?

**Answer:** Loops let a small amount of code do a lot of work by repeating instructions automatically. Without loops, you'd have to copy and paste the same blocks over and over — a simple game would take thousands of blocks instead of a handful.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 8

What is the difference between a `forever` loop and a `repeat (10)` loop?

**Answer:** `forever` keeps running its blocks until the whole project is stopped — it never finishes on its own. `repeat (10)` runs its blocks exactly 10 times and then stops, and the script continues with whatever comes after it.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.8

---

## Question 9

What is a **conditional**, and what block in Scratch represents one?

**Answer:** A conditional is code that only runs when a certain condition is true. In Scratch, the `if … then` and `if … then … else` blocks are conditionals. They check a true/false question and decide which blocks to run based on the answer.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 10

True or false?

```scratch
<(5) > (3)>
```

**Answer:** **True.** 5 is greater than 3, so this boolean is true.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 11

True or false?

```scratch
<(4) = (2)>
```

**Answer:** **False.** 4 does not equal 2, so this boolean is false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 12

True or false?

```scratch
<<(3) > (1)> and <(5) < (2)>>
```

**Answer:** **False.** `and` is only true when **both** sides are true. The left side is true (3 > 1), but the right side is false (5 is not less than 2), so the whole thing is false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 13

True or false?

```scratch
<<(3) > (1)> or <(5) < (2)>>
```

**Answer:** **True.** `or` is true when **at least one** side is true. The left side (3 > 1) is true, so the whole boolean is true — it doesn't matter that the right side is false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 14

True or false?

```scratch
<not <(7) = (7)>>
```

**Answer:** **False.** Inside the `not`, `7 = 7` is true. The `not` block flips true into false, so the whole boolean is false.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.9

---

## Question 15

In a flow diagram, what shape is used for a **decision** (a yes/no question), and how is it different from the shape used for an action?

**Answer:** A **diamond** is used for a decision. Actions (things the program *does*) are drawn as **rectangles**. A diamond always has at least two arrows leaving it — one for "yes" and one for "no" — while a rectangle usually has just one arrow leaving it.

**Standards:** MS-CS-FCP.3.2

---

## Question 16

In a flow diagram, what shape is used for the **start** and **end** of the program?

**Answer:** An **oval** (sometimes drawn as a rounded rectangle). You use one oval to mark where the flow begins and another to mark where it ends.

**Standards:** MS-CS-FCP.3.2

---

## Question 17

Both of these blocks change a variable. What is the difference between them?

```scratch
set [score v] to (0)
```

```scratch
change [score v] by (1)
```

**Answer:** `set` **replaces** the variable's current value with the new one — the old value is gone. `change` **adds** to the current value (you can also subtract with a negative number) — the old value matters because the new value depends on it. Use `set` to reset a variable, and `change` to increase or decrease it.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 18

What do `x` and `y` mean when we talk about a sprite's position? Which one controls left/right, and which one controls up/down?

**Answer:** `x` is the **horizontal** coordinate — it controls how far left or right the sprite is. `y` is the **vertical** coordinate — it controls how far up or down. The point `x: 0, y: 0` is the exact center of the stage.

**Standards:** MS-CS-FCP.3.2

---

## Question 19

Why would a programmer use **clones** instead of just making lots of copies of a sprite by hand?

**Answer:** Clones let one sprite produce as many independent copies as needed *while the program is running*. You only have to write the code once, and every clone runs the same script on its own. Hand-making copies would mean dragging out hundreds of sprites and duplicating the code on each — slow, hard to edit, and impossible if you don't know in advance how many you need.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5

---

## Question 20

Why would a programmer use `broadcast` and `when I receive` instead of putting all the code on one sprite?

**Answer:** Broadcasts let sprites **communicate** with each other. One script can send a message, and any sprite that cares about that message can react to it. This keeps each sprite's code focused on its own job and lets several sprites respond to the same event without knowing about each other's details.

**Standards:** MS-CS-FCP.3.2, MS-CS-FCP.4.5
