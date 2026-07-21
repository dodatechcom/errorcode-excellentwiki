---
title: "[Solution] AZURE Address Space"
description: "AddressSpaceError for address prefixes."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Address Space` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- CIDR overlap with peered VNet
- Too many address prefixes (max 500)

## How to Fix

### Check space

```bash
az network vnet show -n myVNet -g myRG --query addressSpace
```

## Examples

- Example scenario: cidr overlap with peered vnet
- Example scenario: too many address prefixes (max 500)

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
