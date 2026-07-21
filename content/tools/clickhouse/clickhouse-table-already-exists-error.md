---
title: "[Solution] ClickHouse Table Already Exists Error"
description: "Fix ClickHouse table already exists errors when CREATE TABLE encounters duplicate"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Table Already Exists Error

Table already exists errors occur when trying to create a table that already exists in the database.

## Common Causes

- Migration script running multiple times
- Application creates tables on startup
- Using same table name in different databases
- Table was recreated after DROP

## How to Fix

Use IF NOT EXISTS:

```sql
CREATE TABLE IF NOT EXISTS my_table (id UInt64, name String) ENGINE = MergeTree() ORDER BY id;
```

Drop and recreate:

```sql
DROP TABLE IF EXISTS my_table;
CREATE TABLE my_table (id UInt64, name String) ENGINE = MergeTree() ORDER BY id;
```

Check existing tables:

```sql
SELECT database, name, engine FROM system.tables WHERE name = 'my_table';
```

## Examples

```sql
SHOW TABLES FROM mydb LIKE 'my_table';
```
