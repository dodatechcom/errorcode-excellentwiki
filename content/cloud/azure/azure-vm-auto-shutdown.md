---
title: "[Solution] Azure VM Auto Shutdown Error"
description: "Troubleshoot Azure VM scheduled auto shutdown not triggering or failing to deallocate VMs."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Auto shutdown errors occur when scheduled VM shutdown fails to deallocate or stop VMs at the configured time. This can lead to unexpected resource costs.

## Common Causes

- VM is in a deallocated state already and cannot be stopped
- RBAC permissions prevent the scheduled task from executing
- VM is locked by a resource lock that blocks the shutdown operation
- Time zone configuration is incorrect in the auto shutdown schedule

## How to Fix

### Check auto shutdown configuration

```bash
az vm auto-shutdown list \
  --resource-group myRG
```

### Create auto shutdown schedule

```bash
az graph query -q "Resources | where type == 'microsoft.devtestlab/schedules' | project name, properties.targetResourceId, properties.status"
```

### Disable conflicting resource locks

```bash
az lock list \
  --resource-group myRG \
  --query "[].{Name:name,Type:lockType}"
```

## Examples

- Scheduled shutdown runs but the VM remains in a running state
- Auto shutdown notification fires but VM is not deallocated
- Shutdown works for some VMs but not for others in the same resource group

## Related Errors

- [Azure VM Stop Failed]({{< relref "/cloud/azure/azure-stop-failed" >}}) -- VM cannot be stopped.
- [Azure Resource Locks Error]({{< relref "/cloud/azure/azure-resource-locks-error" >}}) -- Resource lock issues.
