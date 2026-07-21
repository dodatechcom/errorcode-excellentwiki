---
title: "[Solution] TimescaleDB Reindex Policy Error"
description: "How to fix TimescaleDB reindex policy errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Reindex policy not set
- Index corrupted
- Reindex taking too long

## How to Fix

```sql
SELECT add_reindex_policy('conditions', 'conditions_time_idx');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs WHERE proc_name = 'policy_reindex';
```
