---
title: "[Solution] DynamoDB Global Table Error - Fix Multi-Region Replication"
description: "Fix DynamoDB global table replication errors by enabling DynamoDB Streams, resolving cross-region write conflicts, and verifying cross-region IAM permissions se"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB global table error occurs when replication between regions fails or when operations on a global table encounter conflicts. The error may appear as `ReplicaNotFoundException`, `GlobalTableNotFoundException`, or replication lag warnings in CloudWatch.

## What This Error Means

DynamoDB global tables provide multi-region, multi-active replication. Changes written to one replica are automatically propagated to other replicas via DynamoDB Streams. When replication fails, items may become inconsistent across regions, and reads from a replica may return stale data.

The error types include `ReplicaNotFoundException` (a replica was removed), `GlobalTableNotFoundException` (the global table configuration is missing), and various stream-related errors.

## Why It Happens

- DynamoDB Streams is not enabled on the table (required for global tables)
- IAM role lacks permission to write to the replica region
- Replica was deleted or is in a `CREATING` or `DELETING` state
- Conflicting writes to the same item in multiple regions (last-write-wins)
- Replication lag due to network issues or high write throughput
- Table class mismatch between replica regions
- AWS account does not have access to the replica region

## How to Fix It

### 1. Verify Global Table Configuration

```bash
aws dynamodb describe-global-table --global-table-name my-table
```

### 2. Enable DynamoDB Streams

```python
client = boto3.client('dynamodb')
client.update_table(
    TableName='my-table',
    StreamSpecification={
        'StreamEnabled': True,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    }
)
```

### 3. Check Replica Status

```python
response = client.describe_global_table(GlobalTableName='my-table')
for replica in response['GlobalTableDescription']['Replicas']:
    print(f"Region: {replica['RegionName']}, Status: {replica['ReplicaStatus']}")
```

### 4. Create a New Replica

```python
client.update_global_table(
    GlobalTableName='my-table',
    ReplicaUpdates=[
        {
            'Create': {
                'RegionName': 'eu-west-1'
            }
        }
    ]
)
```

### 5. Verify IAM Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:BatchWriteItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/my-table"
        }
    ]
}
```

### 6. Handle Write Conflicts

```python
# Use conditional writes to prevent unintended overwrites
try:
    table.put_item(
        Item={
            'id': '123',
            'region': 'us-east-1',
            'data': 'value',
            'version': 1
        },
        ConditionExpression='attribute_not_exists(version) OR version < :ver',
        ExpressionAttributeValues={':ver': 1}
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        # Handle conflict - another region wrote first
        pass
```

## Common Mistakes

- Not enabling DynamoDB Streams before creating a global table
- Assuming global tables handle all conflict resolution automatically (last-write-wins by default)
- Not monitoring replication lag in CloudWatch
- Using a table class (e.g., STANDARD_IA) that is not supported for global tables in all regions

## Related Pages

- [DynamoDB ProvisionedThroughputExceededException](/tools/dynamodb/dynamodb-provisioned-exceeded)
- [DynamoDB Access Denied](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Backup Error](/tools/dynamodb/dynamodb-backup-error)
