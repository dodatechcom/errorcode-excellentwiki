---
title: "[Solution] SQLite SHM file corrupted"
description: "The shared memory (SHM) file used by WAL mode has become corrupted."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite SHM file corrupted

SQLite encounters **SHM file corrupted** when the shared memory (shm) file used by wal mode has become corrupted. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- Concurrent access caused SHM corruption.
- The SHM file was on a network filesystem (not supported).
- Process crash left the SHM file in a bad state.

## How to Fix

### Delete the SHM file

```bash
rm -f mydb.sqlite-shm
# SQLite will recreate it on next open
```

### Avoid using SQLite on NFS for WAL mode

```bash
# Use local storage for SQLite databases
```

### Use PRAGMA locking_mode = EXCLUSIVE to avoid SHM issues

```sql
PRAGMA locking_mode = EXCLUSIVE;
```

## Examples

```bash
rm -f mydb.sqlite-shm
sqlite3 mydb.sqlite "PRAGMA journal_mode = WAL;"
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
