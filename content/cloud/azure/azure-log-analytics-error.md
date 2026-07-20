---
title: "[Solution] Azure Log Analytics Error — workspace, query, and table failures"
description: "Fix Azure Log Analytics error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 157
---

Log Analytics errors involve workspace query failures, data ingestion delays, or table retention issues that prevent operational analytics.

## Common Causes
- Workspace retention period too short for required data retention
- Query exceeding execution timeout for large datasets
- Data source not configured to send logs to workspace
- Resource-specific tables not enabled for RBAC scoping
- Cross-workspace query permissions insufficient

## How to Fix
### Check workspace status
```bash
az monitor log-analytics workspace show \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --query "provisioningState"
```

### Update retention period
```bash
az monitor log-analytics workspace update \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --retention-time 90
```

### List available tables
```bash
az monitor log-analytics workspace table list \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --query "[].{name:name,retentionInDays:retentionInDays,totalRetentionInDays:totalRetentionInDays}"
```

### Run KQL query
```bash
az monitor log-analytics query \
  --workspace myWorkspaceId \
  --analytics-query "Heartbeat | summarize count() by Computer"
```

## Examples
### Create workspace
```bash
az monitor log-analytics workspace create \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --location eastus \
  --retention-time 30
```

### Export query results
```bash
az monitor log-analytics query \
  --workspace myWorkspaceId \
  --analytics-query "Event | where Level == 'Error' | take 100" \
  --output json
```

## Related Errors
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-application-insights-error" >}}
- {{< relref "/cloud/azure/azure-sentinel-error" >}}
