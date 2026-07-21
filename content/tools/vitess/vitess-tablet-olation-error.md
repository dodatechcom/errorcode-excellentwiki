---
title: "[Solution] Vitess Tablet Isolation Level Error"
description: "Fix Vitess transaction isolation level errors when vtgate and MySQL isolation settings conflict"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Isolation Level Error

Isolation level errors occur when vtgate requests a transaction isolation level that the backend MySQL does not support or that conflicts with current settings.

## Common Causes

- Requested isolation level not supported by storage engine
- Mix of InnoDB and MyISAM tables in same transaction
- SERIALIZABLE isolation causing excessive locking
- Session-level isolation override conflicting with global

## How to Fix

Check current isolation level:

```sql
SELECT @@transaction_isolation;
```

Set compatible isolation level:

```sql
SET SESSION transaction_isolation = 'REPEATABLE-READ';
```

Verify InnoDB usage:

```sql
SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'mydb';
```

## Examples

```sql
SET SESSION transaction_isolation = 'READ-COMMITTED';
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```
