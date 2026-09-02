---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
description: ""
day_number: 1
units:
  - ""
standards: []
tags:
  - Design Process
resources:
  - "Engineering Notebook"
draft: false
toc: true
weight: 1
---

{{< icon "calendar" >}} **{{ dateFormat "Monday, January 2nd, 2006" .Date }}**

<!-- OPTIONAL: Uncomment for announcements, sub plans, schedule changes, etc.
{{% alert "message" %}}
Mr. Willingham is out today. Please follow the instructions below.
{{% /alert %}}
-->

{{% objectives %}}

## Objectives

- I can
- I can
- I can

{{% /objectives %}}

{{% warmup %}}

## Warmup

<!-- Head the Engineering Notebook page, then the warmup task -->

{{% checkpoint %}}

### Checkpoint: Warmup

- [ ]
- [ ]

{{% /checkpoint %}}

{{% /warmup %}}

{{% worksession %}}

## Work Session

<!-- Add work session instructions here. If the steps live on myPLTW, say so and give the navigation path. -->

<!-- OPTIONAL: Use buttons for resource links
{{< button text="Open myPLTW" >}}https://my.pltw.org/{{< /button >}}
-->

{{% checkpoint %}}

### Checkpoint: Work Session

- [ ]
- [ ]

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

<!-- Add closing/wrap-up instructions here -->

{{% /closing %}}

## Standards

- [**MS-ENGR-II-X.X**](/design-modeling/description/#ms-engr-ii-x) — Standard description here.
