---
title: "[Solution] AZURE Snapshot Error"
description: "SnapshotError when creating a VM snapshot."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Snapshot Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Source disk not found
- Snapshot quota reached
- Incremental snapshot chain broken

## How to Fix

### Create snapshot

```bash
az snapshot create -g myRG -n mySnap --source myDisk
```

## Examples

- Example scenario: source disk not found
- Example scenario: snapshot quota reached
- Example scenario: incremental snapshot chain broken

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
