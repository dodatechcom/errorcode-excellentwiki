---
title: "[Solution] AZURE Application Gateway"
description: "AppGatewayError for Application Gateway."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Application Gateway` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Gateway already exists
- SKU not available
- WAF policy conflict

## How to Fix

### List gateways

```bash
az network application-gateway list -g myRG
```

## Examples

- Example scenario: gateway already exists
- Example scenario: sku not available
- Example scenario: waf policy conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
