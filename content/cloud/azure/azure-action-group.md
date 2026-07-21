---
title: "[Solution] AZURE Action Group"
description: "ActionGroupError for notification."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Action Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Action group not found
- Email/SMS quota exceeded
- Webhook endpoint unreachable

## How to Fix

### List groups

```bash
az monitor action-group list -g myRG
```

## Examples

- Example scenario: action group not found
- Example scenario: email/sms quota exceeded
- Example scenario: webhook endpoint unreachable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
