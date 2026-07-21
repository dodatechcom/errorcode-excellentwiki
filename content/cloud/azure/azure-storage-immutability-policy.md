---
title: "[Solution] Azure Storage Immutability Policy Error"
description: "Resolve Azure Blob Storage immutability policy errors that block data modifications and deletions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Immutability policy errors prevent modification or deletion of blob data during the policy retention period. This is useful for compliance but can cause operational issues.

## Common Causes

- Immutability policy is set and blobs cannot be deleted or modified until it expires
- Legal hold is applied without an expiration date
- Policy was applied at the container level to all blobs unintentionally
- Attempting to change blob tier while immutability policy is active

## How to Fix

### Check immutability policy

```bash
az storage blob immutability-policy show \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --blob-name myblob.txt
```

### Set immutability policy with expiration

```bash
az storage blob immutability-policy set \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --blob-name myblob.txt \
  --period 365 \
  --policy-mode Unlocked
```

### Remove legal hold

```bash
az storage blob legal-hold release \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --tags tag1 tag2
```

### List all immutability policies

```bash
az storage blob list \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --query "[].{Name:name,ImmutabilityPolicy:properties.immutabilityPolicy}"
```

## Examples

- Delete operation fails with `ImmutabilityPolicyViolation` for blobs under active policy
- Blob tier change from Hot to Cool is blocked because immutability policy is set
- Container-level immutability policy prevents deleting old backups that should be removed

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- General storage errors.
- [Azure Storage Lifecycle]({{< relref "/cloud/azure/azure-storage-lifecycle" >}}) -- Lifecycle management.
