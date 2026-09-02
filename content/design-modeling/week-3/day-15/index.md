---
title: "Day 15: Skimmer Statistics and Your First Box Plot"
date: 2026-08-21T06:00:00-04:00
description: "Enter the class launch data into Excel, calculate ten statistics by formula, and hand-draw a box and whiskers plot."
day_number: 15
units:
  - "Introduction to Design"
standards:
  - MS-ENGR-II-4.5
  - MS-ENGR-II-5.4
tags:
  - Statistics
  - Box Plot
  - Excel
  - Data Analysis
resources:
  - "Engineering Notebook"
  - "Excel"
  - "Graph Paper"
draft: false
toc: true
weight: 5
---

{{< icon "calendar" >}} **Friday, August 21st, 2026**

{{% objectives %}}

## Objectives

- I can enter a real dataset into a spreadsheet accurately.
- I can use spreadsheet formulas to find mean, median, mode, minimum, maximum, range, Q1, and Q3.
- I can hand-draw a box and whiskers plot from a five-number summary.
- I can use center and spread to describe what our class's launches actually looked like.

{{% /objectives %}}

{{% warmup %}}

## Warmup: Get the Data into the Spreadsheet

Wednesday every one of you launched three times, and a Lane Captain wrote every distance down by hand. Thursday you learned the vocabulary. Today those two things come together: you take the entire class's handwritten data, put it into a spreadsheet, and turn all those scattered numbers into one picture that fits on a sheet of graph paper.

The handwritten lane record sheets are passed out. Open **Excel** and build the table exactly like this:

| | A | B | C |
| --- | --- | --- | --- |
| 1 | Trial1 | Trial2 | Trial3 |
| 2 | 15.5 | 18.5 | 20.5 |
| 3 | 4.0 | 7.0 | 3.5 |
| … | one row per student, straight down, until every name from every lane is in | | |

Row 1 is your header row. One student per row. Go lane by lane, in order, so you keep your place on the record sheet.

{{< callout type="important" >}}
**Units matter.** Everything is in **feet**, estimated to the nearest half foot. Type one decimal on every number — 12.0, not 12. Only .0 and .5 endings exist. If you type a number ending in .3 or .7, you misread the sheet — look again.
{{< /callout >}}

{{< callout type="tip" >}}
Type a number, press **Tab** to move right, and press **Enter** at the end of a row — the cursor jumps back to column A on the next row automatically. Do not touch the mouse. You will be twice as fast.
{{< /callout >}}

When you are done, click any cell in your data and check the count at the bottom right of the window. You should have one row for every student in this period. Short a row? You skipped somebody.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] The whole class dataset is in my spreadsheet — one row per student, all three trials.
- [ ] Every number is in feet with one decimal, ending in .0 or .5.
- [ ] My row count matches the number of students in this period.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Calculate the Statistics

Leave a blank row under your data, then build a small results table off to the side — labels in column E, formulas in column F.

Every formula points at the same range: all three trial columns, every row of data. If your data runs from row 2 to row 29, the range is `A2:C29`. Adjust the last row number to match your sheet.

| Statistic | Formula | What it tells you |
| --- | --- | --- |
| Count (n) | `=COUNT(A2:C29)` | How many launches you are describing. It should be 3 × the number of students. |
| Mean | `=AVERAGE(A2:C29)` | Center. Add every launch, divide by n. |
| Median | `=MEDIAN(A2:C29)` | Center. Line every launch up shortest to longest — this is the one in the middle. |
| Mode | `=MODE(A2:C29)` | The distance that shows up most often. Watch this one — we talk about what it does with a tie. |
| Minimum | `=MIN(A2:C29)` | Spread. The shortest launch anybody had. |
| Maximum | `=MAX(A2:C29)` | Spread. The longest launch anybody had. |
| Range | `=MAX(A2:C29)-MIN(A2:C29)` | Spread. Max minus min. Built from exactly two launches. |
| Q1 | `=QUARTILE(A2:C29,1)` | Quarter mark. 25% of launches were shorter than this. |
| Q3 | `=QUARTILE(A2:C29,3)` | Three-quarter mark. 75% of launches were shorter than this. |
| IQR | `=QUARTILE(A2:C29,3)-QUARTILE(A2:C29,1)` | Spread. How wide the middle half of the class is. This is the box in your box plot. |

Copy every value into your notebook, rounded to the tenth. You need five of them — min, Q1, median, Q3, max — in the next part, and your device goes away before then.

