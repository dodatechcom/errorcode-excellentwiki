---
title: "TimescaleDB DDL Error"
description: "DDL operation on hypertable failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL operations on hypertables are failing.

## Common Causes
- Column already exists
- Invalid DDL for hypertable
- Concurrent DDL conflict

## How to Fix
```sql
-- Check table structure
\d mytable

-- Safe DDL for hypertables
ALTER TABLE mytable ADD COLUMN IF NOT EXISTS newcol INTEGER;
```

## Examples
```sql
-- Add column to hypertable
ALTER TABLE mytable ADD COLUMN device_name TEXT;
-- Create index on hypertable
CREATE INDEX idx_mytable_device ON mytable (device_id, time DESC);
```

