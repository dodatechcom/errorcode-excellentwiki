---
title: "[Solution] AZURE Runtime Error"
description: "FunctionRuntimeError for Azure Functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Runtime Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Runtime version mismatch
- Host.json config error
- Dependency resolution fail

## How to Fix

### Check runtime

```bash
az functionapp config show -n myFuncApp -g myRG
```

## Examples

- Example scenario: runtime version mismatch
- Example scenario: host.json config error
- Example scenario: dependency resolution fail

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
