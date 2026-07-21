---
title: "[Solution] TimescaleDB Compression Segment Error"
description: "How to fix TimescaleDB compression segment by errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Segment by column not found
- Segment by column not indexed
- Too many segments created

## How to Fix

```sql
ALTER TABLE mytable SET (timescaledb.compress_segmentby = 'device_id');
```

## Examples

```sql
SELECT * FROM timescaledb_information.compression_settings;
```
