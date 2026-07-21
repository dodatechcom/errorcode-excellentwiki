---
title: "[Solution] AZURE IoT Hub Not Found"
description: "IoTHubNotFound for IoT Hub."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IoT Hub Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Name incorrect
- Deleted by admin
- Subscription mismatch

## How to Fix

### List hubs

```bash
az iot hub list -g myRG
```

## Examples

- Example scenario: name incorrect
- Example scenario: deleted by admin
- Example scenario: subscription mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
