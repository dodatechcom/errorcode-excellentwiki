---
title: "[Solution] DynamoDB Scan Error - Fix Scan Operation Throttled"
description: "Fix DynamoDB scan operation throttling and failures. Use queries instead of scans, add filters, and optimize scan performance."
tools: ["dynamodb"]
error-types: ["scan-error"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB scan operation is being throttled or failing. Scans read every item in a table or index, consuming significant read capacity.

## What This Error Means

When a scan operation fails due to throttling, you see:

```
ProvisionedThroughputExceededException: Rate exceeded
# or
InternalServerError: Internal server error
```

Scans are the most expensive read operation in DynamoDB because they read every item without using an index.

## Why It Happens

- The table is large and the scan consumes more capacity than provisioned
- Multiple concurrent scans are competing for the same capacity
- The scan filter is applied after the scan, wasting read capacity
- The table does not have enough read capacity for the workload
- Auto-scaling has not kicked in during traffic spikes
- The scan is running during peak hours

## How to Fix It

### Replace scans with queries

```python
# Bad: Scan with filter
response = dynamodb.scan(
    TableName='my-table',
    FilterExpression='status = :status',
    ExpressionAttributeValues={':status': {'S': 'active'}}
)

# Good: Query on GSI
response = dynamodb.query(
    TableName='my-table',
    IndexName='status-index',
    KeyConditionExpression='status = :status',
    ExpressionAttributeValues={':status': {'S': 'active'}}
)
```

### Add pagination for large scans

```python
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

items = []
response = table.scan(Limit=100)
items.extend(response['Items'])

while 'LastEvaluatedKey' in response:
    response = table.scan(
        Limit=100,
        ExclusiveStartKey=response['LastEvaluatedKey']
    )
    items.extend(response['Items'])
```

### Use parallel scans for large tables

```python
import boto3
import threading

dynamodb = boto3.client('dynamodb')
total_segments = 10

def scan_segment(segment):
    response = dynamodb.scan(
        TableName='my-table',
        Segment=segment,
        TotalSegments=total_segments
    )
    return response['Items']

threads = [threading.Thread(target=scan_segment, args=(i,)) for i in range(total_segments)]
```

### Increase read capacity or use on-demand

```python
dynamodb.update_table(
    TableName='my-table',
    BillingMode='PAY_PER_REQUEST'
)
```

On-demand mode handles burst capacity automatically.

### Use FilterExpression efficiently

```python
# Only scan items you actually need
response = dynamodb.scan(
    TableName='my-table',
    FilterExpression='begins_with(sk, :prefix)',
    ExpressionAttributeValues={':prefix': {'S': 'user#'}}
)
```

### Create a GSI for common scan patterns

```python
dynamodb.create_table(
    TableName='my-table',
    GlobalSecondaryIndexes=[{
        'IndexName': 'status-index',
        'KeySchema': [
            {'AttributeName': 'status', 'KeyType': 'HASH'},
            {'AttributeName': 'created_at', 'KeyType': 'RANGE'}
        ],
        'Projection': {'ProjectionType': 'ALL'},
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }]
)
```

## Common Mistakes

- Using scans as the default read operation instead of queries
- Not filtering before scanning, wasting read capacity
- Not paginating large scans, causing timeouts
- Not creating GSIs for frequently filtered attributes
- Running scans during peak hours without throttling protection

## Related Pages

- [DynamoDB Query Error]({{< relref "/tools/dynamodb/dynamodb-query-error" >}}) -- query issues
- [DynamoDB Throughput Exceeded]({{< relref "/tools/dynamodb/dynamodb-throughput-exceeded" >}}) -- capacity limits
- [DynamoDB Provisioned Exceeded]({{< relref "/tools/dynamodb/dynamodb-provisioned-exceeded" >}}) -- provisioned capacity
