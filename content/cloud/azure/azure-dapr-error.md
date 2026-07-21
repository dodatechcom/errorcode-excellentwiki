---
title: "[Solution] AZURE Dapr Error"
description: "DaprError for Dapr sidecar."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dapr Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Dapr not enabled
- Component not found
- Pub/sub topic missing

## How to Fix

### Enable Dapr

```bash
az containerapp dapr enable -g myRG -n myApp
```

## Examples

- Example scenario: dapr not enabled
- Example scenario: component not found
- Example scenario: pub/sub topic missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
