---
title: "[Solution] ClickHouse Table Already Exists Error"
description: "How to fix ClickHouse table already exists errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- CREATE TABLE called twice
- Table name collision
- Provisioning script not using IF NOT EXISTS

## How to Fix

Use IF NOT EXISTS:

```sql
CREATE TABLE IF NOT EXISTS my_table (id UInt32) ENGINE = MergeTree() ORDER BY id;
```

## Examples

```sql
CREATE TABLE IF NOT EXISTS my_table (id UInt32, name String) ENGINE = MergeTree() ORDER BY id;
SHOW TABLES LIKE 'my_table';
```
