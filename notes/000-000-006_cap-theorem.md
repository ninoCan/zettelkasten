---
date: 2025-08-13T10:04:00
source: https://en.wikipedia.org/wiki/CAP_theorem
tags: ["Databases", "System Design"]
---

# 000-000-006: CAP Theorem

The theorem formalizes as [trilemma](https://en.wikipedia.org/wiki/Trilemma) the properties that a data system can have:
- (C) Consistency: data reads return the most recent version (or fail)
- (A) Availability: every requests results in a response
- (P) Partition tolerance: operations proceed in spite of node failure

The trilemma entails 3 possible configurations: AP, CA, CP:

- AP: every request will be performed, reading might not be up-to-date
- CA: single node databases, network failure means no service
- CP: operations get refused when they cannot be consistent

Therefore, **distributed** systems can only choose between  AP and CP.

## connections:
- Consistency in CAP -[is not the same as]-> Consistency in [A**C**ID]() 
- CAP -[is generalised by]-> [PACELC](./000-000-007_pacelc-theorem.md)
 
