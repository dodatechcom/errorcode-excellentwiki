---
title: "[Solution] Azure Data Lake Access Error"
description: "Fix Azure Data Lake Storage Gen2 access permission and connectivity errors."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Data Lake access errors prevent applications and services from reading or writing to Data Lake Storage. This breaks data pipelines and analytics workloads.

## Common Causes

- Identity does not have the Storage Blob Data Contributor role on the Data Lake account
- Hierarchical namespace is not enabled, causing POSIX permission issues
- Data Lake firewall blocks the client IP address
- OAuth token for ADLS Gen2 authentication has expired

## How to Fix

### Check RBAC assignments

```bash
az role assignment list \
  --assignee appId \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myDataLake \
  --query "[].roleDefinitionName"
```

### Assign Storage Blob Data Contributor

```bash
az role assignment create \
  --assignee appId \
  --role "Storage Blob Data Contributor" \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myDataLake
```

### Enable hierarchical namespace

```bash
az storage account update \
  --name myDataLake \
  --resource-group myRG \
  --enable-hierarchical-namespace true
```

### Test access with AzCopy

```bash
azcopy copy "https://myDataLake.dfs.core.windows.net/mycontainer/myfolder/*" "./localdir/" --recursive
```

## Examples

- Data Factory pipeline fails with `AuthorizationPermissionMismatch` when writing to Data Lake
- Spark job cannot read Parquet files from Data Lake because the managed identity lacks permissions
- Data Lake firewall blocks access from a VNet without a service endpoint configured

## Related Errors

- [Azure Data Lake Error]({{< relref "/cloud/azure/azure-data-lake-error" >}}) -- General Data Lake errors.
- [Azure Data Lake Gen2]({{< relref "/cloud/azure/azure-data-lake-gen2" >}}) -- Gen2 issues.
