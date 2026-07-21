---
title: "[Solution] AWS DynamoDB Throughput Exceeded"
description: "ProvisionedThroughputExceededException when capacity is consumed."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DynamoDB Throughput Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Provisioned capacity insufficient
- Hot partition consuming too much
- Large items consume more RCU/WCU
- Auto-scaling not yet active

## How to Fix

### Check throughput

```bash
aws dynamodb describe-table --table-name my-table --query Table.ProvisionedThroughput
```
### Increase throughput

```bash
aws dynamodb update-table --table-name my-table --provisioned-throughput ReadCapacityUnits=100,WriteCapacityUnits=100
```
### Enable auto-scaling

```bash
aws application-autoscaling register-scalable-target --service-namespace dynamodb --scalable-dimension dynamodb:table:ReadCapacityUnits --resource-id table/my-table --min-capacity 5 --max-capacity 1000
```

## Examples

- Hot key receiving all writes
- 4 KB items needing 2 RCU worth of data

## Related Errors

- [DynamoDB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General DynamoDB errors
- [Write Capacity]({{< relref "/cloud/aws/aws-dynamodb-write-capacity" >}}) -- Write capacity
