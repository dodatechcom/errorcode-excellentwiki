---
title: "Azure DiskError: I/O Operation Failed"
description: "DiskError: I/O operation failed — Fix Azure managed disk I/O errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `DiskError: I/O operation failed` error occurs when Azure managed disk encounters an I/O failure. This can happen during read/write operations on VM disks and may indicate disk corruption, performance issues, or storage infrastructure problems.

## Common Causes

- Disk IOPS or throughput limit exceeded for the disk tier
- Disk is in a degraded state (storage infrastructure issue)
- The VM is using a shared disk with conflicting access
- Filesystem corruption on the disk
- Detaching a disk while I/O operations are in progress

## How to Fix

Check disk health and performance:

```bash
az disk show \
  --name my-disk \
  --resource-group my-rg \
  --query '{State:diskState,Tier:sku.name,Size:diskSizeGB,IOPS:diskIOPSReadWriteThroughput}'
```

Resize the disk for better performance:

```bash
az disk update \
  --name my-disk \
  --resource-group my-rg \
  --sku Premium_LRS \
  --disk-size-gb 512
```

Check VM disk attachment:

```bash
az vm show \
  --name my-vm \
  --resource-group my-rg \
  --query 'storageProfile.dataDisks[].{Name:name,Size:diskSizeGB,State:managedDisk.id}'
```

Detach and reattach the disk:

```bash
# Detach
az vm disk detach --vm-name my-vm --resource-group my-rg --name my-disk

# Reattach
az vm disk attach --vm-name my-vm --resource-group my-rg --disk my-disk
```

## Examples

- Database VM encounters I/O errors because the Standard HDD disk tier IOPS are exhausted
- Disk corruption after a forced VM shutdown — detach the disk and run chkdsk/fsck from a recovery VM
- Shared disk error when two VMs try to write simultaneously without proper locking

## Related Errors

- [Azure VM Not Found]({{< relref "/cloud/azure/vm-not-found" >}}) — VM resource not found.
- [Azure Storage Error]({{< relref "/cloud/azure/storage-error" >}}) — storage account issues.
- [Azure AKS Error]({{< relref "/cloud/azure/aks-error" >}}) — AKS cluster issues.
