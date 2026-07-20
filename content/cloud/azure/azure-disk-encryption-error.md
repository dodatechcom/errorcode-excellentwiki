---
title: "[Solution] Azure Disk Encryption Error — encryption set, Key Vault, and BitLocker failures"
description: "Fix Azure Disk Encryption error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 120
---

Disk Encryption errors occur when encryption set cannot access Key Vault keys, BitLocker fails to initialize, or disk re-encryption gets stuck.

## Common Causes
- Key Vault access policy not granting disk encryption permissions
- Encryption set key version mismatch or key rotation incomplete
- VM agent not responding preventing extension execution
- Managed disk size exceeding encryption key algorithm limits
- Key Vault soft-delete or purge protection blocking key access

## How to Fix
### Check disk encryption status
```bash
az disk show \
  --resource-group myResourceGroup \
  --name myDisk \
  --query "encryptionSettings"
```

### Set Key Vault access policy
```bash
az keyvault set-policy \
  --name myKeyVault \
  --resource-group myResourceGroup \
  --object-id 00000000-0000-0000-0000-000000000000 \
  --key-permissions wrapKey unwrapKey get
```

### Create encryption set
```bash
az disk-encryption-set create \
  --resource-group myResourceGroup \
  --name myEncryptionSet \
  --key-url https://mykeyvault.vault.azure.net/keys/myKey/myKeyVersion \
  --source-vault myKeyVault
```

### Enable encryption on existing disk
```bash
az disk update \
  --resource-group myResourceGroup \
  --name myDisk \
  --encryption-disk-encryption-set-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/diskEncryptionSets/myEncryptionSet
```

## Examples
### Encrypt VM OS disk
```bash
az vm encryption enable \
  --resource-group myResourceGroup \
  --name myVM \
  --disk-encryption-keyvault myKeyVault
```

### Check encryption health
```bash
az vm encryption show \
  --resource-group myResourceGroup \
  --name myVM
```

## Related Errors
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/disk-error" >}}
