---
title: "no such table: X"
description: "SQLite cannot find the specified table in the database."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["database", "schema", "query"]
weight: 5
---

The `no such table` error means SQLite cannot locate the table referenced in your SQL statement. The table either does not exist, has been dropped, or is being referenced with an incorrect name.

## Common Causes

- The table name is misspelled or uses incorrect casing
- The table has not been created yet (missing schema migration)
- The query targets the wrong database file
- The table was dropped in a previous operation

## How to Fix

Check which tables exist in the database:

```sql
.tables
```

Inspect the schema for the table you expect:

```sql
.schema your_table_name
```

Create the table if it does not exist:

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);
```

## Examples

```sql
-- Querying a table that does not exist
SELECT * FROM orders;
-- Error: no such table: orders

-- Typo in table name
SELECT * FROM usr;
-- Error: no such table: usr
```

Confirm the correct table name:

```sql
.tables
-- Output: users  products  sessions
```

## Related Errors

- [SQLITE_BUSY: database is locked]({{< relref "/tools/sqlite/database-locked" >}})
