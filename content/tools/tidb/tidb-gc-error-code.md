---
title: "TiDB GC Error Code"
description: "GC error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
GC returning specific error code.

## Common Causes
- GC life time too short
- GC blocked by long transactions
- GC worker failed

## How to Fix
```sql
-- Check GC status
SELECT * FROM mysql.tidb WHERE variable_name = 'tikv_gc_safe_point';

-- Check GC life time
SELECT @@tidb_gc_life_time;
```

## Examples
```sql
-- Check GC progress
SELECT * FROM mysql.tidb WHERE variable_name LIKE '%gc%';
-- Adjust GC life time
SET GLOBAL tidb_gc_life_time = '10m';
```

