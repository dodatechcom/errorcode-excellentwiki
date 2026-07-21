---
title: "[Solution] AZURE Node Pool Not Ready"
description: "NodePoolNotReady for AKS node pools."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Node Pool Not Ready` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Nodes not provisioned
- Upgrade in progress
- VMSS provisioning failed

## How to Fix

### Show pool

```bash
az aks nodepool show --cluster myAKS -g myRG -n myPool
```

## Examples

- Example scenario: nodes not provisioned
- Example scenario: upgrade in progress
- Example scenario: vmss provisioning failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
