---
title: "[Solution] ClickHouse Table Function Error"
description: "How to fix ClickHouse table function errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong function parameters
- File not accessible
- Format not matching data

## How to Fix

Use table functions:

```sql
SELECT * FROM s3('https://bucket.s3.amazonaws.com/data.csv', 'KEY', 'SECRET', 'CSV', 'id UInt64, name String');
SELECT * FROM file('/path/to/data.csv', 'CSV', 'id UInt64, name String');
```

## Examples

```sql
SELECT * FROM url('http://example.com/data.json', 'JSONEachRow', 'id UInt64, name String');
SELECT * FROM mysql('host:3306', 'database', 'table', 'user', 'password');
```
