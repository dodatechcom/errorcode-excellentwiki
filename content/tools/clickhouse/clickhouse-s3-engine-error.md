---
title: "[Solution] ClickHouse S3 Engine Error"
description: "Fix ClickHouse S3 table engine errors when reading or writing to S3 storage"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse S3 Engine Error

S3 engine errors occur when ClickHouse cannot access S3-compatible storage.

## Common Causes

- Invalid S3 credentials
- S3 endpoint unreachable
- Bucket does not exist
- Region mismatch in S3 configuration

## How to Fix

Check S3 connectivity:

```bash
aws s3 ls s3://my-bucket/
```

Verify S3 engine config:

```sql
CREATE TABLE s3_table (id UInt64, name String)
ENGINE = S3('https://s3.amazonaws.com/my-bucket/data/{partition}.csv', 'access_key', 'secret_key');
```

Check ClickHouse S3 log:

```bash
grep -i s3 /var/log/clickhouse-server/clickhouse-server.log | tail -20
```

## Examples

```sql
SELECT * FROM s3('https://s3.amazonaws.com/bucket/*.csv', 'key', 'secret', 'CSV');
```
