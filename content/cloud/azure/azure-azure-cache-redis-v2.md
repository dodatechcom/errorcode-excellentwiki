---
title: "[Solution] AZURE Azure Cache Redis"
description: "RedisError for Azure Cache for Redis."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Azure Cache Redis` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Cache name invalid
- SKU not available
- Firewall block

## How to Fix

### List caches

```bash
az redis list -g myRG
```

## Examples

- Example scenario: cache name invalid
- Example scenario: sku not available
- Example scenario: firewall block

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
