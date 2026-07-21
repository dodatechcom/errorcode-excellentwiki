---
title: "[Solution] Azure Logic Apps Run Failed Error"
description: "Fix Azure Logic Apps run failures caused by action timeouts, input validation, and connector errors."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Run failures occur when a Logic App workflow execution fails at one or more actions. This prevents the automation from completing its intended task.

## Common Causes

- An action timed out due to slow external API response
- Input schema validation failed because the input data does not match the expected format
- Connector authentication failed due to expired credentials
- Action retry policy exhausted all attempts without success

## How to Fix

### Check run history

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/runs?api-version=2019-05-01"
```

### Get failed run details

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/runs/{runId}/actions?api-version=2019-05-01"
```

### Update connector connection

```bash
az rest --method PUT \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/connections/myConnection?api-version=2019-05-01" \
  --body '{"properties":{"parameterValues":{"authenticationType":"ManagedServiceIdentity"}}}'
```

### Enable diagnostic logging

```bash
az logic workflow update \
  --name myLogicApp \
  --resource-group myRG \
  --state Enabled
```

## Examples

- Logic App fails with `WorkflowRunTimeout` after running for more than 5 minutes on Consumption plan
- HTTP action fails with `BadRequest` because the JSON payload is missing a required field
- Office 365 connector fails with `TokenExpired` after 90 days without credential refresh

## Related Errors

- [Azure Logic Apps Error]({{< relref "/cloud/azure/azure-logic-apps-error" >}}) -- General Logic Apps errors.
- [Azure API Management Error]({{< relref "/cloud/azure/azure-api-management-error" >}}) -- API Management errors.
