---
title: "[Solution] Azure Files Error — share, sync, SMB, and AAD authentication failures"
description: "Fix Azure Files error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 118
---

Azure Files errors appear as SMB mount failures, sync conflicts, or AAD authentication rejections that prevent file share access.

## Common Causes
- SMB protocol version mismatch between client and share
- Azure AD domain services not joined or token expired
- Storage account keys rotated without updating client credentials
- File share quota exceeded preventing writes
- Network firewall blocking SMB ports 445

## How to Fix
### Check share quota usage
```bash
az storage share stats \
  --name myShare \
  --account-name myStorageAccount \
  --account-key myAccountKey
```

### Enable AAD authentication for Files
```bash
az storage account update \
  --resource-group myResourceGroup \
  --name myStorageAccount \
  --enable-aad-domain-services true
```

### Regenerate storage account key
```bash
az storage account keys renew \
  --resource-group myResourceGroup \
  --account-name myStorageAccount \
  --key key1
```

### Mount share with updated credentials
```bash
sudo mount -t cifs //myaccount.file.core.windows.net/myshare /mnt/myshare \
  -o vers=3.0,username=myuser,password=NewKey123,dir_mode=0777,file_mode=0777
```

## Examples
### Create new file share
```bash
az storage share-rm create \
  --resource-group myResourceGroup \
  --storage-account myStorageAccount \
  --name myNewShare \
  --quota 100
```

### List share contents
```bash
az storage file list \
  --share-name myShare \
  --account-name myStorageAccount \
  --account-key myAccountKey
```

## Related Errors
- {{< relref "/cloud/azure/azure-blob-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
