---
title: "[Solution] AZURE Role Definition"
description: "RoleDefinitionError for custom roles."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Role Definition` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Role name already taken (duplicate)
- Permissions not allowed
- Assignable scopes invalid

## How to Fix

### List roles

```bash
az role definition list
```

## Examples

- Example scenario: role name already taken (duplicate)
- Example scenario: permissions not allowed
- Example scenario: assignable scopes invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
