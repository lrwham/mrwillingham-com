---
title: "Day 15: Minecraft Special"
date: 2026-04-03
description: ""
day_number: 15
units:
  - ""
standards:
  - MS-CS-FCP.2.3
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.1
  - MS-CS-FCP.4.5
  - MS-CS-FCP.4.8
tags:
  - Scratch
  - Minecraft
resources: []
draft: false
toc: true
scratchblocks: false
weight: 5
---

{{< icon "calendar" >}} **Friday, April 3rd, 2026**

{{% objectives %}}

## Objectives

- I can use a command line interface (CLI) to navigate and create files.
- I can use commands in Minecraft Education Edition to modify my world.

{{% /objectives %}}

{{% warmup %}}

## Warmup

Login to Clever and check your progress on **Code.org Lesson 14: Nested Loops**. If you haven't finished it yet, use this time to complete it now.

{{< clever >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have completed Lesson 14: Nested Loops on Code.org.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

### What is a CLI?

A **Command Line Interface (CLI)** is a way to interact with a computer by typing text commands instead of clicking icons and buttons. Before computers had graphical interfaces with windows and menus, the command line was the *only* way to use a computer.

In the 1960s and 70s, programmers used **terminals** — screens that could only display text — to communicate with large mainframe computers. You would type a command, press Enter, and the computer would respond with text. Operating systems like **Unix** (1971) and later **MS-DOS** (1981) were built entirely around this idea. When Apple released the Macintosh in 1984 and Microsoft released Windows in 1985, the **graphical user interface (GUI)** became popular — but the command line never went away.

Today, software developers, system administrators, and power users still rely on the CLI every day. It's faster for many tasks, it can be automated, and it gives you more control than a GUI. Even Minecraft has its own built-in command line.

---

### Terminal Walkthrough

Mr. Willingham will walk the class through using Apple's **Terminal** app. Follow along on your own computer.

{{% steps %}}

### `ls` — List files

Lists the files and folders in your current location. Think of it like opening a folder and seeing what's inside.

```
ls
```

```
ls Desktop
```

### `pwd` — Print working directory

Shows you exactly where you are in the file system. It prints the full path to your current folder.

```
pwd
```

You might see something like: `/Users/student`

### `cd` — Change directory

Moves you into a different folder. Like double-clicking a folder to open it.

```
cd Desktop
```

To go back up one folder:

```
cd ..
```

### `touch` — Create a file

Creates a new, empty file. The file won't have anything in it yet — you're just making it exist.

```
touch hello.txt
```

### `nano` — Edit a file

Opens a simple text editor right inside the terminal. You can type, then press **Ctrl + X** to exit (it will ask if you want to save).

```
nano hello.txt
```

### `mkdir` — Make a directory

Creates a new folder.

```
mkdir my-project
```

You can then `cd my-project` to go inside it.

{{% /steps %}}

---

### Minecraft Education Edition: The Command Line

Minecraft has its own CLI built right into the game. When you press **/** or **T** to open the chat window, you're actually opening a command line. Every command starts with a `/` — just like typing commands in a terminal.

Here are two powerful commands to try:

#### `/tp` — Teleport

Teleports you (or another player) to a specific location in the world. Coordinates in Minecraft are **x** (east/west), **y** (up/down), and **z** (north/south).

```
/tp @s 0 80 0
```

This teleports yourself (`@s`) to coordinates (0, 80, 0) — the center of the world, 80 blocks up.

```
/tp @s ~ ~50 ~
```

The `~` means "relative to where I am now." This teleports you 50 blocks straight up from your current position.

#### `/fill` — Fill a region with blocks

Fills a rectangular area between two sets of coordinates with a block type. This is like building hundreds of blocks instantly.

```
/fill ~0 ~0 ~0 ~10 ~10 ~10 glass
```

This fills a 10x10x10 cube of glass blocks starting from your current position.

```
/fill ~0 ~-1 ~0 ~20 ~-1 ~20 gold_block
```

This creates a 20x20 gold floor right below your feet.

```
/fill ~0 ~0 ~0 ~5 ~3 ~5 air
```

This clears out a room-sized area by filling it with air — useful for carving out spaces.

---

### Independent Worlds

Open **Minecraft Education Edition** and create your own world. Experiment with commands and start building. Have fun with it — this is your world to explore.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I followed along with the Terminal walkthrough.
- [ ] I opened Minecraft Education Edition and created a world.
- [ ] I used `/tp` or `/fill` in Minecraft.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Happy spring break! See you when we get back. If time allows, we will join a multiplayer server.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.2.3**](/scratch/description/#ms-cs-fcp2) — Demonstrate an understanding of the fundamental concepts for how computers process programming commands.
- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences, algorithms, and iteration.
- [**MS-CS-FCP.4.1**](/scratch/description/#ms-cs-fcp4) — Develop a working vocabulary of programming including coding, user interfaces, and programming language.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program.
- [**MS-CS-FCP.4.8**](/scratch/description/#ms-cs-fcp4) — Create a computer program that implements a loop.
