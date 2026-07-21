---
title: "[Solution] AZURE Automation Account"
description: "AutomationError for automation accounts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Automation Account` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Account name taken
- Run As account expired
- Region unavailable

## How to Fix

### List accounts

```bash
az automation account list -g myRG
```

## Examples

- Example scenario: account name taken
- Example scenario: run as account expired
- Example scenario: region unavailable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
