---
title: "[Solution] AZURE App Settings"
description: "AppSettingsError for configuration."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `App Settings` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Setting key/value missing
- Slot setting not marked correctly
- Connection string invalid

## How to Fix

### List settings

```bash
az webapp config appsettings list -g myRG -n myApp
```

## Examples

- Example scenario: setting key/value missing
- Example scenario: slot setting not marked correctly
- Example scenario: connection string invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
