---
title: "Python and VS Code Setup"
description: "Check that Python is installed, set up a project folder in VS Code, run a script, install libraries, and fix common errors."
weight: 9
toc: true
---

Everything in the Python unit starts here. Do this once, then come back when something breaks.

## Is Python Installed?

1. Press `cmd + space` to open Spotlight.
2. Type `IDLE` and press `return`.
3. **IDLE opens:** Python is installed. Click next to the `>>>` prompt, type `print("Hello, world!")`, and press `return`. You should see `Hello, world!` on the next line.
4. **Nothing comes up:** Python is not installed. Continue below.

### Installing Python

1. Press `cmd + space`, search for **Self Service**, and open the CCSD Self Service app.
2. Search for **Python** and click **Install**. Wait for it to finish.
3. Search Spotlight for `IDLE` again. It should open now.

{{< callout type="important" >}}
If Self Service is not working or Python will not install, raise your hand before going any further.
{{< /callout >}}

## Opening VS Code

1. Press `cmd + space`, type `Visual Studio Code`, and press `return`.
2. Go to **File → Open Folder…**.
3. Choose your **Desktop**, click **New Folder**, name it `python-class`, and click **Open**.

Every Python file you write this unit goes in `python-class`. If VS Code asks whether you trust the authors of the folder, click **Yes**.

## Writing and Running a Script

1. **File → New File**, then **File → Save** as `hello.py` inside `python-class`. The `.py` ending matters.
2. Type:

```python
print("Hello, world!")
print("Python is working.")
```

3. Save with `cmd + S`.
4. Click the **Run** (play) button in the top-right corner of the editor. The output appears in the terminal panel at the bottom.

You can also run a script from the integrated terminal (**Terminal → New Terminal**, or `` ctrl + ` ``):

```bash
python3 hello.py
```

## Basic Terminal Commands

| Command | What it does | Example |
| ------- | ------------ | ------- |
| `ls` | List the files and folders where you are | `ls` |
| `pwd` | Print the full path of where you are | `pwd` |
| `cd` | Move into a folder | `cd Desktop` |
| `cd ..` | Go up one folder | `cd ..` |
| `mkdir` | Make a new folder | `mkdir my-project` |
| `touch` | Make a new, empty file | `touch notes.txt` |
| `python3 file.py` | Run a Python script | `python3 hello.py` |

## Installing Libraries

A **library** is code someone else wrote that you can use. Install from the VS Code terminal, once per library:

```bash
python3 -m pip install pandas matplotlib
```

The terminal scrolls for a while. When the prompt comes back, it is done. If `pip` prints an error, raise your hand.

## Troubleshooting

**`python3: command not found`**
Python is not installed. Install it from Self Service (above), then quit and reopen VS Code.

**The Run button runs the wrong file**
The Run button runs whichever file is open in the editor. Click into the file you want first.

**My file runs but nothing appears**
A script with no `print()` runs silently. That is normal. Add a `print()`.

**`SyntaxError`**
Python found a typo. The message gives a line number; go there and look for a missing colon, a mismatched quote, or a misspelled word.

**`FileNotFoundError` when reading a CSV**
The data file is not in the same folder as the script. Drag it into `python-class` and run again.

**A plot window will not close, or windows keep piling up**
Close each plot window before running the script again.
