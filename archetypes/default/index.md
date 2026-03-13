---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
description: ""
day_number: 0
units: ["Podcast"]
tags: []
resources: []
draft: true
toc: true
---

# {{ dateFormat "Monday, January 2nd, 2006" .Date }}

{{< objectives >}}

-

{{< /objectives >}}

{{< warmup "Title" >}}

{{< checkpoint "Warmup" >}}

- [x] First checkpoint item.

{{< /checkpoint >}}

{{< /warmup >}}

{{< worksession "Title" >}}

{{< checkpoint "Work Session" >}}

- [x] First checkpoint item.

{{< /checkpoint >}}

{{< /worksession >}}

{{< closing "Next Steps" >}}

{{< /closing >}}
