---
title: "[Solution] AZURE Resource Group Not Found"
description: "ResourceGroupNotFound for resource groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Resource Group Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Name incorrect
- Deleted by admin
- Wrong subscription

## How to Fix

### List groups

```bash
az group list
```

## Examples

- Example scenario: name incorrect
- Example scenario: deleted by admin
- Example scenario: wrong subscription

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
