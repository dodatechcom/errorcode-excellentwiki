---
title: "[Solution] AWS Timestream Error — database/table/query failures"
description: "Fix AWS Timestream errors. Resolve Timestream database, table, and query issues."
error-types: ["api-error"]
severities: ["error"]
weight: 144
---

An AWS Timestream error occurs when databases fail to create, writes are throttled, or queries return empty results. Timestream is a serverless time-series database but requires proper write and query configuration.

## Common Causes

- Database name already exists
- Write throughput exceeded (Memory store full)
- Query scans too much data without time filter
- Magnetic store writes disabled
- IAM role lacks Timestream permissions

## How to Fix

### List Databases

```bash
aws timestream-write list-databases
```

### Create Database

```bash
aws timestream-write create-database \
  --DatabaseName my-timeseries-db
```

### Create Table

```bash
aws timestream-write create-table \
  --DatabaseName my-timeseries-db \
  --TableName my-table \
  --RetentionProperties '{"MemoryStoreRetentionPeriodInHours":"24","MagneticStoreRetentionPeriodInDays":"365"}'
```

### Write Records

```bash
aws timestream-write write-records \
  --DatabaseName my-timeseries-db \
  --TableName my-table \
  --Records '[{"Dimensions":[{"Name":"host","Value":"server1"}],"MeasureName":"cpu","MeasureValue":"75","MeasureValueType":"DOUBLE","Time":"1234567890"}]'
```

### Query Data

```bash
aws timestream-query query \
  --query-string "SELECT * FROM my-timeseries-db.my-table WHERE time > ago(1h)"
```

## Examples

```bash
# Example 1: Write throttled
# WriteThrottlingException: Memory store is full
# Fix: increase MemoryStoreRetentionPeriod or reduce write rate

# Example 2: Query timeout
# QueryTimeoutException: Query timed out
# Fix: add time filter to reduce scan range
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) — CloudWatch monitoring errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
