---
title: "[Solution] Azure Policy Error — assignment, definition, and remediation failures"
description: "Fix Azure Policy error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 153
---

Policy errors appear as assignment failures, non-compliant resources blocking operations, or remediation tasks not completing within expected timeframes.

## Common Causes
- Policy definition syntax error preventing assignment
- Policy effect (Deny/Audit) blocking legitimate resource operations
- Exemption not applied to resources that need exceptions
- Remediation task unable to access managed identity
- Policy set (initiative) definition not updated with latest policies

## How to Fix
### Check policy compliance
```bash
az policy assignment list \
  --query "[].{name:name,displayName:displayName,notScopes:notScopes}"
```

### Create policy assignment
```bash
az policy assignment create \
  --name myPolicyAssignment \
  --display-name "Require tags on resources" \
  --policy /providers/Microsoft.Authorization/policyDefinitions/require-tags \
  --scope /subscriptions/xxx
```

### Trigger remediation task
```bash
az policy remediation create \
  --name myRemediation \
  --policy-assignment myPolicyAssignment \
  --scope /subscriptions/xxx
```

### Create policy exemption
```bash
az policy exemption create \
  --name myExemption \
  --policy-assignment myPolicyAssignment \
  --exemption-category Waiver \
  --scope /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myVM
```

## Examples
### List built-in policies
```bash
az policy definition list \
  --query "[?contains(name,'tag')].{name:name,displayName:displayName}" \
  --query "[0:5]"
```

### Check remediation status
```bash
az policy remediation show \
  --name myRemediation \
  --scope /subscriptions/xxx
```

## Related Errors
- {{< relref "/cloud/azure/azure-rbac-error" >}}
- {{< relref "/cloud/azure/azure-blueprint-error" >}}
- {{< relref "/cloud/azure/azure-azure-ad-error" >}}
