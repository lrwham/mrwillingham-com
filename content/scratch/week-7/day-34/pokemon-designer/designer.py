"""Pokemon Designer - Day 34

Run this from the same folder as pokemon.csv:

    python3 designer.py

It will ask you to design a Pokemon, then let you compare it
to the real dataset using box plots, scatter plots, and histograms.
You can revise stats and re-plot as many times as you want.
When you're happy, save your Pokemon as a CSV.

Required libraries:

    pip install pandas matplotlib mplcursors
"""
import csv
import random
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

try:
    import mplcursors
    HOVER = True
except ImportError:
    HOVER = False


HERE = Path(__file__).parent
DATA = HERE / "pokemon.csv"

if not DATA.exists():
    sys.exit(
        "Cannot find pokemon.csv in the same folder as designer.py.\n"
        "Make sure both files are in pokemon-designer/."
    )

df = pd.read_csv(DATA)

STATS = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]
SIZE = ["height_m", "weight_kg"]
TYPES = sorted(df["type1"].dropna().unique().tolist())


# ------------------- input helpers -------------------

def ask(message, cast=str, default=None):
    suffix = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{message}{suffix}: ").strip()
        if raw == "" and default is not None:
            return default
        try:
            return cast(raw)
        except ValueError:
            print(f"  That isn't a valid {cast.__name__}. Try again.")


def menu(options, message="Choice"):
    """options: list of (label, value). Returns chosen value, or None on 0."""
    for i, (label, _) in enumerate(options, 1):
        print(f"  {i:2}. {label}")
    print("   0. cancel / back")
    while True:
        choice = ask(message, int)
        if choice == 0:
            return None
        if 1 <= choice <= len(options):
            return options[choice - 1][1]
        print(f"  Pick a number 0-{len(options)}.")


