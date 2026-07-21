---
title: "[Solution] AZURE Access Key Error"
description: "StorageAccessKeyError for keys."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Access Key Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Key expired or rotated
- Account key authentication disabled

## How to Fix

### List keys

```bash
az storage account keys list -g myRG -n myAccount
```

## Examples

- Example scenario: key expired or rotated
- Example scenario: account key authentication disabled

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
