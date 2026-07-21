---
title: "[Solution] AZURE Proximity Group"
description: "ProximityPlacementGroupError."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Proximity Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Group cannot span regions
- VM not in same proximity group
- Colocation status mismatch

## How to Fix

### Show group

```bash
az ppg show -n myPPG -g myRG
```

## Examples

- Example scenario: group cannot span regions
- Example scenario: vm not in same proximity group
- Example scenario: colocation status mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
