---
title: "[Solution] AZURE Container App Environment"
description: "ContainerAppEnvError for environments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container App Environment` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Env name taken
- Log Analytics workspace missing
- VNet already linked

## How to Fix

### List envs

```bash
az containerapp env list -g myRG
```

## Examples

- Example scenario: env name taken
- Example scenario: log analytics workspace missing
- Example scenario: vnet already linked

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
