---
title: "Day 34: Design Your Own Pokémon"
date: 2026-05-07T08:07:24-04:00
description: "Use a Python tool to design a custom Pokémon, compare its stats against the real dataset with box plots, scatter plots, and histograms, and revise until it fits — then sketch it on paper."
day_number: 34
units:
  - "Python and the Terminal"
  - "Data Analysis"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.4.2
  - MS-CS-FCP.6.3
  - MS-CS-FCP.6.4
tags:
  - python
  - pandas
  - matplotlib
  - mplcursors
  - data
  - design
resources: []
draft: false
toc: true
scratchblocks: false
weight: 4
---

{{< icon "calendar" >}} **Thursday, May 7th, 2026**

{{% objectives %}}

## Objectives

- I can design a Pokémon (name, type, six stats, height, weight) and explain my choices.
- I can use **box plots, scatter plots, and histograms** to compare my design against real Pokémon.
- I can **revise** stats that look wrong, based on what the plots show me.
- I can save my final Pokémon as a `.csv` file and sketch it on paper.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Get the Designer

Today is a design day. Mr. Willingham wrote a Python tool that does the plotting for you, so your job is to **make good design choices** and check them against real data.

{{< button text="Download pokemon-designer.zip" >}}pokemon-designer.zip{{< /button >}}

{{% steps %}}

### Download and unzip

Click the button above. In **Downloads**, double-click `pokemon-designer.zip`. You'll get a folder named `pokemon-designer/` with two files:

- `designer.py` — the tool.
- `pokemon.csv` — the dataset.

### Open the folder in VS Code

`File → Open Folder…` and pick `pokemon-designer/`.

It is in your Downloads.

### OPTIONAL Install one new library

We already installed `pandas` and `matplotlib` yesterday. Today you can use **one more**, for hover tooltips on scatter plots. In the VS Code terminal run:

```
python3 -m pip install mplcursors
```

{{< callout type="info" >}}
The tool will still run if `mplcursors` doesn't install — you just won't get hover tooltips. Don't get stuck on this; ask for help and move on.
{{< /callout >}}

### Run the tool

Click on the Play button at the top right of `designer.py` to run it. In the terminal, you should see:

```
============================================
    POKEMON DESIGNER  -  Day 34
============================================

=== Design Your Pokemon ===

Pokemon name: 
```

Follow the prompts. **For now, type any name and pick any type — we're just making sure it works.** When the menu shows up, pick `5. Save and quit` and accept the default filename. You should see "Saved to: …" with a path. Done.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I unzipped `pokemon-designer.zip` into my `python-class` folder.
- [ ] I ran `python3 designer.py` and it asked me for a name.
- [ ] I made it all the way to the menu and saved a Pokémon.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Design Your Real Pokémon

Now you'll design the Pokémon you actually want. The tool does the plotting. Your job is to **decide** and **revise**.

{{% steps %}}

### Brainstorm before you type

Before running the tool again, think about:

- What is your Pokémon's **personality**? Is it sneaky, tough, fast, fragile?
- What is its **primary type**? Does it have a secondary type?
- What is its **role in battle**? A glass cannon (high attack, low defense)? A tank (high HP and defense, low speed)? A speedster?

Your stats should match the personality. A "tank" with `speed = 200` doesn't make sense.

### Use the menu to test your design

When the menu shows up, you have three plot tools:

| Plot          | What it shows                                                        | Best for                                                    |
| ------------- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| Box plot      | Where your stat sits inside the typical range for your **type**.     | "Is my attack normal for a fire type?"                      |
| Scatter plot  | Your Pokémon as a star among **all 800** Pokémon, on two stats.      | "Which real Pokémon is most like mine?"                     |
| Histogram     | The distribution of one stat across **every** Pokémon.               | "Is my speed unusual for any Pokémon, anywhere?"            |

Try **at least one of each**.

### Revise

After looking at a plot, you'll usually spot a stat that's way off. Pick `4. Edit my Pokémon` and adjust it. Then plot again. **Loop until you're happy.**

{{< callout type="info" >}}
Designers don't get it right the first time. The point of today is to *let the data argue with you*, then change your mind.
{{< /callout >}}

### Save your final Pokémon

Once it feels right, pick `5. Save and quit`. Use a filename like `your_pokemon_name.csv`. The tool will print the full path where it saved.

{{% /steps %}}

Distribution
: How often each value shows up in a dataset. A histogram is a picture of a distribution.

Outlier
: A value far outside the typical range. Outliers can be exciting or wrong — your call.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I brainstormed a personality and role before entering numbers.
- [ ] I tried a **box plot**, a **scatter plot**, and a **histogram**.
- [ ] I revised at least one stat after looking at a plot.
- [ ] I saved my final Pokémon as a `.csv` file.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Submit and Sketch

You've finalized the **numbers**. Two last steps.

### Submit your stats

Open your saved `.csv` in VS Code so you can copy the values, then submit them with the form:

{{< button text="Submit Pokémon Stats" >}}https://forms.cloud.microsoft/r/sXg6jdGju0{{< /button >}}

### Sketch it

Now bring it to life. Mr. Willingham has paper. On the paper, draw:

1. Your Pokémon — front view, big enough to see.
2. Its **name**, **type(s)**, and the six **battle stats** along the side.
3. A **one-sentence flavor** description (like "The Seed Pokémon" → "The Glitch Pokémon").

Hand in the paper sketch when you're done.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary including **data** and **data analysis** — students extend yesterday's vocabulary with **distribution**, **outlier**, **box plot**, and **scatter plot**.
- [**MS-CS-FCP.4.2**](/scratch/description/#ms-cs-fcp4) — Use the design process to **brainstorm, implement, test, and revise** an idea — students brainstorm a Pokémon, implement it as data, test it against the real dataset with plots, and revise the stats that don't fit.
- [**MS-CS-FCP.6.3**](/scratch/description/#ms-cs-fcp6) — Analyze and explain the suitability of a computational artifact — students judge whether their designed Pokémon "fits" the real data and explain which stats are typical, unusual, or out of place.
- [**MS-CS-FCP.6.4**](/scratch/description/#ms-cs-fcp6) — Develop work for **creative expression** — students use a computational tool to design an original creature with both numerical stats and a hand-drawn sketch.
