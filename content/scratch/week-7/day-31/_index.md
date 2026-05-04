---
title: "Day 31: The Terminal and VS Code"
date: 2026-05-04
description: "Open VS Code, use the integrated terminal to navigate the file system, and write and run your first Python script."
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
- I can navigate the file system using `ls`, `cd`, and `pwd`.
- I can write a Python script and run it from the terminal.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Is Python Installed?

Before we write a single line of code, we need to confirm Python is installed on your Mac.

{{% steps %}}

### Open Spotlight Search

Press **`⌘ Space`** (Command + Spacebar) to open Spotlight.

### Search for IDLE

Type `IDLE` and press **Return**.

- **If IDLE opens** — Python is installed. Click next to the `>>>` prompt, type `print("Hello, world!")`, and press **Return**. You should see `Hello, world!` printed on the next line. Close IDLE and move on to the Work Session.
- **If nothing comes up** — Python is not installed. Go to Step 3.

### Open CCSD Self Service

Press **`⌘ Space`** again and search for **`Self Service`**. Open the CCSD Self Service app.

### Install Python

Search for **Python** in Self Service and click **Install**. Wait for it to finish.

### Confirm

Once the install completes, press **`⌘ Space`** and search for `IDLE` again. It should open now.

### Try It in IDLE

You have Python installed — let's run one line of code right now. In the IDLE window, click next to the `>>>` prompt, type this exactly, and press **Return**:

```python
print("Hello, world!")
```

You should see `Hello, world!` appear on the next line. That's Python running.
{{% /steps %}}

{{< callout type="important" >}}
If Self Service isn't working or Python won't install, raise your hand now. We'll sort it out before the work session starts.
{{< /callout >}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

### Python Basics in the IDLE

We'll explore some Python basics. Follow along with Mr. Willingham. Some of the examples are listed below if you want to try them on your own.

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

### Python in VS Code

It is usually easier to write Python in a code editor like VS Code instead of IDLE. Let's set that up now.

Use Spotlight Search to open **Visual Studio Code**. Then follow along with Mr. Willingham. We'll setup a project folder called `python-basics`.

1. In VS Code, go to **File → Open Folder**.
2. In the popup, choose your Desktop, then click **New Folder** and name it `python-class`. Click **Open** to open that folder in VS Code.
3. In VS Code, go to **File → New File** and save it as `hello.py` inside your `python-class` folder.
4. Type this exactly:

```python
print("Hello, world!")
print("Python is working.")
```

5. Save the File `⌘ S`
6. Run the code by pressing the Play button.

{{% checkpoint %}}

- [ ] I opened VS Code and created a `python-class` folder.
- [ ] I ran `hello.py` and saw both lines printed in the output terminal.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you used two of the most powerful tools in programming: the **terminal** and a **code editor**. Neither one has a point-and-click interface — you have to type commands and write code. That takes getting used to, but it's how professional developers actually work.

Every day this week you'll open VS Code and write Python. The setup you did today is the foundation for everything else.

Tomorrow: `print()`, variables, and drawing shapes with the `turtle` module.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Students follow a precise sequence of terminal commands to set up a computing environment — a real-world application of sequencing and algorithmic thinking.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Students implement a simple algorithm by writing, saving, and running their first Python script from the terminal.
