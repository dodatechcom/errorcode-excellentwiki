---
title: "[Solution] SQLite DETACH not allowed in transaction"
description: "A DETACH DATABASE statement was issued while in the middle of a transaction that modified the attached database."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite DETACH not allowed in transaction

SQLite produces **DETACH not allowed in transaction** when a detach database statement was issued while in the middle of a transaction that modified the attached database. The ATTACH/DETACH mechanism allows working with multiple databases simultaneously.

## Common Causes

- DETACH is attempted during an active transaction on the attached database.
- The attached database has uncommitted changes.
- A trigger or callback holds a reference to the attached database.

## How to Fix

### Commit or rollback the transaction first

```sql
COMMIT;  -- or ROLLBACK
DETACH DATABASE extra;
```

### Avoid attaching databases that are being modified in the same transaction

```sql
-- Attach only for read-only queries, then detach
```

### Use separate connections for separate databases

```python
conn_main = sqlite3.connect('main.db')
conn_extra = sqlite3.connect('extra.db')
```

## Examples

```sql
BEGIN;
ATTACH DATABASE 'other.sqlite' AS extra;
INSERT INTO extra.my_table VALUES (1);
DETACH DATABASE extra;
-- Error: cannot detach database in transaction
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
