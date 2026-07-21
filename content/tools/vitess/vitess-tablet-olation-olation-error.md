---
title: "[Solution] Vitess Tablet Isolation Error"
description: "Fix Vitess tablet isolation errors when transaction isolation levels cause unexpected behavior"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Isolation Error

Isolation errors occur when transaction isolation level settings cause unexpected query results or performance issues.

## Common Causes

- READ UNCOMMITTED allowing dirty reads
- REPEATABLE READ causing phantom reads in some scenarios
- SERIALIZABLE causing excessive lock waits
- Isolation level mismatch across connection pool

## How to Fix

Check session isolation:

```sql
SELECT @@transaction_isolation;
```

Set appropriate level:

```sql
SET SESSION transaction_isolation = 'READ-COMMITTED';
```

Verify application expectations:

```sql
-- Test for phantom reads
START TRANSACTION;
SELECT COUNT(*) FROM orders WHERE status = 'pending';
-- In another session: INSERT INTO orders (status) VALUES ('pending');
SELECT COUNT(*) FROM orders WHERE status = 'pending';
COMMIT;
```

## Examples

```sql
SET SESSION transaction_isolation = 'READ-COMMITTED';
```
