---
title: "[Solution] Azure Dedicated Host Error — allocation, group, and placement failures"
description: "Fix Azure Dedicated Host error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 117
---

Dedicated Host errors occur when host allocation fails, VM placement cannot satisfy constraints, or host group capacity is exhausted.

## Common Causes
- Host SKU or zone not available in target region
- Host group fault domain count exceeding available hosts
- VM size incompatible with dedicated host SKU
- Host capacity exhausted preventing new VM allocation
- Automatic placement disabled causing manual scheduling issues

## How to Fix
### Check host allocation state
```bash
az dedicated-host list \
  --resource-group myResourceGroup \
  --host-group-name myHostGroup \
  --query "[].{name:name, platformFaultDomain:platformFaultDomain, allocationState:allocationState}"
```

### Create new dedicated host
```bash
az dedicated-host create \
  --resource-group myResourceGroup \
  --host-group-name myHostGroup \
  --name myHost \
  --sku DSv3-Type1 \
  --platform-fault-domain 0 \
  --location eastus
```

### Place VM on dedicated host
```bash
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --size Standard_D4s_v3 \
  --host-group myHostGroup \
  --host myHost
```

### Update host capacity
```bash
az dedicated-host update \
  --resource-group myResourceGroup \
  --host-group-name myHostGroup \
  --name myHost \
  --auto-placement true
```

## Examples
### List available host SKUs
```bash
az dedicated-host list-vm-skus \
  --resource-group myResourceGroup \
  --host-group-name myHostGroup
```

### Check host group with placement policy
```bash
az dedicated-host-group show \
  --resource-group myResourceGroup \
  --name myHostGroup \
  --query "supportAutomaticPlacement"
```

## Related Errors
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/azure-quota-exceeded" >}}
- {{< relref "/cloud/azure/azure-vmss-error" >}}
