---
title: "[Solution] AZURE AzCopy Error"
description: "AzCopyError for AzCopy operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AzCopy Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- AzCopy version too old
- SAS token not provided
- Network connectivity issue

## How to Fix

### Check version

```bash
azcopy --version
```

## Examples

- Example scenario: azcopy version too old
- Example scenario: sas token not provided
- Example scenario: network connectivity issue

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
