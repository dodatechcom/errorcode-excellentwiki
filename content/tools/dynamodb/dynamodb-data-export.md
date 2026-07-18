---
title: "[Solution] DynamoDB Data Export Error - Fix Export to S3 Failed"
description: "Fix DynamoDB export to S3 failures. Resolve export limits, IAM permissions, and S3 bucket issues for DynamoDB data exports."
tools: ["dynamodb"]
error-types: ["data-export"]
severities: ["error"]
weight: 5
---

This error means a DynamoDB table export to S3 failed. The export may have exceeded limits, the S3 bucket may be inaccessible, or the IAM role may lack permissions.

## What This Error Means

When a DynamoDB export to S3 fails, you see:

```
ExportException: Export failed
# or
ValidationException: Export already in progress
# or
AccessDeniedException: User is not authorized to perform: s3:PutObject
```

DynamoDB exports create a point-in-time snapshot of your data in S3 for analytics, migration, or archival.

## Why It Happens

- The S3 bucket does not exist or is in a different region
- The IAM role lacks S3 write permissions
- An export is already in progress for the table
- The export exceeds the 25GB incremental export limit
- The S3 bucket policy does not allow the DynamoDB service principal
- The export format is invalid

## How to Fix It

### Check existing exports

```python
import boto3

dynamodb = boto3.client('dynamodb')
response = dynamodb.list_exports(TableName='my-table')
for export in response['ExportSummaries']:
    print(export['ExportArn'], export['ExportStatus'])
```

### Start an export to S3

```python
response = dynamodb.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:us-east-1:123456789:table/my-table',
    S3Bucket='my-export-bucket',
    S3Prefix='dynamodb-exports/',
    ExportType='FULL_EXPORT'
)
print(response['ExportDescription']['ExportArn'])
```

### Verify S3 bucket permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:PutObject",
    "s3:AbortMultipartUpload"
  ],
  "Resource": "arn:aws:s3:::my-export-bucket/*"
}
```

### Grant DynamoDB access to the S3 bucket

```json
{
  "Effect": "Allow",
  "Principal": {
    "Service": "dynamodb.amazonaws.com"
  },
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::my-export-bucket/*"
}
```

### Check export status

```python
response = dynamodb.describe_export(
    ExportArn='arn:aws:dynamodb:...'
)
print(response['ExportDescription']['ExportStatus'])
print(response['ExportDescription']['ExportPercentage'])
```

### Use S3 bucket in the same region

```python
# Export must be to a bucket in the same region as the table
response = dynamodb.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:us-east-1:123456789:table/my-table',
    S3Bucket='my-us-east-1-bucket',
    ExportType='FULL_EXPORT'
)
```

### Export in DynamoDB JSON or CSV format

```python
response = dynamodb.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:...',
    S3Bucket='my-bucket',
    ExportFormat='DYNAMODB_JSON'  # or 'CSV'
)
```

### Handle export failures with retry

```python
response = dynamodb.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:...',
    S3Bucket='my-bucket',
    ExportType='FULL_EXPORT'
)

# Monitor until complete
import time
while True:
    desc = dynamodb.describe_export(ExportArn=response['ExportDescription']['ExportArn'])
    status = desc['ExportDescription']['ExportStatus']
    if status == 'COMPLETED':
        break
    elif status == 'FAILED':
        raise Exception(f"Export failed: {desc['ExportDescription'].get('FailureMessage')}")
    time.sleep(60)
```

## Common Mistakes

- Not granting the DynamoDB service principal access to the S3 bucket
- Forgetting that exports must be to a bucket in the same region
- Not monitoring export status for failures
- Assuming exports are instantaneous (they take time for large tables)
- Using incremental export when full export was intended

## Related Pages

- [DynamoDB Backup Error]({{< relref "/tools/dynamodb/dynamodb-backup-error" >}}) -- backup failures
- [DynamoDB Access Denied]({{< relref "/tools/dynamodb/dynamodb-access-denied" >}}) -- permission errors
- [DynamoDB Point-in-Time]({{< relref "/tools/dynamodb/dynamodb-point-in-time" >}}) -- PITR issues
