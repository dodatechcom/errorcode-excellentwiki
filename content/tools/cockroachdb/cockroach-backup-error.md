---
title: "[Solution] CockroachDB Backup Error — How to Fix"
description: "Fix CockroachDB backup and restore errors by resolving storage issues, handling encryption failures, tuning parallelism, and recovering from interrupted backups."
tools: ["cockroachdb"]
error-types: ["backup-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB backup error occurs when a scheduled or ad-hoc backup or restore operation fails. Backups are critical for disaster recovery, and failures can leave the cluster without recent recoverable snapshots.

## Why It Happens

CockroachDB backups write SST files to cloud storage or local directories. Failures can occur at any stage — from reading the data to writing to storage to completing the manifest.

- The backup destination (S3, GCS, Azure Blob) is unreachable or credentials are expired
- The backup storage bucket is full or has exceeded its quota
- Encryption key is missing or incorrect for encrypted backups
- The backup job runs out of memory due to large table sizes
- A node failure during backup causes the job to abort
- The backup job exceeds the configured timeout
- The incremental backup chain is broken due to a missing base backup
- Restore fails because the backup files are corrupted or incomplete
- The cluster version is too old to restore from a newer backup format

## Common Error Messages

```text
ERROR: couldn't write backup: write failed: Access Denied
```

The backup cannot write to the destination bucket. The service account or credentials are incorrect.

```text
ERROR: backup job failed: node failure during backup
```

A node crashed during the backup, causing the distributed job to fail.

```text
ERROR: could not restore: backup files are incomplete
```

The restore operation found missing or incomplete backup files in the chain.

```text
ERROR: backup encryption key mismatch
```

The encryption key provided for restore does not match the key used during backup.

## How to Fix It

### 1. Verify Storage Credentials

```sql
-- Test backup to S3
BACKUP DATABASE mydb 
INTO 's3://my-bucket/backup?AWS_ACCESS_KEY_ID=xxx&AWS_SECRET_ACCESS_KEY=yyy';

-- Test backup to GCS
BACKUP DATABASE mydb 
INTO 'gs://my-bucket/backup?AUTH=specified&CREDENTIALS=/path/to/credentials.json';

-- Test backup to Azure
BACKUP DATABASE mydb 
INTO 'azure://mycontainer?AZURE_ACCOUNT_NAME=myaccount&AZURE_ACCOUNT_KEY=mykey';
```

```bash
# Test AWS credentials
aws s3 ls s3://my-bucket/ --region us-east-1

# Test GCS credentials
gsutil ls gs://my-bucket/

# Test Azure credentials
az storage blob list --container-name mycontainer --account-name myaccount
```

### 2. Fix Backup Job Failures

```sql
-- Check backup job status
SHOW JOBS;

-- Find failed backup jobs
SELECT job_id, status, error, fraction_completed, created
FROM [SHOW JOBS]
WHERE job_type = 'BACKUP'
ORDER BY created DESC;

-- Resume a failed incremental backup
RESUME JOB <job_id>;

-- Cancel a stuck backup
CANCEL JOB <job_id>;
```

### 3. Create a Complete Backup Chain

```sql
-- Base backup (full)
BACKUP DATABASE mydb 
INTO 'gs://my-bucket/backups'
AS OF SYSTEM TIME '-10s';

-- Incremental backup (after base)
BACKUP DATABASE mydb 
INTO LATEST IN 'gs://my-bucket/backups'
AS OF SYSTEM TIME '-10s';

-- Check the backup chain
SHOW BACKUP LATEST IN 'gs://my-bucket/backups';

-- List all backups in the chain
SHOW BACKUP 'gs://my-bucket/backups' WITH CHECK;
```

### 4. Restore from Backup

```sql
-- Restore the latest backup
RESTORE DATABASE mydb 
FROM LATEST IN 'gs://my-bucket/backups';

-- Restore to a specific point in time
RESTORE DATABASE mydb 
FROM LATEST IN 'gs://my-bucket/backups'
AS OF SYSTEM TIME '2024-01-15 10:30:00+0000';

-- Restore to a different database name
RESTORE DATABASE mydb 
FROM LATEST IN 'gs://my-bucket/backups'
WITH new_db_name = 'mydb_restored';

-- Restore a specific table
RESTORE TABLE users, orders
FROM LATEST IN 'gs://my-bucket/backups';
```

### 5. Configure Encrypted Backups

```sql
-- Backup with encryption
BACKUP DATABASE mydb 
INTO 'gs://my-bucket/backups'
WITH encryption_passphrase = 'my_secret_key';

-- Restore encrypted backup
RESTORE DATABASE mydb 
FROM LATEST IN 'gs://my-bucket/backups'
WITH encryption_passphrase = 'my_secret_key';
```

### 6. Tune Backup Performance

```sql
-- Increase parallelism for large backups
SET CLUSTER SETTING kv.bulk_sst.max_allowed_overage = 256MB;

-- Check backup progress
SELECT 
    job_id,
    fraction_completed,
    running_status
FROM [SHOW JOBS]
WHERE job_type = 'BACKUP';

-- Monitor backup size
SELECT 
    job_id,
    bytes,
    rows
FROM [SHOW JOBS]
WHERE job_type = 'BACKUP';
```

### 7. Fix Corrupted Backups

```sql
-- Verify backup integrity
SHOW BACKUP 'gs://my-bucket/backups' WITH CHECK;

-- If the backup is corrupted, take a new base backup
BACKUP DATABASE mydb 
INTO 'gs://my-bucket/backups-new'
AS OF SYSTEM TIME '-10s';

-- Verify the new backup
SHOW BACKUP 'gs://my-bucket/backups-new' WITH CHECK;
```

## Common Scenarios

**Scheduled backup fails overnight.** Check the backup job logs in `SHOW JOBS`. Common causes are expired credentials, network issues, or storage quota exceeded. Fix the root cause and resume the job.

**Restore fails with version mismatch.** A backup taken on a newer CockroachDB version cannot be restored to an older version. Upgrade the cluster before restoring, or restore to a cluster running the same or newer version.

**Incremental backup chain is broken.** If a base backup or intermediate incremental is missing, subsequent incrementals cannot be restored. Take a new base backup to restart the chain.

## Prevent It

- Monitor scheduled backup jobs with alerts for failures and run `SHOW JOBS` daily to check status
- Test restore procedures regularly by restoring to a staging cluster and verifying data integrity
- Use encryption for all production backups and store encryption keys securely in a secrets manager
