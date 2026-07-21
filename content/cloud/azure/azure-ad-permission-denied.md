---
title: "[Solution] Azure AD Permission Denied Error"
description: "Resolve Azure AD permission denied errors for delegated and application resource access."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Permission denied errors occur when Azure AD denies access to a resource because the principal lacks the required role or permission. This blocks API calls and resource operations.

## Common Causes

- Service principal does not have the required RBAC role assignment
- Application permissions are not granted for the target API
- Conditional access policy is blocking the access based on device or location
- Resource-specific permissions are missing for the operation

## How to Fix

### Check role assignments

```bash
az role assignment list \
  --assignee appId \
  --scope /subscriptions/xxx/resourceGroups/myRG \
  --query "[].{Role:roleDefinitionName,Scope:scope}"
```

### Assign a role to the service principal

```bash
az role assignment create \
  --assignee appId \
  --role "Contributor" \
  --scope /subscriptions/xxx/resourceGroups/myRG
```

### Grant application permissions

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/servicePrincipals/{spId}/appRoleAssignments" \
  --body '{
    "principalId": "spId",
    "resourceId": "targetResourceId",
    "appRoleId": "appRoleId"
  }'
```

### List available roles

```bash
az role definition list --query "[].{RoleName:roleName,Type:type}" | head -20
```

## Examples

- Service principal gets `403 Forbidden` when trying to read Key Vault secrets
- Application cannot write to Cosmos DB despite having `Contributor` at the subscription level
- Conditional access blocks sign-in from non-compliant devices

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- General Azure AD errors.
- [Azure RBAC Error]({{< relref "/cloud/azure/azure-rbac-error" >}}) -- RBAC issues.
