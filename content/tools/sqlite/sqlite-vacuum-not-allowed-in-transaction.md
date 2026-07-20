---
title: "[Solution] SQLite VACUUM not allowed in transaction"
description: "VACUUM was executed inside an active transaction."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite VACUUM not allowed in transaction

SQLite reports **VACUUM not allowed in transaction** when vacuum was executed inside an active transaction. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- VACUUM cannot run inside a BEGIN...COMMIT block.
- The VACUUM statement was part of a script that began a transaction.

## How to Fix

### Ensure no transaction is active

```sql
COMMIT;  -- finish any active transaction
VACUUM;
```

### Run VACUUM outside of transactions

```bash
sqlite3 mydb.sqlite 'VACUUM;'
```

### Use auto_vacuum instead for continuous space reclamation

```sql
PRAGMA auto_vacuum = INCREMENTAL;
```

## Examples

```sql
BEGIN;
VACUUM;
-- Error: cannot VACUUM from within a transaction
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
