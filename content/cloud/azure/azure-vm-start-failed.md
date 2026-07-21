---
title: "[Solution] AZURE VM Start Failed"
description: "VMStartFailed when Azure cannot start the specified VM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Start Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VM already running
- OS disk corrupted
- VM in failed state
- Azure infrastructure issue

## How to Fix

### Check VM status

```bash
az vm get-instance-view --name myVM --resource-group myRG --query powerState --output tsv
```
### Start VM

```bash
az vm start --name myVM --resource-group myRG
```
### Redeploy VM

```bash
az vm redeploy --name myVM --resource-group myRG
```

## Examples

- VM stuck in stopped state after start
- OS disk in failed state preventing boot

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors
- [Stop Failed]({{< relref "/cloud/azure/azure-vm-stop-failed" >}}) -- Stop errors
