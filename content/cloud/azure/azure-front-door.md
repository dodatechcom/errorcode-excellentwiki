---
title: "[Solution] AZURE Front Door"
description: "FrontDoorError for Azure Front Door."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Front Door` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Front Door name taken globally
- Backend health probe failed
- Origin not reachable

## How to Fix

### List frontdoors

```bash
az network front-door list -g myRG
```

## Examples

- Example scenario: front door name taken globally
- Example scenario: backend health probe failed
- Example scenario: origin not reachable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
