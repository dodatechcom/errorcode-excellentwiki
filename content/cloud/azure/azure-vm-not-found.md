---
title: "[Solution] AZURE VM Not Found"
description: "ResourceNotFound when the specified VM cannot be located."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VM name is incorrect
- VM was deleted
- VM in different resource group
- Subscription ID is wrong

## How to Fix

### Check VM

```bash
az vm show --name myVM --resource-group myRG
```
### List VMs

```bash
az vm list --query "[].{Name:name,ResourceGroup:resourceGroup,Status:powerState}" --output table
```
### Create VM

```bash
az vm create --name myVM --resource-group myRG --image UbuntuLTS --admin-username azureuser --generate-ssh-keys
```

## Examples

- VM myVM not found in resource group myRG
- VM deleted but still referenced in code

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors
- [Allocation Failed]({{< relref "/cloud/azure/azure-vm-allocation-failed" >}}) -- Allocation failures
