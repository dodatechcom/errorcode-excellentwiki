---
title: "[Solution] DynamoDB Provisioned Throughput Exceeded Error — How to Fix"
description: "Fix DynamoDB ProvisionedThroughputExceededException by adjusting read/write capacity, implementing throttling retry logic, using on-demand mode, or adding exponential backoff."
tools: ["dynamodb"]
error-types: ["throughput-error"]
severities: ["error"]
weight: 5
comments: true
---

A `ProvisionedThroughputExceededException` occurs when your application sends more read or write requests to a DynamoDB table than the provisioned capacity allows. The request is throttled and returns a 400 HTTP status code.

## What This Error Means

DynamoDB enforces throughput limits at the table and partition level. When you exceed your provisioned read capacity units (RCUs) or write capacity units (WCUs), DynamoDB rejects the request with `ProvisionedThroughputExceededException`. The error can occur even if the total table throughput is not exhausted, because a single partition may be hot and hitting its own limit of 3000 RCUs or 1000 WCUs.

Unlike `ResourceNotFoundException` or `AccessDeniedException`, this error signals a capacity planning problem rather than a permissions or existence issue.

## Why It Happens

- Your application is sending more traffic than the table's provisioned RCUs or WCUs
- A single partition is receiving a disproportionate amount of traffic (hot partition)
- Burst capacity has been exhausted after idle periods
- A GSI (Global Secondary Index) has lower provisioned capacity than the base table
- The table is in provisioned mode and on-demand bursting is not available
- A time-based workload spike exceeds the configured capacity
- An inefficient query or scan is consuming excessive read capacity

## Common Error Messages

```
ProvisionedThroughputExceededException: The level of configured provisioned throughput for the table was exceeded.
# or
The level of configured provisioned throughput for the global secondary index was exceeded.
# or
The request rate for this table is too high. Reduce your request rate and use exponential backoff.
# or
Throughput exceeds the current throughput limit for the partition. Increase partition throughput.
```

## How to Fix It

### 1. Increase Provisioned Capacity

```bash
aws dynamodb update-table \
    --table-name my-table \
    --provisioned-throughput ReadCapacityUnits=50,WriteCapacityUnits=50
```

Use the AWS Management Console or CLI to adjust the table's RCU and WCU values. Monitor CloudWatch metrics to determine the required capacity.

### 2. Switch to On-Demand Mode

```bash
aws dynamodb update-table \
    --table-name my-table \
    --billing-mode PAY_PER_REQUEST
```

On-demand mode eliminates capacity planning and scales automatically. Use it for unpredictable workloads, new applications, or spiky traffic patterns.

### 3. Implement Exponential Backoff

```python
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
import time

config = Config(retries={'max_attempts': 10, 'mode': 'adaptive'})
client = boto3.client('dynamodb', config=config)

def retry_put_item(table_name, item):
    for attempt in range(10):
        try:
            client.put_item(TableName=table_name, Item=item)
            return
        except ClientError as e:
            if e.response['Error']['Code'] == 'ProvisionedThroughputExceededException':
                wait = min(2 ** attempt, 30)
                time.sleep(wait + random.random())
            else:
                raise
```

### 4. Distribute Traffic Across Partitions

```python
# Add a shard key to distribute writes evenly
import hashlib, random

def get_sharded_partition_key(base_key, shard_count=10):
    shard = random.randint(0, shard_count - 1)
    return f"{base_key}#{shard}"

item = {
    'pk': {'S': get_sharded_partition_key('user_123')},
    'data': {'S': 'value'}
}
```

### 5. Optimize Read Patterns with Parallel Scan

```bash
aws dynamodb scan \
    --table-name my-table \
    --total-segments 4 \
    --segment 0
```

Run parallel scan operations across multiple segments to distribute read load. Each segment processes a distinct subset of the data.

### 6. Use DynamoDB Accelerator (DAX)

```bash
aws dynamodb create-cluster \
    --cluster-name my-dax-cluster \
    --node-type dax.r5.large \
    --replication-factor 3
```

DAX provides in-memory caching that reduces read load on your DynamoDB tables. It can absorb spikes and reduce throttling for read-heavy workloads.

## Common Scenarios

### Sudden Traffic Spike During a Launch

You deploy a new feature and traffic to a specific table increases 10x within minutes. The provisioned capacity is insufficient, causing widespread throttling. The solution is to pre-warm the table by gradually increasing capacity before the launch, or use on-demand mode.

### Hot Partition in a Gaming Leaderboard

A gaming application uses a leaderboard table where the "global" partition key receives all read and write traffic. Despite the table having high total capacity, a single partition is throttled. The fix is to redesign the partition key to distribute traffic across multiple partitions.

### GSI Throttling Due to Uneven Write Distribution

A Global Secondary Index on a low-cardinality attribute causes write throttling. The base table handles writes fine, but the GSI cannot keep up because writes to the index are concentrated on a few values. Increase the GSI's provisioned capacity or redesign the index key.

## Prevent It

- Use on-demand billing mode for unpredictable or spiky workloads
- Design partition keys with high cardinality and uniform access patterns
- Monitor CloudWatch metrics for `ThrottledRequests` and `ConsumedReadCapacityUnits`
- Set up CloudWatch alarms to notify when consumed capacity exceeds 80% of provisioned capacity
- Implement client-side throttling with exponential backoff and jitter
- Pre-warm tables before expected traffic spikes by gradually increasing capacity
- Use DAX to cache frequently accessed data and reduce read load
- Review and optimize table and GSI throughput configuration regularly

## Related Pages

- [DynamoDB Item Size Error](/tools/dynamodb/dynamodb-item-size-error)
- [DynamoDB Conditional Check Error](/tools/dynamodb/dynamodb-condcheck-error)
- [DynamoDB Type Mismatch Error](/tools/dynamodb/dynamodb-type-error)
