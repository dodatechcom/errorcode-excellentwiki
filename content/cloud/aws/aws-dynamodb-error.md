---
title: "[Solution] AWS DynamoDB Query Error"
description: "Fix AWS DynamoDB query errors. Resolve DynamoDB access and query issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "dynamodb", "query", "table", "database"]
weight: 5
---

An AWS DynamoDB query error occurs when operations on DynamoDB tables fail. This can be caused by table configuration, permission, or query issues.

## Common Causes

- Table does not exist or wrong region
- Query does not match table's primary key schema
- IAM permissions not granted for dynamodb actions
- Provisioned throughput exceeded (throttling)
- Item size exceeds 400KB limit

## How to Fix

### Check Table Status

```bash
aws dynamodb describe-table --table-name my-table
```

### Scan Table

```bash
aws dynamodb scan --table-name my-table --limit 10
```

### Query with Correct Key

```bash
aws dynamodb query \
  --table-name my-table \
  --key-condition-expression "pk = :pk" \
  --expression-attribute-values '{":pk": {"S": "user-123"}}'
```

### Check Throughput

```bash
aws dynamodb describe-table --table-name my-table \
  --query 'Table.ProvisionedThroughput'
```

### Enable Auto Scaling

```bash
aws application-autoscaling register-scalable-target \
  --service-namespace dynamodb \
  --scalable-dimension dynamodb:table:ReadCapacityUnits \
  --resource-id table/my-table \
  --min-capacity 5 --max-capacity 1000
```

## Examples

```bash
# Example 1: Table not found
# ResourceNotFoundException: Requested resource not found
# Fix: check table name and region

# Example 2: Throttling
# ProvisionedThroughputExceededException
# Fix: use exponential backoff or increase capacity
```

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS connection error
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
