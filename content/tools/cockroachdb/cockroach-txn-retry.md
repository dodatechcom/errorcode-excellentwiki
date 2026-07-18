---
title: "[Solution] CockroachDB Transaction Retry Error - Fix Transaction Retry"
description: "Fix CockroachDB transaction retry errors. Implement retry logic for serialization errors and handle transaction conflicts."
tools: ["cockroachdb"]
error-types: ["txn-retry"]
severities: ["error"]
weight: 5
---

This error means a CockroachDB transaction was retried due to a serialization conflict. Serializable isolation requires transactions to be retried when conflicts occur.

## What This Error Means

When a transaction conflicts with another, you see:

```
ERROR: restart transaction: TransactionRetryError: retry txn
# or
SQLSTATE 40001: serialization failure
# or
ERROR: TransactionRetryError: WriteTooOld
```

CockroachDB uses serializable isolation by default. When concurrent transactions conflict, one is retried to maintain consistency.

## Why It Happens

- Two transactions modify the same row concurrently
- A read-write transaction conflicts with another write
- The write timestamp was pushed too far into the future
- High contention on hot rows causes frequent retries
- Long-running transactions hold locks that block others
- The application does not implement retry logic

## How to Fix It

### Implement automatic retries

```python
import psycopg2
from psycopg2 import extensions

def execute_with_retry(conn, sql, params=None, max_retries=5):
    for attempt in range(max_retries):
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                    return cur.fetchone()
        except psycopg2.OperationalError as e:
            if 'serialization' in str(e) and attempt < max_retries - 1:
                conn.rollback()
                continue
            raise
```

### Use SAVEPOINT for retryable errors

```sql
BEGIN;
SAVEPOINT cockroach_restart;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
RELEASE SAVEPOINT cockroach_restart;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Reduce contention with optimistic locking

```sql
UPDATE accounts
SET balance = balance - 100
WHERE id = 1 AND version = 5;
-- Check rows_affected to verify version match
```

### Use SELECT FOR UPDATE to lock rows early

```sql
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### Batch updates to reduce conflicts

```python
# Instead of individual updates
for account in accounts:
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, id))

# Use a single statement
cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id IN (%s)", (amount, ids))
```

### Shorten transaction duration

```python
# Read data outside the transaction
data = cursor.execute("SELECT * FROM accounts").fetchall()

# Keep transaction short
with conn:
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
```

### Monitor retry rates

```sql
SELECT * FROM [SHOW CLUSTER SETTINGS]
  WHERE variable LIKE '%transaction%retry%';
```

### Use follower reads for analytics

```sql
SELECT * FROM accounts AS OF SYSTEM TIME follower_read_timestamp();
```

Follower reads avoid conflicts with write transactions.

## Common Mistakes

- Not implementing retry logic for serializable transactions
- Running long transactions that hold locks for extended periods
- Using SELECT FOR UPDATE unnecessarily, increasing contention
- Not monitoring transaction retry rates
- Assuming CockroachDB retries are transparent to the application

## Related Pages

- [CockroachDB Serializable Error]({{< relref "/tools/cockroachdb/cockroach-serializable-error" >}}) -- isolation levels
- [CockroachDB Deadlock]({{< relref "/tools/cockroachdb/cockroach-deadlock" >}}) -- deadlocks
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
