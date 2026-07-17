---
title: "[Solution] DynamoDB Throughput Exceeded - Fix Read Write Capacity"
description: "Fix DynamoDB throughput exceeded errors by enabling application auto-scaling policies, switching to on-demand PAY_PER_REQUEST billing mode, or using DAX caching"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB throughput exceeded error occurs when the combined read or write capacity consumption exceeds the provisioned or on-demand limits. The error may manifest as `ProvisionedThroughputExceededException` for provisioned mode or `RequestLimitExceeded` for on-demand mode.

## What This Error Means

DynamoDB capacity is measured at the partition level. Even if your table-level capacity appears sufficient, individual partitions can become hot and exceed their throughput share. In provisioned mode, you pay for reserved capacity and are throttled when you exceed it. In on-demand mode, DynamoDB scales automatically but has burst limits.

The error includes details about which capacity (read or write) was exceeded and for which table or index.

## Why It Happens

- Traffic exceeds provisioned capacity
- Hot partition key causing uneven distribution
- Large items consuming more capacity units than expected
- BatchGetItem or BatchWriteItem exceeding single-request limits
- Scan or Query operations consuming excessive RCU
- Global secondary indexes consuming separate write capacity
- Sudden traffic spike beyond burst capacity

## How to Fix It

### 1. Enable Auto-Scaling

```python
application_autoscaling = boto3.client('application-autoscaling')

# Register the table as a scalable target
application_autoscaling.register_scalable_target(
    ServiceNamespace='dynamodb',
    ResourceId=f'table/my-table',
    ScalableDimension='dynamodb:table:ReadCapacityUnits',
    MinCapacity=5,
    MaxCapacity=1000
)

# Create a scaling policy
application_autoscaling.put_scaling_policy(
    PolicyName='read-auto-scaling',
    ServiceNamespace='dynamodb',
    ResourceId=f'table/my-table',
    ScalableDimension='dynamodb:table:ReadCapacityUnits',
    TargetTrackingScalingPolicyConfiguration={
        'TargetValue': 70.0,
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'
        }
    }
)
```

### 2. Switch to On-Demand Mode

```python
client = boto3.client('dynamodb')
client.update_table(
    TableName='my-table',
    BillingMode='PAY_PER_REQUEST'
)
```

### 3. Use DAX for Read Caching

```python
# DAX reduces read load by serving cached responses
from amazondax import AmazonDaxClient

dax = AmazonDaxClient(
    endpoints=['my-cluster.abc123.dax-clusters.us-east-1.amazonaws.com:8111'],
    region_name='us-east-1'
)
table = dax.Table('my-table')
response = table.get_item(Key={'id': '123'})
```

### 4. Distribute Partition Keys

```python
import hashlib

def get_distributed_key(base_key, shard_count=10):
    shard = int(hashlib.md5(base_key.encode()).hexdigest(), 16) % shard_count
    return f"{base_key}#{shard}"
```

### 5. Optimize Read Operations

```python
# Instead of Scan, use Query with an index
response = table.query(
    IndexName='status-index',
    KeyConditionExpression=Key('status').eq('active')
)

# Use ProjectionExpression to read only needed attributes
response = table.get_item(
    Key={'id': '123'},
    ProjectionExpression='id, name, #s',
    ExpressionAttributeNames={'#s': 'status'}
)
```

### 6. Use Sparse Indexes

```sql
-- Create a GSI on an attribute that only some items have
-- This reduces the index size and improves query efficiency
```

## Common Mistakes

- Not monitoring CloudWatch metrics for consumed vs. provisioned capacity
- Assuming on-demand mode eliminates all throttling (burst limits still apply)
- Not accounting for GSI and LSI capacity in throughput calculations
- Using Scan operations in production instead of Query with proper indexes

## Related Pages

- [DynamoDB ProvisionedThroughputExceededException](/tools/dynamodb/dynamodb-provisioned-exceeded)
- [DynamoDB Access Denied](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Backup Error](/tools/dynamodb/dynamodb-backup-error)
