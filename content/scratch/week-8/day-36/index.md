---
title: "Day 36: Rock, Paper, Scissors with Teachable Machine"
date: 2026-12-08T08:00:00-05:00
description: "Train an image classifier with your webcam and explore how training data shapes a model."
day_number: 36
units:
  - "Artificial Intelligence"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.3.3
  - MS-CS-FCP.4.2
  - MS-CS-FCP.6.1
tags:
  - AI
  - machine learning
  - Teachable Machine
  - training data
resources:
  - Teachable Machine
  - MIT RAISE Playground
draft: false
toc: true
scratchblocks: false
weight: 2
---

{{< icon "calendar" >}} **Tuesday, December 8th, 2026**

{{% objectives %}}

## Objectives

- I can explain what training data is and why the quality and quantity of examples matters.
- I can collect image samples, train a model, and test it in Teachable Machine.
- I can describe what happens when a model is trained on too few or unrepresentative examples.

{{% /objectives %}}

{{% warmup %}}

## Warmup: How Does a Computer Learn to See?

Answer in your head; we come back to these at the end:

1. To teach a computer the difference between a cat and a dog, what would you give it?
2. If every cat photo were taken in the same room with the same lighting, what would happen in a different room?
3. Why do more examples usually make a better model?

Then spend five minutes on the [MIT RAISE Playground](https://playground.raise.mit.edu/main/). Try one project and write one sentence about what it does and one about what surprised you.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I answered the three questions.
- [ ] I tried one RAISE Playground project and wrote two sentences.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Build a Classifier

Follow Steps 1–5 on [Rock, Paper, Scissors with Teachable Machine](/scratch/projects/teachable-machine-rock-paper-scissors/): open Teachable Machine, rename the three classes, collect at least 50 varied samples per class, train, test, and improve. The vocabulary (training data, class, model, confidence score, epoch) is on that page and on [Unit 3 Vocabulary](/scratch/reference/unit-3-vocab/#artificial-intelligence).

Vary your angle, position, and distance while recording. Fifty varied samples beat two hundred identical ones.

Answer the four testing questions from the project page in your notebook.

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ] I collected at least 50 samples for each of Rock, Paper, and Scissors.
- [ ] My model identifies all three with confidence above 70%.
- [ ] I tested an unusual angle or had a neighbor try it.
- [ ] I answered the four reflection questions.

{{% /checkpoint %}}

{{% /worksession %}}

{{% closing %}}

## Closing

You did what machine learning engineers do: define a problem, collect labeled data, train, evaluate, improve. Face unlock, spam filters, and recommendation feeds were all built with the same loop.

With a neighbor: what surprised you when you tested? Were your warmup predictions right? What is one ethical concern with image recognition, thinking about bias in training data?

Tomorrow we start VEXcode VR.

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including data, data collection, and data analysis (training data, classes, confidence scores).
- [**MS-CS-FCP.3.3**](/scratch/description/#ms-cs-fcp3) — Analyze how computers help humans solve problems (webcam input, training process, classifier output).
- [**MS-CS-FCP.4.2**](/scratch/description/#ms-cs-fcp4) — Utilize the design process to brainstorm, implement, test, and revise (collect, train, test, improve).
- [**MS-CS-FCP.6.1**](/scratch/description/#ms-cs-fcp6) — Summarize ethical issues of a digital world (bias in training data).
