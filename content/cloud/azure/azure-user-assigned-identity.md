---
title: "[Solution] AZURE User Assigned Identity"
description: "UserAssignedIdentityError."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `User Assigned Identity` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- User identity not assigned to resource
- Identity not found in region

## How to Fix

### Create identity

```bash
az identity create -g myRG -n myID
```

## Examples

- Example scenario: user identity not assigned to resource
- Example scenario: identity not found in region

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
