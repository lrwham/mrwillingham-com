---
title: "Day 32: Pokémon Data with Pandas"
date: 2026-12-02T08:00:00-05:00
description: "Load a real dataset, compute statistics with pandas, and draw your first plots with matplotlib."
day_number: 32
units:
  - "Python and the Terminal"
  - "Data Analysis"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.3.3
  - MS-CS-FCP.4.3
  - MS-CS-FCP.4.5
tags:
  - python
  - pandas
  - matplotlib
  - data
resources:
  - Python
  - VS Code
draft: false
toc: true
scratchblocks: false
weight: 3
---

{{< icon "calendar" >}} **Wednesday, December 2nd, 2026**

{{% objectives %}}

## Objectives

- I can open a real `.csv` dataset in a spreadsheet and explore it.
- I can use `pandas` to compute the mean, median, min, and max of a column.
- I can use `matplotlib` to make a histogram and a bar chart.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Meet the Dataset

Today is Project Day 1 of [Pokémon Data](/scratch/projects/python-pokemon-data/). Download `pokemon.csv.zip` from [Datasets](/scratch/reference/datasets/), unzip it, and open it in Numbers or Excel. Spend five minutes answering the questions in the **Meet the Dataset** section.

While it is open, run the library install in the VS Code terminal so any errors show up early:

```bash
python3 -m pip install pandas matplotlib
```

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I opened `pokemon.csv` and found one interesting fact to share.
- [ ] `pandas` and `matplotlib` installed without errors.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Stats and Plots

Drag `pokemon.csv` into `python-class`, then follow **Basic Statistics** and **Plots** on [Pokémon Data](/scratch/projects/python-pokemon-data/#project-day-1-stats-and-plots):

1. `pokemon_stats.py` — load the CSV, print `df.head()`.
2. Mean, median, min, max of `attack`; then `.describe()`; then try other columns.
3. A histogram of `attack`, a bar chart of `type1`, and (stretch) a scatter plot of attack versus defense.

A **library** is code someone else wrote that you install and use. `df` is a **DataFrame** — pandas's word for a table.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I printed the first five rows of the dataset.
- [ ] I printed mean, median, min, and max for at least two columns.
- [ ] I made a histogram and a bar chart.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

You went from a wall of numbers in a spreadsheet to a few lines of code that summarized 800 Pokémon instantly. That is **data analysis**. Tomorrow you flip it: invent a Pokémon and let the data judge it.

Want more? The soccer dataset on the [Datasets](/scratch/reference/datasets/) page works with the same code.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including data, data collection, and data analysis.
- [**MS-CS-FCP.3.3**](/scratch/description/#ms-cs-fcp3) — Analyze the input-process-output-storage model (load a CSV, compute with pandas, print or plot).
- [**MS-CS-FCP.4.3**](/scratch/description/#ms-cs-fcp4) — Cite evidence on how computers represent data (a `.csv` as a structured table of records).
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program (a sequence of pandas calls).
