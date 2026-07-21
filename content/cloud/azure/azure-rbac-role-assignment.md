---
title: "[Solution] AZURE RBAC Role Assignment Error"
description: "AuthorizationFailed or InvalidRoleAssignmentDefinitionId when role assignments fail."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RBAC Role Assignment Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Role definition ID is incorrect
- Scope is invalid
- Managed identity does not exist
- Role assignment already exists

## How to Fix

### Check assignment

```bash
az role assignment list --assignee myIdentity --query "[].{Role:roleDefinitionName,Scope:scope}" --output table
```
### Create assignment

```bash
az role assignment create --assignee myIdentity --role Contributor --scope /subscriptions/mySub/resourceGroups/myRG
```
### Delete assignment

```bash
az role assignment delete --assignee myIdentity --role Contributor --scope /subscriptions/mySub/resourceGroups/myRG
```

## Examples

- Assignment for non-existent managed identity
- Trying to assign Owner without permissions

## Related Errors

- [Azure IAM Error]({{< relref "/cloud/azure/azure-rbac-error" >}}) -- General RBAC errors
- [Role Definition]({{< relref "/cloud/azure/azure-rbac-role-definition" >}}) -- Role definition
