---
title: "[Solution] AZURE Function Host"
description: "FunctionHostError for function host."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function Host` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Storage account connection missing
- Host key invalid
- Scale controller error

## How to Fix

### Restart app

```bash
az functionapp restart -n myFuncApp -g myRG
```

## Examples

- Example scenario: storage account connection missing
- Example scenario: host key invalid
- Example scenario: scale controller error

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
