---
title: "[Solution] AZURE Storage Access Key Error"
description: "InvalidAuthenticationInfo when the access key is wrong or rotated."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Access Key Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Key was rotated and old key cached
- Key copied incorrectly
- Account re-keyed and both keys changed
- Connection string format incorrect

## How to Fix

### Show keys

```bash
az storage account keys list --account-name mystorageaccount --resource-group myRG --query "[].{Key:keyName,Value:value}" --output table
```
### Regenerate key

```bash
az storage account keys renew --account-name mystorageaccount --resource-group myRG --key key1
```
### Test connection

```bash
az storage blob list --account-name mystorageaccount --container-name mycontainer --output table
```

## Examples

- Application using key2 but it was just rotated
- Access key copied with trailing space

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- General storage errors
- [SAS Token]({{< relref "/cloud/azure/azure-storage-sas-token" >}}) -- SAS token issues
