---
title: "[Solution] AZURE Storage Account Not Found"
description: "ResourceNotFound when the specified storage account does not exist."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Account Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Account name is incorrect
- Account was deleted
- Account in different subscription
- Account name is globally unique and taken

## How to Fix

### Check account

```bash
az storage account show --name mystorageaccount --resource-group myRG
```
### List accounts

```bash
az storage account list --resource-group myRG --query "[].{Name:name,SKU:sku.name}" --output table
```
### Create account

```bash
az storage account create --name mystorageaccount --resource-group myRG --location eastus --sku Standard_LRS
```

## Examples

- Storage account not found in resource group
- Account name contains invalid characters

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- General storage errors
- [Access Key]({{< relref "/cloud/azure/azure-storage-access-key" >}}) -- Access key issues
