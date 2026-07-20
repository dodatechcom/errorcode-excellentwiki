---
title: "[Solution] Azure Security Center Error — recommendation, pricing, and auto-provision failures"
description: "Fix Azure Security Center error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 160
---

Security Center errors appear as missing recommendations, auto-provision agent failures, or pricing tier misconfigurations that reduce security visibility.

## Common Causes
- Pricing tier set to Free limiting advanced recommendations
- Auto-provision agent not installed on VMs missing security data
- Regulatory compliance initiative not assigned to subscription
- Defender for Cloud not enabled for specific resource providers
- Log Analytics agent connectivity failing on hybrid machines

## How to Fix
### Check security pricing tier
```bash
az security pricing show \
  --name VirtualMachines \
  --query "pricingTier"
```

### Enable Defender for Servers
```bash
az security pricing create \
  --name VirtualMachines \
  --tier Standard
```

### List security recommendations
```bash
az security assessment list \
  --query "[].{name:name,status:status,resourceDetails:resourceDetails}" \
  --query "[0:10]"
```

### Enable auto-provisioning
```bash
az security auto-provisioning-setting update \
  --name default \
  --auto-provision On
```

## Examples
### Check compliance status
```bash
az security regulatory-compliance-standards list \
  --query "[].{name:name,state:state,failedResources:failedResources}"
```

### Get security assessment
```bash
az security assessment show \
  --name myAssessment \
  --query "status.code"
```

## Related Errors
- {{< relref "/cloud/azure/azure-sentinel-error" >}}
- {{< relref "/cloud/azure/azure-policy-error" >}}
- {{< relref "/cloud/azure/azure-advisor-error" >}}
