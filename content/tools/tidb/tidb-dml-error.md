---
title: "[Solution] TiDB DML Error — How to Fix"
description: "Fix TiDB DML errors by resolving INSERT/UPDATE/DELETE failures, fixing write conflicts, and handling distributed DML operations"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB DML Error

TiDB DML errors occur when Data Manipulation Language operations fail due to distributed execution issues, conflicts, or constraint violations.

## Why It Happens

- INSERT violates unique constraint
- UPDATE/DELETE times out on large datasets
- Transaction conflicts under high concurrency
- TiKV store is not available for writes
- Lock conflict with concurrent transactions
- Batch operation is too large

## Common Error Messages

```
ERROR: duplicate entry for key
```

```
ERROR: lock conflict
```

```
ERROR: TiKV server is busy
```

```
ERROR: transaction too large
```

## How to Fix It

### 1. Fix INSERT Errors

```sql
-- Handle duplicate key
INSERT INTO users (id, name) VALUES (1, 'Alice')
ON DUPLICATE KEY UPDATE name = VALUES(name);

-- Use REPLACE for idempotent inserts
REPLACE INTO users (id, name) VALUES (1, 'Alice');

-- Batch inserts
INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
```

### 2. Fix UPDATE/DELETE Errors

```sql
-- Add WHERE clause to limit scope
UPDATE users SET name = 'Bob' WHERE id = 1;

-- Use LIMIT for large updates
UPDATE large_table SET status = 'done'
WHERE status = 'pending'
LIMIT 1000;

-- Batch delete
DELETE FROM logs WHERE created_at < '2024-01-01' LIMIT 10000;
```

### 3. Handle Write Conflicts

```sql
-- Use optimistic locking
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Use pessimistic locking
BEGIN PESSIMISTIC;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 4. Optimize DML Performance

```sql
-- Disable foreign key checks for bulk operations
SET foreign_key_checks = 0;
INSERT INTO large_table SELECT * FROM staging;
SET foreign_key_checks = 1;

-- Use batch operations
INSERT INTO orders SELECT * FROM staging_orders;
```

## Common Scenarios

- **Duplicate key on INSERT**: Use ON DUPLICATE KEY or REPLACE.
- **Write conflict under concurrency**: Use pessimistic transaction mode.
- **Large UPDATE is slow**: Add LIMIT and process in batches.

## Prevent It

- Use appropriate indexes for WHERE clauses
- Handle duplicate key errors in application
- Use batch operations for bulk data changes

## Related Pages

- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
