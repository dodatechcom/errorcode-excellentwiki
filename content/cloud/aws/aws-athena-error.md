---
title: "[Solution] AWS Athena Error — query/workgroup/result-set failures"
description: "Fix AWS Athena errors. Resolve query execution, workgroup, and result set issues."
error-types: ["api-error"]
severities: ["error"]
weight: 137
---

An AWS Athena error occurs when queries fail to execute, workgroups misconfigure, or result sets are not accessible. Athena provides serverless SQL queries over S3 data but requires proper data formatting and permissions.

## Common Causes

- S3 data not in a supported format (Parquet, ORC, JSON, CSV)
- IAM role does not have S3 read access
- Query exceeds data scanned limit
- Workgroup encryption settings conflict
- Database or table does not exist in Glue catalog

## How to Fix

### Run Query

```bash
aws athena start-query-execution \
  --query-string "SELECT count(*) FROM my_table" \
  --result-configuration OutputLocation=s3://my-bucket/athena-results/ \
  --work-group my-workgroup
```

### Check Query Status

```bash
aws athena get-query-execution \
  --query-execution-id query-xxx
```

### Get Query Results

```bash
aws athena get-query-results \
  --query-execution-id query-xxx
```

### List Workgroups

```bash
aws athena list-work-groups
```

### Create Named Query

```bash
aws athena create-named-query \
  --name my-saved-query \
  --database my-db \
  --query-string "SELECT * FROM my_table LIMIT 10" \
  --work-group my-workgroup
```

## Examples

```bash
# Example 1: Data format not supported
# InvalidRequestException: Data format not recognized
# Fix: convert data to Parquet or use SerDe for custom format

# Example 2: Query limit exceeded
# LimitExceededException: Query limit exceeded
# Fix: increase data scan limit or add WHERE clause
```

## Related Errors

- [AWS Glue Error]({{< relref "/cloud/aws/aws-glue-error" >}}) — Glue catalog errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 access errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
