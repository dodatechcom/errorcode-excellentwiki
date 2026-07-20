---
title: "[Solution] SQLite database already attached"
description: "An ATTACH DATABASE statement tried to attach a database using an alias that is already in use."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite database already attached

SQLite produces **database already attached** when an attach database statement tried to attach a database using an alias that is already in use. The ATTACH/DETACH mechanism allows working with multiple databases simultaneously.

## Common Causes

- The database was previously attached with the same alias.
- The previous ATTACH was not followed by DETACH.
- A migration script ran the ATTACH statement twice.

## How to Fix

### Detach the database first

```sql
DETACH DATABASE extra;
ATTACH DATABASE '/path/to/db.sqlite' AS extra;
```

### Use a different alias

```sql
ATTACH DATABASE '/path/to/db.sqlite' AS extra2;
```

### Check currently attached databases

```sql
SELECT * FROM pragma_database_list;
```

## Examples

```sql
ATTACH DATABASE 'a.sqlite' AS mydb;
ATTACH DATABASE 'b.sqlite' AS mydb;
-- Error: database mydb already exists
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
