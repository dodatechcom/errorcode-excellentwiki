---
title: "[Solution] TimescaleDB Distributed Upgrade Error"
description: "How to fix TimescaleDB distributed upgrade errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Upgrade failing on distributed cluster
- Version mismatch between nodes
- Schema upgrade not synced

## How to Fix

```sql
ALTER EXTENSION timescaledb UPDATE;
```

## Examples

```sql
SELECT * FROM pg_extension WHERE extname = 'timescaledb';
```
