---
title: "[Solution] ClickHouse Table Not Found"
description: "How to fix ClickHouse table not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Table name misspelled
- Wrong database specified
- Table not created yet
- Using distributed table without local table

## How to Fix

List tables:

```sql
SHOW TABLES FROM my_database;
SHOW TABLES;
```

Create table:

```sql
CREATE TABLE my_table (id UInt32, name String) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
SHOW DATABASES;
SHOW TABLES FROM default;
SELECT * FROM system.tables WHERE name = 'my_table';
```
