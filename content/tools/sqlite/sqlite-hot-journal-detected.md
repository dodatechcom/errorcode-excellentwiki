---
title: "[Solution] SQLite hot journal detected"
description: "SQLite found a hot journal that indicates a previous transaction was not properly committed."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite hot journal detected

SQLite encounters **hot journal detected** when sqlite found a hot journal that indicates a previous transaction was not properly committed. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- A crash occurred during a write transaction.
- The process was killed while writing.
- A power failure left an incomplete journal.

## How to Fix

### Let SQLite replay the journal automatically

```sql
-- Opening the database should automatically replay the journal
PRAGMA journal_mode = WAL;
```

### Use PRAGMA integrity_check after recovery

```sql
PRAGMA integrity_check;
```

### Delete the journal only if recovery fails

```bash
# WARNING: may lose uncommitted data
rm mydb.sqlite-journal
```

## Examples

```bash
sqlite3 mydb.sqlite "PRAGMA journal_mode;"
-- Hot journal detected — SQLite will recover automatically
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
