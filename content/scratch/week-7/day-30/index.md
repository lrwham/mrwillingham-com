---
title: "Day 30: Python and VS Code"
date: 2026-11-30T08:00:00-05:00
description: "Confirm Python is installed, set up a project folder in VS Code, and write and run your first script."
day_number: 30
units:
  - "Python and the Terminal"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.5
tags:
  - python
  - terminal
  - vscode
resources:
  - Python
  - VS Code
draft: false
toc: true
scratchblocks: false
weight: 1
---

{{< icon "calendar" >}} **Monday, November 30th, 2026**

{{% objectives %}}

## Objectives

- I can verify that Python is installed on my Mac.
- I can open VS Code and set up a project folder.
- I can write a Python script and run it.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Is Python Installed?

Follow the **Is Python Installed?** section of [Python and VS Code Setup](/scratch/reference/python-setup/#is-python-installed): search Spotlight for IDLE, and install Python from Self Service if it is missing. Finish by running one line in IDLE:

```python
print("Hello, world!")
```

{{< callout type="important" >}}
If Self Service is not working or Python will not install, raise your hand now.
{{< /callout >}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] IDLE opens on my Mac.
- [ ] I ran `print("Hello, world!")` and saw the output.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Python Basics, Then VS Code

Follow along with Mr. Willingham in IDLE. Try these on your own:

```python
print("Hello, world!")
3 + 4
"Hello, " + "Python!"
a = 10
b = 20
a + b
c = a * b
c
d
```

What happens on the last line? That is an error message. Read it.

IDLE is fine for one line at a time. For real scripts we use a code editor. Follow **Opening VS Code** and **Writing and Running a Script** on [Python and VS Code Setup](/scratch/reference/python-setup/#opening-vs-code): make the `python-class` folder, create `hello.py`, and run it with the play button.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I created a `python-class` folder on the Desktop and opened it in VS Code.
- [ ] I ran `hello.py` and saw both lines printed.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

You used two of the most important tools in programming today: a terminal and a code editor. Neither one is point-and-click; you type commands and write code. That is how professionals work, and it takes getting used to.

Tomorrow you build a complete game in Python: a number guessing game.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including sequences and algorithms (a precise sequence of setup steps).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (writing, saving, and running a first script).
