"""Generate the end-of-year crossword PDF for the Scratch programming class.

Reads words and clues from `word-bank.md`, builds a NYT-style interlocking
crossword by placing each word at the best valid intersection with an
already-placed word, then renders a printable PDF with a numbered grid and
Across/Down clue lists. An answer key page is appended for the teacher.

Run from the repo root with:
    .venv/bin/python scripts/crossword/generate.py
Output: static/downloads/end-of-year-crossword.pdf
"""

import random
import re
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle

REPO_ROOT = Path(__file__).resolve().parents[2]
WORD_BANK = REPO_ROOT / "scripts" / "crossword" / "word-bank.md"
DOWNLOADS_DIR = REPO_ROOT / "static" / "downloads"

GRID_SIZE = 15
SEED = 20260520


def load_periods(path: Path) -> dict[int, list[tuple[str, str]]]:
    """Parse `## Period N — Words and Clues` sections into {period: [(word, clue), ...]}.
    Order in the returned dict matches markdown order."""
    periods: dict[int, list[tuple[str, str]]] = {}
    current: int | None = None
    header_re = re.compile(r"^##\s+Period\s+(\d+)\s*[—\-]", re.IGNORECASE)
    row_re = re.compile(r"^\s*\|\s*([A-Za-z]+)\s*\|\s*(.+?)\s*\|\s*$")
    for line in path.read_text().splitlines():
        h = header_re.match(line)
        if h:
            current = int(h.group(1))
            periods.setdefault(current, [])
            continue
        if current is None:
            continue
        m = row_re.match(line)
        if not m:
            continue
        word = m.group(1).upper()
        clue = m.group(2).strip()
        if word == "WORD" or set(word) <= set("-"):
            continue
        periods[current].append((word, clue))
    return periods


def output_path_for(period: int) -> Path:
    """Period 1 keeps the original filename so previously-printed links still
    resolve. Periods 2+ get a `-p<N>` suffix."""
    if period == 1:
        return DOWNLOADS_DIR / "end-of-year-crossword.pdf"
    return DOWNLOADS_DIR / f"end-of-year-crossword-p{period}.pdf"


