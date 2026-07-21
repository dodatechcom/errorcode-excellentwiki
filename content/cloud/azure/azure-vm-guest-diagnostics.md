---
title: "[Solution] Azure VM Guest Diagnostics Error"
description: "Resolve Azure VM guest diagnostics failures preventing health monitoring and metric collection."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Guest diagnostics errors occur when Azure cannot collect health metrics or diagnostic data from a virtual machine. This prevents proactive monitoring and alerting.

## Common Causes

- VM guest diagnostics agent is not installed or has crashed
- Network connectivity between the VM and Azure monitoring endpoints is blocked
- Storage account for diagnostics logs is unreachable or throttled
- Diagnostic configuration file contains invalid counters or sinks

## How to Fix

### Install diagnostics extension

```bash
az vm extension set \
  --resource-group myRG \
  --vm-name myVM \
  --name IaaSDiagnostics \
  --publisher Microsoft.Azure.Diagnostics \
  --settings diagnostics.json
```

### Verify diagnostic settings

```bash
az monitor diagnostic-settings list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM
```

### Check diagnostic storage account

```bash
az storage account show-connection-string \
  --name mystorageaccount \
  --resource-group myRG \
  --query connectionString
```

## Examples

- Metrics stop appearing in the Azure portal after VM reboot
- Diagnostic agent reports `FailedToConnectToStorageAccount` repeatedly
- VM insights page shows stale data with no recent performance counters

## Related Errors

- [Azure Monitor Error]({{< relref "/cloud/azure/azure-monitor-error" >}}) -- Monitoring service errors.
- [Azure Diagnostic Setting]({{< relref "/cloud/azure/azure-diagnostic-setting" >}}) -- Diagnostic configuration issues.
