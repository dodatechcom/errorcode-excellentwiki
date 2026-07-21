---
title: "[Solution] ClickHouse Table Not Found Error"
description: "Fix ClickHouse table not found errors when queries reference non-existent tables"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Table Not Found Error

Table not found errors occur when a query references a table that does not exist in the database.

## Common Causes

- Table dropped during schema migration
- Wrong database name in query
- Table created in different database
- Case sensitivity in table names

## How to Fix

List tables in database:

```sql
SHOW TABLES FROM mydb;
```

Check system tables:

```sql
SELECT database, name FROM system.tables WHERE name = 'my_table';
```

Create table:

```sql
CREATE TABLE mydb.my_table (id UInt64, name String) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SELECT database, name, engine FROM system.tables
WHERE name LIKE '%order%' ORDER BY database;
```
