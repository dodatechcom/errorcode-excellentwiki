---
title: "[Solution] AZURE DNS Zone"
description: "DNSZoneError for DNS zones."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DNS Zone` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Zone name already exists
- Zone not found in subscription
- SOA record not editable

## How to Fix

### List zones

```bash
az network dns zone list -g myRG
```

## Examples

- Example scenario: zone name already exists
- Example scenario: zone not found in subscription
- Example scenario: soa record not editable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
