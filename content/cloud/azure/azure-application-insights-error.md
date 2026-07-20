---
title: "[Solution] Azure Application Insights Error — instrumentation, sampling, and dependency failures"
description: "Fix Azure Application Insights error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 158
---

Application Insights errors appear as missing telemetry data, sampling discarding critical traces, or dependency monitoring gaps that affect observability.

## Common Causes
- Instrumentation key not configured in application settings
- Sampling percentage too aggressive filtering out important events
- Live Metrics not receiving data from monitored application
- Dependency telemetry collection disabled in SDK configuration
- Connection string format incorrect for newer SDK versions

## How to Fix
### Check Application Insights resource
```bash
az monitor app-insights component show \
  --resource-group myResourceGroup \
  --app myAppInsights \
  --query "provisioningState"
```

### Update sampling settings
```bash
az monitor app-insights component update \
  --resource-group myResourceGroup \
  --app myAppInsights \
  --set "samplingConfiguration.maxTelemetryItemsPerSecond=20"
```

### Create Application Insights
```bash
az monitor app-insights component create \
  --resource-group myResourceGroup \
  --app myAppInsights \
  --location eastus \
  --kind web \
  --workspace /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.OperationalInsights/workspaces/myWorkspace
```

### List availability tests
```bash
az monitor app-insights availability-test list \
  --resource-group myResourceGroup \
  --app myAppInsights
```

## Examples
### Get instrumentation key
```bash
az monitor app-insights component show \
  --resource-group myResourceGroup \
  --app myAppInsights \
  --query "instrumentationKey"
```

### Check live metrics
```bash
az monitor app-insights component show \
  --resource-group myResourceGroup \
  --app myAppInsights \
  --query "connectionString"
```

## Related Errors
- {{< relref "/cloud/azure/azure-log-analytics-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-app-service-error" >}}
