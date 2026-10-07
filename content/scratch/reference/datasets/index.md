---
title: "Datasets and Downloads"
description: "The data files and tools used in the Python data lessons."
weight: 10
toc: true
---

Download, unzip, and drag the file into your `python-class` folder before running any code that reads it. See [Python and VS Code Setup](/scratch/reference/python-setup/) if you do not have that folder yet.

## Pokémon

{{< button text="Download pokemon.csv.zip" >}}pokemon.csv.zip{{< /button >}}

About 800 Pokémon, one per row. Columns include `name`, `type1`, `type2`, `hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`, `height_m`, `weight_kg`, and `generation`. Used in the [Pokémon Data](/scratch/projects/python-pokemon-data/) project.

```python
import pandas as pd
df = pd.read_csv("pokemon.csv")
print(df.head())
```

## Pokémon Designer

{{< button text="Download pokemon-designer.zip" >}}pokemon-designer.zip{{< /button >}}

A folder with two files: `designer.py`, a menu-driven tool that lets you invent a Pokémon and plot it against the dataset, and its own copy of `pokemon.csv`. Open the whole folder in VS Code and run `designer.py`. Optional hover tooltips need one more library:

```bash
python3 -m pip install mplcursors
```

## Soccer Players

{{< button text="Download players_info.csv.zip" >}}players_info.csv.zip{{< /button >}}

A second dataset for anyone who wants to try the same pandas and matplotlib code on something other than Pokémon. Open it in Numbers or Excel first to see which columns are numbers.

## Working With a CSV

A `.csv` (comma-separated values) file is plain text: one record per line, columns separated by commas. Spreadsheet apps open it directly, and pandas reads it into a **DataFrame** with `pd.read_csv()`. Keep the file next to your `.py` script so Python can find it.
