---
title: "[Solution] AZURE Storage Account Limit"
description: "StorageAccountLimit for storage accounts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Account Limit` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- 250 accounts per subscription hit
- Region specific limit reached

## How to Fix

### Check usage

```bash
az storage account list --query length(@)
```

## Examples

- Example scenario: 250 accounts per subscription hit
- Example scenario: region specific limit reached

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
