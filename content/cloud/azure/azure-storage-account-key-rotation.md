---
title: "[Solution] Azure Storage Account Key Rotation Error"
description: "Resolve Azure Storage account key rotation failures that break application connectivity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Key rotation errors occur when storage account access keys are rotated but applications still use the old key. This breaks all connections to the storage account.

## Common Causes

- Only one key was rotated while the application uses the other key
- Application configuration was not updated after key rotation
- Connection string cache in the application has not been refreshed
- Key Vault-based key rotation script failed silently

## How to Fix

### Regenerate storage account keys

```bash
az storage account keys renew \
  --account-name mystorageaccount \
  --resource-group myRG \
  --key key1
```

### List current keys

```bash
az storage account keys list \
  --account-name mystorageaccount \
  --resource-group myRG \
  --query "[].{KeyName:keyName,Value:keyValue}"
```

### Rotate both keys sequentially

```bash
az storage account keys renew \
  --account-name mystorageaccount \
  --resource-group myRG \
  --key key1

sleep 30

az storage account keys renew \
  --account-name mystorageaccount \
  --resource-group myRG \
  --key key2
```

### Configure key rotation schedule

```bash
az storage account update \
  --name mystorageaccount \
  --resource-group myRG \
  --key-expiry-permission "read-write"
```

## Examples

- Application stops working immediately after key1 is regenerated because it uses key1
- Key rotation script regenerates key2 but application still uses key1 which is now invalid
- Key Vault secret is updated but the application reads a cached version of the old secret

## Related Errors

- [Azure Storage Access Key]({{< relref "/cloud/azure/azure-storage-access-key" >}}) -- Access key issues.
- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- Key Vault errors.
