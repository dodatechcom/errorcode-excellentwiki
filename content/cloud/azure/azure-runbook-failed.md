---
title: "[Solution] AZURE Runbook Failed"
description: "RunbookError for Automation runbooks."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Runbook Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Script failure in execution
- Module not imported
- Credential not found

## How to Fix

### Start runbook

```bash
az automation runbook start -g myRG -a myAccount -n myRunbook
```

## Examples

- Example scenario: script failure in execution
- Example scenario: module not imported
- Example scenario: credential not found

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
