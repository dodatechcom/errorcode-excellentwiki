---
title: "[Solution] AZURE PIM Activation"
description: "PIMActivationError for Privileged Identity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `PIM Activation` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Role not eligible
- Activation duration too long
- Justification required

## How to Fix

### Activate role

```bash
az role assignment create --assignee user@domain.com --role Reader
```

## Examples

- Example scenario: role not eligible
- Example scenario: activation duration too long
- Example scenario: justification required

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
