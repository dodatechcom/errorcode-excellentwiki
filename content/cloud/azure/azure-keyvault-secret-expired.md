---
title: "[Solution] Azure Key Vault Secret Expired Error"
description: "Fix Azure Key Vault secret expiration errors that block application access to credentials."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Secret expiration errors occur when Key Vault secrets pass their expiration date and become inaccessible. This breaks applications that depend on the secret for authentication.

## Common Causes

- Secret was created with an expiration date that has passed
- Secret was soft-deleted and cannot be recovered without proper permissions
- Secret version was disabled and the application references the disabled version
- Secret rotation was not automated and the old secret expired

## How to Fix

### Check secret expiration

```bash
az keyvault secret show \
  --vault-name myKeyVault \
  --name mySecret \
  --query "{Enabled:attributes.enabled,Expiry:attributes.expires}"
```

### Update secret expiration

```bash
az keyvault secret set-attributes \
  --vault-name myKeyVault \
  --name mySecret \
  --expires 2027-01-01T00:00:00Z
```

### Recover a deleted secret

```bash
az keyvault secret recover \
  --vault-name myKeyVault \
  --name mySecret
```

### Set up auto-rotation

```bash
az keyvault secret set-attributes \
  --vault-name myKeyVault \
  --name mySecret \
  --expires "P90D" \
  --enable-auto-rotation true
```

## Examples

- Application returns 500 errors because the database connection string secret expired yesterday
- Secret was accidentally deleted and the recovery window has passed
- Secret rotation policy exists but the rotation function failed to update the expiration

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- General Key Vault errors.
- [Azure Key Vault Access Denied]({{< relref "/cloud/azure/azure-keyvault-access-denied" >}}) -- Access issues.
