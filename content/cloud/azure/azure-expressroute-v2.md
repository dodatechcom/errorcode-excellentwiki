---
title: "[Solution] AZURE ExpressRoute"
description: "ExpressRouteError for ER circuits."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ExpressRoute` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Circuit not found
- Provider status not provisioned
- Bandwidth limit reached

## How to Fix

### List circuits

```bash
az network express-route list -g myRG
```

## Examples

- Example scenario: circuit not found
- Example scenario: provider status not provisioned
- Example scenario: bandwidth limit reached

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
