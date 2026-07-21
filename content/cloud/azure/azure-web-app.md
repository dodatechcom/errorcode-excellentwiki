---
title: "[Solution] AZURE Web App"
description: "WebAppError for web applications."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Web App` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- App name taken globally
- Runtime stack not supported
- App settings missing

## How to Fix

### List web apps

```bash
az webapp list -g myRG
```

## Examples

- Example scenario: app name taken globally
- Example scenario: runtime stack not supported
- Example scenario: app settings missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