def pick_type(message, allow_none=False):
    """Show the 18 types in a numbered list and return the chosen one.
    If allow_none, the first option is '(no second type)' and returns None.
    """
    options = []
    if allow_none:
        options.append(("(no second type)", None))
    options += [(t, t) for t in TYPES]
    while True:
        for i, (label, _) in enumerate(options, 1):
            print(f"  {i:2}. {label}")
        try:
            choice = int(input(f"{message}: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1][1]
        except ValueError:
            pass
        print(f"  Pick 1-{len(options)}.")


def pick_stat(message, include_size=True):
    cols = STATS + SIZE if include_size else STATS
    return menu([(s, s) for s in cols], message)


# ------------------- design + display -------------------

def show_type_summary(type1):
    same = df[df["type1"] == type1]
    print(f"\nThere are {len(same)} real {type1}-type Pokemon. Typical stats:")
    summary = same[STATS].agg(["mean", "min", "max"]).round(0).astype(int)
    print(summary.to_string())


def design():
    print("\n=== Design Your Pokemon ===\n")
    name = ask("Pokemon name", str)

    print("\nPick a primary type:")
    type1 = pick_type("Type")
    show_type_summary(type1)

    print("\nPick a secondary type (or 1 for none):")
    type2 = pick_type("Type", allow_none=True)

    print("\nNow enter the six battle stats. Most Pokemon are between 20 and 200.")
    poke = {"name": name, "type1": type1, "type2": type2}
    for s in STATS:
        poke[s] = ask(f"  {s}", int, default=70)

    print("\nFinally, size:")
    poke["height_m"] = ask("  height_m (meters)", float, default=1.0)
    poke["weight_kg"] = ask("  weight_kg (kilograms)", float, default=20.0)
    return poke


def show(poke):
    type_label = poke["type1"]
    if poke.get("type2"):
        type_label += f"/{poke['type2']}"
    print(f"\n  {poke['name']} ({type_label})")
    for k in STATS:
        print(f"    {k:11} {poke[k]}")
    for k in SIZE:
        print(f"    {k:11} {poke[k]}")
    print(f"    {'base_total':11} {sum(poke[s] for s in STATS)}")


# ------------------- plots -------------------

AUTO_CLOSE_SECONDS = 10


def show_plot(fig):
    """Display the figure, but auto-close it after AUTO_CLOSE_SECONDS.
    Closing the window yourself still works normally - we stop the
    timer on manual close so it doesn't fire against a dead canvas
    (which can freeze the next plot on some backends).
    """
    timer = fig.canvas.new_timer(interval=AUTO_CLOSE_SECONDS * 1000)

    def auto_close():
        # single-shot: stop ourselves before closing
        timer.stop()
        if plt.fignum_exists(fig.number):
            plt.close(fig)

    def on_manual_close(_event):
        # user closed the window - kill the pending timer
        timer.stop()

    timer.add_callback(auto_close)
    fig.canvas.mpl_connect("close_event", on_manual_close)
    timer.start()

    print(f"  (window will auto-close after {AUTO_CLOSE_SECONDS} seconds)")
    plt.show()


def plot_box(poke, stat=None):
    if stat is None:
        print("\nBox plot - which stat?")
        options = [(s, s) for s in STATS] + [
            ("ALL six stats at once", "ALL"),
            ("Choose for Me (random)", "RANDOM"),
        ]
        stat = menu(options, "Stat")
        if stat is None:
            return
        if stat == "RANDOM":
            stat = random.choice(STATS + ["ALL"])
            print(f"  Picked for you: {stat}")

    same = df[df["type1"] == poke["type1"]]
    fig, ax = plt.subplots()

    if stat == "ALL":
        same[STATS].boxplot(ax=ax)
        ax.scatter(range(1, len(STATS) + 1), [poke[s] for s in STATS],
                   color="red", marker="*", s=250, zorder=10,
                   label=poke["name"])
        ax.set_title(f"{poke['name']} vs all {poke['type1']}-type Pokemon")
    else:
        same[[stat]].boxplot(ax=ax)
        ax.scatter([1], [poke[stat]],
                   color="red", marker="*", s=300, zorder=10,
                   label=poke["name"])
        ax.set_title(f"{poke['name']}'s {stat} vs all {poke['type1']}-type Pokemon")

    ax.set_ylabel("value")
    ax.legend()
    show_plot(fig)


def plot_scatter(poke, x=None, y=None):
    if x is None or y is None:
        print("\nScatter plot - pick the X-axis stat (or 0 to let me choose both):")
        options = [(s, s) for s in STATS + SIZE] + [("Choose for Me (random)", "RANDOM")]
        x = menu(options, "X")
        if x is None:
            return
        if x == "RANDOM":
            pool = STATS + SIZE
            x, y = random.sample(pool, 2)
            print(f"  Picked for you: {x} vs {y}")
        else:
            print("\nNow pick the Y-axis stat:")
            y = pick_stat("Y")
            if y is None:
                return

    fig, ax = plt.subplots()
    dots = ax.scatter(df[x], df[y], alpha=0.4)
    ax.scatter(poke[x], poke[y],
               color="red", marker="*", s=300, zorder=10,
               label=poke["name"])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{x} vs {y} - every Pokemon, plus yours")
    ax.legend()

    if HOVER:
        cur = mplcursors.cursor(dots, hover=True)
        cur.connect(
            "add",
            lambda sel: sel.annotation.set_text(df["name"].iloc[sel.index]),
        )
    else:
        print("  (Install `mplcursors` to get hover tooltips here.)")

    show_plot(fig)


def plot_hist(poke, stat=None):
    if stat is None:
        print("\nHistogram - which stat?")
        options = [(s, s) for s in STATS + SIZE] + [("Choose for Me (random)", "RANDOM")]
        stat = menu(options, "Stat")
        if stat is None:
            return
        if stat == "RANDOM":
            stat = random.choice(STATS + SIZE)
            print(f"  Picked for you: {stat}")

    fig, ax = plt.subplots()
    df[stat].hist(bins=20, ax=ax)
    ax.axvline(poke[stat], color="red", linewidth=3,
               label=f"{poke['name']}: {poke[stat]}")
    ax.set_xlabel(stat)
    ax.set_ylabel("number of Pokemon")
    ax.set_title(f"{stat} across all Pokemon")
    ax.legend()
    show_plot(fig)


# ------------------- recommended plots -------------------

# Each entry is (human-readable label, plot function, kwargs).
# These are the "greatest hits" - plots that usually tell a
# story about the Pokemon you just designed.
RECOMMENDED_PLOTS = [
    ("Scatter: attack vs defense",       plot_scatter, {"x": "attack",    "y": "defense"}),
    ("Scatter: defense vs speed",        plot_scatter, {"x": "defense",   "y": "speed"}),
    ("Scatter: sp_attack vs sp_defense", plot_scatter, {"x": "sp_attack", "y": "sp_defense"}),
    ("Scatter: hp vs attack",            plot_scatter, {"x": "hp",        "y": "attack"}),
    ("Scatter: speed vs attack",         plot_scatter, {"x": "speed",     "y": "attack"}),
    ("Scatter: height_m vs weight_kg",   plot_scatter, {"x": "height_m",  "y": "weight_kg"}),
    ("Box plot: hp",                     plot_box,     {"stat": "hp"}),
    ("Box plot: attack",                 plot_box,     {"stat": "attack"}),
    ("Box plot: defense",                plot_box,     {"stat": "defense"}),
    ("Box plot: speed",                  plot_box,     {"stat": "speed"}),
    ("Box plot: ALL six stats",          plot_box,     {"stat": "ALL"}),
    ("Histogram: hp",                    plot_hist,    {"stat": "hp"}),
    ("Histogram: attack",                plot_hist,    {"stat": "attack"}),
    ("Histogram: speed",                 plot_hist,    {"stat": "speed"}),
]


def plot_surprise(poke):
    label, func, kwargs = random.choice(RECOMMENDED_PLOTS)
    print(f"\nChoose for Me picked:  {label}")
    func(poke, **kwargs)


# ------------------- editing + saving -------------------

def edit(poke):
    items = [
        (f"name (current: {poke['name']})", "name"),
        (f"type1 (current: {poke['type1']})", "type1"),
        (f"type2 (current: {poke.get('type2') or '-'})", "type2"),
    ]
    for k in STATS + SIZE:
        items.append((f"{k} (current: {poke[k]})", k))
    field = menu(items, "Edit which?")
    if field is None:
        return
    if field == "name":
        poke["name"] = ask("New name", str, default=poke["name"])
    elif field == "type1":
        print("\nNew primary type:")
        poke["type1"] = pick_type("Type")
    elif field == "type2":
        print("\nNew secondary type (or 1 for none):")
        poke["type2"] = pick_type("Type", allow_none=True)
    else:
        cast = float if field in SIZE else int
        poke[field] = ask(f"New {field}", cast, default=poke[field])


def save(poke):
    default = poke["name"].lower().replace(" ", "_") + ".csv"
    name = ask("Save as", str, default=default)
    if not name.endswith(".csv"):
        name += ".csv"
    out = HERE / name
    poke["base_total"] = sum(poke[s] for s in STATS)
    cols = ["name", "type1", "type2"] + STATS + ["base_total"] + SIZE
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerow(poke)
    print(f"\nSaved to: {out}")


# ------------------- main loop -------------------

def main():
    print("=" * 44)
    print("    POKEMON DESIGNER  -  Day 34")
    print("=" * 44)
    if not HOVER:
        print("Tip: `pip install mplcursors` for hover tooltips on scatter plots.\n")

    poke = design()
    show(poke)

    while True:
        print("\n--- Main Menu ---")
        action = menu([
            ("Box plot (stat vs same-type Pokemon)", "BOX"),
            ("Scatter plot (two stats vs every Pokemon)", "SCATTER"),
            ("Histogram (one stat across all Pokemon)", "HIST"),
            ("Choose for Me (random recommended plot)", "SURPRISE"),
            ("Edit my Pokemon", "EDIT"),
            ("Show my Pokemon's stats", "SHOW"),
            ("Save and quit", "SAVE"),
        ], "Choice")

        if action is None:
            confirm = ask("Quit without saving? (y/n)", str, default="n")
            if confirm.lower().startswith("y"):
                return
            continue

        if action == "BOX":
            plot_box(poke)
        elif action == "SCATTER":
            plot_scatter(poke)
        elif action == "HIST":
            plot_hist(poke)
        elif action == "SURPRISE":
            plot_surprise(poke)
        elif action == "EDIT":
            edit(poke)
            show(poke)
        elif action == "SHOW":
            show(poke)
        elif action == "SAVE":
            save(poke)
            return


if __name__ == "__main__":
    main()
