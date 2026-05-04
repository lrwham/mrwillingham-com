---
title: "Terminal and VS Code Quick Reference"
description: "A reference card for opening VS Code, using basic terminal commands, and running Python scripts."
draft: false
toc: true
weight: 1
---

## Opening VS Code

Press **`⌘ Space`** to open Spotlight, type `VS Code`, and press **Return**.

To open your project folder: **File → Open Folder…** then navigate to your `python-class` folder.

To open the integrated terminal: **Terminal → New Terminal** (or press `` ⌃` ``).

---

## Basic Terminal Commands

| Command | What It Does | Example |
| ------- | ------------ | ------- |
| `ls` | List files and folders in the current directory | `ls` |
| `cd` | Change into a folder | `cd Documents` |
| `cd ..` | Go up one level | `cd ..` |
| `pwd` | Print the full path of your current location | `pwd` |
| `python3 filename.py` | Run a Python script | `python3 hello.py` |

---

## Writing and Running a Python Script

1. In VS Code, go to **File → New File**.
2. Save it with a `.py` extension — for example, `hello.py`.
3. Write your Python code in the editor.
4. In the terminal, run it:

```bash
python3 hello.py
```

The output appears in the terminal immediately below the command.

---

## Troubleshooting

**`python3: command not found`**
Python is not installed. Press `⌘ Space`, search for **Self Service**, and install Python from the CCSD Self Service app. Restart VS Code and try again.

**My file runs but nothing appears**
Make sure your script has at least one `print()` call. A script with no output runs silently and returns to the prompt — that's normal.

**I see a `SyntaxError`**
Python found a typo in your code. The error message will tell you the line number — go to that line in VS Code and look for a missing colon, mismatched quote, or misspelled keyword.
