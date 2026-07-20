---
title: "[Solution] Azure DDoS Protection Error — policy, metrics, and alert failures"
description: "Fix Azure DDoS Protection error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 108
---

DDoS Protection errors involve protection not activating during attacks, false positive alerts, or metric monitoring gaps that leave resources unprotected.

## Common Causes
- DDoS protection plan not associated with the VNet
- Alert rules using incorrect thresholds for normal traffic patterns
- Protected public IP not included in DDoS protection policy
- Metric logs not routed to Log Analytics for analysis
- Auto-tuned mitigation thresholds too aggressive for legitimate traffic

## How to Fix
### Check DDoS plan association
```bash
az network vnet show \
  --resource-group myResourceGroup \
  --name myVNet \
  --query "ddosProtectionPlan"
```

### Associate VNet with DDoS plan
```bash
az network vnet update \
  --resource-group myResourceGroup \
  --name myVNet \
  --ddos-protection-plan myDdosPlan
```

### Create alert rule for DDoS mitigation
```bash
az monitor metrics alert create \
  --name "DDoSMitigationAlert" \
  --resource-group myResourceGroup \
  --scopes /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/publicIPAddresses/myPublicIP \
  --condition "avg DDoSAttackTraffic > 1000" \
  --action myActionGroup
```

### Enable DDoS telemetry to Log Analytics
```bash
az network watcher flow-log create \
  --resource-group myResourceGroup \
  --nsg myNSG \
  --name myFlowLog \
  --storage-account myStorageAccount \
  --workspace myLogAnalytics \
  --enabled true
```

## Examples
### View DDoS protection metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/publicIPAddresses/myPublicIP \
  --metric "UnderDDoSAttack,AttackMitigationAction"
```

### List DDoS protection plans
```bash
az network ddos-protection list \
  --resource-group myResourceGroup
```

## Related Errors
- {{< relref "/cloud/azure/nsg-error" >}}
- {{< relref "/cloud/azure/azure-firewall-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
