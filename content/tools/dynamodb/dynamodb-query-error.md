---
title: "[Solution] DynamoDB Query Error - Fix Query Operation Failed"
description: "Fix DynamoDB query operation failures. Resolve key condition errors, scan index forward issues, and throttling during query operations."
tools: ["dynamodb"]
error-types: ["query-error"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB query operation failed. The query may have invalid key conditions, missing required parameters, or the table may be throttled.

## What This Error Means

When a DynamoDB query fails, you see:

```
ValidationException: Query condition missed key schema element: <partition_key>
# or
ProvisionedThroughputExceededException: Rate exceeded
# or
SerializationException: Start of structure or map found where not expected
```

Queries are efficient read operations that must specify the partition key and optionally the sort key.

## Why It Happens

- The partition key is missing from the KeyConditionExpression
- The expression uses the wrong attribute name for the key
- The sort key condition is malformed
- The table is throttled due to provisioned capacity limits
- The index name is incorrect
- The expression values or names are not properly formatted

## How to Fix It

### Verify the key condition includes partition key

```python
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ExpressionAttributeValues={
        ':pk': {'S': 'user-123'}
    }
)
```

### Check table key schema

```python
client = boto3.client('dynamodb')
table = client.describe_table(TableName='my-table')
print(table['Table']['KeySchema'])
```

Ensure you are using the correct partition and sort key attribute names.

### Use expression names for reserved words

```python
response = dynamodb.query(
    TableName='my-table',
    KeyConditionExpression='#pk = :pk',
    ExpressionAttributeNames={'#pk': 'partition-key'},
    ExpressionAttributeValues={':pk': {'S': 'value'}}
)
```

### Handle throttling with exponential backoff

```python
import time
import random

def query_with_backoff(table, key_condition, max_retries=5):
    for attempt in range(max_retries):
        try:
            return table.query(KeyConditionExpression=key_condition)
        except client.exceptions.ProvisionedThroughputExceededException:
            time.sleep(2 ** attempt + random.uniform(0, 1))
    raise Exception('Max retries exceeded')
```

### Query an index instead of the table

```python
response = dynamodb.query(
    TableName='my-table',
    IndexName='gsi-index',
    KeyConditionExpression='gsi_pk = :pk',
    ExpressionAttributeValues={':pk': {'S': 'value'}}
)
```

### Use ScanIndexForward for sort key ordering

```python
response = dynamodb.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk AND sk BETWEEN :start AND :end',
    ScanIndexForward=False,  # Descending order
    ExpressionAttributeValues={
        ':pk': {'S': 'user-123'},
        ':start': {'S': '2024-01-01'},
        ':end': {'S': '2024-12-31'}
    }
)
```

### Increase provisioned capacity

```python
client.update_table(
    TableName='my-table',
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)
```

## Common Mistakes

- Forgetting that queries must always include the partition key
- Using ScanIndexForward in the wrong direction
- Not handling throttling with retry logic
- Querying the table instead of using an available GSI
- Confusing query (efficient) with scan (reads entire table)

## Related Pages

- [DynamoDB Scan Error]({{< relref "/tools/dynamodb/dynamodb-scan-error" >}}) -- scan operation issues
- [DynamoDB Throughput Exceeded]({{< relref "/tools/dynamodb/dynamodb-throughput-exceeded" >}}) -- capacity limits
- [DynamoDB Item Not Found]({{< relref "/tools/dynamodb/dynamodb-item-not-found" >}}) -- missing items
