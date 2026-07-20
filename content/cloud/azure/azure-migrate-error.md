---
title: "[Solution] Azure Migrate Error — appliance, discovery, and assessment failures"
description: "Fix Azure Migrate error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 165
---

Migrate errors appear as appliance registration failures, VM discovery gaps, or assessment generation issues that delay migration planning.

## Common Causes
- Migrate appliance not registered with project after deployment
- Appliance connectivity failing due to proxy/firewall restrictions
- VMware vCenter credentials not valid for discovery
- Assessment project in different region than target resources
- Dependency visualization data not collecting network traffic

## How to Fix
### Check project status
```bash
az migrate project show \
  --resource-group myResourceGroup \
  --name myMigrateProject \
  --query "provisioningState"
```

### List discovered servers
```bash
az migrate solution show \
  --resource-group myResourceGroup \
  --project-name myMigrateProject \
  --name myMigrateSolution \
  --query "properties.settings.targetRegion"
```

### Update assessment settings
```bash
az migrate assessment create \
  --resource-group myResourceGroup \
  --project-name myMigrateProject \
  --group-name myServerGroup \
  --assessment-name myAssessment \
  --properties '{"sizingCriterion":"PerformanceBased","vmSize":"Standard_D4s_v3"}'
```

### Verify appliance connectivity
```bash
az migrate appliance list \
  --resource-group myResourceGroup \
  --project-name myMigrateProject \
  --query "[].{name:name,provisioningState:provisioningState}"
```

## Examples
### Create Migrate project
```bash
az migrate project create \
  --resource-group myResourceGroup \
  --name myMigrateProject \
  --location eastus
```

### Export assessment
```bash
az migrate assessment export \
  --resource-group myResourceGroup \
  --project-name myMigrateProject \
  --group-name myServerGroup \
  --assessment-name myAssessment
```

## Related Errors
- {{< relref "/cloud/azure/azure-site-recovery-error" >}}
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/azure-databox-error" >}}
