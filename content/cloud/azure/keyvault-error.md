---
title: "Azure KeyVault: Access Denied to Key or Secret"
description: "KeyVault: Access denied to key/secret — Fix Azure Key Vault authorization errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The KeyVault access denied error occurs when an identity (user, managed identity, or service principal) attempts to access a key, secret, or certificate in Azure Key Vault without the required Key Vault access policy or RBAC role assignment.

## Common Causes

- The identity does not have a Key Vault access policy or RBAC role
- The secret or key has an expiry date and is no longer accessible
- The Key Vault is configured with access policies but the identity is not listed
- Network rules restrict access to specific virtual networks or IP ranges

## How to Fix

Check the Key Vault access policy:

```bash
az keyvault show \
  --name my-keyvault \
  --resource-group my-rg \
  --query 'properties.accessPolicies[].{ObjectId:objectId,Permissions:permissions}'
```

Grant access using RBAC (preferred method):

```bash
az role assignment create \
  --role "Key Vault Secrets User" \
  --assignee-object-id <principal-id> \
  --scope /subscriptions/<sub-id>/resourceGroups/my-rg/providers/Microsoft.KeyVault/vaults/my-keyvault
```

Or using access policies:

```bash
az keyvault set-policy \
  --name my-keyvault \
  --resource-group my-rg \
  --object-id <principal-id> \
  --secret-permissions get list
```

Check network rules:

```bash
az keyvault show \
  --name my-keyvault \
  --resource-group my-rg \
  --query 'properties.networkAcls'
```

## Examples

- Azure Function managed identity cannot retrieve a secret because no access policy is set
- Application gets 403 when accessing a key, but the user has `Key Vault Reader` instead of `Key Vault Crypto User`
- Network rule blocks access from a non-VNet IP address

## Related Errors

- [Azure Auth Failed]({{< relref "/cloud/azure/auth-failed" >}}) — Azure AD authentication failure.
- [Azure Storage Error]({{< relref "/cloud/azure/storage-error" >}}) — storage account issues.
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — AWS IAM authorization errors.
