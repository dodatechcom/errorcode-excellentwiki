---
title: "[Solution] AZURE Stop Failed"
description: "StopFailed when a VM won't stop."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Stop Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Extension still running on the VM
- Lock preventing VM operations
- Guest OS shutdown timeout

## How to Fix

### Force stop

```bash
az vm stop -n myVM -g myRG --force
```

## Examples

- Example scenario: extension still running on the vm
- Example scenario: lock preventing vm operations
- Example scenario: guest os shutdown timeout

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
