---
title: "[Solution] AZURE IoT Hub Quota"
description: "IoTHubQuotaError for message quotas."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IoT Hub Quota` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Messages per day exceeded
- Total device count > quota
- Free tier throttled

## How to Fix

### Show statistics

```bash
az iot hub show -n myHub
```

## Examples

- Example scenario: messages per day exceeded
- Example scenario: total device count > quota
- Example scenario: free tier throttled

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
