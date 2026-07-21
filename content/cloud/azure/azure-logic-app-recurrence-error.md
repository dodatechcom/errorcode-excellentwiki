---
title: "[Solution] Azure Logic Apps Recurrence Error"
description: "Fix Azure Logic Apps recurrence trigger failures that prevent scheduled workflow execution."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Recurrence errors prevent Logic Apps from triggering on schedule. This breaks time-based automations like report generation or cleanup tasks.

## Common Causes

- Recurrence interval is set to an invalid value for the Logic App plan
- The recurrence trigger is disabled after a workflow update
- Time zone is set to UTC and the expected execution is in local time
- Consumption plan has hit the daily recurrence limit

## How to Fix

### Check recurrence trigger configuration

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/triggers?api-version=2019-05-01"
```

### Enable the recurrence trigger

```bash
az rest --method POST \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/triggers/myRecurrenceTrigger/run?api-version=2019-05-01"
```

### Update recurrence schedule

```bash
az logic workflow update \
  --name myLogicApp \
  --resource-group myRG \
  --definition '{
    "triggers": {
      "Recurrence": {
        "type": "Recurrence",
        "recurrence": {
          "frequency": "Day",
          "interval": 1,
          "startTime": "2026-01-01T09:00:00Z",
          "timeZone": "Eastern Standard Time"
        }
      }
    }
  }'
```

### Check run history for skipped runs

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/runs?api-version=2019-05-01&$top=10"
```

## Examples

- Logic App was supposed to run daily at 9 AM but has no runs in the last week
- Recurrence trigger shows `Skipped` status because the workflow was in disabled state
- Hourly recurrence fires twice due to daylight saving time transition

## Related Errors

- [Azure Logic Apps Error]({{< relref "/cloud/azure/azure-logic-apps-error" >}}) -- General Logic Apps errors.
- [Azure Logic App Run Failed]({{< relref "/cloud/azure/azure-logic-app-run-failed" >}}) -- Run failures.
