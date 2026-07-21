---
title: "[Solution] AZURE Traffic Manager"
description: "TrafficManagerError for TM profiles."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Traffic Manager` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Profile not found
- Endpoint monitoring failed
- DNS config conflict

## How to Fix

### List profiles

```bash
az network traffic-manager profile list
```

## Examples

- Example scenario: profile not found
- Example scenario: endpoint monitoring failed
- Example scenario: dns config conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
