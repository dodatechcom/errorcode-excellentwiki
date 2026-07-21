---
title: "[Solution] AZURE Subnet Not Found"
description: "SubnetNotFound for network subnets."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Subnet Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Subnet name incorrect
- Subnet in different VNet
- Deleted subnet

## How to Fix

### List subnets

```bash
az network vnet subnet list --vnet myVNet -g myRG
```

## Examples

- Example scenario: subnet name incorrect
- Example scenario: subnet in different vnet
- Example scenario: deleted subnet

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
