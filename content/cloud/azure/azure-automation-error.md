---
title: "[Solution] Azure Automation Error — runbook, variable, and credential failures"
description: "Fix Azure Automation error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 148
---

Automation errors involve runbook job failures, variable asset retrieval issues, or credential store access problems that halt scheduled tasks.

## Common Causes
- Runbook job hitting timeout limit for long-running processes
- Variable asset encrypted with different key than accessing account
- Credential asset expired or password rotated without update
- Python runbook module compatibility issues with automation runtime
- Hybrid worker not connected or offline for on-premises execution

## How to Fix
### Check runbook status
```bash
az automation runbook show \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation \
  --name myRunbook \
  --query "provisioningState"
```

### List runbook jobs
```bash
az automation job list \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation \
  --runbook-name myRunbook \
  --query "[].{jobId:jobId, status:status, startTime:startTime}"
```

### Update variable value
```bash
az automation variable update \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation \
  --name myVariable \
  --value "newValue123"
```

### Start runbook
```bash
az automation runbook start \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation \
  --name myRunbook
```

## Examples
### Create new runbook
```bash
az automation runbook create \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation \
  --name myNewRunbook \
  --type PowerShell \
  --description "My automation runbook"
```

### List hybrid workers
```bash
az automation hybrid-worker-group list \
  --resource-group myResourceGroup \
  --automation-account-name myAutomation
```

## Related Errors
- {{< relref "/cloud/azure/azure-policy-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
