---
title: "Azure StorageAccount: The Specified Container Does Not Exist"
description: "StorageAccount: The specified container does not exist — Fix Azure Blob Storage container errors."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "storage", "blob", "container", "not-found", "account"]
weight: 5
---

The `The specified container does not exist` error occurs when an Azure Blob Storage API call references a container that has not been created or is in a different storage account. This is one of the most common Azure Storage errors.

## Common Causes

- The container was never created in the storage account
- Wrong storage account name in the connection string or configuration
- The container name contains invalid characters (must be lowercase, no special chars except `-`)
- The container was deleted and the reference is stale

## How to Fix

Check if the container exists:

```bash
az storage container list \
  --account-name mystorageaccount \
  --account-key <key> \
  --query '[].name'
```

Create the container if it does not exist:

```bash
az storage container create \
  --name my-container \
  --account-name mystorageaccount \
  --account-key <key>
```

Verify storage account name in the connection string:

```bash
az storage account show-connection-string \
  --name mystorageaccount \
  --resource-group my-rg
```

Update the connection string in the application:

```bash
az webapp config connection-string set \
  --name my-app \
  --resource-group my-rg \
  --connection-string-type Custom \
  --settings "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=<key>;EndpointSuffix=core.windows.net"
```

## Examples

- Azure Function tries to write to a queue in a container that does not exist
- Connection string points to `myaccount` but the actual account is `my-storage-account`
- Container name in configuration has uppercase letters, but Azure requires lowercase

## Related Errors

- [Azure KeyVault Error]({{< relref "/cloud/azure/keyvault-error" >}}) — KeyVault access denied.
- [Azure Disk Error]({{< relref "/cloud/azure/disk-error" >}}) — disk I/O failure.
- [AWS S3 AccessDenied]({{< relref "/cloud/aws/s3-access-denied2" >}}) — S3 access denied.
