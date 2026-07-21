---
title: "[Solution] Azure Resource Locks Error"
description: "Fix Azure resource lock issues that prevent deletion or modification of protected resources."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Resource lock errors occur when CanNotDelete or ReadOnly locks block intended operations. While protective, incorrect lock placement can prevent legitimate changes.

## Common Causes

- Lock is applied at the resource group level and affects all child resources
- ReadOnly lock prevents updates that are needed for operations
- Lock was applied by a different team and the owner is not known
- Automation scripts do not account for resource locks

## How to Fix

### List resource locks

```bash
az lock list \
  --resource-group myRG \
  --query "[].{Name:name,Type:lockType,Notes:notes}"
```

### Remove a lock

```bash
az lock delete \
  --name myLock \
  --resource-group myRG
```

### Create a CanNotDelete lock

```bash
az lock create \
  --name "protect-prod" \
  --resource-group myRG \
  --lock-type CanNotDelete \
  --notes "Protect production resources from accidental deletion"
```

### Create a ReadOnly lock

```bash
az lock create \
  --name "readonly-lock" \
  --resource-name myVM \
  --resource-group myRG \
  --resource-type Microsoft.Compute/virtualMachines \
  --lock-type CanNotDelete
```

## Examples

- VM deallocation fails because a ReadOnly lock is set at the subscription level
- Resource group deletion fails because a CanNotDelete lock is applied to a critical resource group
- CI/CD pipeline cannot update App Service settings because a ReadOnly lock is set on the resource

## Related Errors

- [Azure Policy Error]({{< relref "/cloud/azure/azure-policy-error" >}}) -- Policy issues.
- [Azure RBAC Error]({{< relref "/cloud/azure/azure-rbac-error" >}}) -- RBAC issues.
