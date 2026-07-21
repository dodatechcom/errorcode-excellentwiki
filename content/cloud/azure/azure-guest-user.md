---
title: "[Solution] AZURE Guest User"
description: "GuestUserError for B2B guests."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Guest User` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Invitation already sent
- User already exists in tenant
- Domain federation required

## How to Fix

### List guests

```bash
az ad user list --filter userType eq Guest
```

## Examples

- Example scenario: invitation already sent
- Example scenario: user already exists in tenant
- Example scenario: domain federation required

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