class Crossword:
    """Builds an interlocking crossword by trying every intersection
    against every already-placed word and picking the highest-scoring
    valid placement."""

    def __init__(self, size: int):
        self.size = size
        self.grid: list[list[str | None]] = [[None] * size for _ in range(size)]
        # placed: (word, clue, row, col, direction) where direction is 'A' or 'D'
        self.placed: list[tuple[str, str, int, int, str]] = []

    def _in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.size and 0 <= c < self.size

    def _score(self, word: str, r: int, c: int, direction: str) -> int | None:
        """Return intersection count if placement is valid, None otherwise."""
        n = len(word)
        if direction == "A":
            if not (self._in_bounds(r, c) and self._in_bounds(r, c + n - 1)):
                return None
            if c > 0 and self.grid[r][c - 1] is not None:
                return None
            if c + n < self.size and self.grid[r][c + n] is not None:
                return None
        else:
            if not (self._in_bounds(r, c) and self._in_bounds(r + n - 1, c)):
                return None
            if r > 0 and self.grid[r - 1][c] is not None:
                return None
            if r + n < self.size and self.grid[r + n][c] is not None:
                return None

        intersections = 0
        for i, ch in enumerate(word):
            rr, cc = (r, c + i) if direction == "A" else (r + i, c)
            existing = self.grid[rr][cc]
            if existing is not None:
                if existing != ch:
                    return None
                intersections += 1
            else:
                # Empty cell — no perpendicular neighbor may already be a letter
                # (would create a stray two-letter "word" we never intended).
                if direction == "A":
                    if rr > 0 and self.grid[rr - 1][cc] is not None:
                        return None
                    if rr < self.size - 1 and self.grid[rr + 1][cc] is not None:
                        return None
                else:
                    if cc > 0 and self.grid[rr][cc - 1] is not None:
                        return None
                    if cc < self.size - 1 and self.grid[rr][cc + 1] is not None:
                        return None
        return intersections

    def _commit(self, word: str, clue: str, r: int, c: int, direction: str) -> None:
        for i, ch in enumerate(word):
            if direction == "A":
                self.grid[r][c + i] = ch
            else:
                self.grid[r + i][c] = ch
        self.placed.append((word, clue, r, c, direction))

    def place_first(self, word: str, clue: str) -> None:
        r = self.size // 2
        c = (self.size - len(word)) // 2
        self._commit(word, clue, r, c, "A")

    def try_place(self, word: str, clue: str) -> bool:
        best: tuple[int, int, str] | None = None
        best_score = 0
        for pword, _pclue, pr, pc, pdir in self.placed:
            for pi, pch in enumerate(pword):
                for wi, wch in enumerate(word):
                    if pch != wch:
                        continue
                    if pdir == "A":
                        new_r, new_c, new_d = pr - wi, pc + pi, "D"
                    else:
                        new_r, new_c, new_d = pr + pi, pc - wi, "A"
                    score = self._score(word, new_r, new_c, new_d)
                    if score is None or score == 0:
                        continue
                    if score > best_score:
                        best_score = score
                        best = (new_r, new_c, new_d)
        if best is None:
            return False
        self._commit(word, clue, *best)
        return True

    def number_grid(self) -> tuple[dict[tuple[int, int], int],
                                   list[tuple[int, str, str, str]]]:
        """Number cells that begin an across or down word.

        Returns:
            numbers: {(r, c) -> number} for every cell that gets a number.
            clues: list of (number, direction, word, clue) sorted by number/dir.
        """
        starts_by_pos: dict[tuple[int, int, str], tuple[str, str]] = {
            (r, c, d): (w, cl) for w, cl, r, c, d in self.placed
        }
        numbers: dict[tuple[int, int], int] = {}
        clues: list[tuple[int, str, str, str]] = []
        n = 0
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    continue
                starts_a = (
                    (c == 0 or self.grid[r][c - 1] is None)
                    and c + 1 < self.size
                    and self.grid[r][c + 1] is not None
                )
                starts_d = (
                    (r == 0 or self.grid[r - 1][c] is None)
                    and r + 1 < self.size
                    and self.grid[r + 1][c] is not None
                )
                if starts_a or starts_d:
                    n += 1
                    numbers[(r, c)] = n
                    if starts_a and (r, c, "A") in starts_by_pos:
                        w, cl = starts_by_pos[(r, c, "A")]
                        clues.append((n, "A", w, cl))
                    if starts_d and (r, c, "D") in starts_by_pos:
                        w, cl = starts_by_pos[(r, c, "D")]
                        clues.append((n, "D", w, cl))
        return numbers, clues

    def bounding_box(self) -> tuple[int, int, int, int]:
        """Return (min_r, max_r, min_c, max_c) over filled cells."""
        rs = [r for r in range(self.size) for c in range(self.size) if self.grid[r][c] is not None]
        cs = [c for r in range(self.size) for c in range(self.size) if self.grid[r][c] is not None]
        return min(rs), max(rs), min(cs), max(cs)


def build(entries: list[tuple[str, str]], size: int, seed: int) -> Crossword:
    rng = random.Random(seed)
    # Bias toward longer words first (they are hardest to fit) but jitter so
    # different seeds explore different layouts.
    ordered = sorted(entries, key=lambda e: (-len(e[0]) + rng.random() * 2, rng.random()))
    cw = Crossword(size)
    cw.place_first(*ordered[0])
    for word, clue in ordered[1:]:
        cw.try_place(word, clue)
    return cw


def build_best(entries: list[tuple[str, str]], size: int,
               base_seed: int, attempts: int) -> Crossword:
    """Try `attempts` different layouts and return the one that placed the
    most words. Ties broken by tighter bounding box (denser puzzle)."""
    best: Crossword | None = None
    best_key = (-1, 0)
    for i in range(attempts):
        cw = build(entries, size, base_seed + i)
        min_r, max_r, min_c, max_c = cw.bounding_box()
        density = -(max_r - min_r) * (max_c - min_c)  # smaller box = better
        key = (len(cw.placed), density)
        if key > best_key:
            best_key = key
            best = cw
    assert best is not None
    return best


def draw_grid(ax, cw: Crossword, numbers: dict[tuple[int, int], int], show_letters: bool) -> None:
    """Draw the crossword grid into a matplotlib axis."""
    min_r, max_r, min_c, max_c = cw.bounding_box()
    # Pad the bounding box by one cell on every side so the surrounding black
    # squares are visible at the edge of the printed grid.
    min_r = max(0, min_r - 1)
    max_r = min(cw.size - 1, max_r + 1)
    min_c = max(0, min_c - 1)
    max_c = min(cw.size - 1, max_c + 1)

    width = max_c - min_c + 1
    height = max_r - min_r + 1
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            x = c - min_c
            y = height - 1 - (r - min_r)
            letter = cw.grid[r][c]
            if letter is None:
                ax.add_patch(Rectangle((x, y), 1, 1, facecolor="#cccccc",
                                       edgecolor="black", linewidth=0.6))
            else:
                ax.add_patch(Rectangle((x, y), 1, 1, facecolor="white",
                                       edgecolor="black", linewidth=0.6))
                num = numbers.get((r, c))
                if num is not None:
                    ax.text(x + 0.06, y + 0.94, str(num),
                            ha="left", va="top", fontsize=6.5)
                if show_letters:
                    ax.text(x + 0.5, y + 0.42, letter,
                            ha="center", va="center",
                            fontsize=13, family="monospace")


