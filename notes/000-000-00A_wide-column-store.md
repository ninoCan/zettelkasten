---
date: 2025-08-16T15:28:38
source: https://www.usenix.org/legacy/events/osdi06/tech/chang/chang_html/index.html
tags: ["Databases", "NoSQL", "Wide-Column"]
---

# 000-000-00A: Wide-Column Store

These NoSQL databases can store a huge and varying number of columns.
Tabular granularity is represented by the mean of **column families**, also called `tablets`.
Each column family contains key-pair records, representing rows.
Records are identified by `row keys`, and contains a set of `column keys` which can be expanded at a row level, so two rows on the same table can have different column keys.
To each column key associate with a **value**, **timestamp**, and possibly a **type**, but not necessarily.

These databases can be thought of as bi-dimensional key-value stores.

## connections:
<!-- Example
[anchor]: <link> "title"
-->
