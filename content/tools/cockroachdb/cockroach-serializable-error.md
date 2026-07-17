---
title: "[Solution] CockroachDB Serializable Error - Fix Isolation Conflict"
description: "Fix CockroachDB serializable isolation errors by implementing automatic retry logic for 40001 errors, using follower reads, and reducing hot-key contention"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB serializable error occurs when a transaction cannot be committed at the serializable isolation level because another concurrent transaction has modified the data it read. The error code is `40001` (serialization failure).

## What This Error Means

CockroachDB defaults to `SERIALIZABLE` isolation, the strongest level. When a transaction reads rows and later tries to commit, CockroachDB checks whether any concurrent transaction has modified those same rows. If so, the current transaction must be retried to ensure serializable semantics.

The error message is `restart transaction: TransactionRetryError: retryable serializable transaction conflict: transaction <ID> was committed faster than it could be retried`.

## Why It Happens

- Two transactions read the same rows and one commits first, causing the other to detect a conflict
- High contention on hot rows (e.g., counters, inventory, leader election)
- Long-running read-write transactions increasing the window of conflict
- Hot partition keys with many concurrent transactions
- Application does not implement automatic retry logic for `40001` errors

## How to Fix It

### 1. Implement Transaction Retry Logic

```go
// Go example
const maxRetries = 5
for i := 0; i < maxRetries; i++ {
    tx, err := db.Begin()
    if err != nil {
        return err
    }
    _, err = tx.Exec("UPDATE inventory SET count = count - 1 WHERE product_id = 1")
    if err != nil {
        tx.Rollback()
        continue
    }
    err = tx.Commit()
    if err == nil {
        return nil
    }
    if pqErr, ok := err.(*pq.Error); ok && pqErr.Code == "40001" {
        time.Sleep(time.Duration(rand.Intn(100*(i+1))) * time.Millisecond)
        continue
    }
    return err
}
return fmt.Errorf("transaction failed after %d retries", maxRetries)
```

```python
# Python example
import psycopg2
import random
import time

def execute_with_retry(conn, query, max_retries=5):
    for attempt in range(max_retries):
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query)
            return
        except psycopg2.errors.SerializationError:
            conn.rollback()
            time.sleep(random.uniform(0.01, 0.1) * (attempt + 1))
    raise Exception("Max retries exceeded")
```

### 2. Reduce Transaction Duration

```sql
-- Do reads first, writes last
BEGIN;
SELECT count FROM inventory WHERE product_id = 1 FOR UPDATE;
-- Application logic here
UPDATE inventory SET count = count - 1 WHERE product_id = 1;
COMMIT;
```

### 3. Use Follower Reads for Stale Reads

```sql
-- Read from a follower to avoid conflicts
SELECT * FROM inventory AS OF SYSTEM TIME follower_read_timestamp()
WHERE product_id = 1;
```

### 4. Reduce Contention with Application-Level Locking

```python
# Use a distributed lock (e.g., via CockroachDB's pg_advisory_lock equivalent)
# Or serialize hot-path updates through a single worker
```

### 5. Partition Hot Tables

```sql
-- Distribute writes across ranges
CREATE TABLE inventory (
    product_id UUID,
    shard INT,
    count INT,
    PRIMARY KEY (product_id, shard)
) PARTITION BY LIST (shard) (
    PARTITION p0 VALUES IN (0),
    PARTITION p1 VALUES IN (1),
    PARTITION p2 VALUES IN (2)
);
```

## Common Mistakes

- Not retrying `40001` errors (they are expected under contention, not bugs)
- Holding transactions open while processing external data
- Using `SELECT FOR UPDATE` on rows that do not need to be locked
- Not using follower reads for analytics queries that can tolerate stale data

## Related Pages

- [CockroachDB Deadlock](/tools/cockroachdb/cockroach-deadlock)
- [CockroachDB Schema Error](/tools/cockroachdb/cockroach-schema-error)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
