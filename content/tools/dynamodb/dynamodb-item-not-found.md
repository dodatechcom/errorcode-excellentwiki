---
title: "[Solution] DynamoDB Item Not Found - Fix ConditionalCheckFailed"
description: "Fix DynamoDB item not found and ConditionalCheckFailedException errors by adding existence checks, implementing retry logic, and validating condition expression"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB item not found error occurs when a `GetItem`, `UpdateItem`, or `DeleteItem` operation references a key that does not exist. The `ConditionalCheckFailedException` occurs when a condition expression evaluates to false, often because the expected item does not exist.

## What This Error Means

DynamoDB returns different errors depending on the operation. `GetItem` returns empty results without an error, but `UpdateItem` and `DeleteItem` with a condition expression throw `ConditionalCheckFailedException` if the condition is not met. The error includes details about which condition failed.

This is a client-side logic error (HTTP 400) indicating that the application expected data to exist in a certain state but found otherwise.

## Why It Happens

- Race condition: another request deleted or modified the item between read and write
- Item was never created (missing initialization step)
- Condition expression does not match the actual item state
- Using `attribute_exists()` when the item genuinely does not exist
- Wrong partition key or sort key in the request
- Item was moved or archived by a different process
- TTL deleted the item before the operation

## How to Fix It

### 1. Check If Item Exists Before Operating

```python
response = table.get_item(Key={'id': '123'})
if 'Item' not in response:
    # Handle the case where item does not exist
    table.put_item(Item={'id': '123', 'data': 'initial'})
```

### 2. Handle ConditionalCheckFailed Gracefully

```python
from botocore.exceptions import ClientError

try:
    table.update_item(
        Key={'id': '123'},
        UpdateExpression='SET #s = :val',
        ConditionExpression='attribute_exists(id)',
        ExpressionAttributeNames={'#s': 'status'},
        ExpressionAttributeValues={':val': 'updated'}
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        # Item does not exist or condition not met
        table.put_item(Item={'id': '123', 'status': 'created'})
```

### 3. Use PutItem with Condition for Upsert

```python
# Create item only if it does not exist
try:
    table.put_item(
        Item={'id': '123', 'data': 'value'},
        ConditionExpression='attribute_not_exists(id)'
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        # Item already exists, do an update instead
        table.update_item(
            Key={'id': '123'},
            UpdateExpression='SET #d = :val',
            ExpressionAttributeNames={'#d': 'data'},
            ExpressionAttributeValues={':val': 'value'}
        )
```

### 4. Verify Key Values

```python
# Double-check the partition key and sort key
key = {
    'pk': 'correct-value',   # Must match the exact key schema
    'sk': 'correct-value'    # If table has a sort key
}
response = table.get_item(Key=key)
```

### 5. Use TransactWriteItems for Atomic Operations

```python
# Ensure item exists before update in a transaction
client.transact_write_items(
    TransactItems=[
        {
            'Update': {
                'TableName': 'my-table',
                'Key': {'id': '123'},
                'UpdateExpression': 'SET #s = :val',
                'ConditionExpression': 'attribute_exists(id)',
                'ExpressionAttributeNames': {'#s': 'status'},
                'ExpressionAttributeValues': {':val': 'active'}
            }
        }
    ]
)
```

## Common Mistakes

- Not implementing retry logic for race conditions on `ConditionalCheckFailedException`
- Assuming `GetItem` returns an error when the item does not exist (it returns empty)
- Using `attribute_exists()` without understanding that it evaluates to false for missing items
- Not logging the full error response to understand which condition failed

## Related Pages

- [DynamoDB ValidationException](/tools/dynamodb/dynamodb-validation-error)
- [DynamoDB Size Limit](/tools/dynamodb/dynamodb-size-limit)
- [DynamoDB Table Not Found](/tools/dynamodb/dynamodb-table-not-found)
