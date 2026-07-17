---
title: "[Solution] Azure Blob Storage Error"
description: "Fix Azure Blob Storage errors. Resolve blob upload, download, and access issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure Blob Storage error occurs when operations on blob storage fail. This can be caused by permissions, configuration, or network issues.

## Common Causes

- Container does not exist or is private
- SAS token is expired or has wrong permissions
- Blob size exceeds block size limits
- CORS policy blocks the request
- Access tier incompatible with operation

## How to Fix

### List Containers

```bash
az storage container list --account-name myaccount --account-key $KEY
```

### Upload Blob

```bash
az storage blob upload --container-name mycontainer --name myblob \
  --file ./local.txt --account-name myaccount --account-key $KEY
```

### Generate SAS Token

```bash
az storage blob generate-sas --container-name mycontainer --name myblob \
  --account-name myaccount --account-key $KEY \
  --permissions rw --expiry 2024-12-31
```

### Set CORS Rules

```bash
az storage cors add --services b --methods GET POST PUT \
  --origins "*" --headers "*" --account-name myaccount --account-key $KEY
```

## Examples

```bash
# Example 1: Container not found
# The specified container does not exist
# Fix: create container first

# Example 2: SAS expired
# Forbidden: SAS token has expired
# Fix: generate new SAS token
```

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) — Storage error
- [Azure CDN Error]({{< relref "/cloud/azure/azure-cdn-error" >}}) — CDN error
