---
title: "[Solution] TimescaleDB Reorder Policy Error"
description: "How to fix TimescaleDB reorder policy errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Reorder policy not set
- Index not found
- Reorder failing on large chunks

## How to Fix

```sql
SELECT add_reorder_policy('conditions', 'conditions_time_idx');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs WHERE proc_name = 'policy_reorder';
```
