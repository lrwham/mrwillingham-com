---
title: "Day 31: The Terminal and Pygame"
date: 2026-05-04
description: "Open VS Code, navigate the file system, create a virtual environment, install Pygame, and run your first Python program."
day_number: 31
units:
  - "Python and the Terminal"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
tags:
  - python
  - terminal
  - vscode
  - pygame
  - command-line
resources:
  - Terminal Setup
draft: false
toc: true
scratchblocks: false
mermaid: false
weight: 1
---

{{< icon "calendar" >}} **Monday, May 4th, 2026**

{{% objectives %}}

## Objectives

- I can verify that Python is installed on my Mac.
- I can open VS Code and use the integrated terminal.
- I can navigate the file system using `ls` and `cd`.
- I can create and activate a Python virtual environment.
- I can install a package using `pip` and run a Pygame example.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Is Python Installed?

Before we write a single line of code, we need to confirm Python is installed on your Mac.

{{% steps %}}

### Open Spotlight Search

Press **`⌘ Space`** (Command + Spacebar) to open Spotlight.

### Search for IDLE

Type `IDLE` and press **Return**.

- **If IDLE opens** — Python is installed. Close IDLE and move on to the Work Session.
- **If nothing comes up** — Python is not installed. Go to Step 3.

### Open CCSD Self Service

Press **`⌘ Space`** again and search for **`Self Service`**. Open the CCSD Self Service app.

### Install Python

Search for **Python** in Self Service and click **Install**. Wait for it to finish.

### Confirm

Once the install completes, press **`⌘ Space`** and search for `IDLE` again. It should open now. Close it — you won't use IDLE for this class.

{{% /steps %}}

{{< callout type="important" >}}
If Self Service isn't working or Python won't install, raise your hand now. We'll sort it out before the work session starts.
{{< /callout >}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: The Terminal and Pygame

### Part 1 — Open VS Code

1. Press **`⌘ Space`** and search for **VS Code**. Open it.
2. Go to **File → Open Folder…** and open your Desktop or Documents folder. Create a new folder called `python-class` if you don't already have one, then open it.
3. Open the integrated terminal with **Terminal → New Terminal** (or press `` ⌃` ``).

You should see a prompt that ends with a `$` or `%`. This is the shell — a text interface for talking to your Mac.

---

### Part 2 — Navigate with the Terminal

The terminal starts in your project folder. Let's explore.

**List files and folders:**

```bash
ls
```

`ls` stands for *list*. It prints the names of everything in your current folder.

**Move into a folder:**

```bash
cd Documents
```

`cd` stands for *change directory*. You're now inside the `Documents` folder.

**Go back up one level:**

```bash
cd ..
```

Two dots (`..`) always means "the folder above this one."

**Find out where you are:**

```bash
pwd
```

`pwd` stands for *print working directory*. It shows the full path to your current location.

{{< callout type="tip" >}}
You don't have to navigate anywhere for the rest of this lesson — just stay in your `python-class` folder. These commands will be important all unit long.
{{< /callout >}}

---

### Part 3 — Set Up Python and Pygame

Follow the [Terminal Setup](terminal-setup/) page to:

1. Create a virtual environment
2. Activate it
3. Install Pygame
4. Run the Pygame aliens example

Work through that page step by step. Come back here when you've seen the game window open.

---

### Part 4 — Write Your First Python File

Now that Pygame is installed, let's write a tiny Python script to make sure everything works together.

1. In VS Code, go to **File → New File** and save it as `hello.py` inside your `python-class` folder.
2. Type this exactly:

```python
print("Hello, world!")
print("Python is working.")
```

3. In the terminal (make sure `(venv)` is still in your prompt), run:

```bash
python3 hello.py
```

You should see:

```
Hello, world!
Python is working.
```

If you do — you're done. Python is installed, your environment is set up, and you know how to run a script.

{{% checkpoint %}}

- [ ] I opened VS Code and created a project folder.
- [ ] I can use `ls`, `cd`, and `pwd` in the terminal.
- [ ] I created and activated a virtual environment — `(venv)` appears in my prompt.
- [ ] I installed Pygame and ran `python3 -m pygame.examples.aliens`.
- [ ] I ran `hello.py` and saw the output printed in the terminal.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you used two of the most powerful tools in programming: the **terminal** and a **code editor**. Neither one has a point-and-click interface — you have to type commands and write code. That takes getting used to, but it's how professional developers actually work.

Every day this week you'll open VS Code, activate your virtual environment, and write Python. The setup you did today is the foundation for everything else.

Tomorrow: `print()`, variables, and drawing shapes with the `turtle` module.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Students follow a precise sequence of terminal commands to set up a computing environment — a real-world application of sequencing and algorithmic thinking.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Students implement a simple algorithm by writing, saving, and running their first Python script from the terminal.
