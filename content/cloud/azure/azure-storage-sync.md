---
title: "[Solution] AZURE Storage Sync"
description: "StorageSyncError for sync groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Sync` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Sync group already exists
- Endpoint conflict
- Cloud tiering enabled issue

## How to Fix

### List sync groups

```bash
az storagesync sync-group list -g myRG -n mySyncService
```

## Examples

- Example scenario: sync group already exists
- Example scenario: endpoint conflict
- Example scenario: cloud tiering enabled issue

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
