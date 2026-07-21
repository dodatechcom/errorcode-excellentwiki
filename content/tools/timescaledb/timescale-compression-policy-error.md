---
title: "[Solution] TimescaleDB Compression Policy Error"
description: "How to fix TimescaleDB compression policy errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Compression policy not set
- Compress after interval wrong
- Policy not enabled

## How to Fix

```sql
SELECT add_compression_policy('conditions', INTERVAL '7 days');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs WHERE proc_name = 'policy_compression';
```
