---
title: "[Solution] AZURE System Assigned Identity"
description: "SystemAssignedError for system identity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `System Assigned Identity` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Not enabled on resource
- Creation failed
- Role assignment to identity failed

## How to Fix

### Assign identity

```bash
az vm identity assign -g myRG -n myVM
```

## Examples

- Example scenario: not enabled on resource
- Example scenario: creation failed
- Example scenario: role assignment to identity failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
