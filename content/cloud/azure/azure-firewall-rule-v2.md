---
title: "[Solution] AZURE Firewall Rule"
description: "FirewallRuleError for SQL firewall."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Firewall Rule` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Client IP not allowed
- Rule start > end IP range
- Max 256 rules per server

## How to Fix

### Add rule

```bash
az sql server firewall-rule create -g myRG -s myServer -n allowMyIP --start 203.0.113.0 --end 203.0.113.255
```

## Examples

- Example scenario: client ip not allowed
- Example scenario: rule start > end ip range
- Example scenario: max 256 rules per server

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
