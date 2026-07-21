---
title: "[Solution] AZURE VPN Gateway"
description: "VPNGatewayError for VPN gateways."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPN Gateway` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Gateway already exists
- SKU not available in region
- Active-Active setup failure

## How to Fix

### List gateways

```bash
az network vpn-gateway list -g myRG
```

## Examples

- Example scenario: gateway already exists
- Example scenario: sku not available in region
- Example scenario: active-active setup failure

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
