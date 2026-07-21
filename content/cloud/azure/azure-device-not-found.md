---
title: "[Solution] AZURE Device Not Found"
description: "DeviceNotFound for IoT devices."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Device Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Device ID incorrect
- Deleted from registry
- Provisioned through DPS only

## How to Fix

### Query devices

```bash
az iot hub query -n myHub -q 'select * from devices'
```

## Examples

- Example scenario: device id incorrect
- Example scenario: deleted from registry
- Example scenario: provisioned through dps only

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
