---
title: "[Solution] DynamoDB Point-in-Time Recovery Error - Fix PITR Not Enabled"
description: "Fix DynamoDB point-in-time recovery errors. Enable PITR, restore from PITR, and resolve recovery window issues."
tools: ["dynamodb"]
error-types: ["point-in-time"]
severities: ["warning"]
weight: 5
---

This error means DynamoDB point-in-time recovery (PITR) is not enabled for your table, or a PITR restore operation failed. PITR provides continuous backups for the last 35 days.

## What This Error Means

When you try to restore from a point in time but PITR is not enabled, you see:

```
PointInTimeRecoveryNotEnabledException: Point in time recovery is not enabled
# or
ValidationException: Restore time is outside the recovery window
```

PITR must be enabled before a failure occurs. It cannot be retroactively applied to recover lost data.

## Why It Happens

- PITR was never enabled on the table
- The requested restore time is older than 35 days
- The table was created without PITR and data was lost
- The restore request uses a time outside the available window
- PITR was disabled at some point, creating a gap in recovery

## How to Fix It

### Enable PITR on existing tables

```python
import boto3

dynamodb = boto3.client('dynamodb')
dynamodb.update_continuous_backups(
    TableName='my-table',
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True
    }
)
```

### Check PITR status

```python
response = dynamodb.describe_continuous_backups(TableName='my-table')
print(response['ContinuousBackupsDescription']['PointInTimeRecoveryDescription'])
```

### Restore from PITR

```python
dynamodb.restore_table_from_point_in_time(
    TargetTableName='my-table-restored',
    SourceTableArn='arn:aws:dynamodb:us-east-1:123456789:table/my-table',
    UseLatestRestorableTime=True,
    # Or specify a time:
    # RestoreDateTime=datetime(2024, 1, 15, 10, 30)
)
```

### Enable PITR for all tables using AWS CLI

```bash
aws dynamodb update-continuous-backups \
  --table-name my-table \
  --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
```

### Set up AWS Backup for automated PITR

```python
backup = boto3.client('backup')
response = backup.create_backup_plan={
    'BackupPlan': {
        'BackupPlanName': 'DynamoDB-PITR',
        'Rules': [{
            'RuleName': 'DailyBackup',
            'TargetBackupVaultName': 'Default',
            'ScheduleExpression': 'cron(0 12 * * ? *)',
            'StartWindowMinutes': 60,
            'CompletionWindowMinutes': 180
        }]
    }
}
```

### Check available restore window

```python
response = dynamodb.describe_continuous_backups(TableName='my-table')
earliest = response['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['EarliestRestorableDateTime']
latest = response['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['LatestRestorableDateTime']
```

### Enable PITR on creation for new tables

```python
dynamodb.create_table(
    TableName='my-new-table',
    KeySchema=[{'AttributeName': 'pk', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'pk', 'AttributeType': 'S'}],
    BillingMode='PAY_PER_REQUEST',
    PointInTimeRecoverySpecification={'PointInTimeRecoveryEnabled': True}
)
```

## Common Mistakes

- Not enabling PITR on critical tables before data loss occurs
- Assuming PITR is enabled by default (it is not)
- Trying to restore to a time older than 35 days
- Not testing PITR restore procedures regularly
- Enabling PITR only on some tables while leaving others unprotected

## Related Pages

- [DynamoDB Backup Error]({{< relref "/tools/dynamodb/dynamodb-backup-error" >}}) -- backup failures
- [DynamoDB Table Not Found]({{< relref "/tools/dynamodb/dynamodb-table-not-found" >}}) -- table issues
- [DynamoDB Access Denied]({{< relref "/tools/dynamodb/dynamodb-access-denied" >}}) -- permission errors
