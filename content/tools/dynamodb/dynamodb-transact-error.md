---
title: "[Solution] DynamoDB Transact Error - Fix TransactionCanceledException"
description: "Fix DynamoDB TransactionCanceledException when transactions fail. Resolve condition checks, conflicts, and transaction limits."
tools: ["dynamodb"]
error-types: ["transact-error"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB transaction was canceled. Transactions are all-or-nothing operations, and if any item fails, the entire transaction is rolled back.

## What This Error Means

When a transaction fails, you see:

```
TransactionCanceledException: Transaction cancelled, reason: ConditionalCheckFailed
# or
TransactionCanceledException: One or more parameter values were invalid
# or
TransactionCanceledException: Transaction request cannot be processed
```

DynamoDB transactions support up to 25 items across multiple tables. Any failure cancels all operations.

## Why It Happens

- A condition check in a TransactWriteItems failed
- An item in the transaction was modified by another request
- One of the items exceeds the 400KB size limit
- The transaction references more than 25 items
- A required key attribute is missing from the request
- The table does not exist or is not active

## How to Fix It

### Handle ConditionalCheckFailed

```python
import boto3
import time

dynamodb = boto3.client('dynamodb')

def transact_write_with_retry(items, max_retries=5):
    for attempt in range(max_retries):
        try:
            return dynamodb.transact_write_items(TransactItems=items)
        except dynamodb.exceptions.TransactionCanceledException as e:
            if 'ConditionalCheckFailed' in str(e):
                time.sleep(2 ** attempt)
                continue
            raise
```

### Reduce transaction scope

```python
# Instead of 25 items, batch in smaller groups
for i in range(0, len(items), 10):
    batch = items[i:i+10]
    dynamodb.transact_write_items(TransactItems=batch)
```

### Use fewer condition checks

```python
# Complex condition - more likely to fail
condition = 'attribute_exists(pk) AND #status = :expected'

# Simpler condition - less contention
condition = 'attribute_exists(pk)'
```

### Verify all items exist

```python
# TransactGetItems to verify before writing
response = dynamodb.transact_get_items(
    TransactItems=[
        {'Get': {'Key': {'pk': {'S': 'key1'}}, 'TableName': 'table1'}},
        {'Get': {'Key': {'pk': {'S': 'key2'}}, 'TableName': 'table2'}}]
)
```

### Check for item size limits

```python
for item in items:
    item_size = len(str(item).encode('utf-8'))
    if item_size > 400000:
        print(f'Item too large for transaction: {item_size}')
```

### Use Put with condition for idempotent writes

```python
dynamodb.transact_write_items(
    TransactItems=[
        {'Put': {
            'TableName': 'my-table',
            'Item': {'pk': {'S': 'key1'}, 'data': {'S': 'value'}},
            'ConditionExpression': 'attribute_not_exists(pk)'
        }}
    ]
)
```

### Increase provisioned capacity

```python
dynamodb.update_table(
    TableName='my-table',
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)
```

## Common Mistakes

- Not retrying transactions that fail due to contention
- Using transactions when conditional writes would suffice
- Including too many items in a single transaction
- Not checking item sizes before including them in transactions
- Assuming transactions are faster than individual writes

## Related Pages

- [DynamoDB Throughput Exceeded]({{< relref "/tools/dynamodb/dynamodb-throughput-exceeded" >}}) -- capacity limits
- [DynamoDB Validation Error]({{< relref "/tools/dynamodb/dynamodb-validation-error" >}}) -- validation issues
- [DynamoDB Item Not Found]({{< relref "/tools/dynamodb/dynamodb-item-not-found" >}}) -- missing items
