---
title: "[Solution] Azure Advisor Error — recommendation, alert, and suppression failures"
description: "Fix Azure Advisor error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 161
---

Advisor errors involve missing recommendations, alert suppression not working, or recommendation categories not displaying expected guidance.

## Common Causes
- Subscription not eligible for Advisor recommendations
- Recommendation category filtered hiding important alerts
- Suppression rules expiring without renewal
- Advisor API throttled due to excessive polling
- Resource provider not registered blocking recommendation generation

## How to Fix
### List all recommendations
```bash
az advisor recommendation list \
  --query "[].{category:category,impact:impact,description:properties.shortDescription.solution}"
```

### Suppress specific recommendation
```bash
az advisor recommendation suppress \
  --resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --rule-name mySuppressionRule \
  --ttl 30
```

### Get recommendation details
```bash
az advisor recommendation show \
  --name myRecommendation \
  --resource-group myResourceGroup \
  --query "properties"
```

### Refresh recommendations
```bash
az advisor recommendation list \
  --category HighAvailability \
  --query "[].{name:name,status:status}"
```

## Examples
### List cost recommendations
```bash
az advisor recommendation list \
  --category Cost \
  --query "[].{name:name,impact:impact,description:properties.shortDescription.solution}"
```

### Check Advisor configuration
```bash
az advisor configuration show \
  --query "lowCpuThreshold"
```

## Related Errors
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-cost-management-error" >}}
- {{< relref "/cloud/azure/azure-security-center-error" >}}
