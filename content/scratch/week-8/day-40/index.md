---
title: "Day 40: Rock, Paper, Scissors with Teachable Machine"
date: 2026-05-15T08:00:00-04:00
description: "Use Google's Teachable Machine to build an image classifier that recognizes Rock, Paper, and Scissors hand signs — exploring data collection, training, and the limits of machine learning models."
day_number: 40
units:
  - "Artificial Intelligence"
standards:
  - MS-CS-FCP.3.2
  - MS-CS-FCP.3.3
  - MS-CS-FCP.3.4
  - MS-CS-FCP.4.2
  - MS-CS-FCP.6.1
tags:
  - AI
  - machine-learning
  - Teachable Machine
  - image-classification
  - training-data
  - data-collection
resources:
  - Teachable Machine
draft: false
toc: true
scratchblocks: false
weight: 5
---

{{< icon "calendar" >}} **Friday, May 15th, 2026**

{{% objectives %}}

## Objectives

- I can explain what *training data* is and why the quality and quantity of examples matters.
- I can collect image samples, train a machine learning model, and test it using Teachable Machine.
- I can describe what happens when a model is trained on too few examples or unrepresentative data.
- I can connect the idea of a classifier to real-world AI applications like face recognition or spam filters.

{{% /objectives %}}

{{% warmup %}}

## Warmup: How Does a Computer Learn to See?

Think back to the BrainPOP lessons this week — specifically the vocabulary you built around *training data* and *machine learning*.

Answer these questions in your notebook or on a piece of paper before we start:

1. If you wanted to teach a computer to tell the difference between a cat and a dog, what would you give it?
2. What do you think would happen if all your cat photos were taken in the same room with the same lighting — and then you tested the model in a different room?
3. Why do you think more examples usually lead to a better model?

We'll come back to these questions at the end of class.

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ] I wrote answers to all three questions.

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session: Build a Rock-Paper-Scissors Classifier

Today you will train a real machine learning model using your webcam. No code required — just your hand and your brain.

### Key Vocabulary

Training Data
: The collection of examples used to teach a machine learning model. For an image classifier, each example is a photo labeled with the correct answer.

Class
: A category your model will learn to recognize. Today your classes are **Rock**, **Paper**, and **Scissors**.

Model
: The result of training — a set of learned patterns the computer uses to make predictions on new input it has never seen before.

Confidence Score
: A percentage that tells you how sure the model is about its prediction. A score of 95% means the model is very confident; a score of 40% means it is guessing.

Epoch
: One complete pass through all your training examples. More epochs can improve accuracy, but too many can cause the model to memorize your exact training photos instead of learning general patterns.

---

### Step 1 — Open Teachable Machine

Go to **[teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)** and click **Get Started**, then choose **Image Project → Standard image model**.

You will see three empty classes. Rename them:

- Class 1 → **Rock**
- Class 2 → **Paper**
- Class 3 → **Scissors**

---

### Step 2 — Collect Training Data

This is the most important step. Your model can only learn from examples you give it. Follow these guidelines carefully.

{{< callout type="important" >}}
**Quality matters more than speed.** Move your hand around slightly for each sample. Change the angle. Move closer and farther. A model trained on 50 varied examples will almost always beat a model trained on 200 nearly identical photos.
{{< /callout >}}

For each class (**Rock**, **Paper**, **Scissors**):

1. Click **Webcam** under the class name.
2. Hold your hand sign in front of the camera.
3. Hold down the **Hold to Record** button and collect **at least 50 samples per class**.
4. While recording, slowly rotate your hand, move it slightly left and right, and vary the distance from the camera.
5. Try recording some samples with your hand lower in the frame and some higher.

**Why vary the examples?** If every Rock sample shows your fist in the exact center of the frame at the exact same distance, the model may only recognize Rock when those conditions are met. Variation teaches the model what Rock looks like *in general*, not just in one specific situation.

