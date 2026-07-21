---
title: "[Solution] TimescaleDB Chunk Create Error"
description: "How to fix TimescaleDB chunk creation errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Chunk interval too small
- Too many chunks created
- Chunk creation failing

## How to Fix

```sql
SELECT * FROM timescaledb_information.chunks ORDER BY range_start DESC LIMIT 5;
```

## Examples

```sql
SELECT * FROM timescaledb_information.hypertables;
```
