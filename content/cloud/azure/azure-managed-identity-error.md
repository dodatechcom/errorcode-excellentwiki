---
title: "[Solution] Azure Managed Identity Error — credential, auth, and token failures"
description: "Fix Azure Managed Identity error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 162
---

Managed Identity errors appear as token acquisition failures, identity not found, or authentication errors when accessing Azure resources without explicit credentials.

## Common Causes
- System-assigned identity not enabled on resource
- User-assigned identity not associated with resource
- Resource moved to different subscription breaking identity links
- Token endpoint unreachable from resource networking configuration
- RBAC role not assigned to managed identity principal

## How to Fix
### Check managed identity status
```bash
az identity show \
  --resource-group myResourceGroup \
  --name myManagedIdentity \
  --query "principalId"
```

### Enable system-assigned identity
```bash
az vm identity assign \
  --resource-group myResourceGroup \
  --name myVM
```

### Assign RBAC role to identity
```bash
az role assignment create \
  --assignee 00000000-0000-0000-0000-000000000000 \
  --role "Storage Blob Data Contributor" \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myStorage
```

### Get identity token
```bash
curl -H "Metadata: true" "http://169.254.169.254/metadata/identity/oauth2/token?resource=https://management.azure.com&api-version=2018-02-01"
```

## Examples
### Create user-assigned identity
```bash
az identity create \
  --resource-group myResourceGroup \
  --name myUserIdentity
```

### Assign identity to VM
```bash
az vm identity assign \
  --resource-group myResourceGroup \
  --name myVM \
  --identities /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myUserIdentity
```

## Related Errors
- {{< relref "/cloud/azure/auth-failed" >}}
- {{< relref "/cloud/azure/azure-rbac-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
