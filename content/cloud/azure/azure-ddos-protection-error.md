---
title: "[Solution] Azure DDoS Protection Error"
description: "Fix Azure DDoS protection configuration errors that leave resources vulnerable to attacks."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

DDoS protection errors occur when the protection plan is not properly configured or is not mitigating attacks. This exposes resources to volumetric and protocol attacks.

## Common Causes

- DDoS protection plan is not associated with the VNet
- Alert thresholds are set too high and attacks go undetected
- DDoS telemetry is not being sent to Log Analytics workspace
- Protection plan is in a different region than the protected VNet

## How to Fix

### Check DDoS protection status

```bash
az network vnet show \
  --name myVNet \
  --resource-group myRG \
  --query "enableDdosProtection"
```

### Enable DDoS protection

```bash
az network vnet update \
  --name myVNet \
  --resource-group myRG \
  --set enableDdosProtection=true \
  --set DdosProtectionPlan.id="/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/ddosProtectionPlans/myDDoSPlan"
```

### Create a DDoS protection plan

```bash
az network ddos-protection create \
  --name myDDoSPlan \
  --resource-group myRG
```

### Monitor DDoS telemetry

```bash
az monitor log-analytics query \
  --workspace myWorkspaceId \
  --analytics-query "AzureDiagnostics | where Category == 'DDoSDosAttackMetrics' | take 100"
```

## Examples

- VNet does not show DDoS protection as enabled even though the plan is associated
- DDoS mitigation does not activate during an attack because the plan is in a different subscription
- Telemetry shows attack but no mitigation because the VNet is not protected

## Related Errors

- [Azure DDoS Protection Error]({{< relref "/cloud/azure/azure-ddos-protection-error" >}}) -- General DDoS errors.
- [Azure VNet Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- VNet configuration.
