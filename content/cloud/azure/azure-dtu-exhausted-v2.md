---
title: "[Solution] AZURE DTU Exhausted"
description: "DTULimitExceeded for DTU consumption."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DTU Exhausted` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- DTU consumption hit the cap
- Query optimization needed
- Scale up needed

## How to Fix

### Scale pool

```bash
az sql elastic-pool update -g myRG -s myServer -n myPool --dtu 200
```

## Examples

- Example scenario: dtu consumption hit the cap
- Example scenario: query optimization needed
- Example scenario: scale up needed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
