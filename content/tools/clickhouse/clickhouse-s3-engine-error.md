---
title: "[Solution] ClickHouse S3 Engine Error"
description: "How to fix ClickHouse S3 table engine errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- S3 credentials invalid
- Bucket not accessible
- Endpoint URL wrong
- File format mismatch

## How to Fix

Create S3 table:

```sql
CREATE TABLE s3_table (
  id UInt64,
  name String
) ENGINE = S3('https://bucket.s3.amazonaws.com/data/*.csv', 'KEY', 'SECRET', 'CSV');
```

## Examples

```sql
SELECT * FROM s3_table LIMIT 10;
SELECT count() FROM s3_table;
```
