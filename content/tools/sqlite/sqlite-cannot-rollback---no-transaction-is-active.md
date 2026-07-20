---
title: "[Solution] SQLite cannot rollback - no transaction is active"
description: "A ROLLBACK statement was issued but no transaction is currently active."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite cannot rollback - no transaction is active

SQLite reports **cannot rollback - no transaction is active** when a rollback statement was issued but no transaction is currently active. Proper transaction management is essential for data integrity.

## Common Causes

- The transaction was already committed or rolled back.
- A previous error caused an automatic rollback.
- Autocommit is on.

## How to Fix

### Start a transaction before issuing ROLLBACK

```sql
BEGIN;
-- operations that may need rollback
ROLLBACK;
```

### Check if the transaction was already rolled back by an error

```sql
-- After an error, the transaction may already be rolled back
```

### Use savepoints for granular rollback control

```sql
BEGIN;
SAVEPOINT sp1;
-- operation
ROLLBACK TO sp1;  -- only rolls back to savepoint
COMMIT;
```

## Examples

```sql
ROLLBACK;
-- Error: cannot rollback - no transaction is active
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
