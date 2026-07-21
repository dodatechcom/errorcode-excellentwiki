---
title: "[Solution] AZURE VNet Not Found"
description: "ResourceNotFound when the specified virtual network does not exist."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VNet Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VNet name is incorrect
- VNet was deleted
- VNet in different subscription
- Resource group name is wrong

## How to Fix

### Check VNet

```bash
az network vnet show --name myVNet --resource-group myRG
```
### List VNets

```bash
az network vnet list --resource-group myRG --query "[].{Name:name,AddressSpace:addressSpace.addressPrefixes}" --output table
```
### Create VNet

```bash
az network vnet create --name myVNet --resource-group myRG --address-prefix 10.0.0.0/16 --subnet-name mySubnet --subnet-prefix 10.0.1.0/24
```

## Examples

- VNet myVNet not found in resource group
- VNet deleted but subnets still referenced

## Related Errors

- [Azure Networking Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- General networking errors
- [Subnet Not Found]({{< relref "/cloud/azure/azure-vnet-subnet-not-found" >}}) -- Subnet not found
