---
title: "[Solution] AZURE Dedicated Host"
description: "DedicatedHostError for dedicated hosts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dedicated Host` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Host allocation failed
- Host group capacity reached
- Host in wrong state

## How to Fix

### List hosts

```bash
az vm host list -g myRG --host-group myHG
```

## Examples

- Example scenario: host allocation failed
- Example scenario: host group capacity reached
- Example scenario: host in wrong state

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
