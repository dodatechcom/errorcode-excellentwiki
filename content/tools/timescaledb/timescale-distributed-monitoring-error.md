---
title: "[Solution] TimescaleDB Distributed Monitoring Error"
description: "How to fix TimescaleDB distributed monitoring errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Monitoring not showing distributed data
- Metrics endpoint not accessible
- Dashboard not configured

## How to Fix

```sql
SELECT * FROM timescaledb_information.data_nodes;
```

## Examples

```sql
SELECT * FROM timescaledb_information.hypertables;
```
