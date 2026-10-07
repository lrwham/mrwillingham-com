---
title: "Pokémon Data"
description: "A two-day Python project: load a real dataset with pandas, compute statistics and draw plots with matplotlib, then design your own Pokémon and test it against the data."
draft: false
toc: true
cascade:
  type: docs
---

Two days of real data analysis in Python. Day 1 answers questions about 800 Pokémon in a few lines of code. Day 2 flips it around: you invent a Pokémon and let the data argue with you about its stats.

Setup, if you have not done it: [Python and VS Code Setup](/scratch/reference/python-setup/). Files: [Datasets and Downloads](/scratch/reference/datasets/).

## Schedule

| Project Day | Plan |
| ----------- | ---- |
| 1 | **Stats and Plots** — explore `pokemon.csv` in a spreadsheet, then mean/median/min/max with pandas and a histogram, bar chart, and scatter plot with matplotlib |
| 2 | **Design Your Own** — use the Pokémon Designer tool to invent a Pokémon, compare it with box plots, scatter plots, and histograms, revise, save as CSV, sketch it |

## Project Day 1: Stats and Plots

### Meet the Dataset

1. Download `pokemon.csv.zip` from [Datasets](/scratch/reference/datasets/), unzip it, and double-click `pokemon.csv`. It opens in Numbers or Excel.
2. Spend five minutes exploring. About how many rows? How many columns? What is your favorite Pokémon's `attack`? Sort `attack` largest to smallest — who is on top? What is the difference between `type1` and `type2`?

### Install the Libraries

In the VS Code terminal, once:

```bash
python3 -m pip install pandas matplotlib
```

`pandas` works with data tables. `matplotlib` draws plots. Drag `pokemon.csv` into your `python-class` folder.

### Basic Statistics

Create `pokemon_stats.py` in `python-class`:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")
print(df.head())
```

Run it. You should see the first five rows. `df` is a **DataFrame**, pandas's word for a table. Then add:

```python
print("Mean attack:   ", df["attack"].mean())
print("Median attack: ", df["attack"].median())
print("Min attack:    ", df["attack"].min())
print("Max attack:    ", df["attack"].max())
print(df["attack"].describe())
```

`df["attack"]` picks one column; `.mean()` asks for one number. `.describe()` prints the whole summary at once. Swap `"attack"` for `"hp"`, `"defense"`, or `"speed"` and run again.

### Plots

A histogram shows the spread of one number column:

```python
df["attack"].hist(bins=20)
plt.title("Attack Stat Distribution")
plt.xlabel("Attack")
plt.ylabel("Number of Pokémon")
plt.show()
```

A bar chart compares categories:

```python
df["type1"].value_counts().plot(kind="bar")
plt.title("Pokémon Count by Primary Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
```

A scatter plot compares two number columns, one dot per Pokémon:

```python
df.plot.scatter(x="attack", y="defense")
plt.title("Attack vs. Defense")
plt.show()
```

Close each plot window before running again. Are high-attack Pokémon usually high-defense too?

## Project Day 2: Design Your Own

### Get the Designer

1. Download `pokemon-designer.zip` from [Datasets](/scratch/reference/datasets/) and unzip it. You get a folder with `designer.py` and `pokemon.csv`.
2. **File → Open Folder…** and open `pokemon-designer`.
3. Optional, for hover tooltips: `python3 -m pip install mplcursors`. The tool runs without it.
4. Run `designer.py`. Type any name and type, reach the menu, and pick **5. Save and quit** to confirm it works.

### Design, Test, Revise

Before typing anything, decide on a **personality** (sneaky, tough, fast, fragile), a **primary type** and maybe a secondary, and a **battle role** — glass cannon, tank, speedster. The stats should match. A tank with `speed = 200` makes no sense.

Run the tool again and enter your real design. Then use the menu:

| Plot | What it shows | Best for |
| ---- | ------------- | -------- |
| Box plot | Where your stat sits in the typical range for your **type** | "Is my attack normal for a fire type?" |
| Scatter plot | Your Pokémon as a star among all 800, on two stats | "Which real Pokémon is most like mine?" |
| Histogram | The distribution of one stat across every Pokémon | "Is my speed unusual anywhere?" |

Try at least one of each. When a stat looks wrong, pick **4. Edit my Pokémon**, fix it, and plot again. Loop until it fits — or until the outlier is on purpose.

### Save and Sketch

Pick **5. Save and quit** with a filename like `your_pokemon_name.csv`. Then, on paper, draw your Pokémon with its name, type(s), six stats, and a one-sentence description ("The Glitch Pokémon").

## Checkpoints

**Day 1**

- [ ] I opened `pokemon.csv` in a spreadsheet and found one interesting fact.
- [ ] `pandas` and `matplotlib` installed without errors.
- [ ] I printed mean, median, min, and max for at least two columns.
- [ ] I made a histogram and a bar chart, and changed at least one column name.

**Day 2**

- [ ] I decided on a personality and role before entering numbers.
- [ ] I tried a box plot, a scatter plot, and a histogram.
- [ ] I revised at least one stat after looking at a plot.
- [ ] I saved my Pokémon as a `.csv` and turned in a sketch.

## Teacher Notes

- The spreadsheet warmup on Day 1 matters: students need to see rows and columns before `df["attack"]` means anything.
- `pip` failures are the main time sink. Have students run the install during the warmup so errors surface early.
- Day 2 collects stats with a form in the original run; a CTLS submission works just as well.
- The soccer dataset on the Datasets page is a ready-made extension for fast finishers.
