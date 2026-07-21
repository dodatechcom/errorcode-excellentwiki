---
title: "[Solution] AZURE VM Allocation Failed"
description: "AllocationFailed when Azure cannot allocate a VM in the target region/zone."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Allocation Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Region has insufficient capacity
- All zones at capacity
- VM size not available in region
- vCPU quota exceeded

## How to Fix

### Try different size

```bash
az vm create --name myVM --resource-group myRG --image UbuntuLTS --size Standard_D2s_v3
```
### Try different region

```bash
az vm create --name myVM --resource-group myRG --image UbuntuLTS --location eastus2
```
### Check quota

```bash
az vm list-usage --location eastus --query "[?name.value==`standardDSv3Family`].{Current:currentValue,Max:limit}" --output table
```

## Examples

- Standard_M128s not available in eastus-1 zone
- vCPU quota of 100 exceeded

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors
- [Capacity Insufficient]({{< relref "/cloud/azure/azure-vm-capacity-insufficient" >}}) -- Capacity
