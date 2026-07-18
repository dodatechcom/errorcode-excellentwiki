---
title: "[Solution] PostgreSQL Snapshot Too Old for Transaction Error — How to Fix"
description: "Fix PostgreSQL snapshot too old errors by reducing transaction duration, tuning old_snapshot_threshold, and avoiding long-running read transactions"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# PostgreSQL Snapshot Too Old for Transaction

This error means a long-running transaction tried to read data that has already been vacuumed away because its required MVCC snapshot is no longer available. PostgreSQL removed the old row versions because no active transaction was expected to need them.

## Why It Happens

- A transaction started many minutes or hours ago and tries to read data that was updated or deleted since
- `old_snapshot_threshold` is set and the snapshot has aged out
- Autovacuum aggressively removes dead tuples while a long-running query is active
- A batch job starts a transaction and processes millions of rows over hours
- A reporting query runs against live data without using a consistent snapshot
- The application holds a transaction open while waiting for user input

## Common Error Messages

```
ERROR: snapshot too old
DETAIL: Snapshot too old to build a snapshot.
```

```
ERROR: could not serialize access due to concurrent update
HINT: The transaction might succeed if retried.
```

```
ERROR: snapshot invalid for query revision 0
DETAIL: The snapshot MVCC data is no longer available.
```

## How to Fix It

### 1. Reduce Transaction Duration

```sql
-- Break long operations into smaller transactions
-- Instead of:
BEGIN;
SELECT * FROM large_table;  -- runs for 30 minutes
-- Use:
-- Batch 1: BEGIN; ... COMMIT;
-- Batch 2: BEGIN; ... COMMIT;
```

### 2. Check old_snapshot_threshold

```sql
-- Check current value (-1 means disabled)
SHOW old_snapshot_threshold;

-- Disable snapshot expiry (default)
ALTER SYSTEM SET old_snapshot_threshold = -1;
SELECT pg_reload_conf();
```

### 3. Monitor Long-Running Transactions

```sql
-- Find active transactions and their duration
SELECT
    pid,
    usename,
    state,
    xact_start,
    now() - xact_start AS duration,
    query,
    query_start,
    backend_start
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY xact_start;

-- Alert on transactions running longer than 5 minutes
SELECT * FROM pg_stat_activity
WHERE xact_start < now() - interval '5 minutes'
  AND state = 'active';
```

### 4. Set a Statement Timeout

```sql
-- Prevent queries from running too long
ALTER SYSTEM SET statement_timeout = '300s';
SELECT pg_reload_conf();

-- Or per-session for reporting queries
SET statement_timeout = '60s';
```

### 5. Use a Replica for Long Reads

```sql
-- Route long-running queries to a replica
-- The replica has its own MVCC state and does not affect the primary

-- In the application, connect to the read replica for reports
-- and the primary for writes
```

### 6. Use REPEATABLE READ When Needed

```sql
-- Take a consistent snapshot at transaction start
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT * FROM orders WHERE created_at > '2025-01-01';
-- This sees a frozen snapshot from the start of the transaction
COMMIT;
```

## Common Scenarios

- **End-of-day reporting**: A report query scans the entire `transactions` table while the table is being updated by live traffic. Use a replica or materialized view.
- **ETL pipeline**: A nightly ETL job reads from a table that is continuously updated. Break the job into smaller time-windowed chunks.
- **Interactive batch operation**: An admin opens a transaction, starts reviewing data, goes to lunch, then comes back and tries to read more data. Set `idle_in_transaction_session_timeout`.

## Prevent It

- Keep all transactions under 5 minutes by using batch processing with frequent commits
- Use `statement_timeout` to catch runaway queries before they hit snapshot issues
- Route long-running analytical queries to a read replica instead of the primary

## Related Pages

- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL Vacuum Error](/tools/postgresql/pg-vacuum-error)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
