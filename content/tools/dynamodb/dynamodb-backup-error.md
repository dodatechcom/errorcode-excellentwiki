---
title: "[Solution] DynamoDB Point-in-Time Recovery Error — How to Fix"
description: "Fix DynamoDB point-in-time recovery (PITR) errors by enabling backups, checking restore time windows, handling table conflicts, and troubleshooting restore failures."
tools: ["dynamodb"]
error-types: ["backup-error"]
severities: ["error"]
weight: 5
comments: true
---

A point-in-time recovery (PITR) error occurs when you attempt to restore a DynamoDB table to a specific time and the operation fails due to configuration issues, time window constraints, or resource conflicts.

## What This Error Means

DynamoDB PITR allows you to restore your table to any point in time within the last 35 days. It creates continuous backups of your table. When you initiate a restore, DynamoDB creates a new table from the backup data at the specified timestamp.

PITR errors occur when the restore operation fails. The error may indicate that PITR was not enabled during the target time window, the target time is outside the recoverable window, or the destination table already exists.

## Why It Happens

- PITR was not enabled during the target restore time period
- The specified restore time is outside the 35-day recovery window
- A destination table with the same name already exists
- The table has a Global Secondary Index that conflicts with the restore
- Insufficient IAM permissions to perform the restore operation
- The table is in the process of being deleted
- Cross-region PITR restore is attempted without proper configuration
- The table has been encrypted with a custom KMS key and the key is inaccessible

## Common Error Messages

```
PointInTimeRecoveryUnavailableException: PITR is not enabled for this table
# or
InvalidRestoreTimeException: Specified restore time is outside the recovery window
# or
TableAlreadyExistsException: A table with the given name already exists
# or
RestoreTableToPointInTime operation failed: KMS key access denied
```

## How to Fix It

### 1. Enable PITR on Your Table

```bash
aws dynamodb update-continuous-backups \
    --table-name my-table \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true

# Verify PITR status
aws dynamodb describe-continuous-backups \
    --table-name my-table
```

PITR must be enabled before you can perform restores. Once enabled, it takes effect immediately and starts tracking changes from that point forward.

### 2. Find the Earliest Restorable Time

```bash
# Get the earliest and latest restorable times
aws dynamodb describe-continuous-backups \
    --table-name my-table \
    --query 'ContinuousBackupsDescription.PointInTimeRecoveryDescription'

# Output will show EarliestRestorableDateTime and LatestRestorableDateTime
```

The restore time must be between these two values. If you specify a time before PITR was enabled, the restore fails.

### 3. Restore to a Point in Time

```bash
# Restore to a specific UTC timestamp
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored \
    --restore-date-time "2025-06-15T10:30:00Z"

# Restore to the latest restorable time
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored \
    --use-latest-restorable-time
```

### 4. Handle Destination Table Name Conflicts

```bash
# Check if the destination table already exists
aws dynamodb list-tables --query "TableNames[?contains(@, 'my-table-restored')]"

# Choose a unique destination table name
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored-v2 \
    --use-latest-restorable-time
```

The destination table name must be unique in the region and account. Delete the existing table or choose a different name.

### 5. Restore with Custom KMS Key Settings

```bash
# If the source table uses a custom KMS key, specify it for the restored table
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored \
    --use-latest-restorable-time \
    --sse-specification-override Enabled=true,SSEType=KMS,KMSMasterKeyId=alias/my-key
```

Ensure the KMS key is accessible and the IAM role has `kms:Decrypt` and `kms:GenerateDataKey` permissions.

### 6. Restore Without Global Secondary Indexes

```bash
# By default, all GSIs are restored. To exclude them:
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored \
    --use-latest-restorable-time \
    --global-secondary-index-override '[]'

# Or override specific GSI settings
aws dynamodb restore-table-to-point-in-time \
    --source-table-name my-table \
    --target-table-name my-table-restored \
    --use-latest-restorable-time \
    --global-secondary-index-override '[
        {
            "IndexName": "status-index",
            "KeySchema": [
                {"AttributeName": "status", "KeyType": "HASH"},
                {"AttributeName": "created_at", "KeyType": "RANGE"}
            ],
            "Projection": {"ProjectionType": "ALL"},
            "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
        }
    ]'
```

### 7. Cross-Region PITR Restore Using Backup Export

```python
import boto3
import json

# PITR restore is same-region only
# For cross-region, use on-demand backup + restore or DynamoDB Export to S3

source_client = boto3.client('dynamodb', region_name='us-east-1')
dest_client = boto3.client('dynamodb', region_name='eu-west-1')

# Step 1: Create an on-demand backup from source
backup = source_client.create_backup(
    TableName='my-table',
    BackupName='my-table-cross-region-backup'
)
backup_arn = backup['BackupDetails']['BackupArn']

# Step 2: Restore from backup into destination region
dest_client.restore_table_from_backup(
    TargetTableName='my-table',
    BackupArn=backup_arn
)
```

## Common Scenarios

### Accidental Data Deletion Recovery

A developer accidentally runs a `DeleteItem` operation that removes critical user data. PITR restore is used to recover the table to a point just before the deletion. The restore creates a new table, and the data is extracted and merged back into the production table.

### Corrupted Data Rollback

A bug in an ETL pipeline corrupts thousands of items with incorrect values. PITR is used to restore the table to a timestamp before the corrupted data was written. The restored table replaces the production table after validation.

### Table Schema Migration Failures

During a schema migration, a new GSI fails to build correctly, causing query errors. PITR restore reverts the table to its previous state. The migration is re-attempted with corrected index definitions.

## Prevent It

- Enable PITR on all production tables as a standard practice
- Monitor `EarliestRestorableDateTime` to ensure PITR coverage has no gaps
- Set up CloudWatch alarms for PITR status changes
- Test PITR restore procedures in a non-production environment regularly
- Use descriptive destination table names with timestamps to avoid conflicts
- Document IAM permissions required for restoring tables
- Automate regular on-demand backups as a supplement to PITR
- Validate KMS key permissions for encrypted tables

## Related Pages

- [DynamoDB Global Table Error](/tools/dynamodb/dynamodb-global-table-error)
- [DynamoDB Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
- [DynamoDB Access Denied Error](/tools/dynamodb/dynamodb-access-denied)
