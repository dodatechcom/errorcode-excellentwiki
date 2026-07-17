---
title: "[Solution] Azure Key Vault Access Error"
description: "Fix Azure Key Vault access errors. Resolve Key Vault permission issues."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "key-vault", "keyvault", "secret", "access-policy"]
weight: 5
---

An Azure Key Vault access error occurs when you cannot access secrets, keys, or certificates stored in Key Vault. This is typically caused by missing access policies or permissions.

## Common Causes

- Access policy does not include the required operations
- User or application not granted access to Key Vault
- Managed identity not configured correctly
- Key Vault firewall blocking the request
- Secret or key does not exist

## How to Fix

### Check Access Policies

```bash
az keyvault show --name myvault --query 'properties.accessPolicies'
```

### Set Access Policy

```bash
az keyvault set-policy --name myvault --object-id $OBJECT_ID \
  --secret-permissions get list set \
  --key-permissions get list wrapKey unwrapKey
```

### Get Secret

```bash
az keyvault secret show --vault-name myvault --name mysecret
```

### Enable Managed Identity Access

```bash
az keyvault set-policy --name myvault \
  --object-id $MANAGED_IDENTITY_OBJECT_ID \
  --secret-permissions get list
```

### Check Key Vault Firewall

```bash
az keyvault show --name myvault --query 'properties.networkAcls'
```

## Examples

```bash
# Example 1: Forbidden
# Operation get is not allowed on this vault
# Fix: add access policy for get operation

# Example 2: Secret not found
# Secret not found: mysecret
# Fix: create the secret in Key Vault
```

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) — AD authentication error
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) — Storage error
