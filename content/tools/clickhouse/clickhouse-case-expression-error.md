---
title: "[Solution] ClickHouse CASE Expression Error"
description: "How to fix ClickHouse CASE expression errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CASE syntax wrong
- THEN type mismatch
- Missing ELSE clause

## How to Fix

```sql
SELECT CASE WHEN score > 90 THEN 'A' WHEN score > 80 THEN 'B' ELSE 'C' END FROM mytable;
```

## Examples

```sql
SELECT CASE id WHEN 1 THEN 'one' WHEN 2 THEN 'two' ELSE 'other' END FROM mytable;
```
