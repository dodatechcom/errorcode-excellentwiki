---
title: "[Solution] Azure Diagnostic Agent Error"
description: "Fix Azure diagnostic extension agent failures preventing VM and service telemetry collection."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Diagnostic agent errors prevent Azure from collecting telemetry data from VMs and services. This results in gaps in monitoring data and broken dashboards.

## Common Causes

- Diagnostic agent extension is not installed or has been uninstalled
- Agent configuration references invalid performance counters
- Storage account for diagnostic data is full or throttled
- Agent is running an outdated version with known bugs

## How to Fix

### Check diagnostic agent status

```bash
az vm extension show \
  --resource-group myRG \
  --vm-name myVM \
  --name IaaSDiagnostics \
  --query "provisioningState"
```

### Reinstall diagnostic agent

```bash
az vm extension set \
  --resource-group myRG \
  --vm-name myVM \
  --name IaaSDiagnostics \
  --publisher Microsoft.Azure.Diagnostics \
  --version 1.18.3.0
```

### Verify agent configuration

```bash
az vm extension show \
  --resource-group myRG \
  --vm-name myVM \
  --name IaaSDiagnostics \
  --query "settings"
```

### Check diagnostic storage account

```bash
az storage account show-usage \
  --name mystorageaccount \
  --resource-group myRG \
  --query "value[?name.value=='UsedCapacity'].currentValue"
```

## Examples

- Diagnostic agent reports `EventLogFull` because the storage account is at 95% capacity
- Performance counters fail to collect because the counter path is incorrect
- Agent installation fails with `ExtensionNotSupported` on the VM OS version

## Related Errors

- [Azure Monitor Error]({{< relref "/cloud/azure/azure-monitor-error" >}}) -- General monitoring errors.
- [Azure VM Guest Diagnostics]({{< relref "/cloud/azure/azure-vm-guest-diagnostics" >}}) -- Guest diagnostics issues.
