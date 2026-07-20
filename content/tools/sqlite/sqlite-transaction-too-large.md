---
title: "[Solution] SQLite transaction too large"
description: "A transaction modified too much data, exceeding internal limits or exhausting memory."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite transaction too large

SQLite reports **transaction too large** when a transaction modified too much data, exceeding internal limits or exhausting memory. Proper transaction management is essential for data integrity.

## Common Causes

- A single transaction inserts millions of rows.
- The undo journal grows too large.
- Memory is exhausted during a large transaction.

## How to Fix

### Commit in batches

```sql
BEGIN;
INSERT INTO big_table SELECT * FROM source LIMIT 10000;
COMMIT;
BEGIN;
INSERT INTO big_table SELECT * FROM source LIMIT 10000 OFFSET 10000;
COMMIT;
```

### Use PRAGMA journal_size_limit to control journal size

```sql
PRAGMA journal_size_limit = 1073741824;  -- 1 GB
```

### Avoid very large single transactions

```sql
-- Break work into chunks of 1000-10000 rows
```

## Examples

```sql
BEGIN;
INSERT INTO big_table SELECT * FROM million_row_source;
-- Error: SQLITE_TOOBIG or out of memory after millions of rows
COMMIT;
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
