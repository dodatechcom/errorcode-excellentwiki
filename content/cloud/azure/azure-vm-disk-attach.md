---
title: "[Solution] AZURE VM Disk Attach Error"
description: "DiskAttachFailed when attaching a managed disk to a VM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Disk Attach Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Disk already attached to another VM
- Disk type not supported on VM size
- Max data disks reached
- Disk in different resource group

## How to Fix

### Check disk state

```bash
az disk show --name myDisk --resource-group myRG --query "{State:diskState,Size:diskSizeGb,Type:storageAccountType}" --output table
```
### Detach disk

```bash
az vm disk detach --resource-group myRG --vm-name myVM --name myDisk
```
### Attach disk

```bash
az vm disk attach --resource-group myRG --vm-name myVM --name myDisk
```

## Examples

- Disk attached to VM-A but trying to attach to VM-B
- UltraSSD on Standard_B2s that does not support it

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors
- [Disk Not Found]({{< relref "/cloud/azure/azure-vm-disk-not-found" >}}) -- Disk not found
