---
title: "[Solution] Azure VM Boot Diagnostics Error"
description: "Fix Azure VM boot diagnostics failures that prevent screenshot and serial log capture during boot."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Boot diagnostics errors prevent Azure from capturing VM screenshots and serial console logs during the boot process. This makes it difficult to troubleshoot VM startup failures.

## Common Causes

- Boot diagnostics storage account is missing or has been deleted
- Managed storage account is disabled but boot diagnostics expects it
- Storage account is read-only due to an immutability policy
- VM was moved across regions without updating the diagnostics configuration

## How to Fix

### Enable boot diagnostics with managed storage

```bash
az vm boot-diagnostics enable \
  --resource-group myRG \
  --name myVM
```

### Retrieve serial console log

```bash
az vm boot-diagnostics get-boot-log \
  --resource-group myRG \
  --name myVM
```

### Disable and re-enable boot diagnostics

```bash
az vm boot-diagnostics disable \
  --resource-group myRG \
  --name myVM

az vm boot-diagnostics enable \
  --resource-group myRG \
  --name myVM
```

## Examples

- Boot diagnostics tab shows blank screenshot after enabling managed storage
- Serial log retrieval fails with `StorageAccountNotFound` error
- VM serial console is empty after switching from custom storage to managed storage

## Related Errors

- [Azure VM Boot Diagnostics Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM issues.
- [Azure Storage Account Not Found]({{< relref "/cloud/azure/azure-storage-account-not-found" >}}) -- Missing storage account.
