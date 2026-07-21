---
title: "[Solution] AZURE Account Name Taken"
description: "StorageAccountAlreadyTaken for name."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Account Name Taken` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Name must be globally unique
- Another sub owns the name

## How to Fix

### Check name

```bash
az storage account check-name --name myuniquename12345
```

## Examples

- Example scenario: name must be globally unique
- Example scenario: another sub owns the name

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
