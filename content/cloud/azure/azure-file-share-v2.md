---
title: "[Solution] AZURE File Share"
description: "FileShareError for Azure Files."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `File Share` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Share quota exceeded
- Protocol SMB mismatch
- Share not in storage account

## How to Fix

### List shares

```bash
az storage share list
```

## Examples

- Example scenario: share quota exceeded
- Example scenario: protocol smb mismatch
- Example scenario: share not in storage account

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