{{% checkpoint %}}

### Checkpoint: Data Collection

- [ ] I collected at least 50 samples for Rock.
- [ ] I collected at least 50 samples for Paper.
- [ ] I collected at least 50 samples for Scissors.
- [ ] I varied the angle, position, and distance of my hand during recording.

{{% /checkpoint %}}

---

### Step 3 — Train Your Model

Click **Train Model**. Teachable Machine will process all your samples and train a classifier.

While you wait (it takes 30–60 seconds), think about what is happening:

- The computer is analyzing patterns in every photo — shapes, edges, colors, positions.
- It is learning rules like "when I see a rounded shape with fingers folded over, that tends to be Rock."
- It did not need a programmer to write those rules. It *figured them out* from your examples.

When training finishes, the **Preview** panel on the right will activate.

---

### Step 4 — Test Your Model

Hold your hand signs up to the camera one at a time and observe the confidence scores.

Answer these questions in your notebook as you test:

1. Which hand sign does your model recognize most reliably? Why do you think that is?
2. Try showing your hand at an unusual angle — one you did not use during training. What happens to the confidence score?
3. Have a neighbor try your model with *their* hand. Does it still work? What does this tell you about your training data?
4. What would you need to do to make the model work for a wider range of people?

{{% checkpoint %}}

### Checkpoint: Testing

- [ ] My model can identify all three hand signs with a confidence score above 70%.
- [ ] I tested an unusual angle or had a neighbor try my model.
- [ ] I answered all four reflection questions in my notebook.

{{% /checkpoint %}}

---

### Step 5 — Improve Your Model (If Time Allows)

If your model is struggling with one class, do not start over. Instead:

1. Click **Edit** on the underperforming class.
2. Add more samples — especially in the positions and angles where the model is struggling.
3. Click **Train Model** again.

This is the real-world machine learning workflow: collect → train → test → improve.

{{% /worksession %}}

{{% closing %}}

## Closing

Let's connect what you did today to the bigger picture.

You just did what data scientists and machine learning engineers do — you:

1. Defined a problem (classify hand signs).
2. Collected labeled training data.
3. Trained a model.
4. Evaluated its performance.
5. Identified where it failed and thought about how to fix it.

Every AI system you interact with — your phone's face unlock, spam filters in email, the "For You" page on social media — was built with this same loop.

**Think-pair-share** with a neighbor or write in your notebook:

- What was the most surprising thing that happened when you tested your model?
- Go back to the warmup questions. Were your predictions correct?
- What is one ethical concern you can think of with image recognition AI? (Think about bias in training data.)

{{% /closing %}}

## Standards

- [**MS-CS-FCP.3.2**](/scratch/description/#ms-cs-fcp3) — Develop a working vocabulary of computational thinking including **data**, **data collection**, **data analysis**, and **automation** — students build and apply vocabulary around training data, classes, confidence scores, and the training process throughout the lesson.
- [**MS-CS-FCP.3.3**](/scratch/description/#ms-cs-fcp3) — Analyze the problem-solving process and how computers help humans solve problems — students directly observe the input-process-output model: webcam images (input) → training algorithm (process) → classifier predictions (output).
- [**MS-CS-FCP.3.4**](/scratch/description/#ms-cs-fcp3) — Develop an algorithm to decompose a problem of a daily task — students decompose the recognition problem into discrete classes and articulate how a classifier uses learned patterns to make decisions.
- [**MS-CS-FCP.4.2**](/scratch/description/#ms-cs-fcp4) — Utilize the design process to brainstorm, implement, test, and revise an idea — students follow the full design loop: collect data, train, evaluate, and improve the model based on test results.
- [**MS-CS-FCP.6.1**](/scratch/description/#ms-cs-fcp6) — Summarize ethical, privacy, and legal issues of a digital world using current case studies — the closing reflection prompts students to consider bias in training data and the real-world implications of image recognition systems.
