---
title: "[Solution] ClickHouse Database Not Found"
description: "How to fix ClickHouse database not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database name misspelled
- Database not created
- Wrong user permissions
- Database on different cluster node

## How to Fix

List databases:

```sql
SHOW DATABASES;
```

Create database:

```sql
CREATE DATABASE IF NOT EXISTS my_database;
```

## Examples

```sql
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS analytics;
SELECT currentDatabase();
```
