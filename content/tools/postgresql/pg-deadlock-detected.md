---
title: "[Solution] PostgreSQL Deadlock Detected Error — How to Fix"
description: "Fix PostgreSQL deadlock detected errors by analyzing lock graphs, optimizing query order, adding indexes, and implementing retry logic"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# PostgreSQL Deadlock Detected Error

This error means two or more transactions are waiting for each other to release locks, creating a circular dependency that PostgreSQL cannot resolve. PostgreSQL detects deadlocks automatically and rolls back the victim transaction to break the cycle.

## Why It Happens

- Two transactions acquire locks on the same rows in opposite order
- A transaction holds a row lock and waits for a lock on another row held by a second transaction
- Long-running transactions increase the window for lock conflicts
- Missing indexes cause table-wide locks instead of row-level locks
- Batch updates touch many rows in an unpredictable order
- Foreign key constraints acquireSHARE ROW EXCLUSIVE locks on referenced tables

## Common Error Messages

```
ERROR: deadlock detected
DETAIL: Process 12345 waits for ShareLock on transaction 67890; blocked by process 67890.
Process 67890 waits for ShareLock on transaction 12345; blocked by process 12345.
```

```
 deadlock detected
 DETAIL: Process 34567 waits for RowExclusiveLock on table orders; blocked by process 23456.
  Process 23456 waits for RowExclusiveLock on table inventory; blocked by process 34567.
```

```
 ERROR: deadlock detected
 HINT: See server log for query details.
```

## How to Fix It

### 1. Analyze the Deadlock from Server Logs

```bash
# Enable deadlock logging
ALTER SYSTEM SET log_lock_waits = on;
ALTER SYSTEM SET deadlock_timeout = '1s';
SELECT pg_reload_conf();

# View deadlock details in the log
tail -f /var/log/postgresql/postgresql-main.log | grep -A 20 "deadlock detected"
```

### 2. Lock Table and Row Ordering

```sql
-- Wrong: two transactions lock rows in different orders
-- Transaction A: UPDATE accounts WHERE id = 1; UPDATE orders WHERE account_id = 1;
-- Transaction B: UPDATE orders WHERE account_id = 2; UPDATE accounts WHERE id = 2;

-- Right: always lock rows in the same global order (e.g., by primary key ascending)
-- Both transactions: UPDATE accounts WHERE id = X; THEN UPDATE orders WHERE account_id = X;
```

### 3. Use SELECT FOR UPDATE with NOWAIT

```sql
-- Fail fast instead of waiting for a lock
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- If locked by another transaction, this raises an error immediately
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

```sql
-- Or skip locked rows
SELECT * FROM accounts WHERE id = 1 FOR UPDATE SKIP LOCKED;
```

### 4. Add Indexes to Reduce Lock Scope

```sql
-- Without an index, UPDATE locks the entire table
-- With an index, UPDATE locks only the matching rows
CREATE INDEX idx_orders_account_id ON orders (account_id);
CREATE INDEX idx_inventory_product_id ON inventory (product_id);
```

### 5. Implement Application-Level Retry Logic

```python
import psycopg2
import random
import time

def execute_with_retry(conn, query, params=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            return cur.fetchall()
        except psycopg2.errors.DeadlockDetected:
            conn.rollback()
            if attempt < max_retries - 1:
                wait = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait)
            else:
                raise
```

### 6. Reduce Transaction Duration

```sql
-- Instead of one long transaction doing many things:
BEGIN;
-- ... 50 queries ...
COMMIT;

-- Break into smaller transactions:
-- Batch 1: BEGIN; ... COMMIT;
-- Batch 2: BEGIN; ... COMMIT;
```

## Common Scenarios

- **Inventory deduction race**: Two purchases try to deduct from the same stock. Lock rows in a consistent order (by product_id ascending).
- **Transfer between accounts**: Account A to B and B to A simultaneously. Always lock the lower ID first.
- **Batch job processing**: A worker processes rows out of order. Use `FOR UPDATE SKIP LOCKED` with a job queue pattern.

## Prevent It

- Always lock rows in a consistent global order across all transactions
- Keep transactions as short as possible to reduce the lock conflict window
- Add appropriate indexes so UPDATE and DELETE operations lock only matching rows

## Related Pages

- [PostgreSQL Lock Timeout](/tools/postgresql/pg-lock-timeout)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [MySQL Lock Wait Timeout](/tools/mysql/mysql-lock-wait-timeout)
