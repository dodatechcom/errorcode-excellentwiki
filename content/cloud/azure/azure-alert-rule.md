---
title: "[Solution] AZURE Alert Rule"
description: "AlertRuleError for metric alerts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Alert Rule` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Condition not set
- Action group missing
- Severity invalid

## How to Fix

### List rules

```bash
az monitor metrics alert list -g myRG
```

## Examples

- Example scenario: condition not set
- Example scenario: action group missing
- Example scenario: severity invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
