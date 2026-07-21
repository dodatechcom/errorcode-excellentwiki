---
title: "[Solution] GCP Cloud SQL Binary Logging Error"
description: "Fix Cloud SQL binary logging errors. Resolve binary log retention, replication, and MySQL binlog configuration issues in GCP Cloud SQL."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud SQL Binary Logging Error

The Cloud SQL Binary Logging error occurs when binary logging configuration causes disk space issues, replication failures, or backup problems.

## Common Causes

- Binlog disk usage exceeds allocated storage
- Replication lag due to binlog write contention
- binlog_expire_logs_seconds is not configured
- Binary logging conflicts with read replicas
- Cloud SQL disk is full due to old binary logs

## How to Fix

### 1. Check binlog disk usage
```bash
gcloud sql instances describe INSTANCE_NAME \
  --format="value(diskUsage)"
```

### 2. Set binlog expiration
```bash
gcloud sql instances patch INSTANCE_NAME \
  --database-flags=binlog_expire_logs_seconds=604800
```

### 3. Check binary logging status
```bash
gcloud sql connect INSTANCE_NAME --user=root --database=mysql
SHOW VARIABLES LIKE 'log_bin%';
SHOW VARIABLES LIKE 'binlog_expire_logs_seconds';
```

### 4. Monitor replication status
```bash
gcloud sql instances describe REPLICA_NAME \
  --format="yaml(replicaConfiguration)"
```

## Examples

### Configure binlog for MySQL
```bash
gcloud sql instances patch my-instance \
  --database-flags=binlog_expire_logs_seconds=259200,binlog_row_image=FULL
```

### Check binlog size
```sql
SHOW BINARY LOGS;
```

## Related Errors

- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}})
- [GCP Database CloudSQL]({{< relref "/cloud/gcp/gcp-database-(cloudsql)" >}})
