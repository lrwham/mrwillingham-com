---
title: "Day 33: Pokémon Data with Pandas"
date: 2026-05-06T08:07:24-04:00
description: "Open a real-world Pokémon dataset in Numbers, then use pandas to compute basic statistics and matplotlib to draw your first plots."
day_number: 33
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
  - statistics
resources: []
draft: false
toc: true
scratchblocks: false
weight: 3
---

{{< icon "calendar" >}} **Wednesday, May 6th, 2026**

{{% objectives %}}

## Objectives

- I can open a real `.csv` dataset in Numbers or Excel and explore it.
- I can use the `pandas` library to compute the **mean**, **median**, **min**, and **max** of a column.
- I can use `matplotlib` to make a histogram and a bar chart from a dataset.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Meet the Dataset

Today we start a short mini-unit on **data**. Before we touch any code, let's see what real data actually looks like.

{{< button text="Download pokemon.csv.zip" >}}pokemon.csv.zip{{< /button >}}

{{% steps %}}

### Download the file

Click the button above. The file `pokemon.csv.zip` will save to your **Downloads** folder.

### Unzip it

Find `pokemon.csv.zip` in Downloads and **double-click** it. macOS will unzip it and leave you with a new file named `pokemon.csv` next to the zip.

### Open it

Double-click `pokemon.csv`. It will probably open in **Numbers** or **Excel** — that's expected. A `.csv` is just a plain text file full of rows and columns, so spreadsheet apps know how to display it.

### Explore on your own (about 5 minutes)

Scroll around. Try to answer:

- About how many **rows** are there? (Scroll to the bottom.)
- About how many **columns** are there?
- Find your favorite Pokémon. What is its `attack` value?
- Click the `attack` column and sort it from largest to smallest. Who has the highest attack?
- What's the difference between `type1` and `type2`?

{{% /steps %}}

Data
: Information stored in a form a computer can work with — usually numbers, words, or both.

Dataset
: A collection of related `data`, often saved together in one file like a `.csv`.

CSV
: Short for **comma-separated values**. Each row is one record. Commas separate the columns.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I downloaded and unzipped `pokemon.csv.zip`.
- [ ] I opened `pokemon.csv` in Numbers or Excel and looked at the data.
- [ ] I found one interesting fact about the dataset and can share it with the class.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session 1: Basic Stats with Pandas

Looking at all those rows in Numbers is fine, but the spreadsheet can't tell us the **average** attack stat across all 800 Pokémon in one click. For that we need code.

We're going to use two new tools called **libraries**:

- `pandas` — the most popular Python library for working with data tables.
- `matplotlib` — the most popular Python library for drawing plots.

A library is just pre-written code that someone else wrote and shared, so you can use it without writing it yourself.

{{% steps %}}

### Install the libraries

Open VS Code and your `python-class` folder. Open the **integrated terminal** (`View → Terminal`) and run this **once**:

```
python3 -m pip install pandas matplotlib
```

The terminal will scroll for a bit. When you see the prompt come back, you're done.

{{< callout type="warning" >}}
If `pip` shows an error, raise your hand.
{{< /callout >}}

### Move the CSV into your project folder

Drag `pokemon.csv` from your Downloads folder into your `python-class` folder. Your code will look for the CSV right next to your Python file.

### Create a new Python file

In VS Code, go to **File → New File** and save it as `pokemon_stats.py` inside `python-class`. Type this in:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")
print(df.head())
```

Run the file (▶ Play button). You should see the first 5 rows of the dataset printed in the terminal.

{{< callout type="info" >}}
`df` is short for **DataFrame** — pandas's word for a data table. Programmers almost always call this variable `df`.
{{< /callout >}}

### Compute mean, median, min, and max

Add these lines to the bottom of your file and run it again:

```python
print("Mean attack:   ", df["attack"].mean())
print("Median attack: ", df["attack"].median())
print("Min attack:    ", df["attack"].min())
print("Max attack:    ", df["attack"].max())
```

Each line picks the `attack` column with `df["attack"]`, then asks pandas for one number.

Mean
: The **average**. Add up all the numbers, then divide by how many there are.

Median
: The **middle** number when the values are sorted from smallest to largest.

### Get all the stats at once

Pandas has a shortcut that prints a full summary in one line:

```python
print(df["attack"].describe())
```

Run it. You'll see `count`, `mean`, `std`, `min`, the quartiles, and `max` — all stacked up.

### Try other columns

Replace `"attack"` with `"hp"`, `"defense"`, or `"speed"`. Run the file each time and notice how the numbers change.

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Work Session 1

- [ ] I installed `pandas` and `matplotlib` without errors.
- [ ] I ran `pokemon_stats.py` and saw the first 5 rows of the dataset printed.
- [ ] I printed the **mean, median, min, and max** for at least two different columns.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session 2: Your First Plots

Numbers in a terminal are useful, but a picture is faster. Let's draw two plots from the same dataset.

{{% steps %}}

### Histogram of attack stats

Add this to the bottom of `pokemon_stats.py`:

```python
df["attack"].hist(bins=20)
plt.title("Attack Stat Distribution")
plt.xlabel("Attack")
plt.ylabel("Number of Pokémon")
plt.show()
```

Run the file. A new window should pop up showing a **histogram** — a bar plot that groups Pokémon by their attack value.

Histogram
: A plot that shows how often values fall into different ranges. Use it to see the **spread** of one number column.

Close the plot window before running the file again, or your computer will fill up with plot windows.

### Bar chart by type

A histogram works for numbers. For categories like `type1` (grass, fire, water, …) we use a **bar chart**. Replace the histogram code with this:

```python
df["type1"].value_counts().plot(kind="bar")
plt.title("Pokémon Count by Primary Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
```

`value_counts()` counts how many Pokémon have each `type1` value, and `.plot(kind="bar")` draws it.

Bar chart
: A plot that compares counts or totals across different **categories**.

### Stretch: scatter plot

If you have time, try this one. It compares two columns at once — every Pokémon becomes one dot:

```python
df.plot.scatter(x="attack", y="defense")
plt.title("Attack vs. Defense")
plt.show()
```

What patterns do you see? Are high-attack Pokémon usually also high-defense?

{{% /steps %}}

{{% checkpoint %}}

### Checkpoint: Work Session 2

- [ ] I made a **histogram** of the `attack` column.
- [ ] I made a **bar chart** of `type1` counts.
- [ ] I changed at least one column name (like `attack` → `speed`) and ran the code again.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

Today you went from staring at a wall of numbers in a spreadsheet to running a few lines of code that summarized **800 Pokémon in milliseconds**. That is the heart of **data analysis**: a small amount of code can answer big questions about a lot of data.

Tomorrow we'll keep working with this same dataset and ask more interesting questions of it.

{{% button text="Soccer Dataset" %}}/downloads/player_info.csv.zip{{% /button %}}

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including **data**, **data collection**, and **data analysis** — students are introduced to all three terms while exploring a real dataset.
- [**MS-CS-FCP.3.3**](/scratch/description/#ms-cs-fcp3) — Analyze the input-process-output-storage model — students load a CSV (input), compute statistics with pandas (process), and print results or display plots (output).
- [**MS-CS-FCP.4.3**](/scratch/description/#ms-cs-fcp4) — Cite evidence on how computers represent data — students see how a `.csv` file represents a structured table of records, and how pandas reads it into a DataFrame.
- [**MS-CS-FCP.4.5**](/scratch/description/#ms-cs-fcp4) — Implement a simple algorithm in a computer program — students write a sequence of pandas calls to load, summarize, and plot a dataset.
