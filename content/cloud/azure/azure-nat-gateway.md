---
title: "[Solution] AZURE NAT Gateway"
description: "NATGatewayError for NAT gateways."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `NAT Gateway` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- NAT gateway already exists
- Public IP insufficient
- Subnet already has NAT

## How to Fix

### List NAT gateways

```bash
az network nat gateway list -g myRG
```

## Examples

- Example scenario: nat gateway already exists
- Example scenario: public ip insufficient
- Example scenario: subnet already has nat

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
