---
title: "[Solution] Azure Key Vault Access Denied Error"
description: "Fix Azure Key Vault access denied errors for secrets, keys, and certificate operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Access denied errors in Key Vault prevent applications and users from reading secrets, keys, and certificates. This breaks application configuration and authentication flows.

## Common Causes

- Identity does not have a Key Vault access policy or RBAC role
- Key Vault firewall blocks the requesting IP address
- Managed identity is not assigned the required role on the Key Vault
- Network ACL default action is set to Deny with no exception for the identity

## How to Fix

### Check access policies

```bash
az keyvault show \
  --name myKeyVault \
  --query "properties.accessPolicies"
```

### Set access policy for an identity

```bash
az keyvault set-policy \
  --name myKeyVault \
  --object-id "objectId" \
  --secret-permissions get list set \
  --key-permissions get list encrypt decrypt
```

### Enable RBAC authorization

```bash
az keyvault update \
  --name myKeyVault \
  --enable-rbac-authorization true
```

### Assign Key Vault Secrets User role

```bash
az role assignment create \
  --assignee "appId" \
  --role "Key Vault Secrets User" \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.KeyVault/vaults/myKeyVault
```

## Examples

- Application receives `Forbidden: vault does not have an access policy` when reading secrets
- Key Vault firewall blocks requests from an on-premises IP range
- Managed identity can read secrets but cannot list them due to missing `list` permission

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- General Key Vault errors.
- [Azure Managed Identity Error]({{< relref "/cloud/azure/azure-managed-identity-error" >}}) -- Managed identity issues.
