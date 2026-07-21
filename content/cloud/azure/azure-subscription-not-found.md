---
title: "[Solution] AZURE Subscription Not Found"
description: "SubscriptionNotFound for subscriptions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Subscription Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Subscription ID incorrect
- Subscription disabled
- Tenant mismatch

## How to Fix

### Show sub

```bash
az account show
```

## Examples

- Example scenario: subscription id incorrect
- Example scenario: subscription disabled
- Example scenario: tenant mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
