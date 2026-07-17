---
title: "[Solution] DynamoDB ProvisionedThroughputExceededException - Fix Throughput"
description: "Fix DynamoDB ProvisionedThroughputExceededException by adding exponential backoff retry logic, adjusting provisioned capacity, or switching to on-demand billing"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB `ProvisionedThroughputExceededException` occurs when a request exceeds the provisioned read or write capacity units for a table or index. The error has HTTP status code 400 and AWS error code `ProvisionedThroughputExceededException`.

## What This Error Means

DynamoDB measures throughput in read capacity units (RCU) and write capacity units (WCU). When you provision a specific capacity, DynamoDB throttles requests that exceed that capacity. The exception includes the table or index name and whether the read or write capacity was exceeded.

Each RCU represents one strongly consistent read of up to 4KB (or 8KB for eventually consistent reads). Each WCU represents one write of up to 1KB. If your operations are larger, they consume multiple capacity units.

## Why It Happens

- Sudden traffic spike exceeding provisioned capacity
- Hot partition key causing uneven load distribution
- Large item reads consuming more RCU than expected
- Batch operations that consume burst capacity
- GSI or LSI writes consuming separate capacity
- On-demand mode not enabled for unpredictable workloads
- Insufficient provisioned capacity for the actual workload

## How to Fix It

### 1. Enable Exponential Backoff in the SDK

```python
import boto3
from botocore.config import Config

config = Config(
    retries={
        'max_attempts': 10,
        'mode': 'adaptive'
    }
)
dynamodb = boto3.resource('dynamodb', config=config)
```

```javascript
// AWS SDK v3 for JavaScript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
const client = new DynamoDBClient({
    maxAttempts: 10,
    retryMode: "adaptive"
});
```

### 2. Increase Provisioned Capacity

```python
table = dynamodb.Table('my-table')
table.update(
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 50
    }
)
```

### 3. Switch to On-Demand Mode

```python
client = boto3.client('dynamodb')
client.update_table(
    TableName='my-table',
    BillingMode='PAY_PER_REQUEST'
)
```

### 4. Fix Hot Partition Keys

```python
# Instead of using a single partition key like "user"
# Use a composite key with a shard suffix
import random
partition_key = f"user_{user_id}#{random.randint(0, 9)}"
```

### 5. Use DAX for Read Caching

```python
# DynamoDB Accelerator reduces read load on the table
from amazondax import AmazonDaxClient
dax = AmazonDaxClient(
    endpoints=['my-dax-cluster.abc123.dax-clusters.us-east-1.amazonaws.com:8111']
)
```

### 6. Use Batch Operations Efficiently

```python
# BatchWriteItem can handle up to 25 items per call
# and is more efficient than individual PutItem calls
response = dynamodb.batch_write_item(
    RequestItems={
        'my-table': [
            {'PutRequest': {'Item': {'id': str(i), 'data': 'value'}}}
            for i in range(25)
        ]
    }
)
```

## Common Mistakes

- Not implementing retry logic with exponential backoff (the SDK does this automatically in v3 but not always in older versions)
- Provisioning capacity based on average traffic instead of peak traffic
- Ignoring GSI and LSI capacity consumption (they have separate throughput)
- Not using `ConditionalExpression` to prevent duplicate writes that waste WCU

## Related Pages

- [DynamoDB Throughput Exceeded](/tools/dynamodb/dynamodb-throughput-exceeded)
- [DynamoDB Access Denied](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Global Table Error](/tools/dynamodb/dynamodb-global-table-error)