def draw_clues(fig, clues: list[tuple[int, str, str, str]],
               left_x: float, top_y: float, col_gap: float, line_h: float,
               wrap_chars: int = 48) -> None:
    """Render Across and Down clue columns starting at (left_x, top_y).
    Long clues wrap onto a second line with a hanging indent so the number
    column stays aligned."""
    across = [(n, w, cl) for n, d, w, cl in clues if d == "A"]
    down = [(n, w, cl) for n, d, w, cl in clues if d == "D"]
    across.sort()
    down.sort()

    def render_block(title: str, items: list[tuple[int, str, str]], x: float) -> None:
        fig.text(x, top_y, title, ha="left", va="top",
                 fontsize=12, fontweight="bold")
        y = top_y - line_h * 1.6
        for num, _w, clue in items:
            first = f"{num:>2}.  {clue}"
            lines = textwrap.wrap(first, width=wrap_chars,
                                  subsequent_indent="      ")
            for line in lines:
                fig.text(x, y, line, ha="left", va="top",
                         fontsize=9, family="DejaVu Sans")
                y -= line_h
            y -= line_h * 0.15  # small gap between clues

    render_block("Across", across, left_x)
    render_block("Down", down, left_x + col_gap)


def render_pdf(cw: Crossword, numbers: dict[tuple[int, int], int],
               clues: list[tuple[int, str, str, str]], out_path: Path,
               period: int) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    title_suffix = "" if period == 1 else f" — Period {period}"
    with PdfPages(out_path) as pdf:
        # ── Page 1: puzzle ────────────────────────────────────────────────
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.5, 0.96, "End-of-Year Crossword" + title_suffix,
                 ha="center", va="top", fontsize=22, fontweight="bold")
        fig.text(0.5, 0.925, "Computer Programming with Scratch  —  Mr. Willingham",
                 ha="center", va="top", fontsize=12, style="italic")
        fig.text(0.08, 0.89, "Name: ______________________________",
                 ha="left", va="top", fontsize=11)
        fig.text(0.08, 0.865,
                 "Solo activity. The first three students to fill in every square correctly get a treat.",
                 ha="left", va="top", fontsize=10)

        grid_ax = fig.add_axes((0.15, 0.45, 0.7, 0.40))
        draw_grid(grid_ax, cw, numbers, show_letters=False)

        draw_clues(fig, clues,
                   left_x=0.06, top_y=0.40,
                   col_gap=0.48, line_h=0.020)

        pdf.savefig(fig)
        plt.close(fig)

        # ── Page 2: answer key ────────────────────────────────────────────
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.5, 0.96, "End-of-Year Crossword" + title_suffix + " — Answer Key",
                 ha="center", va="top", fontsize=18, fontweight="bold")
        fig.text(0.5, 0.93, "Teacher copy. Do not distribute.",
                 ha="center", va="top", fontsize=10, style="italic")
        grid_ax = fig.add_axes((0.1, 0.20, 0.8, 0.68))
        draw_grid(grid_ax, cw, numbers, show_letters=True)
        pdf.savefig(fig)
        plt.close(fig)


def main() -> None:
    periods = load_periods(WORD_BANK)
    if not periods:
        raise SystemExit(f"No `## Period N — Words and Clues` sections found in {WORD_BANK}")
    for period, entries in periods.items():
        if not entries:
            print(f"Period {period}: no entries — skipping")
            continue
        # Period 1 keeps the original seed so previously-printed worksheets
        # are reproducible; later periods get a deterministic offset.
        period_seed = SEED + (period - 1) * 1000
        cw = build_best(entries, GRID_SIZE, period_seed, attempts=2000)
        numbers, clues = cw.number_grid()
        out_path = output_path_for(period)
        render_pdf(cw, numbers, clues, out_path, period)
        placed_words = {w for w, *_ in cw.placed}
        missing = [w for w, _ in entries if w not in placed_words]
        print(f"Period {period}: placed {len(placed_words)}/{len(entries)} words "
              f"in a {GRID_SIZE}x{GRID_SIZE} grid")
        if missing:
            print(f"  Not placed: {', '.join(missing)}")
        print(f"  Wrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
