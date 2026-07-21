---
title: "[Solution] AZURE Module Twin"
description: "ModuleTwinError for IoT module twins."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Module Twin` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Module ID not found
- Desired property update failed
- Reported property too large

## How to Fix

### Get twin

```bash
az iot hub module-twin show -n myHub -d myDevice -m myModule
```

## Examples

- Example scenario: module id not found
- Example scenario: desired property update failed
- Example scenario: reported property too large

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
