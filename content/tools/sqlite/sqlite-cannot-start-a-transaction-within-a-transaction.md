---
title: "[Solution] SQLite cannot start a transaction within a transaction"
description: "A new BEGIN was issued while a transaction was already active."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite cannot start a transaction within a transaction

SQLite reports **cannot start a transaction within a transaction** when a new begin was issued while a transaction was already active. Proper transaction management is essential for data integrity.

## Common Causes

- The previous transaction was not committed or rolled back.
- A COMMIT or ROLLBACK is missing.
- Autocommit is off and a transaction is implicitly active.

## How to Fix

### Commit or rollback the existing transaction first

```sql
-- Check if a transaction is active, then:
COMMIT;
BEGIN;
```

### Use savepoints for nested operations

```sql
BEGIN;
SAVEPOINT sp1;
-- nested operation
RELEASE sp1;
COMMIT;
```

### Ensure autocommit is on between transactions

```python
conn.autocommit = True
```

## Examples

```sql
BEGIN;
BEGIN;
-- Error: cannot start a transaction within a transaction
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
