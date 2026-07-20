---
title: "[Solution] Azure Data Lake Error — ACL, firewall, and path failures"
description: "Fix Azure Data Lake error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 125
---

Data Lake Gen2 errors involve ACL permission denied, firewall blocking access, or path operations failing on hierarchical namespace-enabled accounts.

## Common Causes
- POSIX ACL permissions not set correctly for user or group
- Data Lake firewall rules blocking client IP ranges
- Hierarchical namespace not enabled on storage account
- Path depth exceeding namespace limits
- Service endpoint not configured for Data Lake traffic

## How to Fix
### Set POSIX ACL on directory
```bash
az storage fs access set \
  --path myDirectory \
  --file-system myFileSystem \
  --account-name myDataLakeAccount \
  --account-key myAccountKey \
  --permissions rwxrwxrwx
```

### Check effective permissions
```bash
az storage fs access show \
  --path myDirectory \
  --file-system myFileSystem \
  --account-name myDataLakeAccount \
  --account-key myAccountKey
```

### Enable firewall rule
```bash
az storage account network-rule add \
  --resource-group myResourceGroup \
  --account-name myDataLakeAccount \
  --ip-address 203.0.113.0/24
```

### Create file system
```bash
az storage fs create \
  --name myFileSystem \
  --account-name myDataLakeAccount \
  --account-key myAccountKey
```

## Examples
### Upload file to Data Lake
```bash
az storage fs file upload \
  --file-system myFileSystem \
  --path myDirectory/file.csv \
  --source ./file.csv \
  --account-name myDataLakeAccount \
  --account-key myAccountKey
```

### List directory contents
```bash
az storage fs file list \
  --file-system myFileSystem \
  --path myDirectory \
  --account-name myDataLakeAccount \
  --account-key myAccountKey
```

## Related Errors
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-blob-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
