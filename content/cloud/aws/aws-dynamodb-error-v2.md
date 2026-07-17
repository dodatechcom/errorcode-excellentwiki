---
title: "[Solution] AWS DynamoDB — ProvisionedThroughputExceededException"
description: "Fix AWS DynamoDB ProvisionedThroughputExceededException. Resolve DynamoDB throttling and capacity issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A ProvisionedThroughputExceededException means the DynamoDB table or index has exceeded its provisioned read or write capacity units. DynamoDB throttles requests that exceed the allocated throughput.

## What This Error Means

DynamoDB tables can run in Provisioned or On-Demand capacity mode. In Provisioned mode, you specify read capacity units (RCUs) and write capacity units (WCUs). When request volume exceeds these limits, DynamoDB returns `ProvisionedThroughputExceededException`. Each partition has its own throughput limit, so hot partitions can cause throttling even when total table capacity is not exceeded. The error includes `RequestItems` showing which tables/indexes were throttled.

## Common Causes

- Table provisioned capacity too low for actual workload
- Hot partition (one partition receiving disproportionate traffic)
- Large item reads consuming more RCUs than expected
- Batch operations exceeding single-request capacity
- GSI (Global Secondary Index) writes consuming write capacity
- Sudden traffic spike exceeding provisioned limits

## How to Fix

### Check Table Capacity

```bash
aws dynamodb describe-table --table-name my-table \
  --query 'Table.[ProvisionedThroughput,CapacityMode]'
```

### Monitor Consumed Capacity

```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/DynamoDB \
  --metric-name ConsumedReadCapacityUnits \
  --dimensions Name=TableName,Value=my-table \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-01T01:00:00Z \
  --period 60 \
  --statistics Sum
```

### Increase Provisioned Capacity

```bash
aws dynamodb update-table \
  --table-name my-table \
  --provisioned-throughput ReadCapacityUnits=100,WriteCapacityUnits=50
```

### Switch to On-Demand Mode

```bash
aws dynamodb update-table \
  --table-name my-table \
  --billing-mode PAY_PER_REQUEST
```

### Use Exponential Backoff

```python
import boto3
from botocore.config import Config

config = Config(
    retries=dict(
        max_attempts=10,
        mode='adaptive'
    )
)
dynamodb = boto3.resource('dynamodb', config=config)
table = dynamodb.Table('my-table')
table.get_item(Key={'id': '123'})
```

### Enable Auto-Scaling

```bash
aws application-autoscaling register-scalable-target \
  --service-namespace dynamodb \
  --resource-id table/my-table \
  --scalable-dimension dynamodb:table:ReadCapacityUnits \
  --min-capacity 10 --max-capacity 1000
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
- [AWS DynamoDB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) — original DynamoDB error
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
