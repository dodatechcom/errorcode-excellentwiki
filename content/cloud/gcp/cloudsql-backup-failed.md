---
title: "[Solution] GCP Cloud SQL Backup Failed"
description: "BACKUP_FAILED when automated backups fail."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud SQL Backup Failed` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Backup is not enabled
- Backup window conflicts with maintenance
- Storage is full
- Backup exceeds maximum size

## How to Fix

### Check backup config

```bash
gcloud sql instances describe my-instance --format="value(settings.backupConfiguration)"
```
### Enable backup

```bash
gcloud sql instances patch my-instance --backup-start-time=02:00
```
### List backups

```bash
gcloud sql backups list --instance=my-instance
```

## Examples

- Backup window overlaps with maintenance window
- Storage full preventing backup creation

## Related Errors

- [Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}}) -- General Cloud SQL errors
- [Instance Not Found]({{< relref "/cloud/gcp/cloudsql-instance-not-found" >}}) -- Instance not found
