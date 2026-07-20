---
title: "[Solution] Azure Logic Apps Error — workflow, trigger, and action failures"
description: "Fix Azure Logic Apps error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 146
---

Logic Apps errors involve workflow run failures, trigger misconfigurations, or connector authentication issues that prevent automation execution.

## Common Causes
- Recurrence trigger interval set incorrectly causing missed runs
- Connector API connection expired or credentials rotated
- Workflow run history limit reached causing execution failures
- Managed identity not granted required API permissions
- HTTP trigger returning non-success status codes

## How to Fix
### Check workflow status
```bash
az logic workflow show \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --query "provisioningState"
```

### List workflow runs
```bash
az logic workflow list-runs \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --query "[].{runId:runId, status:status, startTime:startTime}"
```

### Update workflow definition
```bash
az logic workflow update \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --definition @workflow.json
```

### Enable managed identity for workflow
```bash
az logic workflow update \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --set "identity.type=SystemAssigned"
```

## Examples
### Create Logic App
```bash
az logic workflow create \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --location eastus \
  --definition @myworkflow.json
```

### Trigger manual run
```bash
az logic workflow trigger run \
  --resource-group myResourceGroup \
  --name myLogicApp \
  --trigger-name manualTrigger
```

## Related Errors
- {{< relref "/cloud/azure/azure-api-management-error" >}}
- {{< relref "/cloud/azure/azure-app-service-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
