---
title: "[Solution] TimescaleDB Access Node Checkpoint Error"
description: "How to fix TimescaleDB access node checkpoint errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Checkpoint taking too long
- Checkpoint interval too short
- Checkpoint not happening

## How to Fix

```ini
checkpoint_timeout = 15min
checkpoint_completion_target = 0.9
```

## Examples

```sql
SELECT * FROM pg_stat_bgwriter;
```
