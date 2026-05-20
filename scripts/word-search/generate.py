"""Generate the end-of-year word search PDF for the Scratch programming class.

Reads the word list from `word-bank.md`, places each word in a square grid in
one of 8 directions, fills remaining cells with random letters, and renders the
finished puzzle to a letter-sized PDF using matplotlib.

Run from the repo root with:
    .venv/bin/python scripts/word-search/generate.py
Output: static/downloads/end-of-year-word-search.pdf
"""

import random
import re
import string
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle

REPO_ROOT = Path(__file__).resolve().parents[2]
WORD_BANK = REPO_ROOT / "scripts" / "word-search" / "word-bank.md"
OUTPUT_PDF = REPO_ROOT / "static" / "downloads" / "end-of-year-word-search.pdf"

GRID_SIZE = 16
SEED = 20260520  # today's date — keeps the puzzle reproducible across runs

# 8 directions as (dr, dc) deltas
DIRECTIONS = [
    (0, 1),    # E
    (0, -1),   # W
    (1, 0),    # S
    (-1, 0),   # N
    (1, 1),    # SE
    (-1, -1),  # NW
    (1, -1),   # SW
    (-1, 1),   # NE
]


def load_words(path: Path) -> list[str]:
    """Parse the markdown word bank and return the uppercase word list."""
    words: list[str] = []
    in_words = False
    for line in path.read_text().splitlines():
        if line.strip().lower().startswith("## words"):
            in_words = True
            continue
        if in_words and line.strip().startswith("## "):
            break
        if in_words:
            m = re.match(r"^\s*-\s+([A-Za-z]+)\s*$", line)
            if m:
                words.append(m.group(1).upper())
    return words


def try_place(grid: list[list[str]], word: str, r: int, c: int, dr: int, dc: int) -> bool:
    """Place `word` starting at (r,c) heading (dr,dc) if it fits without conflict."""
    n = len(grid)
    end_r = r + dr * (len(word) - 1)
    end_c = c + dc * (len(word) - 1)
    if not (0 <= end_r < n and 0 <= end_c < n):
        return False
    for i, ch in enumerate(word):
        rr, cc = r + dr * i, c + dc * i
        if grid[rr][cc] not in ("", ch):
            return False
    for i, ch in enumerate(word):
        grid[r + dr * i][c + dc * i] = ch
    return True


def place_words(words: list[str], size: int, rng: random.Random) -> tuple[list[list[str]], list[str]]:
    """Place every word in a fresh grid. Returns (grid, placed_words)."""
    grid = [["" for _ in range(size)] for _ in range(size)]
    placed: list[str] = []
    # Place longest words first — they are hardest to fit
    for word in sorted(words, key=len, reverse=True):
        for _ in range(500):
            dr, dc = rng.choice(DIRECTIONS)
            r = rng.randrange(size)
            c = rng.randrange(size)
            if try_place(grid, word, r, c, dr, dc):
                placed.append(word)
                break
        else:
            print(f"WARNING: could not place {word!r} in {size}x{size} grid")
    # Fill remaining empty cells with random letters
    for r in range(size):
        for c in range(size):
            if grid[r][c] == "":
                grid[r][c] = rng.choice(string.ascii_uppercase)
    return grid, placed


def render_pdf(grid: list[list[str]], words: list[str], out_path: Path) -> None:
    """Render the puzzle (grid + word bank) to a letter-sized PDF."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    size = len(grid)

    with PdfPages(out_path) as pdf:
        fig = plt.figure(figsize=(8.5, 11))

        # Header
        fig.text(0.5, 0.95, "End-of-Year Word Search",
                 ha="center", va="top", fontsize=22, fontweight="bold")
        fig.text(0.5, 0.915, "Computer Programming with Scratch  —  Mr. Willingham",
                 ha="center", va="top", fontsize=12, style="italic")
        fig.text(0.08, 0.875, "Name: ______________________________",
                 ha="left", va="top", fontsize=11)
        fig.text(0.62, 0.875, "Partner: ____________________________",
                 ha="left", va="top", fontsize=11)
        fig.text(0.08, 0.85,
                 "Find every word from the bank below. Words go forward, backward, up, down, and diagonally.",
                 ha="left", va="top", fontsize=10)

        # Grid
        grid_ax = fig.add_axes((0.1, 0.32, 0.8, 0.5))
        grid_ax.set_xlim(0, size)
        grid_ax.set_ylim(0, size)
        grid_ax.set_aspect("equal")
        grid_ax.set_xticks([])
        grid_ax.set_yticks([])
        for spine in grid_ax.spines.values():
            spine.set_visible(False)

        for r in range(size):
            for c in range(size):
                # Flip y so row 0 is at the top
                y = size - 1 - r
                grid_ax.add_patch(Rectangle((c, y), 1, 1, fill=False,
                                            edgecolor="black", linewidth=0.5))
                grid_ax.text(c + 0.5, y + 0.5, grid[r][c],
                             ha="center", va="center",
                             fontsize=14, family="monospace")

        # Word bank
        fig.text(0.5, 0.28, "Word Bank",
                 ha="center", va="top", fontsize=14, fontweight="bold")

        sorted_words = sorted(words)
        cols = 3
        rows = (len(sorted_words) + cols - 1) // cols
        col_x = [0.15, 0.45, 0.75]
        for i, word in enumerate(sorted_words):
            col = i // rows
            row = i % rows
            y = 0.25 - row * 0.022
            fig.text(col_x[col], y, f"☐  {word}",
                     ha="left", va="top", fontsize=11, family="monospace")

        fig.text(0.5, 0.04,
                 "Work with your partner. When you find every word, raise your hand for a treat!",
                 ha="center", va="bottom", fontsize=10, style="italic")

        pdf.savefig(fig)
        plt.close(fig)


def main() -> None:
    rng = random.Random(SEED)
    words = load_words(WORD_BANK)
    if not words:
        raise SystemExit(f"No words found in {WORD_BANK}")
    grid, placed = place_words(words, GRID_SIZE, rng)
    render_pdf(grid, placed, OUTPUT_PDF)
    print(f"Placed {len(placed)}/{len(words)} words in a {GRID_SIZE}x{GRID_SIZE} grid")
    print(f"Wrote {OUTPUT_PDF.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
