---
title: "YugabyteDB Transaction Error Code"
description: "Transaction error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Transaction returning specific error code.

## Common Causes
- Transaction conflict
- Lock timeout
- Clock skew

## How to Fix
```sql
-- Check transaction status
SELECT * FROM pg_stat_activity WHERE state = 'active';

-- Kill stuck transaction
SELECT pg_terminate_backend(<pid>);
```

## Examples
```sql
-- Use advisory locks
SELECT pg_advisory_lock(12345);
-- Set statement timeout
SET statement_timeout = '30s';
```

