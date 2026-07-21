---
title: "[Solution] AZURE UDR Error"
description: "UDRCustomError for user defined routes."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `UDR Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Route table linked to subnet
- Missing default route
- Virtual appliance IP invalid

## How to Fix

### Check routes

```bash
az network route-table show -n myRouteTable -g myRG
```

## Examples

- Example scenario: route table linked to subnet
- Example scenario: missing default route
- Example scenario: virtual appliance ip invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
