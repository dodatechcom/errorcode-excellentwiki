---
title: "[Solution] CockroachDB Deadlock Detected - Fix Transaction Deadlocks"
description: "Fix CockroachDB deadlock detected errors by acquiring locks in a consistent order across all code paths, reducing transaction scope, and adding retry logic"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB deadlock detected error occurs when two or more transactions are waiting for each other to release locks, forming a circular dependency. CockroachDB detects these deadlocks and aborts one of the transactions with error code `40P01`.

## What This Error Means

CockroachDB uses a wait-die deadlock detection mechanism. When two transactions hold locks that the other needs, the database identifies the cycle and kills the transaction with the lower priority (or the older transaction). The application receives an error that the transaction was aborted due to a detected deadlock.

The error message includes the transaction IDs involved and the specific rows or keys that are contended.

## Why It Happens

- Two transactions lock rows in opposite order (e.g., TX1 locks row A then B, TX2 locks B then A)
- Long-running transactions holding locks while waiting for additional locks
- Bulk update operations touching the same rows as OLTP transactions
- Missing indexes forcing table-level locks instead of row-level locks
- Application code that performs multiple writes without proper ordering

## How to Fix It

### 1. Order Lock Acquisition Consistently

```sql
-- Always lock rows in the same order (e.g., by ascending ID)
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 2. Reduce Transaction Scope

```sql
-- Instead of one large transaction, break into smaller ones
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

BEGIN;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 3. Use SELECT FOR UPDATE with Ordering

```sql
BEGIN;
-- Lock rows in a deterministic order
SELECT * FROM accounts WHERE id IN (1, 2) ORDER BY id FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 4. Implement Retry Logic

```go
// Go example with retry
for {
    tx, err := db.Begin()
    if err != nil {
        return err
    }
    _, err = tx.Exec("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    if err != nil {
        tx.Rollback()
        if pqErr, ok := err.(*pq.Error); ok && pqErr.Code == "40P01" {
            time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
            continue // retry
        }
        return err
    }
    err = tx.Commit()
    if err == nil {
        break
    }
}
```

### 5. Add Proper Indexes

```sql
-- Ensure queries use row-level locks, not table scans
CREATE INDEX idx_accounts_id ON accounts (id);
```

### 6. Avoid Long-Running Transactions

```sql
-- Set a statement timeout to catch long transactions
SET CLUSTER SETMENT SETTING sql.defaults.statement_timeout = '10s';
```

## Common Mistakes

- Acquiring locks in different order across different code paths
- Holding open transactions while performing HTTP calls or external API requests
- Not implementing transaction retry logic (deadlocks are expected under contention)
- Using `SELECT FOR UPDATE` without an explicit `ORDER BY`, leading to non-deterministic lock ordering

## Related Pages

- [CockroachDB Serializable Error](/tools/cockroachdb/cockroach-serializable-error)
- [CockroachDB Schema Change](/tools/cockroachdb/cockroach-schema-change)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
