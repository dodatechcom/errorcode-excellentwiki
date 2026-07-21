---
title: "[Solution] GCP Backup (CloudSQL)"
description: "CloudSQLBackupError for backups."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Backup (CloudSQL)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Backup already running
- Binary logging required for point-in-time
- Retention days out of range (1-365)

## How to Fix

### Create backup

```bash
gcloud sql backups create --instance=myInstance
```

## Examples

- Example scenario: backup already running
- Example scenario: binary logging required for point-in-time
- Example scenario: retention days out of range (1-365)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
