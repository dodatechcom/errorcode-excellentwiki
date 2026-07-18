---
title: "[Solution] DynamoDB Secondary Index Error - Fix GSI Update Failed"
description: "Fix DynamoDB global secondary index update failures. Resolve GSI limits, throughput, and attribute projection errors."
tools: ["dynamodb"]
error-types: ["secondary-index"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB global secondary index (GSI) could not be created, updated, or queried. GSI operations have strict limits on throughput, projections, and数量.

## What This Error Means

When GSI operations fail, you see:

```
LimitExceededException: Number of GSIs per table exceeded
# or
ValidationException: Global secondary index keys must be a subset
# or
ProvisionedThroughputExceededException: Rate exceeded for index
```

GSIs provide alternate query patterns but consume additional storage and throughput.

## Why It Happens

- The table has reached the 20 GSI limit
- The GSI key schema references attributes not in the base table
- The GSI projection does not include required attributes
- GSI throughput exceeds table provisioned capacity
- The GSI attribute values exceed the 400KB item limit
- Index updates are in progress and the table is backing off

## How to Fix It

### Check existing GSIs

```python
import boto3

dynamodb = boto3.client('dynamodb')
response = dynamodb.describe_table(TableName='my-table')
gsis = response['Table'].get('GlobalSecondaryIndexes', [])
print(f'GSI count: {len(gsis)}')
for gsi in gsis:
    print(f"  - {gsi['IndexName']}: {gsi['KeySchema']}")
```

### Add a new GSI

```python
dynamodb.update_table(
    TableName='my-table',
    GlobalSecondaryIndexUpdates=[
        {'Create': {
            'IndexName': 'new-gsi',
            'KeySchema': [
                {'AttributeName': 'status', 'KeyType': 'HASH'},
                {'AttributeName': 'created_at', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        }}
    ]
)
```

### Check GSI attribute definitions

```python
# All GSI key attributes must be in the base table's AttributeDefinitions
dynamodb.update_table(
    TableName='my-table',
    AttributeDefinitions=[
        {'AttributeName': 'pk', 'AttributeType': 'S'},
        {'AttributeName': 'status', 'AttributeType': 'S'},
        {'AttributeName': 'created_at', 'AttributeType': 'S'}
    ],
    GlobalSecondaryIndexUpdates=[...]
)
```

### Set appropriate projection type

```python
# KEYS_ONLY - only keys, smallest storage
# INCLUDE - keys plus specified attributes
# ALL - all attributes (most storage, most flexible)

'Projection': {
    'ProjectionType': 'INCLUDE',
    'NonKeyAttributes': ['status', 'name', 'email']
}
```

### Delete unused GSIs

```python
dynamodb.update_table(
    TableName='my-table',
    GlobalSecondaryIndexUpdates=[
        {'Delete': {'IndexName': 'unused-gsi'}}
    ]
)
```

### Use on-demand capacity for GSIs

```python
dynamodb.update_table(
    TableName='my-table',
    BillingMode='PAY_PER_REQUEST'
)
```

On-demand mode handles GSI throughput automatically.

## Common Mistakes

- Creating too many GSIs without considering storage costs
- Using `ProjectionType: ALL` when `INCLUDE` would be sufficient
- Not monitoring GSI storage costs
- Forgetting that GSI attributes must be in the base table's AttributeDefinitions
- Deleting a GSI that is still being queried

## Related Pages

- [DynamoDB Query Error]({{< relref "/tools/dynamodb/dynamodb-query-error" >}}) -- query issues
- [DynamoDB Throughput Exceeded]({{< relref "/tools/dynamodb/dynamodb-throughput-exceeded" >}}) -- capacity limits
- [DynamoDB Table Not Found]({{< relref "/tools/dynamodb/dynamodb-table-not-found" >}}) -- table issues
