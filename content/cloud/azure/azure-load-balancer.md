---
title: "[Solution] AZURE Load Balancer"
description: "LoadBalancerError for Azure LB."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Load Balancer` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Frontend IP config missing
- Backend pool empty
- Probe config invalid

## How to Fix

### List LBs

```bash
az network lb list -g myRG
```

## Examples

- Example scenario: frontend ip config missing
- Example scenario: backend pool empty
- Example scenario: probe config invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
