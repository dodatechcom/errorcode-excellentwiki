---
title: "[Solution] DynamoDB BatchWrite Error - Fix BatchWriteItem Unprocessed Items"
description: "Fix DynamoDB BatchWriteItem unprocessed items errors. Handle throttling, retry logic, and batch size limits for batch writes."
tools: ["dynamodb"]
error-types: ["batch-write-error"]
severities: ["error"]
weight: 5
---

This error means DynamoDB could not process all items in a BatchWriteItem request. Some items were returned as unprocessed due to throttling or capacity limits.

## What This Error Means

When a batch write is partially processed, DynamoDB returns:

```
ProvisionedThroughputExceededException: Throughput exceeded
# or
UnprocessedItems: {'my-table': [{'PutRequest': {'Item': {...}}}]}
```

DynamoDB may return some items as unprocessed when write capacity is exhausted during the batch. You must retry these items.

## Why It Happens

- The batch size exceeds 25 items (DynamoDB limit)
- The total request size exceeds 16MB
- Write capacity is throttled during the batch
- Items exceed the 400KB individual item size limit
- Conditional writes fail for some items in the batch
- The table is under heavy write load

## How to Fix It

### Implement retry logic for unprocessed items

```python
import boto3
import time

dynamodb = boto3.client('dynamodb')

def batch_write_with_retry(requests):
    response = dynamodb.batch_write_item(RequestItems=requests)
    
    while response['UnprocessedItems']:
        time.sleep(1)
        response = dynamodb.batch_write_item(
            RequestItems=response['UnprocessedItems']
        )
    
    return response
```

### Batch in groups of 25

```python
def write_items(table_name, items):
    for i in range(0, len(items), 25):
        batch = items[i:i+25]
        requests = {
            table_name: [{'PutRequest': {'Item': item}} for item in batch]
        }
        batch_write_with_retry(requests)
```

### Use DynamoDB resource for easier batching

```python
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
```

The `batch_writer` handles retries and batching automatically.

### Increase write capacity

```python
dynamodb.update_table(
    TableName='my-table',
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)
```

### Use on-demand capacity

```python
dynamodb.update_table(
    TableName='my-table',
    BillingMode='PAY_PER_REQUEST'
)
```

On-demand mode handles burst capacity without throttling.

### Check individual item sizes

```python
import sys

for item in items:
    size = sys.getsizeof(str(item))
    if size > 400000:  # 400KB limit
        print(f'Item too large: {size} bytes')
```

### Use conditional writes carefully

```python
dynamodb.put_item(
    TableName='my-table',
    Item={'pk': {'S': 'key1'}, 'data': {'S': 'value'}},
    ConditionExpression='attribute_not_exists(pk)'
)
```

Conditional failures on one item can cause entire batches to fail.

## Common Mistakes

- Not retrying unprocessed items, which causes data loss
- Sending more than 25 items in a single BatchWriteItem
- Not handling individual item size limits
- Using BatchWriteItem when PutItem would be more appropriate for small writes
- Not using the DynamoDB resource batch_writer for automatic retry handling

## Related Pages

- [DynamoDB Throughput Exceeded]({{< relref "/tools/dynamodb/dynamodb-throughput-exceeded" >}}) -- capacity limits
- [DynamoDB Size Limit]({{< relref "/tools/dynamodb/dynamodb-size-limit" >}}) -- item size limits
- [DynamoDB Validation Error]({{< relref "/tools/dynamodb/dynamodb-validation-error" >}}) -- validation issues
