---
title: "[Solution] SQLite database not attached"
description: "An SQL statement references an attached database that is no longer available."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite database not attached

SQLite produces **database not attached** when an sql statement references an attached database that is no longer available. The ATTACH/DETACH mechanism allows working with multiple databases simultaneously.

## Common Causes

- The database was DETACHed before the query.
- The connection was closed and reopened without re-attaching.
- The alias name is incorrect.

## How to Fix

### Re-attach the database

```sql
ATTACH DATABASE '/path/to/db.sqlite' AS extra;
SELECT * FROM extra.my_table;
```

### Check attached databases

```sql
SELECT * FROM pragma_database_list;
```

### Use fully qualified table names

```sql
SELECT * FROM extra.my_table WHERE extra.my_table.id = 1;
```

## Examples

```sql
DETACH DATABASE extra;
SELECT * FROM extra.my_table;
-- Error: no such database: extra
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
