---
date: 2025-08-11T09:20:11
source:
tags: ["SQL", "keys"]
---

# 000-000-002: Foreign keys target column

The target column of a foreign key must contain **only** distinct values for the join to be successful.
As a result, joins can be performed over a _Unique Key_ rather then a _Primary Key_

## connections:
<!-- Example
[anchor]: <link> "title"
-->
