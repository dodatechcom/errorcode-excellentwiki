---
title: "[Solution] TimescaleDB Chunk Compress Error"
description: "How to fix TimescaleDB chunk compression errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Chunk already compressed
- Compression not enabled
- Compress after policy wrong

## How to Fix

```sql
SELECT compress_chunk(c.chunk_name)
FROM timescaledb_information.chunks c
WHERE c.hypertable_name = 'conditions' AND c.is_compressed = false;
```

## Examples

```sql
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'conditions';
```
