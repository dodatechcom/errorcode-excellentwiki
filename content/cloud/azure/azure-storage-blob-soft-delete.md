---
title: "[Solution] Azure Storage Blob Soft Delete Error"
description: "Fix Azure Blob Storage soft delete issues preventing accidental deletion recovery."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Soft delete errors occur when Azure Blob Storage cannot properly retain deleted blobs for recovery. This can lead to permanent data loss or inability to restore deleted data.

## Common Causes

- Soft delete policy is not enabled on the storage account
- Retention period is set to 0 days, making deletions permanent
- Container-level soft delete is not configured separately from blob-level
- RBAC permissions prevent the user from restoring deleted blobs

## How to Fix

### Enable soft delete for blobs

```bash
az storage account blob-service-properties update \
  --account-name mystorageaccount \
  --resource-group myRG \
  --enable-delete-retention true \
  --delete-retention-days 14
```

### Enable container soft delete

```bash
az storage account blob-service-properties update \
  --account-name mystorageaccount \
  --resource-group myRG \
  --enable-container-delete-retention true \
  --container-delete-retention-days 7
```

### Restore a deleted blob

```bash
az storage blob undelete \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --name myblob.txt
```

### List deleted blobs

```bash
az storage blob list \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --include deleted \
  --query "[].{Name:name,Deleted:deletedTime,Remaining:remainingRetentionDays}"
```

## Examples

- Blob was deleted 2 days ago but soft delete is not enabled so it cannot be restored
- Container soft delete is enabled but blobs inside are not recovered due to missing blob-level policy
- Restore fails with `AccessDenied` because the user lacks storage blob data contributor role

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- General storage errors.
- [Azure Blob Not Found]({{< relref "/cloud/azure/azure-blob-not-found" >}}) -- Blob missing errors.
