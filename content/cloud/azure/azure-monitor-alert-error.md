---
title: "[Solution] Azure Monitor Alert Error"
description: "Fix Azure Monitor alert rule failures that prevent proactive issue detection."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Alert rule errors prevent Azure Monitor from detecting and notifying about infrastructure issues. This can lead to undetected outages and performance degradation.

## Common Causes

- Alert rule references a metric that does not exist for the target resource
- Action group is disabled or has invalid notification targets
- Alert rule condition is misconfigured and never triggers
- Workspace-level alert rules are disabled in the subscription

## How to Fix

### List alert rules

```bash
az monitor metrics alert list \
  --resource-group myRG \
  --query "[].{Name:name,Enabled:enabled,Condition:condition.allOf[0].metricName}"
```

### Create a metric alert

```bash
az monitor metrics alert create \
  --name "HighCPU" \
  --resource-group myRG \
  --scopes /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM \
  --condition "avg Percentage CPU > 80" \
  --action myActionGroup
```

### Check action group status

```bash
az monitor action-group list \
  --resource-group myRG \
  --query "[].{Name:name,Enabled:groupShortName}"
```

### Test alert rule

```bash
az monitor metrics alert show \
  --name "HighCPU" \
  --resource-group myRG \
  --query "condition.allOf[0]"
```

## Examples

- Alert rule fails with `MetricNotFound` because the VM extension is not installed
- Action group email notifications are not received because the action group is disabled
- Alert fires but the action group webhook returns 404 because the endpoint was moved

## Related Errors

- [Azure Monitor Error]({{< relref "/cloud/azure/azure-monitor-error" >}}) -- General Monitor errors.
- [Azure Action Group]({{< relref "/cloud/azure/azure-action-group" >}}) -- Action group issues.
