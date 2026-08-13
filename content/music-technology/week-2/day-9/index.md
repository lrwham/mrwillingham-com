---
title: "Day 9: Four on the Floor & Quantization"
date: 2026-08-13T08:00:00-04:00
description: "Play a four-on-the-floor beat into Soundtrap using a MIDI controller, then clean up the timing with quantization."
day_number: 9
units:
  - "Beat Making"
standards:
  - MSMTC8.CR.1
  - MSMTC8.CR.2
tags:
  - Soundtrap
  - Beat Making
  - Drums
  - MIDI
  - Quantization
resources:
  - "Soundtrap"
  - "MIDI Controller"
draft: false
toc: true
weight: 9
---

{{< icon "calendar" >}} **Thursday, August 13th, 2026**

{{% objectives %}}

## Objectives

- I can play a drum track into Soundtrap using a MIDI controller or the assigned computer keys.
- I can explain what quantization does and apply it to clean up the timing of a recording.
- I can identify a variety of MIDI controller styles: pad, keyboard, pedal, and drums.

{{% /objectives %}}

{{% warmup %}}

## Warmup: MIDI Controller Scavenger Hunt

Visit a common music equipment retailer like [Sweetwater](https://www.sweetwater.com/) or [Guitar Center](https://www.guitarcenter.com/). Search for "MIDI controller".

Find at least one example of each of the following types of MIDI controllers:

- **Pad controller** — usually a grid of squishy square buttons that can be tapped with your fingers
- **Keyboard controller** — looks like a piano; may also contain pads or knobs
- **Pedal controller** — played with your feet. Some look like a row of stomp switches; some look like a big piano laid on the floor. _(Try searching "MIDI foot controller.")_
- **Drum controller** — looks like a drum kit made of plastic and foam, played with drumsticks. _(Try searching "electronic drum kit" or "drum pad controller.")_

### Warmup Form

Submit your findings in the form. Simply name each controller you found.

<iframe title="MIDI Controller Scavenger Hunt form" width="640" height="480" src="https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=-x3OL5-ROEmquMR_D8kYLaF8AO3iXm9Ho39KOx_GABVUQkNWWkREN0xSVEFWQ1gwMVBFVlRQMTIxTi4u&embed=true" frameborder="0" marginwidth="0" marginheight="0" style="border: none; max-width:100%; max-height:100vh" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen> </iframe>

[Backup Link](https://forms.cloud.microsoft/r/34dAEpgFp7)

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have completed the MIDI Controller Scavenger Hunt and submitted my findings in the form.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Part 1 — Four on the Floor

"Four on the floor" is one of the most common drum patterns in popular music. The kick drum plays on **every** beat — 1, 2, 3, 4 — and you'll hear it in house, disco, rock, and pop. Today you'll build it up one drum at a time by **playing** the notes into Soundtrap instead of clicking them into a grid.

### Partner Protocol

You and your table-mate will share one MIDI controller. Each of you works in **your own project on your own computer**. Decide who goes first:

1. **Round 1 — Kick drum:** One of you uses the **MIDI controller**, the other uses the **assigned computer keys**.
2. **Swap** the controller after the kick is recorded.
3. **Round 2 — Snare drum:** The person who used the assigned keys now uses the controller, and vice versa.

This way everyone gets a turn with the controller, and everyone finishes with both tracks in their own project.

### Recording a Live Drum Track

Soundtrap lets you play drum sounds live and record them, instead of clicking them into a step grid.

The **assigned computer keys** are the keys on your laptop that trigger drum sounds when the on-screen keyboard is active in Soundtrap. <!-- TODO: list the exact keys you assigned, e.g. "Use A, S, D, and F for kick, snare, closed hi-hat, and crash." -->

{{< tabs >}}
{{< tab name="1. Open the Instrument tab" >}}
Click **Add track**, choose **Drums & Machines**, choose **Patterns**, then click the **Instrument** tab.
{{< /tab >}}
{{< tab name="2. Arm the track" >}}
Check that the record-enable button on the track is lit, so the track is ready to record.
{{< /tab >}}
{{< tab name="3. Play the notes" >}}
Use the **MIDI controller**, or the **assigned keys** on your computer keyboard, to play the drum sound.
{{< /tab >}}
{{< tab name="4. Record" >}}
Press **Cmd/Ctrl+Space** (or click the Record button) to start recording, and the **spacebar** to stop.
{{< /tab >}}
{{< /tabs >}}

### Build the Beat — One Track at a Time

We'll follow along with Mr. Willingham. Each track is **four measures** long. Today we are recording two tracks — kick and snare. You will add two more tracks on Friday.

1. **Track 1 — Kick drum:** Quarter notes on every beat. Count "1 — 2 — 3 — 4" for four full measures. _(swap input methods after this track)_
2. **Track 2 — Snare drum:** Play the snare on **beats 2 and 4** for four measures. This is the "backbeat."

Listen back after each track. Don't worry if it isn't perfect — we'll fix the timing in Part 2.

{{% checkpoint %}}

### Checkpoint: Work Session 1

- [ ] I have two tracks recorded: kick and snare.
- [ ] Each track is four measures long.
- [ ] I used one input method for the kick and **switched** for the snare.

{{% /checkpoint %}}

{{% /worksession %}}

{{% worksession %}}

## Work Session: Part 2 — Quantization

### What is Quantization?

When you **play** a beat by hand, your hits almost never land exactly on the beat — you're usually a little early or a little late. **Quantization** is a tool that snaps every recorded note to the nearest point on a grid. The grid is usually measured in note values — **1/4 notes, 1/8 notes, or 1/16 notes**. After you quantize, every note sits perfectly in time.

### Quantization is Like Rounding in Math

Think of quantization as **rounding for music**.

- In math, rounding 3.7 to the nearest whole number gives you **4**. Rounding 3.2 gives you **3**.
- In Soundtrap, if your snare hit lands at beat **2.07**, quantization "rounds" it down to beat **2**. If it lands at **1.94**, it rounds **up** to beat **2**.

The grid value you choose is like the **place value** you're rounding to:

- **1/4 note grid** = the coarsest grid, so the biggest rounding. Every note jumps to the nearest quarter note. Tight, locked-in, robotic.
- **1/8 note grid** = a finer grid, so smaller rounding. Good for hi-hats and most grooves.
- **1/16 note grid** = the finest grid, so the smallest rounding. Keeps more of the human feel, but it also leaves sloppy hits closer to where you played them.

{{< callout type="warning" >}}
Match the grid to what you actually played. Everything you recorded today lands on quarter notes, so a **1/4 Note** grid is the right choice — a 1/16 grid would leave your timing mistakes almost exactly where they are. Tomorrow's hi-hat plays eighth notes, so it will need a **1/8 Note** grid.
{{< /callout >}}

### How to Quantize in Soundtrap

1. Select your recorded track, then click **Piano Roll**.
2. Select the notes you want to fix — click and drag to select a range, or click any note and press **Cmd/Ctrl+A** to select all of them.
3. **Right-click** and select **Quantize**, then choose a subdivision.
4. Watch the notes snap onto the grid. Press spacebar and listen — it should sound tighter.

{{< callout type="info" >}}
You can also quantize a whole region without opening the Piano Roll — hover over the region, click **Edit**, then choose **Quantize**.
{{< /callout >}}

Quantize kick and snare using a **1/4 Note** subdivision today. You'll quantize the hi-hat and your choice track on Friday.

{{% checkpoint %}}

### Checkpoint: Work Session 2

- [ ] I quantized the kick track using **1/4 Note**.
- [ ] I quantized the snare track using **1/4 Note**.
- [ ] The beat now plays cleanly in time.
- [ ] I can explain quantization as "rounding" for musical timing.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing: Save Your Project

**We open this same project tomorrow.** Save your project and give it a name you will recognize — if you can't find your file on Friday, you lose the whole period.

### If You Finish Early

Try recording your beat a second time at a **different tempo** — same kick and snare, four measures each, quantized to **1/4 Note**. Save it as a separate project. We'll compare how tempo changes the feel of a four-on-the-floor beat.

You'll add the hi-hat and a fourth sound of your choice on Friday.

{{% checkpoint %}}

### Checkpoint: Closing

- [ ] I have saved my project with a name I will recognize tomorrow.
- [ ] I know where to find my project on Friday.

{{% /checkpoint %}}

{{% /closing %}}

## Standards

- [**MSMTC8.CR.1**](/music-technology/description/#msmtc8cr1) — Generate musical ideas for various purposes and contexts (playing a four-on-the-floor pattern into Soundtrap using a MIDI controller and computer-key input).
- [**MSMTC8.CR.2**](/music-technology/description/#msmtc8cr2) — Select and develop musical ideas for defined purposes and contexts (refining a recorded beat by choosing appropriate quantization grid values for each track).