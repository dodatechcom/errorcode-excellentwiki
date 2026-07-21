---
title: "[Solution] Azure Security Center Compliance Error"
description: "Fix Azure Security Center compliance assessment failures and false positive findings."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Compliance errors in Security Center occur when the service cannot accurately assess resource security posture. This leads to incorrect compliance scores and missed vulnerabilities.

## Common Causes

- Defender for Cloud plan is not enabled for the target resource type
- Resource agent is not reporting data to Security Center
- Compliance policy assignment has conflicting definitions across management groups
- Assessment scope is too narrow and misses non-compliant resources

## How to Fix

### Check Defender plan status

```bash
az security pricing list \
  --query "[].{Name:name,Enabled:pricingTier}"
```

### Enable Defender for a resource type

```bash
az security pricing create \
  --name VirtualMachines \
  --tier Standard
```

### Check compliance state

```bash
az security sub-assessment list \
  --assessed-resource-id "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM" \
  --assessment-name "a]4b2002f-755e-4e02-a555-6a7a8a8a8a8a" \
  --query "[].{Status:status.code,Name:displayName}"
```

### Generate compliance report

```bash
az security regulatory-compliance-standards list \
  --query "[].{Name:name,State:state}"
```

## Examples

- Compliance score shows 60% because Defender for Storage is not enabled
- Assessment shows `NotEvaluated` for VMs because the Log Analytics agent is not installed
- Policy shows `NonCompliant` for disk encryption but the VM uses host-based encryption

## Related Errors

- [Azure Security Center Error]({{< relref "/cloud/azure/azure-security-center-error" >}}) -- General Security Center errors.
- [Azure Policy Error]({{< relref "/cloud/azure/azure-policy-error" >}}) -- Policy issues.
