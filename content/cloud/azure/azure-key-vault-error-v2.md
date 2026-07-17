---
title: "[Solution] Azure Key Vault — ForbiddenByPolicy"
description: "Fix Azure Key Vault ForbiddenByPolicy. Resolve Key Vault access policy and RBAC issues."
cloud: ["azure"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["azure", "key-vault", "forbidden", "policy", "access", "rbac", "secret"]
weight: 5
---

A Key Vault ForbiddenByPolicy error means the calling identity is denied access to the Key Vault resource. The access policy or RBAC role assignment does not grant the required permissions.

## What This Error Means

Azure Key Vault uses two access models: access policies (legacy) and RBAC (recommended). In access policy mode, each vault has an ACL that maps identities to specific permissions (get, list, set, delete) for keys, secrets, and certificates. In RBAC mode, Azure role assignments on the vault resource control access. A ForbiddenByPolicy error (HTTP 403) means the calling identity is not listed in the vault's access policy or lacks the appropriate RBAC role. The error includes the vault name and operation that was denied.

## Common Causes

- Identity not added to Key Vault access policy
- Access policy missing required permission (e.g., `get` for secrets)
- RBAC role not assigned on the Key Vault resource
- Managed identity not configured correctly for the resource
- Key Vault has network restrictions blocking the caller
- Using wrong tenant for multi-tenant Key Vault

## How to Fix

### Check Access Policies

```bash
az keyvault access-policy list --vault-name my-vault --query '[].{objectId:objectId,permissions:permissions}'
```

### Add Access Policy

```bash
az keyvault set-policy \
  --name my-vault \
  --object-id <principal-id> \
  --secret-permissions get list set \
  --key-permissions get list wrapKey unwrapKey \
  --certificate-permissions get list
```

### Assign RBAC Role

```bash
az role assignment create \
  --assignee <principal-id> \
  --role "Key Vault Secrets User" \
  --scope "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.KeyVault/vaults/my-vault"
```

### Test Secret Access

```bash
az keyvault secret show --vault-name my-vault --name my-secret
```

### Check Managed Identity

```bash
az webapp identity show --name my-app --resource-group my-rg
```

### Configure Network Rules

```bash
az keyvault network-rule add \
  --name my-vault \
  --ip-address 203.0.113.50
```

### Grant Access to Managed Identity

```bash
az keyvault set-policy \
  --name my-vault \
  --object-id <managed-identity-principal-id> \
  --secret-permissions get list
```

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error-v2" >}}) — authentication failed
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error-v2" >}}) — redirect URI mismatch
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
