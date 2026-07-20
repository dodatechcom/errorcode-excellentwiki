---
title: "[Solution] SQLite journal file corrupted"
description: "The rollback journal file has become corrupted."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite journal file corrupted

SQLite encounters **journal file corrupted** when the rollback journal file has become corrupted. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- Power failure during journal write.
- Disk failure corrupted the journal file.
- Concurrent access corrupted the journal.

## How to Fix

### Delete the journal file to recover

```bash
rm -f mydb.sqlite-journal
# SQLite will detect corruption and may recover
```

### Use PRAGMA integrity_check

```sql
PRAGMA integrity_check;
```

### Switch to WAL mode for better crash recovery

```sql
PRAGMA journal_mode = WAL;
```

## Examples

```bash
sqlite3 mydb.sqlite "SELECT * FROM t;"
-- Error: journal file corrupted
rm mydb.sqlite-journal
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
