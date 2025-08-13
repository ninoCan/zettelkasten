---
date: 2025-08-13T10:37:15
sources: [
 "https://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html",
"https://en.wikipedia.org/wiki/PACELC_design_principle#cite_note-Musings2020-2",
]
tags: ["Databases", "System Design", "Distributed Systems"]
---

# 000-000-007: PACELC Theorem

The theorem recognizes a fallacy in the [CAP](https://en.wikipedia.org/wiki/CAP_theorem): Availability and Consistencies are not well defined.
Then, it introduces [latency](https://en.wikipedia.org/wiki/Latency_(engineering)) to clarify ambiguities in the categories of the latter theorem.

![](https://upload.wikimedia.org/wikipedia/commons/3/3c/PACELC_theorem.png)

The theorem focuses only of **distributed** systems. The system must specify its behaviour both when a (P) partition occurs, or else (E) when no partitions are occurring in normal circumstances.
This defines 4 behaviours:
- PA/EL—prioritize Availability and Latency: High Availability (HA)
- PA/EC—prioritize Availability, process all requests in spite of time
- PC/EL—prioritize Latency, provide a baseline for Consistency
- PC/EC—always prioritize Consistency, ACID compliant


## connections:
- PACELC -[extends]-> [CAP](./000-000-006_cap-theorem.md)

