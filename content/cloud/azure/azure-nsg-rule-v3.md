---
title: "[Solution] AZURE NSG Rule"
description: "NSGRuleError for network security groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `NSG Rule` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- NSG rule limit (1000) reached
- Priority conflict
- Port/Source validation error

## How to Fix

### List rules

```bash
az network nsg rule list -g myRG --nsg myNSG
```

## Examples

- Example scenario: nsg rule limit (1000) reached
- Example scenario: priority conflict
- Example scenario: port/source validation error

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
