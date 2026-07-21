---
title: "[Solution] AZURE Managed Identity"
description: "ManagedIdentityError for managed identities."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Managed Identity` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Identity already exists
- User-assigned identity not found
- System-assigned not enabled

## How to Fix

### List identities

```bash
az identity list -g myRG
```

## Examples

- Example scenario: identity already exists
- Example scenario: user-assigned identity not found
- Example scenario: system-assigned not enabled

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
