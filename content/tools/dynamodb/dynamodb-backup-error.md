---
title: "[Solution] DynamoDB Backup Error - Fix Point-In-Time Recovery"
description: "Fix DynamoDB backup and point-in-time recovery errors by enabling PITR on the target table, checking IAM permissions for backup operations, and verifying table "
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB backup error occurs when creating, restoring, or managing on-demand backups or point-in-time recovery (PITR). The error may appear as `BackupNotFoundException`, `ContinuousBackupsUnavailableException`, or `TableNotFoundException` during backup operations.

## What This Error Means

DynamoDB supports two backup mechanisms: on-demand backups (manual snapshots) and point-in-time recovery (continuous backup with hourly recovery points). Backup errors indicate that the backup operation cannot proceed, either because the backup does not exist, the feature is not enabled, or the table is in an incompatible state.

The errors are typically `ValidationException` or `ResourceNotFoundException` with specific messages about the backup operation.

## Why It Happens

- Point-in-time recovery is not enabled on the table
- Table is in a `CREATING`, `DELETING`, or `UPDATING` state
- Backup name conflicts with an existing backup
- Table is too large for on-demand backup within the timeout
- IAM role lacks `dynamodb:CreateBackup` or `dynamodb:RestoreTableFromBackup` permissions
- Continuous backup window has not yet produced a recovery point
- Restoring to a table that already exists without specifying a different name
- Cross-region restore without proper permissions

## How to Fix It

### 1. Enable Point-In-Time Recovery

```python
client = boto3.client('dynamodb')

client.update_continuous_backups(
    TableName='my-table',
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True
    }
)
```

### 2. Check Backup Status

```bash
aws dynamodb describe-continuous-backups --table-name my-table
aws dynamodb list-backups --table-name my-table
```

### 3. Create an On-Demand Backup

```python
response = client.create_backup(
    TableName='my-table',
    BackupName='my-backup-2024-01-15'
)
# Wait for backup to complete
```

### 4. Restore from Backup

```python
client.restore_table_from_backup(
    TargetTableName='my-table-restored',
    BackupArn='arn:aws:dynamodb:us-east-1:123456789012:table/my-table/backup/0123456789'
)
```

### 5. Restore to Point in Time

```python
client.restore_table_to_point_in_time(
    TargetTableName='my-table-pitr',
    SourceTableName='my-table',
    UseLatestRestorableTime=True
)
```

### 6. Verify IAM Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:CreateBackup",
                "dynamodb:DeleteBackup",
                "dynamodb:DescribeBackup",
                "dynamodb:ListBackups",
                "dynamodb:RestoreTableFromBackup",
                "dynamodb:RestoreTableToPointInTime",
                "dynamodb:DescribeContinuousBackups",
                "dynamodb:UpdateContinuousBackups"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/my-table"
        }
    ]
}
```

## Common Mistakes

- Not enabling PITR before it is needed (restoring requires a recovery point to exist)
- Assuming on-demand backups are instant (large tables may take minutes to hours)
- Not setting a backup retention period for PITR (default is 35 days, but you should verify)
- Restoring to the same table name without first deleting the existing table
- Not testing backup restoration as part of disaster recovery drills

## Related Pages

- [DynamoDB Table Not Found](/tools/dynamodb/dynamodb-table-not-found)
- [DynamoDB Access Denied](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Global Table Error](/tools/dynamodb/dynamodb-global-table-error)
