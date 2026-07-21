---
title: "[Solution] ClickHouse Database Not Found Error"
description: "Fix ClickHouse database not found errors when connecting to non-existent databases"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Database Not Found Error

Database not found errors occur when queries reference a database that does not exist.

## Common Causes

- Database was dropped
- Typo in database name
- Database created on different cluster node
- Default database changed in config

## How to Fix

List all databases:

```sql
SHOW DATABASES;
```

Create database:

```sql
CREATE DATABASE IF NOT EXISTS mydb;
```

Check database in config:

```xml
<default_database>default</default_database>
```

## Examples

```sql
SELECT name, engine, metadata_path FROM system.databases WHERE name = 'mydb';
```
