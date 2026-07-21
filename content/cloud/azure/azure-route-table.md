---
title: "[Solution] AZURE Route Table"
description: "RouteTableError for route tables."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Route Table` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Route already exists
- Address prefix conflict
- Next hop type invalid

## How to Fix

### List tables

```bash
az network route-table list -g myRG
```

## Examples

- Example scenario: route already exists
- Example scenario: address prefix conflict
- Example scenario: next hop type invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
