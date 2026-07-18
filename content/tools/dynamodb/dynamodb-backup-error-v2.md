---
title: "[Solution] DynamoDB Backup Error v2 - Fix On-Demand Backup Failed"
description: "Fix DynamoDB on-demand backup failures. Resolve backup limits, IAM permissions, and storage issues for DynamoDB backups."
tools: ["dynamodb"]
error-types: ["backup-error"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB on-demand backup could not be created. The backup may exceed limits, the IAM role may lack permissions, or the table may be in an incompatible state.

## What This Error Means

When on-demand backup creation fails, you see:

```
LimitExceededException: Backup limit has been reached
# or
InternalServerError: Internal server error
# or
ValidationException: Backup already in progress
```

DynamoDB on-demand backups are full table snapshots that can be restored at any time. They are limited per-account and per-table.

## Why It Happens

- The account has reached the maximum number of on-demand backups (10 per table)
- The IAM role creating the backup lacks `dynamodb:CreateBackup` permission
- The table is being modified (deletion in progress)
- The table is too large for the backup service to handle
- A concurrent backup is already in progress for the same table
- The table is in a `DELETING` or `CREATING` state

## How to Fix It

### Check existing backups

```python
import boto3

dynamodb = boto3.client('dynamodb')
response = dynamodb.list_backups(
    TableName='my-table',
    BackupType='USER'
)
print(f'Existing backups: {len(response["BackupSummaries"])}')
```

### Delete old backups

```python
dynamodb.delete_backup(BackupArn='arn:aws:dynamodb:...')
```

Remove backups that are no longer needed.

### Check backup limits

```python
# Per account: 50 on-demand backups
# Per table: 10 on-demand backups
# Table size: 500GB maximum for on-demand backup
```

### Verify IAM permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:CreateBackup",
    "dynamodb:DeleteBackup",
    "dynamodb:DescribeBackup",
    "dynamodb:ListBackups"
  ],
  "Resource": "arn:aws:dynamodb:*:*:table/my-table"
}
```

### Wait for table modification to complete

```python
dynamodb = boto3.client('dynamodb')
response = dynamodb.describe_table(TableName='my-table')
print(response['Table']['TableStatus'])  # Should be 'ACTIVE'
```

### Use point-in-time recovery instead

```python
dynamodb.update_continuous_backups(
    TableName='my-table',
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True
    }
)
```

PITR provides continuous backup without the on-demand backup limits.

### Check backup status

```python
response = dynamodb.describe_backup(BackupArn='arn:aws:dynamodb:...')
print(response['BackupDetails']['BackupStatus'])  # CREATING, AVAILABLE
```

### Use AWS Backup for managed backups

```python
import boto3

backup = boto3.client('backup')
response = backup.start_backup_job(
    BackupVaultName='my-vault',
    ResourceArn='arn:aws:dynamodb:...'
)
```

AWS Backup can manage DynamoDB backups with scheduling and lifecycle policies.

## Common Mistakes

- Not monitoring backup count before attempting to create new ones
- Forgetting that on-demand backups have a 500GB table size limit
- Not setting up PITR as a continuous backup strategy
- Not cleaning up old backups that consume the per-table limit
- Using on-demand backups when PITR would be more cost-effective

## Related Pages

- [DynamoDB Table Not Found]({{< relref "/tools/dynamodb/dynamodb-table-not-found" >}}) -- table issues
- [DynamoDB Access Denied]({{< relref "/tools/dynamodb/dynamodb-access-denied" >}}) -- IAM permission errors
- [DynamoDB Validation Error]({{< relref "/tools/dynamodb/dynamodb-validation-error" >}}) -- validation issues
