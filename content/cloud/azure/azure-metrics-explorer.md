---
title: "[Solution] AZURE Metrics Explorer"
description: "MetricsExplorerError for custom metrics."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Metrics Explorer` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Metric not available
- Aggregation type wrong
- Time granularity invalid

## How to Fix

### Get metrics

```bash
az monitor metrics list --resource /subscriptions/... --metric CPU
```

## Examples

- Example scenario: metric not available
- Example scenario: aggregation type wrong
- Example scenario: time granularity invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
