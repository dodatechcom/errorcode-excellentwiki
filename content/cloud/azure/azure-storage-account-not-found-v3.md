---
title: "[Solution] AZURE Storage Account Not Found"
description: "StorageAccountNotFound for storage accounts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Account Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Account name incorrect
- Deleted account
- Account in wrong subscription

## How to Fix

### List accounts

```bash
az storage account list
```

## Examples

- Example scenario: account name incorrect
- Example scenario: deleted account
- Example scenario: account in wrong subscription

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
