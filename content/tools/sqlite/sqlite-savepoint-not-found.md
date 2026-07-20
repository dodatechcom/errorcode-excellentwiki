---
title: "[Solution] SQLite savepoint not found"
description: "A ROLLBACK TO or RELEASE SAVEPOINT references a savepoint name that does not exist."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite savepoint not found

SQLite reports **savepoint not found** when a rollback to or release savepoint references a savepoint name that does not exist. Proper transaction management is essential for data integrity.

## Common Causes

- A typo in the savepoint name.
- The savepoint was already released or rolled back.
- Savepoints are not nested correctly.

## How to Fix

### Use consistent and unique savepoint names

```sql
BEGIN;
SAVEPOINT sp_step1;
-- operations
RELEASE sp_step1;
SAVEPOINT sp_step2;
-- operations
RELEASE sp_step2;
COMMIT;
```

### Check available savepoints

```sql
-- SQLite does not list savepoints; track them in your application logic
```

### Use ROLLBACK TO and RELEASE carefully

```sql
SAVEPOINT sp1;
-- operations
ROLLBACK TO sp1;  -- undo operations but keep transaction
RELEASE sp1;       -- remove the savepoint
```

## Examples

```sql
BEGIN;
SAVEPOINT sp1;
ROLLBACK TO sp2;
-- Error: no such savepoint: sp2
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
