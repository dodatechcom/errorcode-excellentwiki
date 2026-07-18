---
title: "[Solution] MariaDB S3 Storage Error — How to Fix"
description: "Fix MariaDB S3 backup and storage errors including access denied, endpoint issues, multipart upload failures, and connectivity problems"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB S3 Storage Error

MariaDB can use S3-compatible object storage for backups and data import/export. S3 errors occur when authentication fails, the bucket does not exist, or the request exceeds S3 limits.

## Why It Happens

- AWS credentials are missing or expired
- The S3 bucket does not exist or is in a different region
- IAM policy does not grant required S3 permissions
- Multipart upload fails due to network timeout
- The S3 endpoint URL is incorrect
- SSL certificate verification fails for private endpoints

## Common Error Messages

```
ERROR: Unable to connect to S3 endpoint: Access Denied
```

```
mariabackup: error: S3 upload failed: 'InvalidAccessKeyId'
```

```
ERROR: The specified bucket does not exist
```

```
mariabackup: error: S3 multipart upload failed: 'EntityTooLarge'
```

## How to Fix It

### 1. Verify AWS Credentials

```bash
aws sts get-caller-identity
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
```

### 2. Fix S3 Bucket and Region Issues

```bash
aws s3 ls s3://my-mariadb-backups/
aws s3api get-bucket-location --bucket my-mariadb-backups
export AWS_DEFAULT_REGION=eu-west-1
```

### 3. Fix Multipart Upload Failures

```bash
mariabackup --backup --stream=xbstream 2>/dev/null |   aws s3 cp - s3://my-backups/full.xbstream --part-size 134217728
```

### 4. Fix S3-Compatible Storage (MinIO)

```bash
export AWS_ACCESS_KEY_ID=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
aws s3 ls --endpoint-url http://minio-host:9000 s3://my-backups/
```

## Common Scenarios

- **Backup fails after credential rotation**: Update credentials and test.
- **MinIO connection refused**: Verify MinIO is running with health check.
- **S3 upload too slow**: Use local cache, then sync to S3 in background.

## Prevent It

- Rotate AWS credentials before expiry
- Use IAM roles on EC2/ECS instead of static credentials
- Test backup/restore to S3 on a schedule

## Related Pages

- [MariaDB Backup Error](/tools/mariadb/mariadb-backup-error)
- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MySQL S3 Error](/tools/mysql/mysql-s3-error)
