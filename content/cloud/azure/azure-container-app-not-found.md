---
title: "[Solution] AZURE Container App Not Found"
description: "ContainerAppNotFound for Container Apps."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container App Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Name incorrect
- Deleted by admin
- Environment mismatch

## How to Fix

### List apps

```bash
az containerapp list -g myRG
```

## Examples

- Example scenario: name incorrect
- Example scenario: deleted by admin
- Example scenario: environment mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
