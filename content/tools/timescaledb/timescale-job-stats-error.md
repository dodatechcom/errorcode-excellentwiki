---
title: "[Solution] TimescaleDB Job Stats Error"
description: "How to fix TimescaleDB job statistics errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job stats not available
- Job stats stale
- Job not running

## How to Fix

```sql
SELECT * FROM _timescaledb_internal.job_stats;
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
