---
title: "[Solution] Azure VM Scale Set Error — scaling, upgrade, and health failures"
description: "Fix Azure VM Scale Set error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 116
---

VMSS errors include scaling delays, rolling upgrade failures, or instance health probe mismatches that cause service degradation under load.

## Common Causes
- Autoscale metric threshold not triggering scale-out during load
- Instance not reaching running state due to extension failures
- Rolling upgrade policy stopping on first failure
- Health probe not configured causing instances to stay in unhealthy state
- Spot instance eviction during scaling operations

## How to Fix
### Check scale set instance health
```bash
az vmss list-instances \
  --resource-group myResourceGroup \
  --vmss-name myVMSS \
  --query "[].{instanceId:instanceId, provisioningState:provisioningState, powerState:powerState}"
```

### Update autoscale rule
```bash
az monitor autoscale rule create \
  --resource-group myResourceGroup \
  --autoscale-name myAutoscale \
  --condition "Percentage CPU > 70 avg 5m" \
  --scale out 2
```

### Set rolling upgrade policy
```bash
az vmss update \
  --resource-group myResourceGroup \
  --name myVMSS \
  --set upgradePolicy.rollingUpgradePolicy.maxBatchInstancePercent=20 \
  --set upgradePolicy.rollingUpgradePolicy.maxUnhealthyInstancePercent=20 \
  --set upgradePolicy.rollingUpgradePolicy.maxUnhealthyUpgradedInstancePercent=20
```

### Redeploy failed instance
```bash
az vmss redeploy \
  --resource-group myResourceGroup \
  --vmss-name myVMSS \
  --instance-id 0
```

## Examples
### Manually add instances
```bash
az vmss scale \
  --resource-group myResourceGroup \
  --name myVMSS \
  --new-capacity 5
```

### Check instance extension status
```bash
az vmss extension list \
  --resource-group myResourceGroup \
  --vmss-name myVMSS \
  --instance-id 0
```

## Related Errors
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-load-balancer-error" >}}
