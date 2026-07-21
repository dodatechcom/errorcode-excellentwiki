---
title: "[Solution] AZURE Diagnostic Setting"
description: "DiagSettingError for diagnostic settings."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Diagnostic Setting` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Setting already exists
- Destination resource not found
- Log/ metric categories invalid

## How to Fix

### List settings

```bash
az monitor diagnostic-settings list --resource /subscriptions/...
```

## Examples

- Example scenario: setting already exists
- Example scenario: destination resource not found
- Example scenario: log/ metric categories invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
