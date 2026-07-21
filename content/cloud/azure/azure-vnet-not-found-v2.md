---
title: "[Solution] AZURE VNet Not Found"
description: "VNetNotFound for virtual network."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VNet Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VNet name incorrect
- Deleted by admin
- Wrong resource group

## How to Fix

### List VNets

```bash
az network vnet list -g myRG
```

## Examples

- Example scenario: vnet name incorrect
- Example scenario: deleted by admin
- Example scenario: wrong resource group

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
