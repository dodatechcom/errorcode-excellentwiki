---
title: "[Solution] AZURE Conditional Access"
description: "ConditionalAccessError for CA policies."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Conditional Access` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Policy blocks sign-in
- Device compliance failure
- MFA required but not done

## How to Fix

### Check sign-in

```bash
az sign-in log list
```

## Examples

- Example scenario: policy blocks sign-in
- Example scenario: device compliance failure
- Example scenario: mfa required but not done

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
