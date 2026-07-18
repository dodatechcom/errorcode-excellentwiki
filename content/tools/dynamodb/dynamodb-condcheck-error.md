---
title: "[Solution] DynamoDB Conditional Check Failed Error — How to Fix"
description: "Fix DynamoDB ConditionalCheckFailedException by debugging condition expressions, verifying attribute existence, fixing type mismatches, and using idempotent write operations."
tools: ["dynamodb"]
error-types: ["condcheck-error"]
severities: ["error"]
weight: 5
comments: true
---

A `ConditionalCheckFailedException` occurs when a `PutItem`, `UpdateItem`, or `DeleteItem` operation includes a condition expression that evaluates to false. The operation is rejected and the item is not modified.

## What This Error Means

DynamoDB condition expressions let you perform write operations only when specific conditions are met. Common use cases include optimistic locking, preventing overwrites, and ensuring attributes have expected values. When the condition is not satisfied, DynamoDB throws `ConditionalCheckFailedException` and the write is not applied.

This is not a data corruption error. It is a signal that the current state of the item does not match the expected preconditions. The operation must be retried with updated data after re-reading the item.

## Why It Happens

- The item does not exist when the condition expects it to exist
- The item already exists when using `attribute_not_exists` for idempotent inserts
- An attribute value does not match the expected value in the condition
- Concurrent updates from multiple clients cause optimistic locking failures
- The condition expression references attributes that do not exist on the item
- The condition expression has a syntax error or type mismatch
- Transactional write operations have conflicting conditions

## Common Error Messages

```
ConditionalCheckFailedException: The conditional request failed
# or
The conditional request failed because the item does not exist
# or
ConditionalCheckFailed: Attempted a condition on a non-existent attribute
# or
TransactionCanceledException: ConditionalCheckFailed - Item with key already exists
```

## How to Fix It

### 1. Use attribute_not_exists for Idempotent Creates

```python
import boto3
from botocore.exceptions import ClientError

client = boto3.client('dynamodb')

def create_item_if_not_exists(table_name, item):
    try:
        client.put_item(
            TableName=table_name,
            Item=item,
            ConditionExpression='attribute_not_exists(pk)'
        )
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return False  # Item already exists
        raise
```

### 2. Implement Optimistic Locking with Version Numbers

```python
import boto3

client = boto3.client('dynamodb')

def update_with_version(table_name, key, updates, expected_version):
    try:
        update_expr = 'SET #data = :data, #version = :new_version'
        expr_attr_names = {'#data': 'data', '#version': 'version'}
        expr_attr_values = {
            ':data': {'S': updates['data']},
            ':new_version': {'N': str(expected_version + 1)},
            ':expected_version': {'N': str(expected_version)}
        }
        
        client.update_item(
            TableName=table_name,
            Key=key,
            UpdateExpression=update_expr,
            ConditionExpression='#version = :expected_version',
            ExpressionAttributeNames=expr_attr_names,
            ExpressionAttributeValues=expr_attr_values
        )
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return False  # Stale version
        raise
```

### 3. Check Attribute Existence with attribute_exists

```python
# Only update if the item already exists
client.update_item(
    TableName='my-table',
    Key={'pk': {'S': 'user#123'}},
    UpdateExpression='SET #status = :status',
    ConditionExpression='attribute_exists(pk)',
    ExpressionAttributeNames={'#status': 'status'},
    ExpressionAttributeValues={':status': {'S': 'active'}}
)
```

### 4. Debug Condition Expressions Locally

```python
import boto3

client = boto3.client('dynamodb')

# Read the current item first to verify state
response = client.get_item(
    TableName='my-table',
    Key={'pk': {'S': 'user#123'}}
)
item = response.get('Item', {})
print(f"Current item: {item}")
print(f"Current status: {item.get('status', {}).get('S')}")

# Now craft the condition based on actual state
# If status should be 'pending', condition must match
```

### 5. Use TransactWriteItems with Idempotency Token

```python
import boto3
import uuid

client = boto3.client('dynamodb')

def transactional_create(table_name, item):
    token = str(uuid.uuid4())
    try:
        client.transact_write_items(
            TransactItems=[{
                'Put': {
                    'TableName': table_name,
                    'Item': item,
                    'ConditionExpression': 'attribute_not_exists(pk)'
                }
            }],
            ClientRequestToken=token
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'TransactionCanceledException':
            # Check nested reasons
            pass
```

### 6. Retry with Updated Data

```python
import time
import random

def retry_on_condition_failure(table_name, key, update_fn, max_retries=3):
    for attempt in range(max_retries):
        try:
            return update_fn()
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                if attempt == max_retries - 1:
                    raise
                time.sleep(random.uniform(0.1, 0.5))
                # Re-read item and recompute update
            else:
                raise
```

## Common Scenarios

### Concurrent Inventory Updates in E-Commerce

Two users simultaneously attempt to purchase the last item in stock. Both requests read the inventory count as 1, and both try to decrement it with `SET #count = #count - :dec` conditioned on `#count > :zero`. One succeeds and the other gets `ConditionalCheckFailedException`. The second user must retry and will see the count is now 0.

### Duplicate User Registration

A signup API uses `attribute_not_exists(email)` to prevent duplicate registrations. A race condition causes two simultaneous requests for the same email. The first succeeds, the second gets `ConditionalCheckFailedException`. The application returns a proper "already registered" response.

### Stale Cache Updates

A background job reads a DynamoDB item, processes it, and writes the result back with a version check. If the item was updated by another process between read and write, the condition fails. The job re-reads the updated item and retries the processing with fresh data.

## Prevent It

- Always use `attribute_not_exists` for idempotent create operations
- Implement optimistic locking using a version number attribute
- Handle `ConditionalCheckFailedException` gracefully with proper error responses
- Read the current item state before crafting condition expressions
- Use retry logic with exponential backoff for concurrent update scenarios
- Use `TransactWriteItems` with `ClientRequestToken` for idempotent transactions
- Log condition expression details when debugging failures
- Keep condition expressions simple and test them against sample data

## Related Pages

- [DynamoDB Provisioned Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
- [DynamoDB Item Size Error](/tools/dynamodb/dynamodb-item-size-error)
- [DynamoDB Type Mismatch Error](/tools/dynamodb/dynamodb-type-error)
