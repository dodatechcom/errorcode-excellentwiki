---
title: "[Solution] AZURE File Not Found"
description: "FileNotFound for Azure Files."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `File Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Path incorrect
- File deleted
- Share not mounted

## How to Fix

### List files

```bash
az storage file list -s myshare
```

## Examples

- Example scenario: path incorrect
- Example scenario: file deleted
- Example scenario: share not mounted

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
