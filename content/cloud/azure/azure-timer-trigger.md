---
title: "[Solution] AZURE Timer Trigger"
description: "TimerTriggerError for timer functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Timer Trigger` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- CRON expression invalid
- Schedule not set
- Timezone mismatch

## How to Fix

### Update settings

```bash
az functionapp config appsettings set -n myFuncApp -g myRG --settings WEBSITE_TIME_ZONE=UTC
```

## Examples

- Example scenario: cron expression invalid
- Example scenario: schedule not set
- Example scenario: timezone mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
