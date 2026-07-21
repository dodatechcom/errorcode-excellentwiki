---
title: "[Solution] AZURE VM Stop Failed"
description: "VMStopDeallocateFailed when Azure cannot stop the VM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Stop Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VM already stopped
- Third-party agent blocking shutdown
- VM part of VMSS with autoscaling
- Stop operation timed out

## How to Fix

### Check status

```bash
az vm get-instance-view --name myVM --resource-group myRG --query powerState --output tsv
```
### Force stop

```bash
az vm stop --name myVM --resource-group myRG --no-wait
```
### Redeploy

```bash
az vm redeploy --name myVM --resource-group myRG
```

## Examples

- Custom extension blocking shutdown
- VMSS VM cannot be stopped while autoscaler active

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors
- [Start Failed]({{< relref "/cloud/azure/azure-vm-start-failed" >}}) -- Start errors
