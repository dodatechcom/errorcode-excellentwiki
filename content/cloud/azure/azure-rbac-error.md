---
title: "[Solution] Azure RBAC Error — role assignment, permission, and scope failures"
description: "Fix Azure RBAC error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 163
---

RBAC errors appear as insufficient permissions, role assignment conflicts, or scope access issues that prevent resource management operations.

## Common Causes
- Role assignment at child scope conflicting with parent deny assignment
- Custom role definition containing unsupported action or scope
- Principal not found (deleted user/group/service principal)
- Insufficient permissions to create role assignments at target scope
- Resource group lock preventing role assignment modifications

## How to Fix
### Check role assignments
```bash
az role assignment list \
  --scope /subscriptions/xxx \
  --query "[].{name:name,principalName:principalName,roleDefinitionName:roleDefinitionName}"
```

### Create role assignment
```bash
az role assignment create \
  --assignee myServicePrincipal \
  --role "Contributor" \
  --scope /subscriptions/xxx/resourceGroups/myRG
```

### Remove role assignment
```bash
az role assignment delete \
  --assignee myServicePrincipal \
  --role "Contributor" \
  --scope /subscriptions/xxx/resourceGroups/myRG
```

### Create custom role
```bash
az role definition create \
  --role-definition '{
    "Name": "My Custom Role",
    "Description": "Custom role for specific operations",
    "Actions": ["Microsoft.Storage/storageAccounts/read"],
    "NotActions": [],
    "AssignableScopes": ["/subscriptions/xxx"]
  }'
```

## Examples
### List available roles
```bash
az role definition list \
  --query "[?contains(roleName,'Reader')].{name:name,roleName:roleName}"
```

### Check effective permissions
```bash
az role assignment list \
  --assignee myUser \
  --include-inherited \
  --query "[].{scope:scope,role:roleDefinitionName}"
```

## Related Errors
- {{< relref "/cloud/azure/azure-managed-identity-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
- {{< relref "/cloud/azure/azure-policy-error" >}}
