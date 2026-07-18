---
title: "[Solution] DynamoDB Global Table Replication Error — How to Fix"
description: "Fix DynamoDB global table replication errors by resolving conflicts, checking region connectivity, verifying IAM roles, monitoring replication lag, and handling schema changes."
tools: ["dynamodb"]
error-types: ["global-table-error"]
severities: ["error"]
weight: 5
comments: true
---

A global table replication error occurs when DynamoDB global tables experience conflicts, replication lag, or configuration failures that prevent data from synchronizing across AWS regions. These issues can cause data inconsistency and application errors.

## What This Error Means

DynamoDB global tables provide multi-region, multi-master replication. When you write to a table in one region, DynamoDB automatically replicates the data to all other replica regions. Replication errors can occur due to network issues, IAM misconfiguration, conflicting writes, or schema mismatches between replicas.

The error manifests as stale data in some regions, replication lag warnings, or explicit error messages from DynamoDB Streams that power the replication process.

## Why It Happens

- Network connectivity issues between AWS regions
- IAM roles used for replication lack sufficient permissions
- Conflicting writes to the same item in different regions (last-writer-wins conflicts)
- Schema changes applied to one replica but not others
- DynamoDB Streams is not enabled on the source table
- Replica table is deleted or in a DELETING state
- Cross-region replication limits (eventual consistency, ~1 second lag SLA)
- Throttling on the replica table in the destination region

## Common Error Messages

```
Global table replication failed: Replication group update in progress
# or
An error occurred while replicating data to region us-west-2
# or
Replication is delayed due to insufficient write capacity in the replica region
# or
GlobalTableNotFoundException: The specified global table does not exist
```

## How to Fix It

### 1. Check Global Table Status

```bash
aws dynamodb describe-global-table \
    --global-table-name my-global-table

aws dynamodb describe-global-table-settings \
    --global-table-name my-global-table
```

Verify all replica regions are in `ACTIVE` status. Replicas in `CREATING`, `UPDATING`, or `DELETING` states cannot process replication.

### 2. Verify IAM Roles for Replication

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:DescribeStream",
                "dynamodb:ListStreams"
            ],
            "Resource": "arn:aws:dynamodb:*:123456789012:table/my-table/stream/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": "arn:aws:dynamodb:*:123456789012:table/my-table"
        }
    ]
}
```

The DynamoDB service-linked role must have permissions to read from the source stream and write to all replica tables.

### 3. Monitor Replication Lag

```bash
# CloudWatch metric: ReplicationLatency
aws cloudwatch get-metric-statistics \
    --namespace AWS/DynamoDB \
    --metric-name ReplicationLatency \
    --dimensions Name=TableName,Value=my-table \
    --start-time $(date -u -d '-1 hour' +%Y-%m-%dT%H:%M:%SZ) \
    --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) \
    --period 300 \
    --statistics Average
```

High replication lag indicates the replica table cannot keep up with the write rate. Increase write capacity on the replica table or switch to on-demand billing.

### 4. Handle Write Conflicts

```python
import boto3
from datetime import datetime

client = boto3.client('dynamodb')

# Global tables use last-writer-wins conflict resolution
# To handle conflicts, include a timestamp attribute

def write_with_timestamp(table_name, key, data):
    timestamp = datetime.utcnow().isoformat()
    data['last_updated'] = {'S': timestamp}
    
    client.put_item(
        TableName=table_name,
        Item={**key, **data}
    )

# When reading, check for the most recent timestamp
def read_with_latest_timestamp(table_name, key):
    response = client.get_item(
        TableName=table_name,
        Key=key,
        ConsistentRead=True
    )
    return response.get('Item')
```

### 5. Add a Replica Region

```bash
aws dynamodb update-global-table \
    --global-table-name my-global-table \
    --replica-updates '[{"Create": {"RegionName": "eu-west-1"}}]'
```

Adding replicas requires DynamoDB Streams to be enabled. The operation is asynchronous and may take several minutes to complete.

### 6. Remove and Re-add a Stuck Replica

```bash
# Remove the problematic replica
aws dynamodb update-global-table \
    --global-table-name my-global-table \
    --replica-updates '[{"Delete": {"RegionName": "us-west-2"}}]'

# Wait for deletion to complete, then re-add
aws dynamodb update-global-table \
    --global-table-name my-global-table \
    --replica-updates '[{"Create": {"RegionName": "us-west-2"}}]'
```

### 7. Check Stream Settings on Source Table

```bash
aws dynamodb describe-table \
    --table-name my-table \
    --query 'Table.StreamSpecification'

# Should show:
# {
#     "StreamEnabled": true,
#     "StreamViewType": "NEW_AND_OLD_IMAGES"
# }
```

Streams must be enabled with `NEW_AND_OLD_IMAGES` for global tables. This setting cannot be changed after table creation in some configurations.

## Common Scenarios

### Replication Lag During Traffic Spikes

A Black Friday sale causes a 50x traffic spike to the primary table in us-east-1. The replica in eu-west-1 has lower provisioned capacity and cannot keep up, causing replication lag of several minutes. The fix is to ensure all replicas have adequate capacity for peak loads, or use on-demand billing.

### Conflicting Writes from Mobile Users

A mobile application allows offline writes that sync to DynamoDB when connectivity is restored. Two users simultaneously update the same item in different regions. Global tables use last-writer-wins, so one update is silently lost. Implement application-level conflict resolution with version vectors.

### Schema Change Propagation Failure

A new attribute is added to items in one region, but the application in another region fails because it expects the old schema. Global tables replicate data but do not enforce schema consistency. Use a backward-compatible schema migration strategy across all regions.

## Prevent It

- Use on-demand billing mode for all replica tables to handle traffic spikes
- Monitor `ReplicationLatency` CloudWatch metric with alarms set at 5 seconds
- Ensure all replicas have at least the same write capacity as the primary table
- Avoid schema changes that are not backward-compatible across regions
- Use DynamoDB Streams for custom replication logic if you need conflict resolution
- Test global table configuration in a staging environment with multiple regions
- Implement application-level conflict detection for critical data
- Keep global tables in the same AWS partition (e.g., commercial, gov-cloud)

## Related Pages

- [DynamoDB Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
- [DynamoDB Backup Error](/tools/dynamodb/dynamodb-backup-error)
- [DynamoDB Access Denied Error](/tools/dynamodb/dynamodb-access-denied)
