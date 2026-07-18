---
title: "[Solution] CockroachDB Deadlock Error — How to Fix"
description: "Fix CockroachDB transaction deadlocks by restructuring lock ordering, reducing transaction scope, using SELECT FOR UPDATE, and configuring deadlock detection."
tools: ["cockroachdb"]
error-types: ["deadlock-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB deadlock error occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. CockroachDB detects deadlocks automatically and aborts one transaction to break the cycle.

## Why It Happens

Deadlocks occur when transactions acquire locks on rows in inconsistent order. CockroachDB uses a wait-graph to detect deadlocks and will abort one of the conflicting transactions, but the application must handle the resulting error.

- Two transactions lock rows in opposite order (e.g., T1 locks row A then B, T2 locks row B then A)
- Long-running transactions hold locks while waiting for user input or external API calls
- Batch updates lock multiple rows without a consistent ordering strategy
- SELECT FOR UPDATE on one table followed by a write to a related table creates cross-table lock chains
- Transactions retry in a loop without backing off, causing livelock
- The application uses implicit transactions (auto-commit) that hold locks longer than expected

## Common Error Messages

```text
ERROR: deadlock detected
 DETAIL: Transaction (12345678-abcd-1234-abcd-123456789abc) transaction sequence 42 
 waitss for: lock acquisition on row (100,)/100@789
 which is held by transaction (87654321-dcba-4321-dcba-987654321abc) 
 transaction sequence 41
 which waits for: lock acquisition on row (200,)/200@789
 which is held by transaction (12345678-abcd-1234-abcd-123456789abc)
```

This is the classic deadlock: two transactions each hold a lock the other needs.

```text
ERROR: restart transaction: TransactionRetryError: retry txn 
 TransactionAbortedError (REASON_UNKNOWN)
```

A transaction was aborted due to contention. This can be caused by a deadlock that was resolved by the system.

```text
ERROR: unimplemented: max retries reached (0)
```

The automatic retry limit was exceeded. CockroachDB retries some transactions automatically but gives up after a threshold.

```text
ERROR: query canceled: result row count exceeded 2
```

While not a deadlock, this can occur when a deadlock resolution causes a partially completed batch to produce unexpected results.

## How to Fix It

### 1. Establish Consistent Lock Ordering

```sql
-- Bad: T1 locks accounts then orders, T2 locks orders then accounts
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE orders SET status = 'paid' WHERE account_id = 1;
COMMIT;

-- Transaction 2 (different order)
BEGIN;
UPDATE orders SET status = 'cancelled' WHERE account_id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 1;
COMMIT;

-- Good: Both transactions lock accounts first, then orders
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE orders SET status = 'paid' WHERE account_id = 1;
COMMIT;

-- Transaction 2 (same order)
BEGIN;
UPDATE accounts SET balance = balance + 50 WHERE id = 1;
UPDATE orders SET status = 'cancelled' WHERE account_id = 1;
COMMIT;
```

### 2. Use SELECT FOR UPDATE to Lock Early

```sql
-- Bad: Read then write (gap between lock acquisition)
BEGIN;
SELECT balance FROM accounts WHERE id = 1;
-- ... some processing ...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Good: Lock the row immediately with SELECT FOR UPDATE
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
-- Row is locked for the duration of the transaction
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 3. Reduce Transaction Scope

```sql
-- Bad: Long transaction holding locks
BEGIN;
SELECT * FROM inventory WHERE product_id = 1 FOR UPDATE;
-- Call external payment API (seconds of delay)
-- ... payment processing ...
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 1;
UPDATE orders SET status = 'paid' WHERE id = 100;
COMMIT;

-- Good: Split into smaller transactions
-- Transaction 1: Reserve inventory
BEGIN;
SELECT quantity FROM inventory WHERE product_id = 1 FOR UPDATE;
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 1;
COMMIT;

-- Transaction 2: Create order (after payment succeeds)
BEGIN;
INSERT INTO orders (id, product_id, status) VALUES (100, 1, 'paid');
COMMIT;
```

### 4. Implement Retry Logic with Backoff

```go
// Go: Retry deadlocked transactions with exponential backoff
func executeWithRetry(db *sql.DB, fn func(tx *sql.Tx) error) error {
    maxRetries := 3
    for i := 0; i < maxRetries; i++ {
        tx, err := db.BeginTx(context.Background(), nil)
        if err != nil {
            return err
        }
        err = fn(tx)
        if err == nil {
            return tx.Commit()
        }
        tx.Rollback()
        
        if strings.Contains(err.Error(), "deadlock") ||
           strings.Contains(err.Error(), "restart transaction") {
            backoff := time.Duration(math.Pow(2, float64(i))) * 100 * time.Millisecond
            time.Sleep(backoff)
            continue
        }
        return err
    }
    return fmt.Errorf("max retries reached")
}
```

```python
# Python: Retry with tenacity
import time
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import psycopg2

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.1, max=5),
    retry=retry_if_exception_type(psycopg2.errors.DeadlockDetected)
)
def execute_deadlock_safe(conn, sql, params=None):
    with conn.cursor() as cur:
        cur.execute(sql, params)
        conn.commit()
```

### 5. Configure Deadlock Detection

```sql
-- CockroachDB detects deadlocks automatically
-- The default timeout is 500ms for deadlock detection
-- Adjust if needed (rarely necessary)
SET CLUSTER SETTING kv.lock_table.deadlock_detection_enabled = true;
```

## Common Scenarios

**Deadlocks during batch processing.** Batch updates that touch the same rows in different order are prone to deadlocks. Sort the rows by primary key before updating to ensure consistent lock ordering.

**Deadlocks in microservices.** Two services updating shared tables can deadlock if they have different transaction patterns. Document the lock ordering convention and enforce it in code reviews.

**Deadlocks increase under high concurrency.** More concurrent transactions increase the probability of lock conflicts. Use connection pooling with limited concurrency to cap the number of simultaneous transactions.

## Prevent It

- Establish and document a table lock ordering convention for all transactions in the application
- Keep transactions as short as possible — never include external API calls or user interaction within a transaction
- Use `SELECT FOR UPDATE` for read-then-write patterns to acquire locks early and reduce the window for deadlocks
