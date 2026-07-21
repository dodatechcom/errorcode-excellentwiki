---
title: "[Solution] AZURE App Registration"
description: "AppRegError for app registrations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `App Registration` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- App already registered
- Identifier URI taken
- Redirect URI invalid

## How to Fix

### Create app

```bash
az ad app create --display-name myApp
```

## Examples

- Example scenario: app already registered
- Example scenario: identifier uri taken
- Example scenario: redirect uri invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
