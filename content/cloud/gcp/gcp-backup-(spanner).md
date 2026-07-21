---
title: "[Solution] GCP Backup (Spanner)"
description: "SpannerBackupError for backups."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Backup (Spanner)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Backup already exists with name
- Database not in READY state for backup
- Backup expired (max 366 days)

## How to Fix

### Create backup

```bash
gcloud spanner backups create myBackup --instance=myInstance --database=myDB
```

## Examples

- Example scenario: backup already exists with name
- Example scenario: database not in ready state for backup
- Example scenario: backup expired (max 366 days)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
