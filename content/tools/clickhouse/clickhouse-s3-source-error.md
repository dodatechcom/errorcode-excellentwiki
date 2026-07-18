---
title: "[Solution] ClickHouse S3 Source Error — How to Fix"
description: "Fix ClickHouse S3 table function errors including credential issues, file format problems, and performance issues reading from S3"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse S3 Source Error

S3 source errors in ClickHouse occur when using the s3() table function to read data from S3-compatible storage. These include authentication failures, format mismatches, and performance issues.

## Why It Happens

- AWS credentials are missing or incorrect
- The S3 bucket or path does not exist
- The file format specification does not match the actual data
- The S3 endpoint URL is wrong for non-AWS S3
- The file is too large to process in a single operation
- The S3 request times out due to network issues

## Common Error Messages

```
Code: 210. DB::Exception: S3 endpoint error: Access Denied
```

```
Code: 62. DB::Exception: Failed to parse S3 object
```

```
Code: 210. DB::Exception: S3 endpoint returned 404 Not Found
```

```
Code: 241. DB::Exception: Memory limit exceeded while reading S3 file
```

## How to Fix It

### 1. Fix S3 Credentials

```sql
-- Use table function with credentials
SELECT * FROM s3(
  'https://s3.amazonaws.com/my-bucket/data/*.csv',
  'AKIAIOSFODNN7EXAMPLE',
  'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
  'CSV',
  'id UInt64, name String, value Float64'
);
```

### 2. Fix File Format Issues

```sql
-- For CSV files
SELECT * FROM s3(
  'https://s3.amazonaws.com/my-bucket/data/*.csv',
  'key', 'secret',
  'CSVWithNames',
  'id UInt64, name String'
);

-- For JSON files
SELECT * FROM s3(
  'https://s3.amazonaws.com/my-bucket/data/*.json',
  'key', 'secret',
  'JSONEachRow',
  'id UInt64, name String'
);
```

### 3. Fix S3 Endpoint for Non-AWS S3

```sql
-- For MinIO or other S3-compatible storage
SELECT * FROM s3(
  'http://minio-host:9000/my-bucket/data/*.csv',
  'minioadmin',
  'minioadmin',
  'CSVWithNames',
  'id UInt64, name String',
  'auto',
  'minio-host:9000'
);
```

### 4. Optimize S3 Read Performance

```sql
-- Use parallel reads
SET max_threads = 8;

-- Use glob pattern for multiple files
SELECT * FROM s3(
  'https://s3.amazonaws.com/my-bucket/data/year=2024/month=01/*.csv',
  'key', 'secret',
  'CSVWithNames',
  'id UInt64, name String, dt Date'
);
```

## Common Scenarios

- **S3 access denied after credential rotation**: Update the key/secret in the query.
- **File format mismatch**: Ensure the format specification matches the actual file format.
- **Slow S3 reads**: Use parallel reads and smaller file sizes.

## Prevent It

- Use IAM roles instead of static credentials when running on AWS
- Test S3 access with a simple query before deploying complex ETL
- Use proper file naming and partitioning for efficient S3 reads

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse Format Error](/tools/clickhouse/clickhouse-format-error)
- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
