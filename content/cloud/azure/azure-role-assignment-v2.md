---
title: "[Solution] AZURE Role Assignment"
description: "RoleAssignmentError for RBAC assignments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Role Assignment` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Role not found
- Principal does not exist
- Assignment already exists

## How to Fix

### List assignments

```bash
az role assignment list -g myRG
```

## Examples

- Example scenario: role not found
- Example scenario: principal does not exist
- Example scenario: assignment already exists

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
