---
title: "[Solution] SQLite File Is Encrypted or Not a Database"
description: "Fix SQLite 'file is encrypted or not a database' error. Resolve encryption and format issues."
tools: ["sqlite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQLite File Is Encrypted or Not a Database

This error occurs when SQLite tries to open a file that is either encrypted with SQLCipher or is not a valid SQLite database file. The file's header does not match the expected SQLite format.

## Common Causes

- The database is encrypted with SQLCipher but no key is provided
- The file path points to a non-database file (e.g., a log file)
- The database file was partially written or corrupted
- A different database format was mistaken for SQLite

## How to Fix

### Verify File is a Valid SQLite Database

```bash
file your_database.db
# Should say: SQLite 3.x database
```

### Provide Decryption Key for SQLCipher

```bash
sqlite3 your_database.db
PRAGMA key = 'your-encryption-key';
```

### Open with Correct Password in Application

```python
import sqlite3

conn = sqlite3.connect('your_database.db')
conn.execute("PRAGMA key = 'your-key'")
```

### Check File Path

```bash
# Ensure you're opening the right file
ls -la your_database.db
file your_database.db
```

### Convert Encrypted to Unencrypted

```bash
# With SQLCipher CLI
sqlcipher encrypted.db "PRAGMA key='secret'; .dump" | sqlite3 plain.db
```

## Examples

```bash
# Opening non-database file
sqlite3 config.log
# Error: file is encrypted or is not a database

# Missing SQLCipher key
sqlite3 encrypted.db
# Error: file is encrypted or is not a database
# Fix: PRAGMA key = 'correct-key';
```

## Related Errors

- [Malformed DB]({{< relref "/tools/sqlite/malformed-db" >}}) — database structure is corrupted
- [I/O Error]({{< relref "/tools/sqlite/io-error2" >}}) — disk I/O failure