{{< callout type="warning" >}}
If a formula returns an error or something wild: you almost certainly typed a number as text, or your range is wrong. Numbers sit on the **right** side of their cells. Anything hugging the left side is text — retype it.
{{< /callout >}}

{{% checkpoint %}}

### Checkpoint: Statistics

- [ ] All ten statistics are calculated with formulas, not typed in by hand.
- [ ] My count is 3 × the number of students.
- [ ] All ten values are copied into my notebook, rounded to the tenth.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session: Draw the Box Plot by Hand

Devices closed. Graph paper, pencil, ruler. Excel can draw this for you in four clicks and you would learn nothing — later we will let it, and you will already know whether its answer is right.

The five numbers you need are the **five-number summary**: minimum, Q1, median, Q3, maximum.

1. **Draw the number line.** Use the long edge of the paper. Let 1 square = 1 foot, and run it from 0 to 35. Label every 5 feet. Title the axis **Distance (feet)**.
2. **Mark your five numbers** as small ticks above the line: min, Q1, median, Q3, max. A half-foot value lands on a half square.
3. **Build the box.** Draw a rectangle from Q1 to Q3, about 8 squares tall. This box holds the middle half of every launch this class made.
4. **Draw the median line** straight down through the box at the median. It will not be in the middle of the box, and that is information, not a mistake.
5. **Draw the whiskers.** One horizontal line from the left edge of the box out to the min, one from the right edge out to the max. Cap each with a short vertical tick.
6. **Label everything.** Write the actual number under each of the five marks, and title the whole plot: **Skimmer Launch Distances — Period ___, n = ___.**

{{< callout type="important" >}}
Reality check before you glue it in: your five numbers must go in order left to right — min ≤ Q1 ≤ median ≤ Q3 ≤ max. If your median sits outside the box, or a whisker points the wrong way, you swapped two numbers.
{{< /callout >}}

Cut the plot out and glue or tape it into your Engineering Notebook under today's date, with your statistics written beside it. This page gets checked.

### Key Vocabulary

Five-Number Summary
: Minimum, Q1, median, Q3, maximum — the five numbers a box plot is built from.

Box and Whiskers Plot
: A picture of the five-number summary: a box from Q1 to Q3 with a line at the median, and whiskers out to the minimum and maximum.

Interquartile Range (IQR)
: Q3 minus Q1 — the width of the box, and the width of the middle 50% of the data.

{{% checkpoint %}}

### Checkpoint: Box Plot

- [ ] My hand-drawn box plot is labeled, titled, and glued into my notebook.
- [ ] My five numbers go in order — min, Q1, median, Q3, max.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: What Is This Picture Telling Us?

Everybody's plot should look the same, because everybody used the same data. Now we argue about what it means. Be ready to answer out loud:

- **Range vs. IQR.** The range is built from exactly two launches. The IQR is built from the middle half. Which one honestly describes a typical launch in this room?
- **Mean vs. median.** Suppose a student launched 2.0, 24.0, and 25.0 feet. Their mean is 17.0. Their median is 24.0. Which number is the honest description of that student — and what happened on trial 1?
- **Mode.** What did Excel hand back? What did it do about a tie? Is mode a useful statistic for measured distances at all?
- **Lopsided box.** Is your median closer to Q1 or to Q3? What does that say about how the launches were bunched up?
- **Whisker length.** One whisker is longer than the other. Why would that happen with skimmers?

Then Mr. Willingham puts up the full analysis of every launch from both periods — the kind of analysis an engineer runs on real test data. Was there a "fast lane"? Did the class get better from trial 1 to trial 3? Is one period really better than the other, or is it noise? Does the outlier rule find anything? And how much did you vary against *yourself* — can you actually say your skimmer beat your neighbor's?

{{% checkpoint %}}

### Checkpoint: Closing

- [ ] I can explain the difference between range and IQR in my own words.
- [ ] I can say which of mean or median better describes a student with one bad launch, and why.

{{% /checkpoint %}}

{{% /closing %}}

## Standards

- [**MS-ENGR-II-4.5**](/design-modeling/description/#ms-engr-ii-4) — Utilize an Engineering Design Notebook as a record of process (the ten statistics and the hand-drawn, labeled box plot glued in under today's date).
- [**MS-ENGR-II-5.4**](/design-modeling/description/#ms-engr-ii-5) — Use mathematical and scientific reasoning as evidence to support an engineering solution (computing center and spread for the whole class's launch data and reading what the box plot says about the test).
