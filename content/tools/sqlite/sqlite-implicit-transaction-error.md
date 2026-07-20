---
title: "[Solution] SQLite implicit transaction error"
description: "A statement that modifies data was executed without an explicit transaction, and the implicit transaction failed."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite implicit transaction error

SQLite reports **implicit transaction error** when a statement that modifies data was executed without an explicit transaction, and the implicit transaction failed. Proper transaction management is essential for data integrity.

## Common Causes

- Autocommit is on and each statement is its own transaction.
- A statement in an implicit transaction failed, rolling back partial changes.
- The developer expected multiple statements to be atomic.

## How to Fix

### Wrap related statements in an explicit transaction

```sql
BEGIN;
INSERT INTO accounts (id, balance) VALUES (1, 1000);
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### Use savepoints for sub-operations

```sql
BEGIN;
SAVEPOINT sp1;
INSERT INTO log VALUES ('step1');
RELEASE sp1;
COMMIT;
```

### Understand that each statement in autocommit mode is atomic by itself

```python
# With autocommit=True, each execute() is its own transaction
```

## Examples

```sql
-- Without explicit transaction:
INSERT INTO accounts VALUES (1, 1000);
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- If UPDATE fails, INSERT is NOT rolled back (different transactions)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
