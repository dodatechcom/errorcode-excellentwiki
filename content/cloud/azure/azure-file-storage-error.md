---
title: "[Solution] AZURE File Storage Error"
description: "FileStorageError for Azure Files."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `File Storage Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Share quota 100 TiB
- SMB protocol mismatch
- File handles open

## How to Fix

### List shares

```bash
az storage share list
```

## Examples

- Example scenario: share quota 100 tib
- Example scenario: smb protocol mismatch
- Example scenario: file handles open

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
