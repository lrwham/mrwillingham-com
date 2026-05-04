---
title: "Setting Up Python with a Virtual Environment"
description: "Step-by-step terminal commands to create a virtual environment, activate it, install Pygame, and run an example game."
draft: false
toc: true
weight: 1
---

## What You're About To Do

You're going to use the Terminal inside VS Code to set up a clean Python workspace for this unit. Here's the plan:

1. Open your project folder in VS Code
2. Create a **virtual environment** — a private Python workspace just for your project
3. **Activate** that environment so Python uses the right packages
4. Install **Pygame** using `pip`
5. Run a quick example game to make sure everything works

---

## Step 1 — Open VS Code and Your Project Folder

{{< callout type="important" >}}
Ask Mr. Willingham where to save your Python folder. The recommended location is your Desktop or Documents — somewhere you can find it again.
{{< /callout >}}

1. Open **VS Code** from the dock or Spotlight (`⌘ Space` → type `VS Code`).
2. Go to **File → Open Folder…** and choose your project folder (or create a new one called `python-class`).
3. Open the integrated terminal: **Terminal → New Terminal** (or `` ⌃` ``).

You should see a prompt ending in `$`. That's the shell — it's waiting for you to type a command.

---

## Step 2 — Create a Virtual Environment

In the terminal, type this command exactly and press **Return**:

```bash
python3 -m venv venv
```

What this does:
- `python3` — run Python 3
- `-m venv` — use the built-in `venv` module
- `venv` (the last word) — the name of the folder it creates

You'll see a new folder called `venv/` appear in the VS Code sidebar. Don't open or edit anything inside it.

---

## Step 3 — Activate the Virtual Environment

Still in the terminal, run:

```bash
source venv/bin/activate
```

Your prompt will change to start with `(venv)` — like this:

```
(venv) lawton@MacBook python-class %
```

That `(venv)` at the beginning means the virtual environment is **active**. Any packages you install now will stay inside this project and won't affect anything else on the Mac.

{{< callout type="warning" >}}
You need to run `source venv/bin/activate` every time you open VS Code for this project. If you don't see `(venv)` at the start of your prompt, the environment is not active.
{{< /callout >}}

---

## Step 4 — Install Pygame with pip

With the virtual environment active, install Pygame:

```bash
pip install pygame
```

You'll see a stream of output as pip downloads and installs packages. Wait for it to finish. It's done when you see the `(venv)` prompt again.

To confirm the install worked, run:

```bash
python3 -c "import pygame; print(pygame.version.ver)"
```

If you see a version number (like `2.6.1`) printed out, Pygame is installed correctly.

---

## Step 5 — Run an Example Pygame Game

Pygame ships with a set of example programs. Run this command to see the list:

```bash
python3 -m pygame.examples.aliens
```

A small window should open with a space shooter game. Use the **arrow keys** to move and **spacebar** to shoot. Close the window when you're done.

If the window opened and you played (or at least saw it), your setup is complete.

---

## Cheat Sheet

| Command | What It Does |
| ------- | ------------ |
| `python3 -m venv venv` | Creates a virtual environment in a folder named `venv` |
| `source venv/bin/activate` | Activates the virtual environment (do this every session) |
| `pip install pygame` | Installs Pygame into the active virtual environment |
| `python3 -m pygame.examples.aliens` | Runs Pygame's built-in aliens example game |
| `deactivate` | Turns off the virtual environment (you don't need this now) |

---

## Troubleshooting

**`python3: command not found`**
Python is not installed or not on the PATH. Go back to the warmup and install Python via CCSD Self Service, then restart VS Code.

**`pip: command not found`**
The virtual environment is probably not active. Make sure you see `(venv)` in your prompt, then try again.

**The Pygame window opened but crashed immediately**
This can happen on older Macs. Try a different example instead:

```bash
python3 -m pygame.examples.stars
```

If the stars window opens, your setup is complete and you're ready to go.
