---
title: "[Solution] SQLite Immediate vs deferred transaction locking error"
description: "Confusion between IMMEDIATE and DEFERRED transaction modes causes unexpected lock behavior."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite Immediate vs deferred transaction locking error

SQLite raises a **Immediate vs deferred transaction locking error** error when confusion between immediate and deferred transaction modes causes unexpected lock behavior. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Using DEFERRED when the first operation is a write.
- Using IMMEDIATE when only reads are needed, causing unnecessary contention.
- Nested transactions mixing lock modes.

## How to Fix

### Use IMMEDIATE for transactions that write early

```sql
BEGIN IMMEDIATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### Use DEFERRED for read-only or late-write transactions

```sql
BEGIN DEFERRED;
SELECT * FROM accounts WHERE id = 1;
-- Write later if needed, then COMMIT
```

### Use EXCLUSIVE only when you need full database lock

```sql
BEGIN EXCLUSIVE;
VACUUM;
COMMIT;
```

## Examples

```sql
BEGIN DEFERRED;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- May get SQLITE_BUSY if another connection is writing
-- Fix: use BEGIN IMMEDIATE instead
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
