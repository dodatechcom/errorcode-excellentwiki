---
title: "[Solution] Azure Encryption at Rest Error"
description: "Resolve Azure encryption at rest failures for storage, databases, and managed disks."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Encryption at rest errors occur when Azure cannot apply or verify encryption for data stored in services. This impacts compliance and data protection.

## Common Causes

- Customer-managed key in Key Vault is disabled or expired
- Encryption scope is not configured for the storage account
- Managed disk encryption extension is not installed
- Key Vault access policy does not allow the encryption operation

## How to Fix

### Check encryption status

```bash
az storage account show \
  --name mystorageaccount \
  --resource-group myRG \
  --query "encryption"
```

### Enable customer-managed key encryption

```bash
az storage account update \
  --name mystorageaccount \
  --resource-group myRG \
  --encryption-key-source Microsoft.Keyvault \
  --encryption-key-vault https://myKeyVault.vault.azure.net \
  --encryption-key-name myKey
```

### Check Key Vault key status

```bash
az keyvault key show \
  --vault-name myKeyVault \
  --name myKey \
  --query "attributes.enabled"
```

### Enable disk encryption

```bash
az vm encryption enable \
  --resource-group myRG \
  --name myVM \
  --disk-encryption-keyvault myKeyVault
```

## Examples

- Storage account reports encryption failure because the Key Vault key was soft-deleted
- Managed disk encryption fails because the Key Vault does not have a Key Encryption Key
- Database encryption at rest fails because the TDE protector certificate has expired

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- Key Vault issues.
- [Azure Storage Encryption]({{< relref "/cloud/azure/azure-storage-encryption" >}}) -- Storage encryption.
