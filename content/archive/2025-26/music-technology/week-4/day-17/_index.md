---
title: "Day 17: MIDI & the Piano Roll"
date: 2026-04-14
description: "Learn about MIDI and how to use the piano roll to create drum patterns."
day_number: 17
units:
  - "Beat Making"
standards:
  - MSMTC8.CR.1
  - MSMTC8.CR.2
tags:
  - GarageBand
  - Beat Making
  - Drums
  - MIDI
resources:
  - "GarageBand"
  - "Drum Worksheet Packet (printed)"
draft: false
toc: true
weight: 1
---

{{< icon "calendar" >}} **Tuesday, April 14th, 2026**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can identify the parts of a drum kit.
- I can use the piano roll to create MIDI patterns.
- I can program drum beats using MIDI.

{{% /objectives %}}

{{% warmup %}}

## Warmup

Login to Clever and watch the Edpuzzle video about MIDI. In the video Colin explains what MIDI is. The Musical Instrument Digital Interface (MIDI) is a way for electronic instruments and computers to communicate. It allows you to control virtual instruments, like the drum kit in GarageBand, using a MIDI controller or by programming patterns in the piano roll.

In the video he uses microcontrollers and MIDI to make a drum machine.

{{< clever >}}

As you watch, jot a quick answer to these on the back of your drum worksheet packet:

1. What do the letters **M-I-D-I** stand for?
2. Is MIDI *audio* (actual sound) or *instructions* (telling an instrument what to play)?
3. Name one thing MIDI lets you do that a plain audio recording cannot.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I have watched the video.
- [ ] I can briefly explain what MIDI is and what the letters in MIDI stand for.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

### What Is the Piano Roll?

Before MIDI, before computers, there were **player pianos** — real acoustic pianos that could play themselves. Instead of a person pressing the keys, the piano read a long sheet of paper called a **piano roll**. The paper had holes punched in it, and as the roll scrolled past a reader bar, each hole told the piano *which key to press* and *how long to hold it*. Wider holes meant longer notes. Holes further to the left or right meant lower or higher pitches.

<video controls>
  <source src="https://cdn.mrwillingham.com/player-piano.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

That idea never went away. When digital audio workstations like GarageBand were built, engineers borrowed the same visual language: **time flows left to right**, and **pitch is stacked top to bottom**. A note is just a rectangle — the longer the rectangle, the longer the note holds. Instead of punching holes in paper, you click and drag to place notes on a grid.

![GarageBand piano roll](https://cdn.mrwillingham.com/garageband-piano-roll.png)

For drums, each horizontal row in the piano roll is a different drum sound (kick, snare, hi-hat, etc.) instead of a different pitch. That's what the MIDI drum mapping table is for — it tells you which row plays which drum.

### Understanding MIDI Drum Mappings

In GarageBand's piano roll, each drum sound is triggered by a specific MIDI note number. The note you click determines which drum sound plays. 

Refer to the **[MIDI Drum Mappings](midi-mappings/)** page for the complete guide to which notes control which sounds. You'll find a quick reference table of the most commonly used drums (kick, snare, hi-hat, toms, cymbals) as well as the complete General MIDI drum map.

The drum notation key shows how these sounds are notated on the staff. **[Drum Notation Key](drum-notation-key/)**.

### Programming Your First Drum Beat

Grab your printed **Drum Worksheet Packet** from Mr. Willingham. The packet shows each beat of the measure broken into grid squares — exactly like the piano roll in GarageBand.

{{% steps %}}

##### Create a new Drummer/Drum Kit track

Open GarageBand and add a **Software Instrument** track with a drum kit patch. Open the piano roll (double-click the region or press **E**).

##### Find your drum notes

Using the **[MIDI Drum Mappings](midi-mappings/)** table, locate these three rows on the piano roll:

- **C1 (36)** — Kick
- **D1 (38)** — Snare
- **F#1 (42)** — Closed Hi-Hat

##### Program "Rock Steady"

Follow the **Rock Steady** pattern on your printed packet. Click once in each grid square that has an **X**. Work one drum at a time — hi-hat first, then kick, then snare.

##### Loop it and listen

Press the spacebar to play. Does it sound like a beat? If something feels off, check the grid against your packet square-by-square.

{{% /steps %}}

If you finish early, try programming the **Add Toms** pattern, which adds toms and cymbals to the mix. Use the MIDI mappings page to find the right notes for each tom and cymbal.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I can locate the MIDI mappings for at least 5 different drum sounds.
- [ ] I have successfully programmed a drum pattern in the piano roll using at least 3 different drum sounds.

{{% /checkpoint %}}

{{% /worksession %}}

<!-- OPTIONAL: Second work session block
{{% worksession %}}

## Work Session 2

{{% checkpoint %}}

### Checkpoint: Work Session 2

- [ ]

{{% /checkpoint %}}

{{% /worksession %}}
-->

{{% closing %}}

## Closing

### Return Your Packet

The **Drum Worksheet Packet** is a class set. Leave it in class.

### Exit Ticket

Before you leave, be ready to answer:

1. What MIDI note triggers the **kick**? The **snare**? The **closed hi-hat**?
2. Why is MIDI more flexible than recording a drum loop as audio? (Hint: think about changing the tempo or swapping the drum kit.)

{{% /closing %}}

## Standards

- [**MSMTC8.CR.1**](/music-technology/description/#msmtc8cr1) — Generate musical ideas for various purposes and contexts (programming rhythmic ideas using MIDI note numbers in the piano roll).
- [**MSMTC8.CR.2**](/music-technology/description/#msmtc8cr2) — Select and develop musical ideas for defined purposes and contexts (selecting drum sounds and arranging them into a complete beat pattern).
