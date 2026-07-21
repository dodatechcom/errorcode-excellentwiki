---
title: "[Solution] AZURE Private Link"
description: "PrivateLinkError for private link."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Private Link` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Private link service not found
- Connection approval pending
- NAT IP unavailable

## How to Fix

### List endpoints

```bash
az network private-link-service list
```

## Examples

- Example scenario: private link service not found
- Example scenario: connection approval pending
- Example scenario: nat ip unavailable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
