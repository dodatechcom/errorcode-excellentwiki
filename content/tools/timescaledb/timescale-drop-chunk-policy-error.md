---
title: "[Solution] TimescaleDB Drop Chunk Policy Error"
description: "How to fix TimescaleDB drop chunk policy errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Retention policy not set
- Retention interval too short
- Policy not enabled

## How to Fix

```sql
SELECT add_retention_policy('conditions', INTERVAL '30 days');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs WHERE proc_name = 'policy_retention';
```
