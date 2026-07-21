---
title: "[Solution] AZURE Start Failed"
description: "StartFailed when a VM doesn't start."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Start Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Allocation failure during start
- Azure host issues
- OS corruption preventing boot

## How to Fix

### Start VM

```bash
az vm start -n myVM -g myRG
```

## Examples

- Example scenario: allocation failure during start
- Example scenario: azure host issues
- Example scenario: os corruption preventing boot

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
