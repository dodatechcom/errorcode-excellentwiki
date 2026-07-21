---
title: "[Solution] AZURE Storage Lifecycle"
description: "StorageLifecycleError for lifecycle rules."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Lifecycle` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Rule limit (100) reached
- Filter not supported
- Action type invalid

## How to Fix

### List rules

```bash
az storage account management-policy show -g myRG -n myAccount
```

## Examples

- Example scenario: rule limit (100) reached
- Example scenario: filter not supported
- Example scenario: action type invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
