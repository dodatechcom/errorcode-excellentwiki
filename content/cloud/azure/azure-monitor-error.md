---
title: "[Solution] Azure Monitor Error — metrics, alert, and action group failures"
description: "Fix Azure Monitor error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 156
---

Monitor errors involve metric collection gaps, alert rule misconfigurations, or action group notification failures that impact operational visibility.

## Common Causes
- Metric namespace not supported for the resource provider
- Alert condition threshold not matching expected workload patterns
- Action group webhook endpoint returning non-200 responses
- Diagnostic settings not enabled on monitored resource
- Time grain interval causing metric data gaps

## How to Fix
### Check metric availability
```bash
az monitor metrics list-definitions \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --query "[?contains(name,'Percentage')].{name:name,metricName:metricNames[0]}"
```

### Create alert rule
```bash
az monitor metrics alert create \
  --name "HighCPUAlert" \
  --resource-group myResourceGroup \
  --scopes /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --condition "avg Percentage CPU > 80" \
  --window-size 5m \
  --evaluation-frequency 1m \
  --action myActionGroup
```

### Create action group
```bash
az monitor action-group create \
  --resource-group myResourceGroup \
  --name myActionGroup \
  --short-name myAlertGroup \
  --action email myEmail admin@contoso.com
```

### Enable diagnostic settings
```bash
az monitor diagnostic-settings create \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --name myDiagnostics \
  --storage-account myStorageAccount \
  --logs '[{"category":"Audit","enabled":true}]'
```

## Examples
### List active alerts
```bash
az monitor metrics alert list \
  --resource-group myResourceGroup \
  --query "[].{name:name,severity:severity,enabled:enabled}"
```

### Check metric values
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --metric "Percentage CPU" \
  --aggregation Average \
  --interval PT1M
```

## Related Errors
- {{< relref "/cloud/azure/azure-log-analytics-error" >}}
- {{< relref "/cloud/azure/azure-application-insights-error" >}}
- {{< relref "/cloud/azure/azure-action-group-error" >}}
